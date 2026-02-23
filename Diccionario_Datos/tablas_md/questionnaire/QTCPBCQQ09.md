# questionnaire.QTCPBCQQ09

> Patient Behaviour Observation Chart : Verbal Disruption

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Behaviour Observation Chart : Verbal Disruption

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q09Q1 | date |  |  | SI | Date |
| Q09Q10 | varchar |  |  | SI | Staff |
| Q09Q2 | time |  |  | SI | Time |
| Q09Q3 | varchar |  |  | SI | Type |
| Q09Q4 | varchar |  |  | SI | Other type |
| Q09Q5 | varchar |  |  | SI | Situation / Trigger |
| Q09Q6 | varchar |  |  | SI | What happened? |
| Q09Q7 | varchar |  |  | SI | What did you do? |
| Q09Q8 | varchar |  |  | SI | Behavioural outcome |
| Q09Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*