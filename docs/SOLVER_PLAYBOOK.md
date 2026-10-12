# Reproducible DFIR playbook — no answers

The case can be analyzed on **Ubuntu, Kali, macOS or Windows** with Python 3 and standard system utilities. No port scanning or attack tooling is necessary.

## 1. Verify your materials
Extract `The-Silent-Network-Architect-Student.zip` and run:

```bash
python3 tools/validate_evidence.py
python3 tools/workbench.py inventory
```

The manifest covers the evidence, including the nested synthetic reference export. Preserve the original downloadable ZIP. Work on copies of files if you need to sort or transform them.

## 2. Form two competing hypotheses
One hypothesis should explain the monitoring anomaly as expected maintenance or telemetry failure. A competing hypothesis should assess whether privileged actions were outside ticket scope. Do not declare either one true at intake. Use the change governance and source-of-truth policy records to test both.

## 3. Index artifacts without prejudging them

```bash
python3 tools/workbench.py timeline --limit 25
python3 tools/workbench.py search "CHG-" --limit 20
python3 tools/workbench.py inspect evidence/06_control_plane/controller_audit.csv
```

You can filter time and file scope:

```bash
python3 tools/workbench.py timeline --after 2026-10-06T02:00:00Z --before 2026-10-06T02:20:00Z --source 06_control_plane --limit 25
python3 tools/workbench.py search "health" --source 08_soc --limit 15
```

Search reads evidence files and prints source path and line; it is not an answer generator.

## 4. Normalize clocks
Before combining control-plane and edge-firewall records, read the bounded NTP calibration in `evidence/06_control_plane/ntp_samples.csv`. State the conversion formula, offset in seconds, uncertainty, and range over which you used it. You can inspect timestamps directly using the workbench timeline. Never assume all strings that look like timestamps have the same timezone.

## 5. Triangulate identity and scope
Join `logon_id` across Windows and endpoint records and `session_id` across privileged-access and controller audit. Evaluate **account permission, allowed assets, allowed action and ticket approval separately**. A ticket reference embedded in a log message can be forged or misapplied.

## 6. Evaluate network and collection claims
Use independent-looking but **synthetically generated** evidence models: DNS queries, flow records, proxy requests, a receiving-object receipt and archive catalog. Compare timestamps, network endpoints, requested operation, byte lengths, digest, and filename/member metadata. A self-reported checksum or proxy status is not enough by itself to prove data contents.

## 7. Reconstruct evidence gaps
Compare the switch SPAN administrative state and packet count against the SIEM ingest and agent heartbeat. Calculate the interval of reduced collection from explicit transition timestamps. Analyze scheduling and log-clear records separately from restored network rule state. Do not assert a task binary is malicious without its code or trustworthy behavioral evidence.

## 8. Deliver a professional case disposition
Populate `templates/ANSWER_SHEET.csv` (Q01-Q30) and `templates/ANALYST_REPORT.md`. Classify findings as **supported, inconsistent or inconclusive**. For critical decisions, cite two artifact types. Explain where synthetic artifacts cannot support a real-world factual assertion.

### Analyst environment troubleshooting
- Python reports 'file not found': work from the extracted package root, or provide a repo-relative path.
- PowerShell: use `py -3` instead of `python3`.
- A match is too broad: provide `--source` or a narrower search phrase.
- ZIP errors: redownload the package and compare checksums before continuing.
- A single-source answer is ambiguous: write that limitation in your report rather than inventing precision.
