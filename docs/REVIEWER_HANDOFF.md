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
| Private instructor solution with 30 executed-case screenshots | Delivered separately by author | **Completed privately; not present in this public repository** |

## Scope and integrity disclosures
All logs are *modeled synthetic telemetry*. The Zeek-format traffic is **not** a PCAP and the Windows-like table is **not** EVTX. Embedded external address space and domains are reserved for documentation. No malware, 8GB memory image, E01 disk evidence, real people or third-party licensed materials are included. This package uses only standard free analysis tools. No claim is made that HTB has reviewed or agreed to compensate the author.

## What reviewers can verify now
- Contents are internally consistent and explicitly sourced.
- Participant evidence is accessible offline on common systems.
- Time offsets, identity paths, governance scope and data-transfer receipts are testable.
- Proposed findings require confirmation across source families.
- The student ZIP should open successfully and match repository evidence exactly.

## Honest open issues before official submission
The private instructor write-up now includes 30 executed terminal screenshots and a replay script whose expected outputs have been checked from a self-contained confidential archive. These are executions against **simulated case exhibits**, not native captures from Windows/Linux VMs. To justify Insane, obtain realistic native artifacts where useful and perform independent blind solves; more synthetic noise alone is insufficient. All 30 questions are now exact-value prompts, but their difficulty and deterministic solutions require independent examiner verification.

Official requirements: https://help.hackthebox.com/en/articles/8463668-sherlocks-submission-requirements

### IP and reviewer coordination
This repository's author credit is not a transfer of intellectual property. If submission terms prohibit public source distribution before review, agree the required visibility and private delivery mechanism before submitting. Do not put instructor answers in the public repository.

## Reviewer selection: grading format
The current case has 30 canonical exact-answer questions in `questions/INVESTIGATION.md`; the six-question grading alternative was retired to remove ambiguity. The non-graded analyst conclusion remains mandatory educational practice. Read `docs/GRADER_HANDOFF.md` before accepting a grading configuration.
