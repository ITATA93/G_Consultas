# questionnaire.QTCPDARQQ7

> Peritoneal Dialysis Assessment Record : Peritoneal equilibration test (pet) study

**Schema:** questionnaire
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Assessment Record : Peritoneal equilibration test (pet) study

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q7Q1 | date |  |  | SI | Date |
| Q7Q2 | varchar |  |  | SI | Transport classification |
| Q7Q3 | varchar |  |  | SI | 24 hour urine volume, Residual Renal Function (RRF... |
| Q7Q4 | varchar |  |  | SI | Comment |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*