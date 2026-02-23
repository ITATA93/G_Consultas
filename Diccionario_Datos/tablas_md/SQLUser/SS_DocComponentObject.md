# SQLUser.SS_DocComponentObject

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSDOCOBJ_RowId | bigint | PK |  | NO | - |
| SSDOCOBJ_Code | varchar |  |  | NO | Code |
| SSDOCOBJ_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSDOCOBJ_Component_DR | bigint |  | FK | SI | DesRef to Component |
| SSDOCOBJ_CreatedDate | date |  |  | SI | Created Date |
| SSDOCOBJ_CreatedTime | time |  |  | SI | Created Time |
| SSDOCOBJ_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSDOCOBJ_DateFrom | date |  |  | SI | Date From |
| SSDOCOBJ_DateTo | date |  |  | SI | Date To |
| SSDOCOBJ_Desc | varchar |  |  | NO | Description |
| SSDOCOBJ_LanguageCode | varchar |  |  | SI | Language Code |
| SSDOCOBJ_Model | varchar |  |  | SI | Model Name |
| SSDOCOBJ_Owner | varchar |  |  | SI | Owner |
| SSDOCOBJ_PageID | integer |  |  | NO | Confluence Page ID in source system - for upload u... |
| SSDOCOBJ_PageName | varchar |  |  | SI | Confluence Page Name in source system - for upload... |
| SSDOCOBJ_RegionSite | varchar |  |  | SI | Region/Site (saved for created by system={blank}, ... |
| SSDOCOBJ_System | varchar |  |  | SI | System created |
| SSDOCOBJ_UpdatedDate | date |  |  | SI | Updated Date |
| SSDOCOBJ_UpdatedTime | time |  |  | SI | Updated Time |
| SSDOCOBJ_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*