#!/usr/bin/env python3
"""Spoiler-minimized cross-source case validation.

Checks exhibit consistency rather than embedding the intended question answers.
All case content is simulated. This is an author QA aid, not a grading key.
"""
from __future__ import annotations
import csv
import hashlib
from datetime import datetime, timedelta, timezone
from pathlib import Path, PureWindowsPath
import zipfile

ROOT=Path(__file__).resolve().parents[1]
EV=ROOT/"evidence"

def table(part):
    with (EV/part).open(newline="",encoding="utf-8") as stream:
        return list(csv.DictReader(stream))

def stamp(s):
    return datetime.fromisoformat(s.replace("Z","+00:00"))

tickets={x["ticket_id"]:x for x in table("02_governance/change_tickets.csv")}
control=table("06_control_plane/controller_audit.csv")
edge=table("05_network/acl_policy_log.csv")
ntp=table("06_control_plane/ntp_samples.csv")
flows=table("05_network/netflow.csv")
proxy=table("05_network/proxy_requests.csv")
receipts=table("07_receipts/receiving_object_audit.csv")
catalog=table("09_export/export_catalog.csv")
snapshots=table("06_control_plane/config_snapshots.csv")
spans=table("05_network/span_counters.csv")
siem=table("08_soc/siem_health.csv")
logons=table("03_identity/windows_security.csv")
pam=table("03_identity/privileged_access.csv")
process=table("04_endpoint/process_activity.csv")
tasks=table("04_endpoint/scheduled_tasks.csv")
files=table("04_endpoint/file_audit.csv")
dns=table("05_network/dns_queries.csv")
policies=table("02_governance/access_policy.csv")
assert all([tickets,control,edge,ntp,flows,proxy,receipts,catalog,snapshots,spans,siem,logons,pam,process,tasks,files,dns,policies])

# Bound each local device event by an explicitly observed offset and controller/flow anchors.
for e in edge:
    device=e["device"]
    candidates=[r for r in ntp if r["device"]==device]
    assert len(candidates)==1, ("Clock calibration missing or ambiguous",device)
    sample=candidates[0]
    local=datetime.fromisoformat(e["edge_local_time"]).replace(tzinfo=timezone.utc)
    t=local-timedelta(seconds=int(sample["offset_seconds_device_ahead"]))
    assert stamp(sample["valid_from_utc"])<=t<=stamp(sample["valid_until_utc"])
    matches=[c for c in control if c["config_revision"]==e["revision"] and stamp(c["timestamp_utc"])==t]
    if e["operation"] in ("apply_exception","restore_baseline"):
        assert len(matches)==1, ("No unique controller change",e["edge_record_id"])
    if e["operation"]=="traffic_rule_match":
        assert sum(
            x["src_ip"]==e["source_ip"] and x["dst_ip"]==e["destination_ip"]
            and x["dst_port"]==e["destination_port"]
            and stamp(x["start_utc"])<=t<=stamp(x["end_utc"]) for x in flows
        )==1, ("Firewall flow not unique",e["edge_record_id"])

assert all(c["ticket_label"] in tickets for c in control)
assert any(
    tickets[c["ticket_label"]]["approved"]=="yes"
    and c["target"].split("/")[0]!=tickets[c["ticket_label"]]["authorized_asset"]
    and c["operation"] not in ("read_only_status",)
    for c in control
), "No out-of-scope ticket use"
assert any(x["approved"]=="no" for x in tickets.values())
assert len({x["revision"] for x in snapshots})>=3

# SPAN controller transitions must agree with the switch's physical collection view.
transitions=[c for c in control if c["operation"] in ("disable_mirror","enable_mirror")]
assert len(transitions)>=2
for event in transitions:
    mirror=event["target"].split("/")[-1]
    expected_state="disabled" if event["operation"]=="disable_mirror" else "enabled"
    assert any(x["mirror_id"]==mirror and x["admin_state"]==expected_state
               and x["timestamp_utc"]==event["timestamp_utc"] for x in spans)
