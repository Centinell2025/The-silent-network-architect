# LAB-01 — Integridad y cadena de custodia

**Dificultad:** Foundations · **Escenario:** NB-IR-2026-104 · **Autor:** Beacon of the Eagle LLC

## Objetivo
Demuestra la integridad de los objetos sin confundir un hash con la autenticidad de su origen. La infraestructura de Northbridge Systems, sus personas y sus datos son ficticios. Los analistas deben presentar inferencias apoyadas en evidencias, no suposiciones.

## Preparación
Trabaja con Python 3.10+ en Kali Linux, Ubuntu o Windows; sin instalación adicional ni acceso a Internet. En la raíz del paquete extraído:

```bash
python3 labs/runner.py start LAB-01 --output student_work
python3 tools/workbench.py inventory
python3 tools/workbench.py timeline --limit 25
```

En Windows, utiliza `py -3` si `python3` no existe. Para PCAP emplea `python3 tools/packet_inspector.py summary` y para fuentes CSV, `python3 tools/workbench.py inspect evidencia.csv` cambiando la ruta por un archivo real.

## Tres ejercicios verificables

### LAB-01-C1
**Problema:** Comprueba el hash del archivo exportado frente a su catálogo y explica qué valida realmente.

**Fuentes obligatorias:**
- `evidence/09_export/export_catalog.csv`
- `evidence/09_export/network-audit-bundle.zip`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-01-C2
**Problema:** Evalúa la diferencia entre los hashes del manifiesto y la atestación externa del recibo.

**Fuentes obligatorias:**
- `evidence/07_receipts/receiving_object_audit.csv`
- `evidence/09_export/export_catalog.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.

### LAB-01-C3
**Problema:** Determina las principales limitaciones de atribución al consultar alertas y registros de identidades.

**Fuentes obligatorias:**
- `evidence/00_intake/soc_alerts.csv`
- `evidence/03_identity/windows_security.csv`

**Entrega:** conclusión concreta, dos citas con identificadores o SHA-256 calculado, explicación alternativa y nivel de confianza.


## Evaluación
Edita `student_work/LAB-01/submission.json`; después:

```bash
python3 labs/runner.py validate LAB-01 --output student_work
```

El estado PASS valida únicamente **estructura y referencias**, no demuestra que la inferencia sea correcta. El examinador revisará fuentes, precisión, incertidumbre y recomendaciones operativas. Máximo interno: 12 puntos (4 por ejercicio).
