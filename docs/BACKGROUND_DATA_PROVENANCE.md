# Mixed-signal evidence and provenance

This release adds **synthetically generated** background telemetry with baseline traffic and process events. It improves the *triage exercise* but is **not a native capture** from a laboratory or real infrastructure. It must never be described as a PCAP, Sysmon EVTX, E01, memory image or Zeek capture from actual network equipment.

| Exhibit | Purpose | How to analyze |
|---|---|---|
| `10_background/zeek_conn.log` | 200 Zeek-format, synthetic network connections; 4 are correlated to core NetFlow exhibits and the remainder represent ordinary noise | Read tab-separated Zeek columns; join 5-tuple/time and compare to NetFlow/proxy |
| `10_background/endpoint_activity.csv` | 171 events: 165 benign-ish ambient processes and 6 principal process-chain anchors | Join `process_guid`, `parent_guid`, `logon_id`; process reputation is deliberately unverified |
| `10_background/edge_syslog.log` | 113 firewall-style events with an edge-device clock ahead of UTC | Use the NTP calibration before correlating to controller and network flow |

## Limits

1. None of the background signals independently proves malicious activity. An exact matching 5-tuple in NetFlow and the Zeek-format log is **cross-source consistency**, not a claim of true independent acquisition.
2. The harmless exported ZIP remains only 1,133 bytes. It is a pedagogical proxy for network-design records, not realistic enterprise-scale data exfiltration.
3. Activity was generated as a deterministic fictional fixture; process signature fields should not be treated as validated code-signing evidence.
4. This material does **not** fulfill the HTB expectation to create convincing native forensic artifacts and independently blind-test a Sherlock at Insane difficulty.

## Analysis note

A good answer must distinguish a matching ticket label from an authorized action. A flow to an unfamiliar endpoint is not proof of compromise. Cross-check policy, session, data-access, clock correction, application upload and receipt before making an incident determination.
