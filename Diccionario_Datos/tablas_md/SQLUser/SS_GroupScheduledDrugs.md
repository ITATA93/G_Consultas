# SQLUser.SS_GroupScheduledDrugs

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSSDC_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSSDC_Accept | varchar |  |  | SI | Accept |
| SSSDC_Check | varchar |  |  | SI | Check |
| SSSDC_Childsub | double |  |  | NO | Childsub |
| SSSDC_Collect | varchar |  |  | SI | Collect |
| SSSDC_Completed | varchar |  |  | SI | Completed  |
| SSSDC_Disposal | varchar |  |  | SI | Disposal |
| SSSDC_Order | varchar |  |  | SI | Allowed to Prescribe/Order |
| SSSDC_Pack | varchar |  |  | SI | Pack |
| SSSDC_Pending | varchar |  |  | SI | Pending  |
| SSSDC_Rejected | varchar |  |  | SI | Rejected |
| SSSDC_Return | varchar |  |  | SI | Return |
| SSSDC_RowId | varchar |  |  | NO | - |
| SSSDC_SchedDrug_DR | bigint |  | FK | SI | Des Ref to Scheduled Drug |
| SSSDC_ViewAccepted | varchar |  |  | SI | View Accepted |
| SSSDC_ViewCheck | varchar |  |  | SI | View Checked |
| SSSDC_ViewCollected | varchar |  |  | SI | View Collected |
| SSSDC_ViewCompleted | varchar |  |  | SI | View Completed  |
| SSSDC_ViewDisposal | varchar |  |  | SI | View Disposals |
| SSSDC_ViewPacked | varchar |  |  | SI | View Packed |
| SSSDC_ViewRejected | varchar |  |  | SI | View Rejected |
| SSSDC_ViewReturns | varchar |  |  | SI | View Returns |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*