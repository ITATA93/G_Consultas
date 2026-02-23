# Tools_Upload.TU_GroupDetails

**Schema:** Tools_Upload
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUGRUN_Action | varchar |  |  | SI | Next Action  |
| TUGRUN_AutoProgress | bit |  |  | SI | Auto Progress Yes/No |
| TUGRUN_CreateDate | date |  |  | SI | Create Date  |
| TUGRUN_CreateTime | time |  |  | SI | Create Time  |
| TUGRUN_Date | date |  |  | SI | Start Date  |
| TUGRUN_Group_DR | bigint |  | FK | SI | Link to Set |
| TUGRUN_ImportFileClient | varchar |  |  | SI | LastImportedFile (Client) |
| TUGRUN_ImportFileServer | varchar |  |  | SI | LastImportedFile (Server) |
| TUGRUN_Message | varchar |  |  | SI | Last Message |
| TUGRUN_SetList | varchar |  |  | SI | List of "linked" RunIDs from Sets - contains $List... |
| TUGRUN_Status_DR | varchar |  | FK | SI | Entry status - from STDT UploadGroupStatus |
| TUGRUN_Time | time |  |  | SI | Start Time  |
| TUGRUN_UpdateDate | date |  |  | SI | Date updated |
| TUGRUN_UpdateTime | time |  |  | SI | Time updated |
| TUGRUN_UpdateUser_DR | bigint |  | FK | SI | User  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*