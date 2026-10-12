# Reviewer handoff — The Silent Network Architect

**Proposed author:** Beacon of the Eagle LLC / Centinell Suite Defense  
**Scenario company:** Northbridge Systems, fictional  
**Claimed maturity:** fully packaged **candidate exercise**; not yet a verified Insane Sherlock.

## Fast reviewer route (no spoilers)
1. [Student download](../downloads/The-Silent-Network-Architect-Student.zip) is self-contained and does not contain a solution key.
2. Open `START_HERE.md`, then `docs/SCENARIO.md`.
3. Use `questions/INVESTIGATION.md`, `tools/workbench.py` and `templates/ANSWER_SHEET.csv`.
4. Validate the evidence with `python3 tools/validate_evidence.py`.
5. Check release QA via GitHub Actions or `python3 tests/test_package.py` and `python3 tests/test_case_logic.py` when using the **repository** (tests are author-side, not required in student ZIP).
6. Evaluate scope, ambiguity and answer format against `docs/ANSWER_FORMAT.md`, not an informal response expectation.

## Deliverable inventory
| Item | Location | Access |
|---|---|---|
| Scenario / architecture / identities | `docs/` | Student and reviewer |
| 30 main questions | `questions/INVESTIGATION.md` | Student and reviewer |
| 10 extra ungraded reasoning prompts | `questions/EXPERT_CORRELATION.md` | Optional |
| Data and synthetic export | `evidence/` | Student and reviewer |
| Answers worksheet and analyst report | `templates/` | Student and reviewer |
| Integrity manifest | `manifest/SHA256SUMS.txt` | Student and reviewer |
| Automated evidence and question checks | `tests/` | Repository author / QA |
| Final instructor solution with **real screenshots** | Separately supplied by author | **Not yet completed** |

## Scope and integrity disclosures
All logs are *modeled synthetic telemetry*. The Zeek-format traffic is **not** a PCAP and the Windows-like table is **not** EVTX. Embedded external address space and domains are reserved for documentation. No malware, 8GB memory image, E01 disk evidence, real people or third-party licensed materials are included. This package uses only standard free analysis tools. No claim is made that HTB has reviewed or agreed to compensate the author.

## What reviewers can verify now
- Contents are internally consistent and explicitly sourced.
- Participant evidence is accessible offline on common systems.
- Time offsets, identity paths, governance scope and data-transfer receipts are testable.
- Proposed findings require confirmation across source families.
- The student ZIP should open successfully and match repository evidence exactly.

## Honest open issues before official submission
HTB requires a **full intended investigation write-up with screenshots showing how to answer every question**; that deliverable still needs to be produced from actual analysis and privately delivered. To justify Insane, build more genuine multi-OS source artifacts and run independent blind solves; more synthetic noise alone is insufficient. Q25-Q30 narrative prompts may need exact-format replacement if the target grader supports only static answers.

Official requirements: https://help.hackthebox.com/en/articles/8463668-sherlocks-submission-requirements

### IP and reviewer coordination
This repository's author credit is not a transfer of intellectual property. If submission terms prohibit public source distribution before review, agree the required visibility and private delivery mechanism before submitting. Do not put instructor answers in the public repository.

## Reviewer selection: grading format
The primary 30-question case contains six narrative tasks. If the deployment requires exact answers for all 30, use the six non-spoiler alternatives in `questions/STATIC_GRADING_CANDIDATE.md`, and read `docs/GRADER_HANDOFF.md` before agreeing on a grading contract. The alternate has **not** been selected or accepted by HTB staff.
