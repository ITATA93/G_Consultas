# questionnaire.QTCSDCQQ06

> Syringe Driver Checklist : Syringe driver checks

**Schema:** questionnaire
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Syringe Driver Checklist : Syringe driver checks

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q06Q1 | date |  |  | SI | Date |
| Q06Q2 | time |  |  | SI | Time |
| Q06Q3 | numeric |  |  | SI | Confirm volume remaining in syringe (mL) |
| Q06Q4 | varchar |  |  | SI | Site checked |
| Q06Q5 | varchar |  |  | SI | Site changed |
| Q06Q6 | varchar |  |  | SI | Light checked |
| Q06Q7 | varchar |  |  | SI | Check performed by |
| Q06Q8 | numeric |  |  | SI | Confirm volume remaining in syringe (mL) |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*