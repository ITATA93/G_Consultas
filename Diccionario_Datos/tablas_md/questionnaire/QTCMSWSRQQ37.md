# questionnaire.QTCMSWSRQQ37

> Medical Social Worker Screening and Reassessment : Reassessment / Follow-up

**Schema:** questionnaire
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Medical Social Worker Screening and Reassessment : Reassessment / Follow-up

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q37Q1 | date |  |  | SI | Date |
| Q37Q2 | time |  |  | SI | Time |
| Q37Q3 | varchar |  |  | SI | Reassessment / Follow-Up |
| Q37Q4 | varchar |  |  | SI | Social worker's name |
| Q37Q5 | numeric |  |  | SI | Social worker's ID No |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*