# questionnaire.QTCPHRQQ03

> Identified Medication Issues : Issues

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Identified Medication Issues : Issues

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q03Q1 | date |  |  | SI | Date |
| Q03Q2 | time |  |  | SI | Time |
| Q03Q3 | varchar |  |  | SI | Issue identified |
| Q03Q4 | varchar |  |  | SI | Identified by |
| Q03Q5 | varchar |  |  | SI | Proposed action |
| Q03Q6 | varchar |  |  | SI | Person responsible |
| Q03Q7 | date |  |  | SI | Date of action |
| Q03Q8 | varchar |  |  | SI | Result of action |
| Q03Q9 | varchar |  |  | SI | Contact number |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*