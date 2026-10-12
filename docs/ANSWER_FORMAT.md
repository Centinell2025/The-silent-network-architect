# Candidate answer format and evidence standard

All 30 graded questions in `questions/INVESTIGATION.md` have an exact output format; additional professional analysis is ungraded by default. These are **author conventions**, subject to reviewer approval.

| Requested type | Output |
|---|---|
| Event time | `YYYY-MM-DDTHH:MM:SSZ` (UTC, zero milliseconds) |
| Whole seconds or bytes | Decimal integer with **no** commas or unit suffix |
| IDs, hostnames, accounts, SHA-256, IPs | Exact case and punctuation from source, 64 lowercase hex for SHA-256 |
| Two filenames | Alphabetical basenames joined by one semicolon, no space |
| HTTP response | Three-digit numeric string |
| Qualitative report | Claim → primary source file:row → corroboration → alternative → confidence and limitation |

## Submission worksheet
Fill `templates/ANSWER_SHEET.csv` with an answer and cited source line IDs for each Q01–Q30. Record an offset calculation where relevant. Exact outputs are important for automated grading, but **evidence** is important for the instructor assessment.

## Confidence
High: independent modeled sources with consistent fields/times; Moderate: corroboration incomplete; Low: weak inference; Unsupported: absent from evidence. These levels are a training convention, not a professional certification.

## Attribution
The evidence can link a service account to a logon, a jump host and controller actions. It **cannot** determine a real human's identity from a shared workstation and logs.
