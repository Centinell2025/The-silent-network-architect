# LAB-11 — Reglas SOC y falsos positivos

**Dificultad:** Expert · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Diseña detecciones basadas en comportamientos correlacionados y un triage proporcional. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-11 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-11-C1
**Problema:** Propón una alerta que detecte acción fuera del alcance de un ticket.

**Fuentes obligatorias:**
- `evidence/02_governance/change_tickets.csv`
- `evidence/06_control_plane/controller_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-11-C2
**Problema:** Propón una alerta por pérdida de tráfico aunque el heartbeat sea verde.

**Fuentes obligatorias:**
- `evidence/05_network/span_counters.csv`
- `evidence/08_soc/siem_health.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-11-C3
**Problema:** Propón una heurística para distinguir una subida normal de una anómala.

**Fuentes obligatorias:**
- `evidence/05_network/netflow.csv`
- `evidence/05_network/proxy_requests.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-11/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-11 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
