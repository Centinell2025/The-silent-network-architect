# Artifact provenance and analyst handling

## Collection model
All evidence was generated for this exercise. Event IDs are synthetic scenario identifiers, not original vendor event semantics unless explicitly designated (e.g., Windows Event 4624, 4698, 1102). Timestamps ending in `Z` are UTC. `edge_local_time` is **not** UTC.

| Folder | Source | Why it matters |
|---|---|---|
| 00_intake | SOC alert | Initial detection, not ground truth |
| 01_environment | Asset inventory, DHCP and network topology | Host and subnet identification |
| 02_governance | Change tickets, policy and maintenance attestations | Authorized scope and time |
| 03_identity | Windows Security, privileged access | Source identity and logon sessions |
| 04_endpoint | Processes, file reads, task scheduling | Collection and persistence |
| 05_network | DNS, proxy, NetFlow, firewall rule and SPAN counters | Egress corroboration and telemetry gap |
| 06_control_plane | Controller configuration, edge device audit and NTP | Exact change reconstruction |
| 07_receipts | Receiving-object audit | Independent receipt of egress and checksum claim |
| 08_soc | Alert feed, SIEM health | Detection blind spots |
| 09_export | A verifiable ZIP payload | Match claimed content/size/hash with exhibits |

## Timestamp normalization
- Most logs are UTC ISO 8601 timestamps.
- The edge device uses its own clock and records `edge_local_time`. Use contemporaneous `offset_seconds_device_ahead` in `06_control_plane/ntp_samples.csv`.
- Conversion: `UTC = device_local_time - offset_seconds_device_ahead`.
- NTP calibration is a bounded, synthetic observation for this case; do not generalize offsets beyond the stated range.
- A same-minute match without normalization is insufficient for exact timeline conclusions.

## Correlation hints (not solutions)
`session_id`, `logon_id`, `actor`, `src_ip`, `config_revision`, `ticket_id`, `rule_id`, `dst_ip`, `sni`, `sha256`, `object_id` and `task_name` are joinable fields. Some benign and malicious records deliberately share ticket labels and approved windows; investigate full authorized **asset/action scope**.

## Evidence limitations
- Agent heartbeat is not a guarantee that network capture was functioning.
- NetFlow alone proves traffic metadata, not the payload content or the human behind it.
- A proxy upload and receiving-object audit strengthen transfer evidence but remain simulation records.
- This case contains no verified real-world adversary identity, device seizure, malware binary or external provider attestation.
- The ZIP represents a synthetic export; it is a small verifiable stand-in for sensitive network design material.

## Checksums
Run `python3 tools/validate_evidence.py` at repository root. This uses only Python's standard library, checks checksums and verifies referential/event-level properties without revealing the instructor answers. For the binary export: compare its computed SHA-256 and byte length to both `09_export/export_catalog.csv` and the 07_receipts records.

## Advanced packet fixture (optional)
`evidence/11_packet_fixture/synthetic_network_fixture.pcap` contains deterministic, generated Ethernet/IPv4 TCP SYN/ACK exchanges and DNS examples, indexed by `CAPTURE_PROVENANCE.csv`. It is a **genuine PCAP-format file** but **not a live-captured PCAP**; do not claim it independently proves source-system events or application payload. Use `python3 tools/packet_inspector.py summary` and `docs/ADVANCED_PACKET_ANALYSIS.md` to compare modeled tuples, document coverage gaps and draw explicitly bounded conclusions. The SHA-256 is registered in `manifest/SHA256SUMS.txt`.
