# questionnaire.QGXXXMOPROCQQ01

> Obstetric procedures : Procedure details

**Schema:** questionnaire
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Obstetric procedures : Procedure details

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q01Q1 | date |  |  | SI | Date |
| Q01Q10 | varchar |  |  | SI | Procedure |
| Q01Q2 | time |  |  | SI | Time |
| Q01Q3 | varchar |  |  | SI | Procedure |
| Q01Q4 | varchar |  |  | SI | Indication |
| Q01Q5 | varchar |  |  | SI | Benefits and risks explained to patient |
| Q01Q6 | bit |  |  | SI | Discussed procedure with mother |
| Q01Q7 | bit |  |  | SI | Consent obtained |
| Q01Q8 | varchar |  |  | SI | Discussed procedure with mother |
| Q01Q9 | varchar |  |  | SI | Consent obtained |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*