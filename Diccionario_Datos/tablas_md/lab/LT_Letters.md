# lab.LT_Letters

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTMN_RowID | varchar | PK |  | NO | - |
| LTMN_Date | date |  |  | SI | Last Date |
| LTMN_LetterCode | varchar |  |  | NO | Letter Code |
| LTMN_NumberPendingPatients | numeric |  |  | SI | Number of Pending Patients |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*