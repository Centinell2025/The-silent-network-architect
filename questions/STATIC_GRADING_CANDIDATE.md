# HTB-style exact-answer option — provisional, spoiler-free

This is a **grading-format alternative**, not a separate Sherlock or an officially validated platform specification. The primary case contains Q01-Q30 in `INVESTIGATION.md`. Keep **Q01–Q24 unchanged**. If the target reviewer requires every Sherlock question to use a deterministic string, use the six replacement prompts below in place of **Q25–Q30** and treat the original six analysis questions as the final ungraded analyst report. Do not submit both versions as 36 distinct graded questions.

The answers for the six alternatives must be derived from multiple exhibits and verified against the **private** instructor key. Exact capitalization, seconds and UTC normalization matter.

| Position | Proposed exact-answer replacement | Response type |
|---|---|---|
| Q25 | Which exact Zeek `uid` identifies the connection whose source/destination IP and ports match the suspicious HTTPS upload flow in `netflow.csv`? | Zeek connection UID |
| Q26 | After applying the documented, time-bounded edge clock correction, what is the exact UTC timestamp of `EDGE-072`'s `traffic_rule_match`? | ISO 8601 UTC timestamp |
| Q27 | Which exact Windows scheduled task name was registered on the jump host under the service principal and subsequently executed as SYSTEM? | Original task path |
| Q28 | What Windows Security Event ID describes the local Security log clear following the scheduled-task registration? | Decimal integer |
| Q29 | How many whole seconds elapsed between the suspicious outbound proxy POST and the corresponding receiving-object receipt? | Decimal integer |
| Q30 | What exact NTP sample ID supports correction of the edge device's local timestamps during the incident? | NTP sample ID |

## Reviewer workflow
1. Choose *either* the narrative version (Q25–Q30 original, if essay grading is available) or this exact-answer alternative **before publishing**.
2. Verify there is precisely one accepted value for each question; verify the same value under Windows and Linux parsing.
3. Capture the actual analysis commands and output in the **private** write-up, for each of the six alternatives.
4. Check that questions are not solved solely by reading an author's documentation instead of analyzing the supplied artifacts.
5. Keep the original free-response reasoning tasks as a supplemental executive report — they assess thinking better than static flags.

Both options are provisional. HTB staff decide whether a proposed question form, difficulty and scoring method meets platform requirements.
