# web_Msg.LBC_TestSetWorkGroup

**Schema:** web_Msg
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSWG_CareProviderReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] CareProvider ReportPage
The Report... |
| LBCTSWG_Code | varchar |  |  | SI | Code
Required by User.LBCTestSetWorkGroup. |
| LBCTSWG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSWG_CreatedDate | date |  |  | SI | Created Date |
| LBCTSWG_CreatedTime | time |  |  | SI | Created Time |
| LBCTSWG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSWG_DateFrom | date |  |  | SI | Effective Date |
| LBCTSWG_DateTo | date |  |  | SI | End Date
Last day the record is active  |
| LBCTSWG_Department_DR | bigint |  | FK | SI | Department
The Department under which to include ... |
| LBCTSWG_Desc | varchar |  |  | SI | Description
Required by User.LBCTestSetWorkGroup. |
| LBCTSWG_Footer | varchar |  |  | SI | The Footer (if any) to appear after the Data and C... |
| LBCTSWG_Header | varchar |  |  | SI | The Header (if any) to appear after the Column Hea... |
| LBCTSWG_LocationReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Location ReportPage
The ReportPage... |
| LBCTSWG_Owner | varchar |  |  | SI | Owner |
| LBCTSWG_ReferringDoctorReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Referring Doctor ReportPage
The Re... |
| LBCTSWG_RowID | varchar |  |  | SI | - |
| LBCTSWG_Section_DR | bigint |  | FK | SI | Section
The Section under which to include this g... |
| LBCTSWG_Sequence | double |  |  | SI | Sequence
The sequence of this group on a Doctors ... |
| LBCTSWG_ThirdPartyReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Third Party ReportPage
The ReportP... |
| LBCTSWG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSWG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSWG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*