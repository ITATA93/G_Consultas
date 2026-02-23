# questionnaire.QGXXXMIAQQ18

> Induction Assessment : CTG

**Schema:** questionnaire
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Induction Assessment : CTG

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | varchar |  |  | SI | Fetus number |
| Q18Q2 | varchar |  |  | SI | Heart monitoring |
| Q18Q3 | numeric |  |  | SI | Baseline |
| Q18Q4 | varchar |  |  | SI | 3 accelerations |
| Q18Q5 | varchar |  |  | SI | Variability |
| Q18Q6 | varchar |  |  | SI | Decelerations |
| Q18Q7 | varchar |  |  | SI | Acceptable |
| Q18Q8 | varchar |  |  | SI | Difficult to interpret |
| Q18Q9 | varchar |  |  | SI | Reassuring |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*