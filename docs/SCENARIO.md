# Incident brief: an apparently healthy network

**Case:** NB-IR-2026-104  
**Organization:** Northbridge Systems (invented training organization)  
**Date:** 6 October 2026 (UTC unless noted)  
**Assignment:** External incident responder attached to the Security Operations Center.

Northbridge's small SOC protects an enterprise network with a core switch, a perimeter firewall, a network configuration controller, a jump server for privileged access, central monitoring, directory services and protected architecture records. Maintenance windows are routine; engineering work often produces benign authentication, health telemetry and network configuration records. The team relies on several different event streams to reconstruct incidents.

After midnight, the monitoring team confirmed a scheduled agent maintenance operation. Shortly afterward, a low-confidence alert reported falling mirrored-network ingestion. Yet the sensor heartbeat dashboard remained green. A network engineer suggested the same approved change might be responsible; a ticket reference also appears inside the network-controller records. The SOC escalated only after an unfamiliar outbound upload was observed.

The head of operations asks for a report that answers: **Did maintenance cause the telemetry gap? Was anyone using privileged infrastructure beyond its approved scope? Was protected architecture material copied outside? Was a recurring access mechanism left behind? What can be safely contained without destroying evidence?**

An architecture team is concerned about partner interconnect information. Leadership wants **proof, not speculation**, of the records involved, the permitted change boundary, and what the artifacts do *not* tell us. Some records use inconsistent clocks, while unrelated legitimate system activity overlaps the same window.

## Your role
You have read-only access to sanitized, independently modeled records collected into this package. You have no direct access to original systems, no entitlement to interrogate live accounts, no third-party confirmation, and no unredacted personal information. Do not make claims beyond this evidence.

## Investigation objective
Reconstruct a defendable UTC timeline; separate legitimate operations from unauthorized changes; correlate identity, network-control, host file access, DNS/flow/proxy, receiving receipt and persistence; identify gaps; and recommend containment and recovery without over-attributing human identity.

## Evidence custody
Work on copies, check SHA-256 values against `manifest/SHA256SUMS.txt`, record your transformation steps and preserve source filenames. The simulated company and all artifacts are fictional. Hashes test package integrity, not the authenticity of a real incident.

## Submission expectation
Complete `questions/INVESTIGATION.md`, an analyst report in `templates/ANALYST_REPORT.md`, and an answer sheet listing exact file and record references. An explanation is strongest when it compares competing explanations and explicitly acknowledges uncertainty.
