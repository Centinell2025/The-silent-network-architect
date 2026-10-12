# Scoring and ambiguity-control handoff

**Candidate:** The Silent Network Architect | **Case:** NB-IR-2026-104

## Principles
- A question must be answerable using **only material included in the student archive**.
- Each exact item must have one stable expected value, without guessing case, spelling, locale or units.
- Questions that demand judgment must state the scoring dimensions; an essay must **not** be silently treated as an exact-match answer.
- A corroborating source can confirm the event but may not contain the same requested field (e.g. alert time vs. sensor-disabling time); do not mistake proximity for duplicate exact evidence.
- Answers involving device-local edge times must be normalized inside the calibration interval, with original and corrected values recorded privately.

## Primary scoring version
`questions/INVESTIGATION.md`: Q01–Q24 exact values plus Q25–Q30 qualitative explanations; model rubric in `docs/GRADING_AND_QA.md`.

## Alternate exact-only version
`questions/STATIC_GRADING_CANDIDATE.md`: Q01–Q24 from primary file unchanged, Q25–Q30 replaced with deterministic questions about network linkage, bounded clock correction, scheduled task, log-clear event, transfer-to-receipt latency and NTP calibration. Original six narratives move to optional analytic report.

## Pre-submission checklist
- [ ] Reviewer approves which scoring method HTB supports
- [ ] Author verifies one correct answer against source evidence for every graded item
- [ ] Author documents source path, exact row/ID, extraction command, normalization and expected value privately
- [ ] A second analyst independently derives all answers, without author hints
- [ ] Every answer has a real screenshot from the author's actual forensic analysis
- [ ] No answer key or screenshots accidentally included in public ZIP
- [ ] Reviewer has confidential instructor package via approved private mechanism

**No claim is made that the current candidate already satisfies all items.**
