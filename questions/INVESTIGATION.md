# The Silent Network Architect — Investigator Questions
**Case:** NB-IR-2026-104 | **Difficulty design target:** Insane (not calibrated or HTB-approved)

## Your assignment
Northbridge Systems is a **fictional** organization. Determine whether the interruption of network monitoring was an authorized maintenance effect or part of an unauthorized operation. You must demonstrate **how** your answers follow from evidence. Only explicitly supported claims receive credit.

This is a **30-question, exact-answer** version suitable for examiner review. Each question asks for a uniquely specified value. The investigative method itself is the challenge: timeline reconstruction, bounded device clock correction, authorization beyond ticket labels, multi-hop identity correlation, separating routine from suspect telemetry, sample-archive integrity, and persistence after restoration.

**Mandatory evidence standard:** For each answer, include the requested literal plus supporting file/row IDs in your private worksheet. Use at least two *different source families* wherever possible; a repeated log extract is not independent corroboration. All timestamps must be **UTC**, `YYYY-MM-DDTHH:MM:SSZ`. When asked for seconds or byte counts, answer in base-10 integer form with no units. Use exact case, punctuation and leading zeroes for identifiers. Answer only from the supplied material.

### Phase 1 — Approval boundary, identity and access (WHO / WHAT / WHY)

1. **Q01 — Authority laundering.** Identify the **approved change ticket ID** that was reused as a label for a successful controller operation outside the ticket's permitted asset and action scope. Verify the original approval against a controller audit row.
2. **Q02 — Shared privileged session.** Identify the **privileged session ID** linking the same service principal to both an edge firewall exception and disabling the mirrored network sensor, despite the permitted change scope.
3. **Q03 — Policy-violating principal.** Identify the **account name** that both performed a remote-interactive jump-host login and authenticated the controller session, although service-account interactive access was disallowed.
4. **Q04 — Shared device origin.** Determine the **hostname** bound by DHCP to the source IP of that prohibited remote-interactive login during the lease interval. Do **not** give a human name.
5. **Q05 — Endpoint correlation key.** Give the **Windows logon_id** needed to join that remote-interactive logon to the later packaging/upload processes on the jump host.
6. **Q06 — Unauthorized exception request.** Give the **ticket ID** of the edge exception request that was still unapproved when control-plane changes were applied.

### Phase 2 — Controller and firewall clock reconstruction (WHERE / WHEN / HOW)

7. **Q07 — Crossing the boundary.** Give the **destination IPv4 address** denied by the baseline edge policy, permitted in the temporary revision, and reached by the later suspicious upload flow.
8. **Q08 — Configuration provenance.** Give the **first configuration revision ID** that permitted the destination in Q07, confirmed in both a controller event and the config snapshots.
9. **Q09 — Normalize a device clock.** Give the **exact UTC time** that the exception was applied, derived from the edge device's local `apply_exception` time and the independently recorded clock offset; confirm the controller event time.
10. **Q10 — Identify the traffic match.** Give the **edge_record_id** whose corrected local time falls inside the suspicious HTTPS NetFlow connection and whose 5-tuple endpoints match it.
11. **Q11 — Precision correlation.** Give the **exact corrected UTC time** of the traffic match in Q10; show the offset calculation, not just the unsynchronized device string.

### Phase 3 — Hidden monitoring blackout (WHAT / WHEN / WHY)

12. **Q12 — Sensor blind spot.** Give the **mirror_id** whose administrative disable is supported by both controller audit and switch packet counters while the SIEM agent heartbeat remained healthy.
13. **Q13 — Blackout start.** Give the **exact UTC disable timestamp** from the mirrored-switch transition, corroborated by a controller operation.
14. **Q14 — Blackout end.** Give the **exact UTC restoration timestamp** from the enabled-switch transition, corroborated by controller audit.
15. **Q15 — Quantify the gap.** Calculate the **total elapsed seconds** between the controller-supported disable and restore transitions. Do not use the later SOC alert as the start.
16. **Q16 — Detection lag.** Calculate the **integer number of seconds** between the actual mirror disable and the first medium-severity mirror-feed SOC alert.
17. **Q17 — Misleading health signal.** Give the exact **agent_heartbeat field value** recorded for NB-SIEM-01 during a zero-packet mirror-ingest observation, showing why endpoint health was an insufficient proxy for capture.

### Phase 4 — Protected files and outbound transfer (HOW / WHERE / WHAT)

18. **Q18 — Source of data.** Give the **two protected-file basenames** read by the controller-session principal and then found inside the export archive. Sort alphabetically and join with exactly one semicolon, without spaces.
19. **Q19 — Bind archive to session.** Give the **catalog_id** for the archive produced on the jump host while capture was disabled and whose creator logon ID matches the suspicious endpoint process chain.
20. **Q20 — Verify content, not a claim.** Calculate the **lowercase SHA-256** of the actual archived export file, and compare it to the catalog, proxy claim and receipt.
21. **Q21 — Check claimed transfer size.** Give the exact **byte length** of the actual exported archive that matches the application-level upload/receipt records. Do not confuse it with TCP flow overhead.
22. **Q22 — Correlate network tuple.** Give the **Zeek-format uid** for the connection whose origin IP/port and destination IP/port match the NetFlow upload; contrast it with the benign monitoring connection.
23. **Q23 — Resolve the destination.** Give the exact **DNS queried hostname** whose answer and querying endpoint match that upload, recorded before the POST.
24. **Q24 — Application identification.** Give the **proxy request_id** that jointly matches the network-flow endpoints, exported size, exported digest and subsequent receiving record.
25. **Q25 — HTTP result.** Give the **three-digit HTTP response status** shared by that upload's proxy request and the correlated receiving-object audit.
26. **Q26 — Receiving record.** Give the exact **object_id** of the receipt whose source/destination, content length and digest match the packaged archive.
27. **Q27 — Receipt lag.** Calculate the **whole seconds** between the correlated proxy POST timestamp and the matching receiving-object timestamp.

### Phase 5 — Persistence, cleanup and recovery boundary (WHAT / WHEN / SO WHAT)

28. **Q28 — Persistence registration.** Give the **task_event_id** for the task registered under the service principal on the jump host, which later ran under SYSTEM after network-mirror restoration.
29. **Q29 — Evidence cleanup.** Give the **Windows Security numeric Event ID** of the security audit log-clear event that followed the suspicious task registration.
30. **Q30 — Restored network state.** Give the **revision ID** that re-established the edge rule's deny baseline after the suspicious transfer but before the observed log-clear event.

## Required ungraded DFIR decision report
Complete `templates/ANALYST_REPORT.md` and the additional exercises in `questions/EXPERT_CORRELATION.md`. Your report must answer **who/what/when/where/how/why**, distinguish proof from inference, explain the limits of synthetic evidence and human attribution, identify affected business functions, and propose prioritized containment, evidence preservation and recovery. The report tests expert judgment, but the 30 prompts above define the exact-answer candidate.

**Research ethics:** Do not scan any host or contact any destination. All accounts, logs, IPs and infrastructure are synthetic. The true human actor and method of initial credential access remain unproven.
