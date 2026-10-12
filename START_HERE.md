# START HERE | The Silent Network Architect
> **Beacon of the Eagle LLC — Centinell Suite Defense**  
> Author attribution only. **Northbridge Systems is entirely fictional.**

## Your mission
Investigate case **NB-IR-2026-104** and deliver a defensible determination of whether an authorized network maintenance change explains the loss of visibility, or whether multiple systems were affected by an unauthorized operation. Avoid jumping to attribution or intent.

**Your inputs**: 30 staged questions, fictional network and endpoint evidence, a minimal sample export ZIP, a diagram, background traffic, and a SHA-256 manifest. **Your outputs**: answers and cited evidence, a normalized UTC timeline, and an incident report separating verified facts from inference. No real targets, malware, VM setup, proprietary tooling, Internet access or credentials are required.

## Start in five minutes
1. Download and extract `downloads/The-Silent-Network-Architect-Student.zip`, keeping the original archive untouched.
2. Open `docs/SCENARIO.md` and `docs/NETWORK_ARCHITECTURE.md` to understand the fictional environment.
3. Read `questions/INVESTIGATION.md`. Investigate rather than guessing.
4. Run the local validation and use the analyst workbench:

```bash
python3 tools/validate_evidence.py
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 15
python3 tools/workbench.py search "maintenance" --limit 12
```

On Windows PowerShell, replace `python3` with `py -3` if needed. This command-line workbench needs only the Python standard library. It does not change evidence files.

5. Copy `templates/ANALYST_REPORT.md` and `templates/ANSWER_SHEET.csv` outside the extracted evidence folder. Fill them in as you investigate.

## Rules that affect your conclusions
- Most times are UTC. The edge firewall uses local device time: correct it using contemporaneous `ntp_samples.csv` observations.
- The existence of a change ticket does not prove its authorization **for a particular operation and asset**.
- An agent's healthy heartbeat cannot establish that mirrored packet capture was operational.
- A shared workstation, account and source IP do not identify a human attacker.
- A synthetic receipt or a matching hash cannot establish an actual real-world exfiltration. Keep your claims within the **fictional scenario** and available artifacts.
- Each important conclusion needs **two independently modeled source types**, and a limitation or alternative hypothesis.

## Open tools only
Python 3, a file viewer, Git, the operating-system ZIP utilities, and optionally jq/Wireshark on genuinely captured files. No Python package installation is required. The Zeek-format and other source tables are simulated telemetry, **not captures from actual devices**.

## Next reading
- `docs/SCENARIO.md` — immersive handoff (spoiler-free)
- `docs/SOLVER_PLAYBOOK.md` — stages and reproducible analysis methods
- `docs/EVIDENCE_GUIDE.md` — source caveats, fields and time normalization
- `docs/ANSWER_FORMAT.md` — exact answer conventions
- `docs/QUALITY_ACCEPTANCE_PLAN.md` — transparent author quality gates

This candidate is not approved, sponsored or endorsed by Hack The Box. Target difficulty **Insane** remains unverified.
