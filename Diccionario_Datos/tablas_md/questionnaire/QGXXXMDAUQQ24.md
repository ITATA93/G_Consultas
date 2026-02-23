# questionnaire.QGXXXMDAUQQ24

> Day Assessment Unit : CTG

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Day Assessment Unit : CTG

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q24Q1 | varchar |  |  | SI | Baby Number |
| Q24Q2 | numeric |  |  | SI | Fetal heart baseline |
| Q24Q3 | varchar |  |  | SI | 3 Accelerations |
| Q24Q4 | varchar |  |  | SI | Unreactive |
| Q24Q5 | varchar |  |  | SI | Variability |
| Q24Q6 | varchar |  |  | SI | Decelerations |
| Q24Q7 | varchar |  |  | SI | Difficult to interpret |
| Q24Q8 | varchar |  |  | SI | Acceptable |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*