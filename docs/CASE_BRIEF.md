# NB-IR-2026-104: The Silent Network Architect
**Date:** 2026-10-06 (all case UTC unless explicitly stated)
**Case class:** possible network-control-plane compromise / loss of monitoring assurance
**Organization:** Northbridge Systems, fictional
**Analyst role:** external DFIR lead with access to supplied, sanitized exhibits

## Initial SOC handoff
At 02:06:07Z, the SOC received a low-confidence signal that the mirror feeding NB-SIEM-01 may have stopped reporting packets. Endpoint heartbeat dashboards remained green. A network engineer had been carrying out an approved monitoring maintenance window earlier that night; engineers suspect routine change fallout. A change ticket tag visible in controller logs seems to support this explanation.

There is no confirmed breach classification at handoff. Determine whether this was an expected maintenance effect, a telemetry failure, or an unauthorized, coordinated action. The compliance team has asked whether topology records were copied outside the network and whether a recurring access path was left behind.

## Rules of engagement
1. Investigate only the included synthetic exhibits. No scanning or contacting any listed IP or domain.
2. Preserve original artifacts; analyze copies; verify provided hashes.
3. Treat edge device timestamps as **local device time** until corrected from independent NTP samples.
4. Do not equate an approved ticket's existence with authorization of every activity labeled with that ticket.
5. Account use, host attribution, and human identity are different evidentiary claims.
6. For each major conclusion: state the underlying rows/IDs, at least two independent evidence sources, alternative interpretations, and confidence.

## Decision deliverables
- Absolute incident timeline (UTC), including initial access, control-plane modifications, sensor visibility loss, collection, outbound transfer, persistence, restoration and anti-forensic events.
- Determination of change authorization **by action and asset**, not just by time window.
- Whether data left Northbridge, what its supported content was, and the evidence limits.
- Distinction between affected telemetry collection and healthy service heartbeat.
- Bounded containment/recovery plan protecting logs, controller history and stored evidence.
- Attribution claim that does not overstate what a shared host/service account proves.
