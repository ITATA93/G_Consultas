# questionnaire.QGXXXISSQQ35

> Insulin Sliding Scale : Administration Record:

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Insulin Sliding Scale : Administration Record:

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q35Q1 | date |  |  | SI | Administration Date: |
| Q35Q2 | time |  |  | SI | Administration Time: |
| Q35Q3 | varchar |  |  | SI | Results (mmol/L) |
| Q35Q4 | varchar |  |  | SI | Dose (Units): |
| Q35Q5 | varchar |  |  | SI | Executed by: |
| Q35Q6 | varchar |  |  | SI | Overseer: |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*