# questionnaire.QTCPDARQQ6

> Peritoneal Dialysis Assessment Record : Peritoneal dialysis adequacy

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Peritoneal dialysis adequacy

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q6Q1 | date |  |  | SI | Date |
| Q6Q2 | varchar |  |  | SI | Total Creatinine Clearance (CCL) |
| Q6Q3 | varchar |  |  | SI | Residual Creatinine Clearance (CCL) |
| Q6Q4 | varchar |  |  | SI | Dialysis Creatinine Clearance (CCL) |
| Q6Q5 | varchar |  |  | SI | Total KT/V |
| Q6Q6 | varchar |  |  | SI | Residual KT/V |
| Q6Q7 | varchar |  |  | SI | 24 hour urine Volume, Residual Renal Function (RRF... |
| Q6Q8 | varchar |  |  | SI | Comment |
| Q6Q9 | varchar |  |  | SI | Dialysis KT/V |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*