# questionnaire.QTCENDONPRQQ38

> Endoscopy Nursing Procedure Report : Procedure Observations

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endoscopy Nursing Procedure Report : Procedure Observations

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q38Q1 | varchar |  |  | SI | Observation time |
| Q38Q2 | numeric |  |  | SI | Pulse (bpm) |
| Q38Q3 | numeric |  |  | SI | SpO2 (%) |
| Q38Q4 | numeric |  |  | SI | Oxygen delivery rate (l/min) |
| Q38Q5 | varchar |  |  | SI | Oxygen delivery method |
| Q38Q6 | varchar |  |  | SI | Level of consciousness |
| Q38Q7 | varchar |  |  | SI | Pain status |
| Q38Q8 | varchar |  |  | SI | Comments |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*