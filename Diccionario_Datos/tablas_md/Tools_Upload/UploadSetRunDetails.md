# Tools_Upload.UploadSetRunDetails

**Schema:** Tools_Upload
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUSRUN_CCRSession | varchar |  |  | SI | CCR Credentials |
| TUSRUN_CreateDate | date |  |  | SI | Create Date  |
| TUSRUN_CreateTime | time |  |  | SI | Create Time  |
| TUSRUN_Date | date |  |  | SI | Start Date  |
| TUSRUN_Set_DR | bigint |  | FK | SI | Link to Set |
| TUSRUN_Status_DR | varchar |  | FK | SI | Entry status - from STDT UploadStatus |
| TUSRUN_Time | time |  |  | SI | Start Time  |
| TUSRUN_UpdateDate | date |  |  | SI | Date updated |
| TUSRUN_UpdateTime | time |  |  | SI | Time updated |
| TUSRUN_UpdateUser_DR | bigint |  | FK | SI | User  |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*