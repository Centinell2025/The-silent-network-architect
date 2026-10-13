# LAB-06 — Procesos y salto privilegiado

**Dificultad:** Advanced · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Reconstruye una cadena de procesos y eventos desde el acceso remoto al empaquetado. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-06 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-06-C1
**Problema:** Relaciona inicio de sesión con procesos ejecutados en el jump host.

**Fuentes obligatorias:**
- `evidence/03_identity/windows_security.csv`
- `evidence/04_endpoint/process_activity.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-06-C2
**Problema:** Distingue los procesos relevantes de actividad normal de fondo.

**Fuentes obligatorias:**
- `evidence/04_endpoint/process_activity.csv`
- `evidence/10_background/endpoint_activity.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-06-C3
**Problema:** Relaciona lectura de archivos y empaquetado sin afirmar ejecución de malware no demostrado.

**Fuentes obligatorias:**
- `evidence/04_endpoint/file_audit.csv`
- `evidence/04_endpoint/process_activity.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-06/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-06 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
