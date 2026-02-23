# lab.DQ_Questionare

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DQ_RowID | varchar | PK |  | NO | - |
| DQ_Date | date |  |  | SI | Date |
| DQ_Order | varchar |  |  | NO | Order Number |
| DQ_Status | varchar |  |  | SI | Status |
| DQ_Time | time |  |  | SI | Time |
| DQ_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*