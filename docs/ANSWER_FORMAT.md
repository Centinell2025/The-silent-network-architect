# Answer format and evidence standard

Questions Q01-Q24 expect **one exact value or a specified pair of values**. Q25-Q30 expect reasoned explanations with citations and a bounded confidence judgment. These formats are author guidance and are not claimed to be HTB's final grading configuration.

| Answer type | Format | Avoid |
|---|---|---|
| Timestamp | `YYYY-MM-DDTHH:MM:SSZ` exactly UTC | Local device time without calibration |
| Seconds | Non-negative base-10 integer | Phrases like "around ten minutes" |
| Account, hostname, ticket, rule, revision, object or session | Exact case-sensitive literal from artifact | Nicknames or guessed extensions |
| SHA-256 | 64 lowercase hex digits | Partial hash, SHA-1 or spaces |
| Two filenames | Alphabetical filenames separated by a single semicolon | Full UNC paths and unsupported guesses |
| Network destination | IPv4 literal printed in evidence | Hostname instead of requested IP |
| HTTP response | 3-digit status integer | "Success" |
| Interpretation | Supported claim → exact source IDs → alternative → limitation → confidence | Overclaiming actor identity |

## Evidence citations
Example **format only** (not a case solution):
`evidence/01_environment/asset_inventory.csv :: row AS-000 :: hostname field`.

A meaningful conclusion should refer to different source families (e.g. source-governance plus device-audit; network telemetry plus endpoint behavior), not two duplicate rows of the same generated file.

## Confidence labels
- **High (within the simulation):** corroborated observations from at least two distinct modeled systems with compatible times and values.
- **Moderate:** one strong observation with partial corroboration or a plausible unresolved alternative.
- **Low:** inference or ambiguous record with missing corroboration.
- **Unsupported:** theory not established by available evidence.

No score, external accreditation or real-world forensic authenticity is implied by these labels.
