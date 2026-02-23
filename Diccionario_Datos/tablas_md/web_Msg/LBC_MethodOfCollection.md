# web_Msg.LBC_MethodOfCollection

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCMC_Code | varchar |  |  | SI | Code
Required by User.LBCMethodOfCollection. |
| LBCMC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCMC_Comments | varchar |  |  | SI | Comments |
| LBCMC_CreatedDate | date |  |  | SI | Created Date |
| LBCMC_CreatedTime | time |  |  | SI | Created Time |
| LBCMC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCMC_DateFrom | date |  |  | SI | Effective date for the record |
| LBCMC_DateTo | date |  |  | SI | Last day the record is active  |
| LBCMC_Desc | varchar |  |  | SI | Description
Required by User.LBCMethodOfCollectio... |
| LBCMC_Owner | varchar |  |  | SI | Owner |
| LBCMC_PCode_DR | bigint |  | FK | SI | P-Code DR |
| LBCMC_RowID | varchar |  |  | SI | - |
| LBCMC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCMC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCMC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*