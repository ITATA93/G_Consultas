# web_Msg.LBC_ContainerManufacturer

**Schema:** web_Msg
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCCONM_128_Code | varchar |  |  | SI | 128 Code |
| LBCCONM_Code | varchar |  |  | SI | Code
Required by User.LBCContainerManufacturer. |
| LBCCONM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCONM_CreatedDate | date |  |  | SI | Created Date |
| LBCCONM_CreatedTime | time |  |  | SI | Created Time |
| LBCCONM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCONM_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCONM_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCONM_Desc | varchar |  |  | SI | Description
Required by User.LBCContainerManufact... |
| LBCCONM_Owner | varchar |  |  | SI | Owner |
| LBCCONM_RowID | varchar |  |  | SI | - |
| LBCCONM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCONM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCONM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*