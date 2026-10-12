# Optional expert investigation review -- multi-artifact reasoning

These questions supplement the 30 principal prompts. They are **not** new HTB graded answer fields. Their purpose is to expose weaknesses in a solver's evidence reasoning before official submission.

For each answer, provide primary record IDs, the precise join keys used, an alternate hypothesis, what would disprove your conclusion, and a business implication.

1. **Who or what is proven?** Reconstruct the complete account-to-device chain beginning at the shared workstation and ending at the privileged controller. Identify which records show an account, a network endpoint and a human; do not merge those identities.
2. **How could the malicious action blend in?** Show how a forged approval label could look legitimate in the configuration audit. Determine the authoritative record for scope and explain why the UTC change window alone cannot authorize the action.
3. **Was monitoring genuinely healthy?** Distinguish sensor heartbeat from observed packet ingestion. Quantify the capture blackout using controller, SPAN, SIEM and timing sources. Explain uncertainty introduced by polling versus actual control-plane transitions.
4. **What packet evidence actually exists?** Compare one suspicious 5-tuple in the augmented Zeek-format fixture to NetFlow, firewall device-local syslog and proxy. List which fields are measured versus represented by synthetic metadata.
5. **What crossed the boundary?** Link file access, process packaging, archive member count, hash/size, proxy request, traffic flow and the remote receiving receipt; label any evidence that is merely self-reported by the sender.
6. **Would a rushed analyst wrongly blame maintenance?** Build a false-positive comparison between normal monitoring health uploads and the suspicious jump-host transfer. Check principal, source asset, ticket-authorized action, destination and receipt type.
7. **What persists after the network restoration?** Correlate task registration, privileged session and task execution. State what the current artifacts cannot prove about the actual contents or intent of the task binary.
8. **Does log clearing erase the case?** Explain why a forwarded or previously collected event might remain available after a local Windows Security clear event, and list verification steps not supported by the existing evidence.
9. **What is the smallest defensible incident claim?** Write a five-sentence executive conclusion marking every claim supported, weakly supported, or unknown. Avoid naming a human attacker.
10. **Which preservation action is first?** Prioritize evidence sources at risk of rotation, volatile session state, network device configuration, controller audit and exported files. Explain dependencies before isolating systems.

Reviewer grading suggestion: 0-4 for each, rewarding multi-source corroboration, competing explanations, correct time normalization and non-overclaiming. These are *training rubric suggestions*, not assertions about HTB's grading implementation.
