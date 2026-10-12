# Network architecture -- fictional Northbridge Systems

This is the required multi-host architecture map for the training case. All addresses are simulated and non-routable or documentation-only.

```mermaid
flowchart LR
  WS22["NB-WS-22 10.42.10.77<br/>Shared operations seat"] -->|Remote interactive logon| J["NB-JUMP-01 10.42.10.25<br/>Windows jump host"]
  WS11["NB-WS-11 10.42.10.44<br/>Engineering workstation"] -->|Approved maintenance| NMS["NB-NMS-01 10.42.30.12<br/>Network monitoring"]
  J -->|Delegated privileged session| CTRL["NB-NET-CTRL 10.42.30.15<br/>Controller"]
  J -->|Protected file reads| FS["NB-FS-01 10.42.20.18<br/>Architecture files"]
  CTRL -->|Configure SPAN-7| SWITCH["NB-CORE-SW-02 10.42.0.14<br/>Core switch"]
  CTRL -->|Configure ACL-EGRESS-24| EDGE["NB-EDGE-01 10.42.0.1<br/>Edge firewall"]
  SWITCH -.->|SPAN mirrored packets| SIEM["NB-SIEM-01 10.42.30.30<br/>Capture sensor"]
  J -->|HTTPS to outside| EDGE
  NMS -->|Normal health POST| EDGE
  EDGE -->|Documentation network| EXT["External reserved IP space<br/>RFC 5737"]
  DC["NB-DC-01 10.42.10.10<br/>Identity and DNS"] -.-> J
  BKP["NB-BKP-01 10.42.20.40<br/>Backup service"] -.-> NMS
```

## Trust boundaries
- **VLAN 110:** workstations and jump access; identity required before privileged movement.
- **VLAN 120:** protected servers; read operations must meet explicit asset and principal authorization.
- **VLAN 130:** monitoring and controller; SPAN state is **not** proven by an endpoint-agent heartbeat.
- **VLAN 199:** control network and perimeter transport; policy changes require action-specific approval.
- **Outside:** reserved documentation addresses such as 203.0.113.0/24 and 198.51.100.0/24; do not contact.

The diagram documents expected connections and trust zones; it is not a proof that every drawn path was used during this incident. Validate each actual event from the exhibits. This is a topology diagram, not a traffic-capture replacement.
