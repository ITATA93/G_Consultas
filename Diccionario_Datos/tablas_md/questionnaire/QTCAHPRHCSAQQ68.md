# questionnaire.QTCAHPRHCSAQQ68

> Cervical Spine Assessment : Movement Loss / Muscle Power

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cervical Spine Assessment : Movement Loss / Muscle Power

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q68Q1 | varchar |  |  | SI | Movement |
| Q68Q2 | numeric |  |  | SI | Major |
| Q68Q3 | numeric |  |  | SI | Moderate |
| Q68Q4 | numeric |  |  | SI | Minimum |
| Q68Q5 | numeric |  |  | SI | Nil |
| Q68Q6 | varchar |  |  | SI | Pain |
| Q68Q7 | numeric |  |  | SI | Muscle  power /5 |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*