# web_Msg.LBC_ReportGroup

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
| LBCRG_Code | varchar |  |  | SI | Code
Required by User.LBCReportGroup. |
| LBCRG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCRG_CreatedDate | date |  |  | SI | Created Date |
| LBCRG_CreatedTime | time |  |  | SI | Created Time |
| LBCRG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCRG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCRG_DateTo | date |  |  | SI | Last day the record is active  |
| LBCRG_Desc | varchar |  |  | SI | Description
Required by User.LBCReportGroup. |
| LBCRG_Owner | varchar |  |  | SI | Owner |
| LBCRG_ReportGroupTime | integer |  |  | SI | This property defines the age (in seconds) after A... |
| LBCRG_RowID | varchar |  |  | SI | - |
| LBCRG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCRG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCRG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*