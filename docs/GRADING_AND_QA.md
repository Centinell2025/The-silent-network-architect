# Investigation grading and review standard
**Case:** NB-IR-2026-104 | **Publisher:** Beacon of the Eagle LLC — Centinell Suite Defense

## Candidate grading model
- 30 exact-value questions; every answer is derivable from student artifacts without access to the key.
- Recommended author test: 30 x 3 points = 90; 10 points for evidence citations and qualified final incident statement. This is **not** an official HTB scoring claim.
- Questions are deliberately sequenced to follow the investigation, not to reveal answer values through wording.
- Dates must be normalized to UTC ISO 8601 seconds. Durations and byte lengths are base-10 integers. SHA-256 is 64 lowercase hex characters. Filenames are basenames; Q18 requires alphabetical sort and one semicolon.

## Qualitative scoring (separate and ungraded by default)
For `questions/EXPERT_CORRELATION.md` and the incident report, assess: (1) source integrity, (2) at least two independent source families, (3) alternative hypotheses, (4) correct uncertainty and human-attribution limits, and (5) actionable incident containment. The investigator must not assert evidence not present.

## Difficulty validation — target Insane, not yet demonstrated
A multi-source question is not automatically Insane. Insane requires expert-level reconstruction, difficult adversary detection and measured challenge from blind solves. Minimum release gates: independently generated authentic telemetry where possible, no answer clues in public repository QA, privately verified answer key with actual source paths and commands, screenshots of the intended solution to **every** graded question, and external experienced analysts completing the challenge blind.

## Case invariants
- Ticket approval does not authorize a different asset or action.
- Account, host and human identity are not interchangeable.
- Calibrate edge device timestamps within the observed NTP window.
- A green agent heartbeat does not establish a healthy SPAN capture.
- Flow bytes include protocol overhead; the ZIP size must be checked against the archive itself and the application/receipt fields.
- A process name or scheduled task, alone, is not proof of malicious binary execution.
- All described data and observability streams are explicitly fictional, not captured from live systems.

## Release verification
Run `python3 tools/validate_evidence.py`, `python3 tools/build_student_zip.py --check` and `python3 tests/test_package.py`, plus `python3 tests/test_grading_handout.py` and the non-spoiler cross-source checks. Keep secrets and private instructor keys outside this repository.
