# Assessment and review contract
**Status:** author-side candidate, not HTB approval.

- Q01-Q24: precise, deterministic answers (timestamps in UTC `YYYY-MM-DDTHH:MM:SSZ`, identifiers and lowercase SHA-256 as printed). Exact spelling matters.
- Q25-Q30: short evidence-based analyst conclusions evaluated by a human rubric.
- Total proposed weighting: 24 x 3 = 72 points; 6 x 4 = 24 points; 4 points for properly cited final incident synopsis = 100.
- Reviewer can convert reasoning prompts into individually scored fact fields if their automated grader does not support narrative answers.

## Reasoning rubric (each Q25-30, 0-4)
0 unsupported or irrelevant; 1 unsupported hypothesis; 2 one source and qualified uncertainty; 3 two independent sources and alternative tested; 4 two+ sources, exact IDs, justified confidence, clear limitation and defensible business action.

## Quality gates
1. Every exact question corresponds to visible student evidence.
2. Important conclusions require independent corroboration.
3. Clock correction is documented and unambiguous.
4. Approved window, action, asset and ticket all assessed separately.
5. Data transfer evidence triangulates filename/hash/size, network flow, application/proxy and receipt.
6. Normal maintenance, normal outbound telemetry and unrelated users are plausible distractors.
7. Persistence survives restoration of temporary network controls.
8. Hash checks pass and no answer-key file is distributed to players.
9. Human attribution remains explicitly unproved; no guessing from account name.
10. Learner report includes operational containment and recovery prioritization.

## Review caveat
Technical rigor is designed to support high difficulty; **Insane** classification is a target, not an independently validated acceptance result.
