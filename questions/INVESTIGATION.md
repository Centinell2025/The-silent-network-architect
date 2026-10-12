# Analyst Investigation -- The Silent Network Architect
**Case:** NB-IR-2026-104  **Target level:** Insane

Use exact UTC timestamps, filenames, session IDs, rule IDs and SHA-256 values. Cite record IDs / file paths for every response. **For consequential conclusions, corroborate with two independent evidence sources.** Do not infer a person's identity from account credentials alone.

## Phase I -- Establish what can be trusted (WHAT / WHERE / WHEN)
1. [Q01] Which precise device did the initial SOC alert name as the affected network control-plane asset?
2. [Q02] At what exact UTC time did the SOC alert fire?
3. [Q03] Which approved change ticket is cited in the suspicious network-controller remarks?
4. [Q04] Which asset is permitted by that approved ticket's *authorized_asset* field?
5. [Q05] Which ticket covering an edge-rule exception is explicitly not approved, despite time overlap?
6. [Q06] What device clock offset (in **seconds ahead of UTC**) must be used to interpret the edge firewall records?
7. [Q07] At what **corrected UTC time** was the unauthorized edge ACL revision applied?

## Phase II -- Trace access and control (WHO / HOW)
8. [Q08] Which account performed the first suspicious interactive authentication on the jump host?
9. [Q09] Which source IP initiated that interactive session?
10. [Q10] What exact Windows logon type identifies its interactive remote character?
11. [Q11] Which Windows `logon_id` links that login to later endpoint process activity?
12. [Q12] Which asset hostname did the DHCP inventory associate with the suspicious source IP?
13. [Q13] Which privileged-access `session_id` then connects the jump host to the network controller?
14. [Q14] Which `rule_id` was modified to allow the suspicious outbound network path?
15. [Q15] Which `config_revision` first applied that modification?

## Phase III -- Reconstruct the blind spot (WHY / WHEN)
16. [Q16] Which `mirror_id` was administratively disabled on the core switch?
17. [Q17] What is the exact UTC timestamp at which its collection was restored?
18. [Q18] How many seconds elapsed between disable and restoration?
19. [Q19] What health value did the SIEM agent report *while* SPAN counters were zero, illustrating why green health was misleading?

## Phase IV -- Prove or disprove the data-loss allegation (WHAT / WHERE / HOW)
20. [Q20] Which **two exact filenames** in the file-audit trail were read from the protected server before packaging? List them alphabetically separated by a semicolon.
21. [Q21] What is the SHA-256 of the archived export present in `evidence/09_export/`?
22. [Q22] What exact destination IP received the outbound transfer according to NetFlow?
23. [Q23] What HTTP response status confirms that the proxy accepted the outbound upload operation?
24. [Q24] Which `object_id` appears in the independent receiving-object receipt?

## Phase V -- Draw defensible conclusions (WHY / SO WHAT)
25. [Q25] Why does the approved CHG label not authorize the controller, switch, file server or edge-rule actions? Cite exact ticket scope and audit operations.
26. [Q26] Distinguish the normal NMS maintenance and its telemetry upload from the suspicious jump-host transfer. Identify exact differentiating sources and fields.
27. [Q27] What evidence demonstrates an unauthorized *collection-and-transfer sequence*, rather than merely a large network flow? Address file reads, packaging, DNS, proxy, NetFlow and receiving receipt; distinguish observable fact from inferred motive.
28. [Q28] Which scheduled task created later in the timeline represents potential persistence, and which subsequent log event indicates anti-forensic behavior? Explain what remains unverified.
29. [Q29] What can and cannot be concluded about the human adversary from the observed service principal, jump-host session, source IP and DHCP lease?
30. [Q30] Produce a five-step prioritized containment, evidence-preservation and recovery plan. Explain which controls must be revalidated even if the firewall rule and SPAN mirror were returned to their previous values.

## Required final conclusion
A 250-400-word incident determination with **supported, unsupported and inconclusive** findings, three UTC milestones and at least four artifact references from distinct sources. Do not equate a plausible story with proof.
