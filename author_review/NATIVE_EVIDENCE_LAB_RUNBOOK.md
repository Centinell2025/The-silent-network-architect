# Native evidence capture plan — isolated training environment

This is a **future lab collection runbook**, not a claim that native artifacts have already been acquired. Only capture systems you own or are explicitly authorized to operate. Never probe public addresses from the fictional case. Beacon of the Eagle LLC is the author; Northbridge Systems is imaginary.

## Minimum lab
One Windows evaluation VM acting as a workstation or jump host, one Ubuntu server VM with private network access, and a Kali forensic workstation. Keep the case on a **host-only or otherwise isolated** hypervisor network and use neutral demonstration traffic only. Record OS versions, collector versions, timezone, VM clock offset, observer network interface and data-generation steps.

## Windows — Security and Sysmon evidence
In a Windows VM under an administrator account, after enabling the appropriate audit policies and running permitted test actions:

```powershell
mkdir C:\ForensicExports -ErrorAction SilentlyContinue
wevtutil epl Security C:\ForensicExports\Security.evtx
wevtutil epl System C:\ForensicExports\System.evtx
Get-FileHash C:\ForensicExports\Security.evtx -Algorithm SHA256
```

Sysmon EVTX may be exported **only if the actual Sysmon provider has been installed and configured** on that training VM. Never fabricate EVTX metadata. Sanitize account names and sensitive machine IDs before public distribution without destroying event relationships.

## Linux — journal / authentication
From an isolated Ubuntu VM, collect a bounded window containing both normal and controlled test events:

```bash
sudo journalctl --utc --output=short-iso-precise > ubuntu-journal-utc.log
sudo journalctl --utc --output=json > ubuntu-journal.json
sha256sum ubuntu-journal-utc.log ubuntu-journal.json
```

Do not copy real system journals with personal usernames, keys or organization data into a public challenge. Use an isolated test image with fictional lab accounts.

## PCAP — only your own isolated interface
From Kali or Ubuntu attached to the host-only lab network:

```bash
sudo tcpdump -i <LAB_INTERFACE> -s 0 -w authorized-lab-traffic.pcap 'tcp port 443 or udp port 53'
# In another terminal, generate only benign authorized traffic within the lab.
# Stop tcpdump manually, then:
sha256sum authorized-lab-traffic.pcap
```

Replace the interface placeholder with your own training NIC; **do not copy/paste literally**. No contact with documentation IP addresses, external public networks or unauthorized third parties is needed. Ensure the PCAP contains genuine observed local traffic, not fake frames labeled as captures.

## Evidence admission checks
1. Preserve raw EVTX, JSON journal and PCAP plus collection method and collection time; compute hashes before transformation.
2. Derive normalized CSV secondarily (not instead of the native files). Cross-check native timestamps and event IDs.
3. Mix expected maintenance, denied actions, ordinary DNS and noise with intentionally abnormal but harmless controlled events.
4. Have an independent reviewer prove each case question from native exhibits; update the student ZIP, manifest and answer key together.
5. Use `python3 tools/build_student_zip.py --write` and existing repo tests after **any** student-source edit; rerun GitHub Actions.

Native capture collection cannot be completed by a model without access to those running VMs. This document is a reproducibility and safety plan.
