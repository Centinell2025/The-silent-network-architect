# Host processes, services and identity context

All systems, applications, principals and user handles are fictitious. Product-like names denote simulation artifacts and do not imply a real installed product. Values below describe the expected environment, not necessarily evidence of attacker activity.

| Host | OS / device type (simulated) | Important services or processes | Purpose |
|---|---|---|---|
| NB-WS-22 | Windows 11 operations workstation | RDP client, workstation logon session | Shared engineering operations seat |
| NB-WS-11 | Windows 11 engineering workstation | SSH / approved maintenance shell | Normal patch maintenance |
| NB-JUMP-01 | Windows Server jump host | Windows Security, Windows Task Scheduler, controller client, archive-util.exe, telemetry-agent.exe | Privileged transit, investigations of process ancestry and scheduled tasks |
| NB-DC-01 | Windows Server directory controller | Active Directory-like authentication audit, internal DNS | Account/session and domain resolution context |
| NB-FS-01 | Windows file server | SMB service, file auditing | Architectural documents requiring privileged read approval |
| NB-BKP-01 | Windows or Linux backup appliance | Backup service and backup monitoring | Routine background operations |
| NB-NMS-01 | Windows Server monitoring host (simulated) | nms-agent.exe, Windows Security authentication, health telemetry, scheduled maintenance | Approved engineering change target |
| NB-NET-CTRL | Linux-based controller appliance | Privileged access API and config revision audit | Network ACL and mirror management |
| NB-EDGE-01 | Network firewall appliance | ACL-EGRESS-24, local system clock, NTP telemetry | Egress control and device-local timestamps |
| NB-CORE-SW-02 | Managed switch | SPAN-7 admin counters | Sensor traffic mirroring |
| NB-SIEM-01 | Linux collector / sensor | SIEM ingest process, agent heartbeat | Ingest health and capture data |

## Identity profiles
| Principal | Expected role | Access constraints |
|---|---|---|
| m.ellis | Network engineer | Permitted maintenance actions only under explicitly approved tickets |
| s.kato | Change approver | Authorization authority for defined scope |
| j.reyes | Backup administrator | Backup activities, not network control-plane authorization |
| svc-netops | Automation service identity | Controller jobs under approved action scope; **interactive use prohibited** |
| svc-backup | Backup service identity | Backup health processes only |
| SYSTEM | Windows built-in local service identity | Could run legitimate or unauthorized scheduled tasks; not a human identity |

## Process name realism boundaries
Process labels and Windows event IDs appear in normalized, simulated tables. They are **not native EVTX/E01/PCAP exports**. A process name alone cannot establish execution trust; analysts must examine timestamps, principal, parent association, file provenance, task registration and related telemetry.

No real credentials, PII, exploit payloads or proprietary executables are included.
