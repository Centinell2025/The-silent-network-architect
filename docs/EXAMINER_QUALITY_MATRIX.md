# Examiner quality assessment — expanded evidence extension

**No answers, flags, passwords or instructor solutions in this file.**

The examiner should perform a genuine blind solve of the 30 canonical questions and use the 12 supplementary packet-analysis exercises as an additional quality check.

## Acceptance matrix (0–4 per dimension; author target 4)

| Dimension | A 4/4 requires | A weak answer indicates |
|---|---|---|
| Evidence integrity | Independent hash verification of ZIP/PCAP/evidence manifest | Assuming a printed digest is proof |
| Chronology | UTC correction with bounded NTP data and transition references | Confusing edge local timestamps with UTC |
| Authorization | Ticket, asset, action, approval and session all separately assessed | Assuming ticket text confers authority |
| Identity | Principal, device and human clearly distinguished | Claiming a person's identity from a shared endpoint |
| Observability | Switch packet ingest assessed separately from heartbeat | Treating green SIEM status as healthy capture |
| Data-transfer chain | Archive members, byte size, hash, endpoint flow, proxy and receipt | Treating TLS port / flow bytes as full content |
| Packet analysis | Demonstrates what the synthetic PCAP can and cannot establish | Claiming it proves real exfiltration or TLS contents |
| False-positive control | Compares benign maintenance against suspected misuse | Labeling every unusual event malicious |
| Recovery | Balances preservation, isolation, integrity and continuity | Restoring an ACL without investigating persistence |
| Reproducibility | Investigator can derive answers from delivered files without author-only hints | Depends on hidden scripts or missing files |

## Blind test record

Record reviewer ID (pseudonymous), version SHA, environment/tool versions, initial hypothesis, time to first confirmed breach of authorization, timestamp normalization calculation, network and export findings, 30-question exact score, 12 exercise scores, incorrect hypotheses, ambiguities, number of hints and final recommendation.

## Still requiring external validation

- At least two experienced analysts who did not author the material.
- Genuine independent telemetry from a controlled VM capture, if the author wishes to claim native realism. The new PCAP is **constructed offline**, not acquired from actual packet observations.
- HTB examiner review, IP and submission approval, and categorization.

**Beacon of the Eagle LLC is the creator; Northbridge Systems is a fictional scenario.**
