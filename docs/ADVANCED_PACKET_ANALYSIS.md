# Packet-Level Investigation — Advanced Case Extension

**Case:** NB-IR-2026-104 | **Publisher:** Beacon of the Eagle LLC / Centinell Suite Defense

## What is this artifact?

The file `evidence/11_packet_fixture/synthetic_network_fixture.pcap` is a **valid PCAP file generated entirely by Python** for offline defensive training. It contains deterministic Ethernet/IPv4 TCP handshakes, benign background connections, and synthetic DNS query/response pairs. The companion `CAPTURE_PROVENANCE.csv` indexes the modeled conversations. **It is not traffic captured from Windows, Kali, Ubuntu, an appliance, or a real network.** TLS payload content, genuine file exfiltration, and application data are not present. Do not interpret this fixture as native evidence or independent corroboration of CSVs from which it was generated.

The PCAP is useful for packet parsing, network tuples, stream orientation, calculating metadata, comparing sources and judging evidentiary limits. Everything is offline, uses reserved documentation IP ranges and fictitious hosts.

## Investigator exercises (advanced, separate from the 30 graded questions)

For each exercise, submit a source path, extraction command, UTC-corrected event time where appropriate, competing explanation, evidentiary limitation and action.

| Task | Assignment | Required evidence families |
|---|---|---|
| PX01 | Inventory L2/L3 traffic, record link type, frame count, IPv4 protocols and first/last UTC observation | PCAP header, parser or Wireshark |
| PX02 | Identify all four modeled case NetFlow 5-tuples in the PCAP without presuming which is malicious | NetFlow, fixture packets, provenance |
| PX03 | Compare nominal HTTPS port numbers with the actual packet payload; explain whether TLS or HTTP bodies are recoverable | PCAP, proxy/receiving record |
| PX04 | Show whether DNS response addresses and queried names in the PCAP are sufficient to prove an HTTP upload; contrast the proper claim standard | PCAP, DNS CSV, proxy |
| PX05 | Reconstruct the separate controller session and outward-facing flow by time, topology and source ports. Avoid conflating the two connections | NetFlow, controller, PAM, PCAP |
| PX06 | Analyze routine status traffic as a false positive. Produce an evidence matrix separating maintenance authorization, endpoint and destination | Governance, file/process/network |
| PX07 | Calculate the difference between `bytes_src_to_dst` in NetFlow, TCP packets present in this lightweight trace and actual archive byte length; explain why they differ | NetFlow, PCAP, real ZIP, proxy |
| PX08 | Find two plausible benign network observations in background noise and state the extra evidence needed before escalating either one | PCAP, synthetic index, policy |
| PX09 | Write a two-paragraph limitations section specifying which sources are genuinely independent versus derived/modelled | Provenance, manifest, observations |
| PX10 | Reassess containment sequencing when raw packet data, privileged-session records, volatile logs and restored ACL state have different preservation risks | Controller, SPAN, Windows, custody |
| PX11 | Map each observable intrusion stage to a detection opportunity; give a proposed SIEM rule without treating service-account access alone as proof | Identity, controller, sensor, file, proxy |
| PX12 | Write an executive determination with *supported*, *inconclusive* and *unsupported* claims, and three specific collection tasks for a real investigation | At least four different source families |

## Analyst tooling

```bash
python3 tools/generate_synthetic_pcap.py --check
sha256sum evidence/11_packet_fixture/synthetic_network_fixture.pcap
python3 tools/workbench.py inventory
# If tshark is installed:
tshark -r evidence/11_packet_fixture/synthetic_network_fixture.pcap -q -z io,phs
tshark -r evidence/11_packet_fixture/synthetic_network_fixture.pcap -Y 'tcp.flags.syn == 1 && tcp.flags.ack == 0' -T fields -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport
```

Windows PowerShell may use `py -3` and `Get-FileHash`. Wireshark is optional and available under a free license. Do **not** scan any address or assume a network connection is required.

## Grading

These are **12 ungraded specialist exercises**, complementing—not replacing—Q01–Q30. Suggested peer-review scale per task: 0 (not supported), 1 (single observation), 2 (correct multi-source linkage), 3 (alternative hypothesis and time constraints), 4 (reproducible, clear uncertainty and operational consequences). Suggested total 48 points is for internal author review, not an HTB guarantee.

## Chain of custody and limitations

Do not conflate the SHA-256 of a generated test PCAP with the SHA-256 of a real acquisition. This dataset is recreated by `tools/generate_synthetic_pcap.py`; `tools/refresh_evidence_hashes.py` registers its digest in `manifest/SHA256SUMS.txt`. Regenerate evidence, rebuild the student ZIP and rerun all tests together. Adding generated PCAP does **not** satisfy an independently captured native-PCAP requirement.