assert any(r["mirrored_ingest_packets"]=="0" and r["agent_heartbeat"]
           for r in siem), "No independent misleading heartbeat comparator"

# Identity is only an account-to-host-to-controller chain, not a human assertion.
assert all(a["linked_logon_id"] in {l["logon_id"] for l in logons}
           for a in pam)
assert any(l["account"]==p["principal"] and l["logon_id"]==p["linked_logon_id"]
           for p in pam for l in logons)
assert all(c["session_id"] in {p["session_id"] for p in pam} for c in control)
assert all(p["logon_id"] in {l["logon_id"] for l in logons}|{"0x0"}
           for p in process)

# Archive content is real benign ZIP bytes, not a hash string fabricated by the tests.
for item in catalog:
    payload=ROOT/item["artifact_path"]
    assert payload.is_file()
    actual_bytes=payload.read_bytes()
    digest=hashlib.sha256(actual_bytes).hexdigest()
    assert item["sha256"]==digest
    assert len(actual_bytes)==int(item["size_bytes"])
    with zipfile.ZipFile(payload) as archive:
        assert archive.testzip() is None
        members=set(archive.namelist())
        assert len(members)==int(item["source_file_count"])
    assert all(any(r["path"].endswith(m) for r in files) for m in members)
    matched_proxy=[p for p in proxy if p["sha256_claim"]==digest
                   and p["bytes_out"]==item["size_bytes"]]
    assert len(matched_proxy)==1
    upload=matched_proxy[0]
    matched_receipt=[r for r in receipts if
                     r["sha256_claim"]==digest and
                     r["content_length"]==item["size_bytes"] and
                     r["src_ip"]==upload["src_ip"] and
                     r["dest_ip"]==upload["dst_ip"]]
    assert len(matched_receipt)==1
    assert matched_receipt[0]["http_status"]==upload["http_status"]
    assert sum(x["src_ip"]==upload["src_ip"] and x["dst_ip"]==upload["dst_ip"]
               and stamp(x["start_utc"])<=stamp(upload["timestamp_utc"])<=stamp(x["end_utc"])
               for x in flows)==1
    assert any(x["answer_ip"]==upload["dst_ip"] and x["src_ip"]==upload["src_ip"]
               for x in dns)

# Background data must not create ambiguous 5-tuple matches to the cataloged transfer.
zeek=(EV/"10_background/zeek_conn.log").read_text(encoding="utf-8").splitlines()
zeek_rows=[line.split("\t") for line in zeek if line and not line.startswith("#")]
assert len(zeek_rows)>=190 and all(len(r)==12 for r in zeek_rows)
for upload in [p for p in proxy if p["sha256_claim"]]:
    linked=[x for x in flows if x["src_ip"]==upload["src_ip"] and x["dst_ip"]==upload["dst_ip"]
            and stamp(x["start_utc"])<=stamp(upload["timestamp_utc"])<=stamp(x["end_utc"])]
    assert len(linked)==1
    x=linked[0]
    assert sum(r[2]==x["src_ip"] and r[3]==x["src_port"] and
               r[4]==x["dst_ip"] and r[5]==x["dst_port"] for r in zeek_rows)==1
assert len(table("10_background/endpoint_activity.csv"))>=160
assert len((EV/"10_background/edge_syslog.log").read_text().splitlines())>=100

# Persistence-related observations are present, but malicious binary intent is not asserted.
registrations=[t for t in tasks if t["operation"]=="create"]
assert registrations
assert any(r["task_name"]==x["task_name"] and r["operation"]=="run"
           and stamp(r["timestamp_utc"])>stamp(x["timestamp_utc"])
           for x in registrations for r in tasks)
assert any(x["win_event_id"]=="1102" for x in logons)
print("PASS: cross-source joins, bounded NTP, authorization, SPAN, archive/hash, DNS, flow, receipt, task and background ambiguity")
