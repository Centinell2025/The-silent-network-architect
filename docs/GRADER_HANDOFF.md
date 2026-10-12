# Examiner scoring handoff — canonical 30 questions

There is **one active question bank**: `questions/INVESTIGATION.md`, Q01–Q30. Questions in `questions/EXPERT_CORRELATION.md` are supplemental, ungraded expert reasoning.

## Determinism and scoring
1. Each numbered question specifies a requested field or numerical calculation. Do not accept unsupported narrative answers in place of exact values.
2. Reviewers may use a separate, **confidential** expected-answer CSV and complete write-up with source evidence and commands for each question.
3. Accept one canonically represented answer per question. Request a revision before release if answer capitalization, units, escaping or time normalization is ambiguous.
4. See `docs/ANSWER_FORMAT.md` for exact output conventions and `docs/GRADING_AND_QA.md` for qualitative judgment standards.
5. Confirm that the question bank does not depend on author-only files, real-world access or paid software.

## Human evaluation checklist
- [ ] All 30 accepted answers independently derived from the delivered student ZIP
- [ ] All source rows and required join keys shown in confidential instructor write-up
- [ ] Actual screenshot of each solution's path and required corroboration
- [ ] No alternative exact value accidentally produced by background data
- [ ] Blind test by independent experienced DFIR practitioner
- [ ] Private author write-up sent only through accepted review route

**Status:** automatic repository integrity is verified; human blind solve and genuine screenshots are still pending. An HTB difficulty classification is not self-certified.
