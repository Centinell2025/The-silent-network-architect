# CVE statement, data generation and provenance

## CVEs
**No CVE or exploitation of a known software vulnerability was used** to produce the current synthetic evidence. This challenge depicts a simulated misuse of access credentials, improper change approval scope, control-plane configuration changes, missing telemetry assurance and possible persistence. It does not attribute the initial credential acquisition to any specific vulnerability. If the scenario later introduces a genuine CVE, list the exact ID, impacted versions, exploitation preconditions and method used to generate reproducible artifacts.

## PII and PCI
**No real PII or PCI data is included.** Northbridge Systems, employee usernames, ticket numbers, network design text and log timestamps were fabricated. There are no real email addresses, card numbers, government IDs or payment transactions. The sample export contains two small benign synthetic topology files; it is not a real stolen data set. Documentation-only IP addresses and .example domains were used deliberately.

## Evidentiary basis
- Each CSV represents a separately modeled telemetry feed with an explicit synthetic origin, not a native vendor log.
- ZIP contents are harmless, deterministic reference material; hashing detects post-publication changes, not authenticity of a claimed real collection.
- The receipt is a synthetic receiving-system observation and is **not** an independent third-party attestation.
- Event ID 4624 / 4698 / 1102 labels imitate common Windows audit semantics, but data is not exported EVTX.
- Clock offset and UTC reconstruction are bounded to the documented calibration interval.
- The actor's biological identity, original credential compromise method and long-term command-and-control intent remain unproven.

## Open-source, noncommercial analysis
Python 3 standard library, csv/sha256sum/unzip or 7-Zip, Wireshark/TShark (if a real capture is added later), jq, Volatility 3 (if memory is added later) and common Linux shell utilities are sufficient or appropriate. No paid forensic software is necessary for this version.

## Improving dataset realism before Insane consideration
Generate native evidence from an isolated Kali/Ubuntu/Windows lab where possible, include believable business background (ordinary maintenance, benign DNS, approved file reads, normal egress), preserve vendor-native fields, capture traffic independently, then have external solvers validate all answers.
