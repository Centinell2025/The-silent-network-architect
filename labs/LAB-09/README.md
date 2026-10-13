# LAB-09 — Análisis PCAP sintético

**Dificultad:** Expert · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Inspecciona las estructuras de los paquetes y evalúa qué hechos no pueden demostrarse. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-09 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-09-C1
**Problema:** Documenta metadatos de los paquetes e identifica claramente su origen sintético.

**Fuentes obligatorias:**
- `evidence/11_packet_fixture/synthetic_network_fixture.pcap`
- `evidence/11_packet_fixture/CAPTURE_PROVENANCE.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-09-C2
**Problema:** Comprueba coincidencias y ausencias entre la captura sintética y NetFlow.

**Fuentes obligatorias:**
- `evidence/11_packet_fixture/CAPTURE_PROVENANCE.csv`
- `evidence/05_network/netflow.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-09-C3
**Problema:** Contrasta representación Zeek y paquetes modelados sin fingir dos adquisiciones independientes.

**Fuentes obligatorias:**
- `evidence/11_packet_fixture/CAPTURE_PROVENANCE.csv`
- `evidence/10_background/zeek_conn.log`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-09/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-09 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
