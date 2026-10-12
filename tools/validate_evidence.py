#!/usr/bin/env python3
"""Offline non-spoiler validation of the fictional Sherlock student corpus."""
from __future__ import annotations
import csv, hashlib, pathlib, zipfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"

def load(path):
    with (ROOT / path).open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def fail_if(condition, msg):
    if condition: raise AssertionError(msg)

def main():
    manifest = ROOT / "manifest" / "SHA256SUMS.txt"
    count = 0
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"): continue
        digest, name = line.split("  ", 1)
        path = ROOT / name
        fail_if(not path.is_file(), "Missing " + name)
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        fail_if(actual != digest, "Hash mismatch for " + name)
        count += 1
    fail_if(count < 15, "Insufficient integrity coverage")
    alerts = load("evidence/00_intake/soc_alerts.csv")
    logins = load("evidence/03_identity/windows_security.csv")
    processes = load("evidence/04_endpoint/process_activity.csv")
    controller = load("evidence/06_control_plane/controller_audit.csv")
    access = load("evidence/03_identity/privileged_access.csv")
    proxies = load("evidence/05_network/proxy_requests.csv")
    flows = load("evidence/05_network/netflow.csv")
    receipts = load("evidence/07_receipts/receiving_object_audit.csv")
    catalog = load("evidence/09_export/export_catalog.csv")
    dhcp = load("evidence/01_environment/dhcp_leases.csv")
    tickets = load("evidence/02_governance/change_tickets.csv")
    fail_if(len(alerts)<2 or len(logins)<5 or len(controller)<4, "Key sources too sparse")
    fail_if(not all(x["timestamp_utc"].endswith("Z") for x in controller), "Controller UTC missing")
    fail_if(not set(x["linked_logon_id"] for x in access).issubset(set(x["logon_id"] for x in logins)), "Access to Windows logon mismatch")
    fail_if(not set(x["logon_id"] for x in processes).issubset(set(x["logon_id"] for x in logins)|{"0x0"}), "Process to Windows logon mismatch")
    fail_if(not set(x["src_ip"] for x in proxies).issubset(set(x["src_ip"] for x in flows)), "Proxy flow source mismatch")
    fail_if(not set(x["ticket_label"] for x in controller).issubset(set(x["ticket_id"] for x in tickets)), "Controller references nonexistent ticket")
    fail_if(not all(x["ip"] and x["hostname"] for x in dhcp), "Incomplete DHCP lease")
    for item in catalog:
        p = ROOT/item["artifact_path"]
        fail_if(not p.exists(), "Export archive missing")
        fail_if(len(p.read_bytes()) != int(item["size_bytes"]), "Catalog archive length mismatch")
        fail_if(hashlib.sha256(p.read_bytes()).hexdigest() != item["sha256"], "Catalog archive digest mismatch")
        with zipfile.ZipFile(p) as z:
            fail_if(len(z.namelist()) != int(item["source_file_count"]), "Source member count mismatch")
            fail_if(z.testzip() is not None, "ZIP CRC failure")
        matches = [r for r in receipts if r["sha256_claim"] == item["sha256"] and r["content_length"] == item["size_bytes"]]
        fail_if(not matches, "Missing transfer receipt match")
    print(f"PASS: {count} SHA-256 entries, source joins, real ZIP integrity and transfer receipt consistency.")
if __name__ == "__main__":
    main()
