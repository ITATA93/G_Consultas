# questionnaire.QTCPBCQQ10

> Patient Behaviour Observation Chart : Physical aggression

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Behaviour Observation Chart : Physical aggression

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q10Q1 | date |  |  | SI | Date |
| Q10Q10 | varchar |  |  | SI | Staff |
| Q10Q2 | time |  |  | SI | Time |
| Q10Q3 | varchar |  |  | SI | Type |
| Q10Q4 | varchar |  |  | SI | Other type |
| Q10Q5 | varchar |  |  | SI | Situation / Trigger |
| Q10Q6 | varchar |  |  | SI | What happened? |
| Q10Q7 | varchar |  |  | SI | What did you do? |
| Q10Q8 | varchar |  |  | SI | Behavioural outcome |
| Q10Q9 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*