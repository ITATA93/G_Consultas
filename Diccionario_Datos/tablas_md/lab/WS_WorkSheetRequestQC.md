# lab.WS_WorkSheetRequestQC

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSRQ_ParRef | varchar | PK |  | NO | WS_WorkSheetRequest Parent Reference |
| WKSRQ_Comment | varchar |  |  | SI | Comment |
| WKSRQ_Date | date |  |  | SI | Date |
| WKSRQ_Position | varchar |  |  | NO | Position |
| WKSRQ_QC_RowID_DR | varchar |  | FK | SI | QC RowID DR |
| WKSRQ_Result | varchar |  |  | SI | Result |
| WKSRQ_RowID | varchar |  |  | NO | - |
| WKSRQ_TestItem_DR | varchar |  | FK | NO | Test Item DR |
| WKSRQ_Time | time |  |  | SI | Time |
| WKSRQ_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*