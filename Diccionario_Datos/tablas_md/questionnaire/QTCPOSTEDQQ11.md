# questionnaire.QTCPOSTEDQQ11

> Postpartum Emergency Documentation : Add action(s) for postpartum pre-eclampsia / eclampsia event

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Postpartum Emergency Documentation : Add action(s) for postpartum pre-eclampsia / eclampsia event

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q11Q1 | numeric |  |  | SI | Action order number |
| Q11Q2 | time |  |  | SI | Time stamp |
| Q11Q3 | varchar |  |  | SI | Action type |
| Q11Q4 | varchar |  |  | SI | Other (specify) |
| Q11Q5 | varchar |  |  | SI | By whom |
| Q11Q6 | varchar |  |  | SI | Notes |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*