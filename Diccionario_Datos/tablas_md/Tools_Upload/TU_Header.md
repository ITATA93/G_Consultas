# Tools_Upload.TU_Header

**Schema:** Tools_Upload
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUH_ChangeLog | varchar |  |  | SI | Does this Upload support the Change Log (CHANGECHE... |
| TUH_Code | varchar |  |  | NO | - |
| TUH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUH_CreateDate | date |  |  | SI | - |
| TUH_CreateTime | time |  |  | SI | - |
| TUH_Description | varchar |  |  | NO | - |
| TUH_FeatureGroup_DR | bigint |  | FK | SI | Grouping Option via FeatureGroup |
| TUH_ForbidParallelLoads | varchar |  |  | SI | Indicate if forbid parallel uploads, by default no |
| TUH_FreezeDate | date |  |  | SI | used to compare if a new freeze is required  |
| TUH_FreezeForCode | varchar |  |  | SI | Reference to the original Header (just Code)  |
| TUH_FreezeForID | varchar |  |  | SI | Reference to the original Header (ID for Reporting... |
| TUH_FreezeTime | time |  |  | SI | used to compare if a new freeze is required  |
| TUH_FreezeVersion | integer |  |  | SI | To keep freezed copies this flag indicates a "used... |
| TUH_FromDate | date |  |  | SI | - |
| TUH_GroupSequence | integer |  |  | SI | Batch / Sort Order in FeatureGroup |
| TUH_InstructionsURL | varchar |  |  | SI | URL for Instructions |
| TUH_Owner | varchar |  |  | SI | Owner |
| TUH_TemplateURL | varchar |  |  | SI | URL to Excel/CSV/XML etc. Template |
| TUH_ToDate | date |  |  | SI | - |
| TUH_UpdDate | date |  |  | SI | - |
| TUH_UpdTime | time |  |  | SI | - |
| TUH_UploadType | varchar |  |  | SI | with introducing Owner Management for this class t... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*