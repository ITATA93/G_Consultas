# questionnaire.QGXXXMANIQQ40

> Intrapartum Assessment : CTG

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intrapartum Assessment : CTG

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q40Q1 | varchar |  |  | SI | Baby number |
| Q40Q2 | numeric |  |  | SI | Fetal heart baseline |
| Q40Q3 | varchar |  |  | SI | 3 accelerators |
| Q40Q4 | varchar |  |  | SI | Unreactive |
| Q40Q5 | varchar |  |  | SI | Variability |
| Q40Q6 | varchar |  |  | SI | Decelerations |
| Q40Q7 | varchar |  |  | SI | Difficult to interpret |
| Q40Q8 | varchar |  |  | SI | Acceptable |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*