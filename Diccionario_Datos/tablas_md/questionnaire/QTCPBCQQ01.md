# questionnaire.QTCPBCQQ01

> Patient Behaviour Observation Chart : Patient Behaviour Observational Chart

**Schema:** questionnaire
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Patient Behaviour Observation Chart : Patient Behaviour Observational Chart

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | date |  |  | SI | Date |
| Q01Q2 | time |  |  | SI | Time |
| Q01Q3 | varchar |  |  | SI | Behaviour |
| Q01Q4 | varchar |  |  | SI | What happened before |
| Q01Q5 | varchar |  |  | SI | What happened next |
| Q01Q6 | varchar |  |  | SI | Is the person sleeping (record times) |
| Q01Q7 | varchar |  |  | SI | Persons present |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*