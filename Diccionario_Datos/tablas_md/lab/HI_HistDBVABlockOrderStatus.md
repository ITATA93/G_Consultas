# lab.HI_HistDBVABlockOrderStatus

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HIVAOS_ParRef | varchar | PK |  | NO | HI_HistDayBookVisitAccessBlock Parent Reference |
| HIVAOS_Completed | varchar |  |  | SI | Completed |
| HIVAOS_DateCompleted | date |  |  | SI | Date Completed |
| HIVAOS_ProcedureStatus_DR | varchar |  | FK | SI | Procedure Status DR |
| HIVAOS_RowID | varchar |  |  | NO | - |
| HIVAOS_Sequence | varchar |  |  | NO | Sequence |
| HIVAOS_TimeCompleted | time |  |  | SI | Time Completed |
| HIVAOS_UserCompleted_DR | varchar |  | FK | SI | User Completed DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*