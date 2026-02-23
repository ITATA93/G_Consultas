# web_Msg.LBC_SpecimenGroup

**Schema:** web_Msg
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCSPG_Code | varchar |  |  | SI | Code
Required by User.LBCSpecimenGroup. |
| LBCSPG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPG_CreatedDate | date |  |  | SI | Created Date |
| LBCSPG_CreatedTime | time |  |  | SI | Created Time |
| LBCSPG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSPG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCSPG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSPG_Desc | varchar |  |  | SI | Description
Required by User.LBCSpecimenGroup. |
| LBCSPG_Owner | varchar |  |  | SI | Owner |
| LBCSPG_RowID | varchar |  |  | SI | - |
| LBCSPG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSPG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSPG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*