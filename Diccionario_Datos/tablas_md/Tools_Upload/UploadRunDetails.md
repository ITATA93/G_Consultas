# Tools_Upload.UploadRunDetails

**Schema:** Tools_Upload
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TURUN_Action | varchar |  |  | SI | Next Action  |
| TURUN_ExportDocument_DR | bigint |  | FK | SI | LastExportedFile |
| TURUN_ImportFileClient | varchar |  |  | SI | LastImportedFile |
| TURUN_ImportFileServer | varchar |  |  | SI | LastImportedFile |
| TURUN_LastStarted | varchar |  |  | SI | Last Started |
| TURUN_Message | varchar |  |  | SI | Last Message |
| TURUN_ProgressStatus | varchar |  |  | SI | Progress Information  |
| TURUN_Sequence | integer |  |  | SI | Entry status - from  |
| TURUN_SetRun_DR | bigint |  | FK | SI | Link to RunSet |
| TURUN_SetTask_DR | bigint |  | FK | SI | Link to Task in Set |
| TURUN_StartDate | date |  |  | SI | Start Date  |
| TURUN_StartTime | time |  |  | SI | Start Time  |
| TURUN_Status_DR | varchar |  | FK | SI | Entry status - from  |
| TURUN_UpdateDate | date |  |  | SI | Date updated |
| TURUN_UpdateTime | time |  |  | SI | Time updated |
| TURUN_UpdateUser_DR | bigint |  | FK | SI | User  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*