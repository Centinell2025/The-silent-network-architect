# The Silent Network Architect

> **BEACON OF THE EAGLE LLC — AUTHOR SEAL**  
> **CENTINELL SUITE DEFENSE**  
> Cybersecurity · Digital Forensics · Incident Response  
> © 2026 Beacon of the Eagle LLC — [Corporate attribution](BEACON-OWNERSHIP.md)

**Hack The Box Sherlock candidate | DFIR / Network Forensics | Target difficulty: Insane**

> A network can appear healthy while its most important evidence is being deliberately silenced.

A suspicious infrastructure change surfaces at fictional **Northbridge Systems**. Monitoring reports healthy agents, yet network visibility drops at a critical moment. A previously approved maintenance ticket appears in configuration remarks. The investigator must establish what actually occurred, normalize conflicting timestamps, distinguish authorized engineering work from misuse of a service account, verify an outbound transfer and persistent access, and reach a defensible conclusion without inferring a real-world attacker identity.

## Investigator mission
Determine **who/what/when/where/how/why**, separate facts from hypotheses, and deliver a defensible incident report supporting containment, recovery, and evidence preservation.

## Download
- [START HERE — Quick-start guide](START_HERE.md) — installation-free, step-by-step analyst workflow.
- [Immersive Scenario](docs/SCENARIO.md) — investigator assignment, background and competing hypotheses.
- [Solver Playbook](docs/SOLVER_PLAYBOOK.md) — Ubuntu, Kali, Windows and macOS instructions.
- [Answer Format & Confidence](docs/ANSWER_FORMAT.md) — consistent scoring and traceability.
- [Examiner Handoff](docs/REVIEWER_HANDOFF.md) — what reviewers can run and what is still missing.
- [Grader Handoff](docs/GRADER_HANDOFF.md) — deterministic answer and ambiguity checks.
- [Blank Analyst Report](templates/ANALYST_REPORT.md) / [Answer Sheet](templates/ANSWER_SHEET.csv) — investigation deliverables.
- [Student Evidence Package](downloads/The-Silent-Network-Architect-Student.zip) -- self-contained training package (no solutions).
- [Investigation Questions](questions/INVESTIGATION.md) -- 30 graduated challenges.
- [Optional Exact-Answer Grading](questions/STATIC_GRADING_CANDIDATE.md) -- six provisional auto-grading replacements for reviewer selection.
- [Expert Correlation Review](questions/EXPERT_CORRELATION.md) -- 10 ungraded advanced evidence exercises.
- [Case Brief](docs/CASE_BRIEF.md) -- initial SOC handoff.
- [Evidence Guide](docs/EVIDENCE_GUIDE.md) -- source descriptions, uncertainty and normalization.
- [Mixed-signal Provenance](docs/BACKGROUND_DATA_PROVENANCE.md) -- realistic-looking, explicitly synthetic background evidence.
- [Quality Acceptance Plan](docs/QUALITY_ACCEPTANCE_PLAN.md) -- remaining steps before an Insane submission.
- [Network Architecture Diagram](docs/NETWORK_ARCHITECTURE.md) -- multi-host map and trust boundaries.
- [Hosts, Services and Accounts](docs/HOSTS_SERVICES_AND_IDENTITIES.md) -- OS, processes and identities.
- [CVE, PII/PCI and Evidence Provenance](docs/CVE_PII_AND_EVIDENCE_PROVENANCE.md) -- data-generation disclosures.
- [HTB Author Readiness](docs/HTB_AUTHOR_READINESS.md) -- verified and outstanding submission gates.
- [SHA-256 Checksums](manifest/SHA256SUMS.txt) -- hashes of every text evidence file and the archived payload.

**Do not use GitHub's README alone as the challenge. Download and analyze the evidence.** No VM, offensive exploit, Internet access or real targets are required.

## Candidate metadata
| Field | Value |
|---|---|
| Sherlock title | The Silent Network Architect |
| Target category | DFIR / Network Forensics |
| Target difficulty | Insane (aspirational, subject to HTB review) |
| Investigation time | Not benchmarked; difficulty subject to blind testing |
| Scenario | Fully fabricated Northbridge Systems |
| Evidence | Multi-source synthetic records, export payload, cryptographic manifest |
| Grading | 24 precise-response questions + 6 investigative reasoning tasks |

## Design features
- Windows Security and process records, controller audit, switch SPAN counters, firewall/NTP telemetry, DNS, flow and proxy evidence, service-ticket policy, storage receipt, SIEM health and a file-export package.
- Supplemental Zeek-format connections, endpoint activity and firewall-style syslog, containing background noise and cross-source checkpoints (simulated, **not native captures**).
- Multi-hop session correlation, time-offset reconstruction, scope and authorization analysis, data-exfiltration proof, persistence, anti-forensics, false-positive elimination and confidence-scoped attribution.
- Answers must reference primary artifacts and **two independent sources** for consequential conclusions.
- Some facts can be proven; the actor's human identity **cannot** be established from the provided data.

## Repo layout
```text
docs/            case brief, chain of custody, grading guidance, ethics
evidence/        normalized synthetic investigative exhibits
manifest/        SHA256SUMS for evidence and export payload
questions/       investigation instructions and 30 questions
tools/           standard-library analyst workbench and checksum verifier
downloads/       self-contained student ZIP, no solutions\ntemplates/       blank analyst report and 30-answer worksheet
```

## Ethical and publication notice
All companies, people, logs, IP addresses, domains and exported content are **synthetic**. External networks use RFC 5737 documentation IP space; DNS uses `.example`. The archive is harmless data, not a real stolen dataset. The repo deliberately contains **no instructor answer key**. Keep solutions in a controlled private reviewer channel.

**Author portfolio:** Centinell Suite Defense / Beacon of the Eagle LLC. Northbridge Systems is a fictional training entity, not the author's actual business. Submission/acceptance and compensation are not guaranteed.

**Review status (2026-10-12):** This is an advanced *candidate prototype*, not a validated Insane Sherlock. Native forensic artifacts, a private screenshot-backed walkthrough, and blind difficulty testing remain open requirements before submission.
