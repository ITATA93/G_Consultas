# questionnaire.QTCRMSRBQQ20

> Review of Motor / Sensory Regional Blocks : Primary cannula site check

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Review of Motor / Sensory Regional Blocks : Primary cannula site check

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q20Q1 | date |  |  | SI | Date |
| Q20Q2 | time |  |  | SI | Time |
| Q20Q3 | varchar |  |  | SI | Condition of site |
| Q20Q4 | varchar |  |  | SI | Cannula left in situ |
| Q20Q5 | varchar |  |  | SI | Condition of cannula |
| Q20Q6 | varchar |  |  | SI | Site check notes |
| Q20Q7 | varchar |  |  | SI | Checked by |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*