# SQLUser.OEC_RemoteDutyPref

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REMOPREF_RowId | bigint | PK |  | NO | - |
| Q05Q1 | - |  |  | SI | Banknotes |
| Q05Q2 | - |  |  | SI | Number |
| Q05Q3 | - |  |  | SI | Coins combined |
| Q05Q4 | - |  |  | SI | Currency |
| Q05Q5 | - |  |  | SI | Total amount |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REMOPREF_ARCIM_List | varchar |  |  | SI | List of Order Item Master |
| REMOPREF_Code | varchar |  |  | NO | Code |
| REMOPREF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REMOPREF_CreatedDate | date |  |  | SI | Created Date |
| REMOPREF_CreatedTime | time |  |  | SI | Created Time |
| REMOPREF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REMOPREF_DMOCP_List | varchar |  |  | SI | List of DMO Care Providers |
| REMOPREF_DateFrom | date |  |  | SI | Date From |
| REMOPREF_DateTo | date |  |  | SI | Date To |
| REMOPREF_Desc | varchar |  |  | NO | Description |
| REMOPREF_DutyType | varchar |  |  | SI | Restrict to all Order Item Master of Remote Duty T... |
| REMOPREF_HasDMOCP | varchar |  |  | SI | Has DMO Care Provider Data |
| REMOPREF_OffsetDateFrom | varchar |  |  | SI | Date From Offset |
| REMOPREF_OffsetDateTo | varchar |  |  | SI | Date To Offset |
| REMOPREF_OrdStatus_List | varchar |  |  | SI | List of Order Status |
| REMOPREF_Owner | varchar |  |  | SI | Owner |
| REMOPREF_RecLoc_List | varchar |  |  | SI | List of Receiving Locations |
| REMOPREF_SharedContext | varchar |  |  | SI | Shared Context |
| REMOPREF_Summary | varchar |  |  | SI | Long description / summary |
| REMOPREF_TabCaption | varchar |  |  | SI | Tab Caption |
| REMOPREF_Triaged | varchar |  |  | SI | Has Triaged Flagged |
| REMOPREF_UpdatedDate | date |  |  | SI | Updated Date |
| REMOPREF_UpdatedTime | time |  |  | SI | Update Time |
| REMOPREF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*