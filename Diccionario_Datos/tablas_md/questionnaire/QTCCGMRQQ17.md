# questionnaire.QTCCGMRQQ17

> Continuous Glucose Monitoring Record : Carbohydrate ratio (grams/Unit)

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Continuous Glucose Monitoring Record : Carbohydrate ratio (grams/Unit)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q17Q1 | time |  |  | SI | Time from |
| Q17Q2 | time |  |  | SI | Time to |
| Q17Q3 | numeric |  |  | SI | Ratio |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*