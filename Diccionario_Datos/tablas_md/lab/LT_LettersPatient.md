# lab.LT_LettersPatient

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTPT_ParRef | varchar | PK |  | NO | LT_Letters Parent Reference |
| LTPT_Date | date |  |  | SI | Date of Entry |
| LTPT_Patient_DR | varchar |  | FK | NO | Patient DR |
| LTPT_RowID | varchar |  |  | NO | - |
| LTPT_User_DR | varchar |  | FK | SI | User dr |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*