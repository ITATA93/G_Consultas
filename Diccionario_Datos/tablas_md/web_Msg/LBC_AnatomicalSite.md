# web_Msg.LBC_AnatomicalSite

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
| LBCAS_Code | varchar |  |  | SI | Code
Required by User.LBCAnatomicalSite. |
| LBCAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAS_CreatedDate | date |  |  | SI | Created Date |
| LBCAS_CreatedTime | time |  |  | SI | Created Time |
| LBCAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAS_DateFrom | date |  |  | SI | Effective date for the record |
| LBCAS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCAS_Desc | varchar |  |  | SI | Description
Required by User.LBCAnatomicalSite. |
| LBCAS_Owner | varchar |  |  | SI | Owner |
| LBCAS_RowID | varchar |  |  | SI | - |
| LBCAS_Sequence | double |  |  | SI | Display Sequence |
| LBCAS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*