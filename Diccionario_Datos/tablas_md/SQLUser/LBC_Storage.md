# SQLUser.LBC_Storage

**Schema:** SQLUser
**Columnas:** 27
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCST_RowID | bigint | PK |  | NO | - |
| LBCST_AllowedBloodProductGroups | varchar |  |  | SI | Allowed Blood Product Groups |
| LBCST_BloodProductUse | varchar |  |  | SI | Used for Blood Products |
| LBCST_Code | varchar |  |  | NO | Code |
| LBCST_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCST_CreatedDate | date |  |  | SI | Created Date |
| LBCST_CreatedTime | time |  |  | SI | Created Time |
| LBCST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCST_DateFrom | date |  |  | SI | Effective date for the record |
| LBCST_DateTo | date |  |  | SI | Last day the record is active |
| LBCST_Desc | varchar |  |  | NO | Description |
| LBCST_EmergencyBloodStock | varchar |  |  | SI | Emergency Blood Stock
For the BloodNet extract. U... |
| LBCST_Freezer | varchar |  |  | SI | Constitutes Freezer Storage |
| LBCST_LabSite_DR | bigint |  | FK | NO | Lab Site |
| LBCST_MaterialStorageUse | varchar |  |  | SI | Used for Blood Products |
| LBCST_Owner | varchar |  |  | SI | Owner |
| LBCST_StockTracking | varchar |  |  | SI | Stock tracking |
| LBCST_StorageGroup_DR | bigint |  | FK | NO | Storage Group |
| LBCST_UpdatedDate | date |  |  | SI | Updated Date |
| LBCST_UpdatedTime | time |  |  | SI | Updated Time |
| LBCST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q02Q1 | - |  |  | SI | Diámetro (#) |
| Q02Q2 | - |  |  | SI | Ubicación |
| Q02Q3 | - |  |  | SI | Complejidad |
| Q02Q4 | - |  |  | SI | Observación |
| Q02Q5 | - |  |  | SI | Lateralidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*