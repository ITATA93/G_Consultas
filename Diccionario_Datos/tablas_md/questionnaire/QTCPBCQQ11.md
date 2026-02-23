# questionnaire.QTCPBCQQ11

> Patient Behaviour Observation Chart : Restlessness

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Behaviour Observation Chart : Restlessness

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | date |  |  | SI | Date |
| Q11Q10 | varchar |  |  | SI | Staff |
| Q11Q2 | time |  |  | SI | Time |
| Q11Q3 | varchar |  |  | SI | Type |
| Q11Q4 | varchar |  |  | SI | Other type |
| Q11Q5 | varchar |  |  | SI | Situation / Trigger |
| Q11Q6 | varchar |  |  | SI | What happened? |
| Q11Q7 | varchar |  |  | SI | What did you do? |
| Q11Q8 | varchar |  |  | SI | Behavioural outcome |
| Q11Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*