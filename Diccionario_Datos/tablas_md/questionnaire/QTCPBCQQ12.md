# questionnaire.QTCPBCQQ12

> Patient Behaviour Observation Chart : Psychotic Symptoms

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Behaviour Observation Chart : Psychotic Symptoms

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q12Q1 | date |  |  | SI | Date |
| Q12Q10 | varchar |  |  | SI | Other Type |
| Q12Q2 | time |  |  | SI | Time |
| Q12Q3 | varchar |  |  | SI | Type |
| Q12Q4 | varchar |  |  | SI | Situation / Trigger |
| Q12Q5 | varchar |  |  | SI | What happened? |
| Q12Q6 | varchar |  |  | SI | What did you do? |
| Q12Q7 | varchar |  |  | SI | Behavioural outcome |
| Q12Q8 | varchar |  |  | SI | Notes |
| Q12Q9 | varchar |  |  | SI | Staff |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*