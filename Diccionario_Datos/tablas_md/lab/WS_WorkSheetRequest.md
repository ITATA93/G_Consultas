# lab.WS_WorkSheetRequest

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Web Services**. Integración con sistemas externos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WKSR_ParRef | varchar | PK |  | NO | WS_WorkSheet Parent Reference |
| WKSR_CreatedDate | date |  |  | SI | Created Date |
| WKSR_Number | double |  |  | NO | Number |
| WKSR_PatientBBPack | varchar |  |  | SI | Patient or BBPack |
| WKSR_PrintedDate | date |  |  | SI | Printed Date |
| WKSR_PrintedTime | time |  |  | SI | Printed Time |
| WKSR_RequestsEntered | double |  |  | SI | Requests Entered |
| WKSR_RowId | varchar |  |  | NO | - |
| WKSR_Status | varchar |  |  | SI | Status |
| WKSR_UserSite_DR | varchar |  | FK | SI | User Site DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*