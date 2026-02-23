# SQLUser.OEC_SchemaGroupItem

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCGITM_ParRef | varchar | PK |  | NO | OEC_Schema Parent Reference |
| ChildQ99DR | - |  |  | SI | Child Reference: Staff present |
| Q87Q1 | - |  |  | SI | Joules given |
| Q87Q2 | - |  |  | SI | Care provider |
| Q87Q3 | - |  |  | SI | Date |
| Q87Q4 | - |  |  | SI | Time |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SCGITM_Childsub | double |  |  | NO | Childsub |
| SCGITM_CreatedDate | date |  |  | SI | Created Date |
| SCGITM_CreatedTime | time |  |  | SI | Created Time |
| SCGITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SCGITM_ItmMast_DR | varchar |  | FK | NO | Order Item |
| SCGITM_RowId | varchar |  |  | NO | - |
| SCGITM_UpdatedDate | date |  |  | SI | Updated Date |
| SCGITM_UpdatedTime | time |  |  | SI | Updated Time |
| SCGITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SCGITM_UploadStatus | varchar |  |  | SI | DrugUpload loaded status, used for refresh load (s... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*