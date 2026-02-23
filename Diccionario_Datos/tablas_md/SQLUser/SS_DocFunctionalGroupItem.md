# SQLUser.SS_DocFunctionalGroupItem

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSDOCITM_ParRef | bigint | PK |  | NO | SSDocFunctionalGroup Parent Reference |
| SSDOCITM_Area | varchar |  |  | SI | Functional Area Code |
| SSDOCITM_Caption | varchar |  |  | NO | Link Caption |
| SSDOCITM_Childsub | double |  |  | NO | Childsub |
| SSDOCITM_Code | varchar |  |  | NO | Code |
| SSDOCITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSDOCITM_CreatedDate | date |  |  | SI | Created Date |
| SSDOCITM_CreatedTime | time |  |  | SI | Created Time |
| SSDOCITM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSDOCITM_DateFrom | date |  |  | SI | Date From |
| SSDOCITM_DateTo | date |  |  | SI | Date To |
| SSDOCITM_Desc | varchar |  |  | SI | Regional Description |
| SSDOCITM_LanguageCode | varchar |  |  | SI | Language Code |
| SSDOCITM_LocalURL | varchar |  |  | SI | Local URL (site overwrite) |
| SSDOCITM_Name | varchar |  |  | NO | Item Name (non unique) |
| SSDOCITM_PageID | integer |  |  | SI | Confluence Page ID in source system - for upload u... |
| SSDOCITM_RegionSite | varchar |  |  | SI | Region/Site (saved for created by system={blank}, ... |
| SSDOCITM_RowId | varchar |  |  | NO | - |
| SSDOCITM_Sequence | integer |  |  | SI | Display Sequence in Group |
| SSDOCITM_UpdatedDate | date |  |  | SI | Updated Date |
| SSDOCITM_UpdatedTime | time |  |  | SI | Updated Time |
| SSDOCITM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*