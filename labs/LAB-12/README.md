# LAB-12 — Informe ejecutivo de respuesta

**Dificultad:** Expert · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Redacta una decisión operativa que distinga hechos, hipótesis y acciones reversibles. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-12 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-12-C1
**Problema:** Separa hechos confirmados y dudas sobre el corte de visibilidad.

**Fuentes obligatorias:**
- `evidence/06_control_plane/controller_audit.csv`
- `evidence/08_soc/siem_health.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-12-C2
**Problema:** Ordena acciones de preservación y contención según riesgo de perder evidencias.

**Fuentes obligatorias:**
- `evidence/04_endpoint/scheduled_tasks.csv`
- `evidence/03_identity/windows_security.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-12-C3
**Problema:** Evalúa las afirmaciones defendibles sobre exportación y destino.

**Fuentes obligatorias:**
- `evidence/09_export/export_catalog.csv`
- `evidence/07_receipts/receiving_object_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-12/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-12 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
