# web_Msg.OEC_Sentence

**Schema:** web_Msg
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SENT_ARCIM_DR | varchar |  | FK | SI | Order Item
Required by User.OECSentence. |
| SENT_AdminRouteIVType | varchar |  |  | SI | Administration IV Type |
| SENT_AdminRoute_DR | bigint |  | FK | SI | Administration Route |
| SENT_AgeFrom | integer |  |  | SI | Lower Age Boundary (inclusive) |
| SENT_AgeFromUnit | varchar |  |  | SI | Lower Age Boundary Unit |
| SENT_AgeTo | integer |  |  | SI | Upper Age Boundary (inclusive) |
| SENT_AgeToUnit | varchar |  |  | SI | Upper Age Boundary Unit |
| SENT_BSAFormula | varchar |  |  | SI | BSA Formula |
| SENT_BSAFrom | double |  |  | SI | Lower BSA Boundary (inclusive) |
| SENT_BSATo | double |  |  | SI | Upper BSA Boundary (inclusive) |
| SENT_Code | varchar |  |  | SI | Code
Required attribute removed, currently not ap... |
| SENT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SENT_CreatedDate | date |  |  | SI | Created Date |
| SENT_CreatedTime | time |  |  | SI | Created Time |
| SENT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SENT_DateFrom | date |  |  | SI | Date From |
| SENT_DateTo | date |  |  | SI | Date To |
| SENT_Desc | varchar |  |  | SI | Description
Required by User.OECSentence. |
| SENT_Owner | varchar |  |  | SI | Owner |
| SENT_Params_DR | bigint |  | FK | SI | Order Item Details - Default Parameters |
| SENT_RowId | varchar |  |  | SI | - |
| SENT_Sequence | integer |  |  | SI | Sequence Sort Order |
| SENT_Sex_DR | bigint |  | FK | SI | Sex restriction |
| SENT_UpdatedDate | date |  |  | SI | Updated Date |
| SENT_UpdatedTime | time |  |  | SI | Updated Time |
| SENT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| SENT_WeightFrom | integer |  |  | SI | Lower Weight Boundary (inclusive) |
| SENT_WeightFromUnit | varchar |  |  | SI | Lower Weight Boundary Unit |
| SENT_WeightTo | integer |  |  | SI | Upper Weight Boundary (inclusive) |
| SENT_WeightToUnit | varchar |  |  | SI | Upper Weight Boundary Unit |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*