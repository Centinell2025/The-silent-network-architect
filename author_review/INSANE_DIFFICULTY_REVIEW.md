# Difficulty engineering review — Insane candidate (author-only)

**Publisher:** Beacon of the Eagle LLC | **Program:** Centinell Suite Defense
**Scenario:** fictional Northbridge Systems | **Version:** canonical Q01–Q30 (12 October 2026)

## Meaningful increase in investigation difficulty

The former question bank contained too many direct requests for the contents of one field in one CSV. The canonical [30 questions](../questions/INVESTIGATION.md) now require staged cross-source reconstruction and exact values derived from that investigation. The intent is to test how investigators separate the real signal from benign activity, not merely whether they can use `grep`.

| Stage | Evidence dependency | Failure mode the player must avoid |
|---|---|---|
| Change approval and account | Governance + controller + PAM + Windows + DHCP | Assuming a reused ticket label is authorization or that an account equals a human |
| Firewall timeline | NTP calibration + device-local audit + config snapshots + NetFlow | Treating edge local clock as UTC or equating firewall rules with observed traffic |
| Monitoring blind spot | Core switch counters + controller audit + SIEM heartbeat + SOC alert | Concluding packet monitoring is healthy solely because the agent is green |
| Data access and transfer | File audit + endpoint chain + real sample ZIP + hashes + DNS + NetFlow + Zeek-format + proxy + receipt | Equating network-flow overhead with archive bytes or trusting a hash string without calculating it |
| Persistence and cleanup | Task Scheduler + Windows audit + controller restore + later execution | Claiming system recovery because ACL/SPAN was restored or declaring an unexamined executable malicious |

## Demonstrable current strengths

- 30 canonical exact-answer prompts, staged in five investigative phases.
- Additional open-ended professional-analysis questions that test competing hypotheses, evidence strength and containment.
- SHA-256 manifest and executable checksum / ZIP parity tests.
- Offline cross-platform Python workbench and a student package without private answer key.
- Actual 1,133-byte benign sample ZIP (not only a filename/hash reference) for verifying content.
- Transparent synthetic provenance and evidence limitations.
- Separate private instructor document with the intended command sequence, exact answers and source references.
- Company attribution seal clearly outside the fictional evidence records.

## Insane acceptance test — not yet passed

**An Insane label requires evidence beyond this author's own assertion.** HTB describes an expert, multi-faceted challenge that may take up to five days; duration is a range, not a promise or an assessment of this exercise.

Before asking for Insane classification:

1. Replace or augment author-generated normalized CSVs with **native, independently analyzable artifacts** captured in a controlled local lab (e.g., genuine EVTX/Sysmon, Linux journal/auth and PCAP from the isolated scenario).
2. Add materially plausible legitimate background activity and complex false-positive possibilities; make major attack steps hard to identify from curated labels alone.
3. Independently execute the full intended solve and capture **real screenshots demonstrating each of the 30 exact answers**, plus clock calculations, archive digest and important corroborations.
4. Have two experienced, independent DFIR analysts solve without any hints or privileged author material; record time-to-detection, contradictions, wrong turns and uncertainty.
5. Evaluate each exact-answer question for only one accepted output; confirm numeric/time representation and ensure no public tests, README or repository history compromise the surprise.
6. Complete a confidential instructor package for HTB including scenario, all questions, exact keys, walkthrough, screenshots, architecture and non-PII declarations.
7. Discuss whether public availability of this pre-submission Git history is appropriate; **deleting a clue from HEAD does not erase it from earlier commits**. A separate clean private submission repository can mitigate future exposure.

## What an examiner should *not* infer

- Passing CI validates programmed integrity checks, **not Insane difficulty** or independent authenticity of generated telemetry.
- A forged-looking ticket or an unusual service logon is not independently proof of a specific human adversary.
- The sample archive and receipt model do not prove real-world information theft.
- A generated screenshot or console mockup does not replace a genuine investigator screenshot required by HTB.
- This document is not an assertion of approval, guaranteed compensation or security certification.

**Internal recommendation:** use the current package for a structured private dry-run. Do not call the project Insane-ready until the above gates are verified. Difficulty is an outcome measured with solvers, not a numeric label assigned by the author.
