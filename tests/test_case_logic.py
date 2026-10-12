#!/usr/bin/env python3
"""Author-side cross-artifact integrity tests; requires no commercial tooling."""
from pathlib import Path
from datetime import datetime, timedelta, timezone
import csv, hashlib, zipfile

R = Path(__file__).resolve().parents[1]
def records(path):
    with (R/path).open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
def date(s):
    return datetime.fromisoformat(s.replace("Z","+00:00"))

tickets = {x["ticket_id"]:x for x in records("evidence/02_governance/change_tickets.csv")}
audit = records("evidence/06_control_plane/controller_audit.csv")
ntp = next(x for x in records("evidence/06_control_plane/ntp_samples.csv") if x["device"]=="NB-EDGE-01")
edge = records("evidence/05_network/acl_policy_log.csv")
span = records("evidence/05_network/span_counters.csv")
siem = records("evidence/08_soc/siem_health.csv")
auth = records("evidence/03_identity/windows_security.csv")
session = records("evidence/03_identity/privileged_access.csv")
process = records("evidence/04_endpoint/process_activity.csv")
dns = records("evidence/05_network/dns_queries.csv")
proxy = records("evidence/05_network/proxy_requests.csv")
flow = records("evidence/05_network/netflow.csv")
catalog = records("evidence/09_export/export_catalog.csv")
receipt = records("evidence/07_receipts/receiving_object_audit.csv")

def normalized(local):
    t = datetime.fromisoformat(local).replace(tzinfo=timezone.utc)
    return t - timedelta(seconds=int(ntp["offset_seconds_device_ahead"]))

for e in edge:
    utc = normalized(e["edge_local_time"])
    assert date(ntp["valid_from_utc"]) <= utc <= date(ntp["valid_until_utc"])
    if e["operation"] == "apply_exception":
        assert any(x["config_revision"]==e["revision"] and date(x["timestamp_utc"])==utc for x in audit)
    elif e["operation"] == "restore_baseline":
        assert any(x["config_revision"]==e["revision"] and date(x["timestamp_utc"])==utc for x in audit)
    elif e["operation"] == "traffic_rule_match":
        assert any(x["src_ip"]==e["source_ip"] and x["dst_ip"]==e["destination_ip"]
                   and date(x["start_utc"]) <= utc <= date(x["end_utc"]) for x in flow)

approved = tickets["CHG-2847"]
assert approved["approved"]=="yes" and approved["authorized_asset"]=="NB-NMS-01"
assert all(x["ticket_label"]=="CHG-2847" for x in audit)
assert any(x["target"].startswith("NB-EDGE-01/") and x["target"].split("/")[0] != approved["authorized_asset"] for x in audit)
assert tickets["CHG-2861"]["approved"]=="no"

disable = next(x for x in span if x["admin_state"]=="disabled" and x["counter_id"]=="SPAN-102")
restore = next(x for x in span if x["counter_id"]=="SPAN-105")
assert date(restore["timestamp_utc"]) - date(disable["timestamp_utc"]) == timedelta(seconds=675)
assert any(x["mirrored_ingest_packets"]=="0" and x["agent_heartbeat"]=="OK" for x in siem)

logon = next(x for x in auth if x["event_id"]=="WIN-1009")
pam = next(x for x in session if x["session_id"]=="CTRL-SESS-884")
assert logon["account"] == pam["principal"] == "svc-netops"
assert logon["logon_id"] == pam["linked_logon_id"]
assert all(x["logon_id"] == logon["logon_id"] for x in process if x["account"]=="svc-netops")
assert any(x["win_event_id"]=="4698" for x in auth) and any(x["win_event_id"]=="1102" for x in auth)

item = catalog[0]
p = R / item["artifact_path"]
assert hashlib.sha256(p.read_bytes()).hexdigest() == item["sha256"]
assert p.stat().st_size == int(item["size_bytes"])
with zipfile.ZipFile(p) as z:
    assert len(z.namelist()) == int(item["source_file_count"]) and z.testzip() is None
matches = [x for x in proxy if x["sha256_claim"] == item["sha256"]]
assert len(matches)==1
upload = matches[0]
assert upload["bytes_out"] == item["size_bytes"] and upload["http_status"]=="201"
assert any(x["sha256_claim"]==item["sha256"] and x["content_length"]==item["size_bytes"]
           and x["src_ip"]==upload["src_ip"] and x["dest_ip"]==upload["dst_ip"]
           for x in receipt)
assert any(x["src_ip"]==upload["src_ip"] and x["dst_ip"]==upload["dst_ip"]
           and date(x["start_utc"])<=date(upload["timestamp_utc"])<=date(x["end_utc"])
           for x in flow)
assert any(x["answer_ip"]==upload["dst_ip"] and x["src_ip"]==upload["src_ip"] for x in dns)

zeek_path=R/"evidence/10_background/zeek_conn.log"
lines=[l for l in zeek_path.read_text().splitlines() if l and not l.startswith("#")]
assert len(lines)>=190
conn=[x.split("\t") for x in lines]
assert all(len(x)==12 for x in conn)
assert sum(x[2]=="10.42.10.25" and x[3]=="55212" and x[4]=="203.0.113.77" for x in conn)==1

edr=records("evidence/10_background/endpoint_activity.csv")
assert len(edr)>=160
assert any(x["process_guid"]=="PG-210" and x["logon_id"]=="0x8AF" for x in edr)
assert all(any(y["process_guid"]==x["process_guid"] and y["logon_id"]==x["logon_id"]
               for y in edr) for x in process if x["account"]=="svc-netops")
syslog=(R/"evidence/10_background/edge_syslog.log").read_text().splitlines()
assert len(syslog)>=100
for eid in ("EDGE-071","EDGE-072","EDGE-073"):
    assert any(eid in x for x in syslog)
print("PASS: clock normalization, evidence joins, ticket scope, sensor blackout, case facts and >=450 augmented mixed-signal events")
