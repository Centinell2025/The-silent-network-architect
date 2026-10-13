# LAB-08 — DNS, NetFlow y proxy

**Dificultad:** Advanced · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Construye una correlación defensiva sin confundir telemetría de salud y subida anómala. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-08 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-08-C1
**Problema:** Comprueba la relación entre resolución DNS y petición de aplicación.

**Fuentes obligatorias:**
- `evidence/05_network/dns_queries.csv`
- `evidence/05_network/proxy_requests.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-08-C2
**Problema:** Une una conexión NetFlow a su petición según IP y tiempo.

**Fuentes obligatorias:**
- `evidence/05_network/netflow.csv`
- `evidence/05_network/proxy_requests.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-08-C3
**Problema:** Diferencia los recibos de una transferencia rutinaria y una operación sospechosa.

**Fuentes obligatorias:**
- `evidence/05_network/proxy_requests.csv`
- `evidence/07_receipts/receiving_object_audit.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-08/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-08 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
