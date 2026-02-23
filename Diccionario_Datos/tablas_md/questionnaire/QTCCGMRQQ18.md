# questionnaire.QTCCGMRQQ18

> Continuous Glucose Monitoring Record : Insulin sensitivity (mmol / L per Unit)

**Schema:** questionnaire
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Continuous Glucose Monitoring Record : Insulin sensitivity (mmol / L per Unit)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q18Q1 | time |  |  | SI | Time from |
| Q18Q2 | time |  |  | SI | Time to |
| Q18Q3 | numeric |  |  | SI | Sensitivity |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*