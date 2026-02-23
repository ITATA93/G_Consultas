# questionnaire.QTCAHPRHLSAQQ61

> Lumbar Spine Assessment : Movement Loss / Muscle Power

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Lumbar Spine Assessment : Movement Loss / Muscle Power

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q61Q1 | varchar |  |  | SI | Movement |
| Q61Q2 | numeric |  |  | SI | Major |
| Q61Q3 | varchar |  |  | SI | Pain |
| Q61Q4 | numeric |  |  | SI | Muscle Power /5 |
| Q61Q5 | numeric |  |  | SI | Moderate |
| Q61Q6 | numeric |  |  | SI | Minimum |
| Q61Q7 | numeric |  |  | SI | Nil |
| Q61Q8 | varchar |  |  | SI | Deviation |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*