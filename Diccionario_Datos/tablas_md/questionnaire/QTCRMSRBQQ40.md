# questionnaire.QTCRMSRBQQ40

> Review of Motor / Sensory Regional Blocks : Secondary cannula site check

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Review of Motor / Sensory Regional Blocks : Secondary cannula site check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q40Q1 | date |  |  | SI | Date |
| Q40Q2 | time |  |  | SI | Time |
| Q40Q3 | varchar |  |  | SI | Condition of site |
| Q40Q4 | varchar |  |  | SI | Cannula left in situ |
| Q40Q5 | varchar |  |  | SI | Condition of cannula |
| Q40Q6 | varchar |  |  | SI | Site check notes |
| Q40Q7 | varchar |  |  | SI | Checked by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*