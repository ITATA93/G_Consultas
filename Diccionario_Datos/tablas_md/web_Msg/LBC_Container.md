# web_Msg.LBC_Container

**Schema:** web_Msg
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCCON_Code | varchar |  |  | SI | Code
Required by User.LBCContainer. |
| LBCCON_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCON_Comments | varchar |  |  | SI | Comments |
| LBCCON_CreatedDate | date |  |  | SI | Created Date |
| LBCCON_CreatedTime | time |  |  | SI | Created Time |
| LBCCON_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCON_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCON_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCON_Desc | varchar |  |  | SI | Description
Required by User.LBCContainer. |
| LBCCON_Manufacturer_DR | bigint |  | FK | SI | Manufacturer |
| LBCCON_MaxVolume | double |  |  | SI | Max Volume |
| LBCCON_Owner | varchar |  |  | SI | Owner |
| LBCCON_RowID | varchar |  |  | SI | - |
| LBCCON_Thumbnail | bigint |  |  | SI | Thumbnail |
| LBCCON_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCON_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCON_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*