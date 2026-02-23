# web_Msg.LBC_Specimen

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCSP_Code | varchar |  |  | SI | Code
Required by User.LBCSpecimen. |
| LBCSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSP_CreatedDate | date |  |  | SI | Created Date |
| LBCSP_CreatedTime | time |  |  | SI | Created Time |
| LBCSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCSP_DateFrom | date |  |  | SI | Date Active From |
| LBCSP_DateTo | date |  |  | SI | Date Active To |
| LBCSP_Desc | varchar |  |  | SI | Description
Required by User.LBCSpecimen. |
| LBCSP_Group_DR | bigint |  | FK | SI | Specimen Group |
| LBCSP_Owner | varchar |  |  | SI | Owner |
| LBCSP_RowID | varchar |  |  | SI | - |
| LBCSP_Sequence | double |  |  | SI | Sequence |
| LBCSP_SuitableForPooling | varchar |  |  | SI | Suitable for pooling |
| LBCSP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCSP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*