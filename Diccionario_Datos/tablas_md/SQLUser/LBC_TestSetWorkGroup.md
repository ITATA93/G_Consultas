# SQLUser.LBC_TestSetWorkGroup

**Schema:** SQLUser
**Columnas:** 29
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSWG_RowID | bigint | PK |  | NO | - |
| ChildQ05DR | - |  |  | SI | Child Reference: Hemangiomas y Mancha Mongólica |
| LBCTSWG_CareProviderReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] CareProvider ReportPage
The Report... |
| LBCTSWG_Code | varchar |  |  | NO | Code |
| LBCTSWG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSWG_CreatedDate | date |  |  | SI | Created Date |
| LBCTSWG_CreatedTime | time |  |  | SI | Created Time |
| LBCTSWG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSWG_DateFrom | date |  |  | SI | Effective Date |
| LBCTSWG_DateTo | date |  |  | SI | End Date
Last day the record is active  |
| LBCTSWG_Department_DR | bigint |  | FK | SI | Department
The Department under which to include ... |
| LBCTSWG_Desc | varchar |  |  | NO | Description |
| LBCTSWG_Footer | varchar |  |  | SI | The Footer (if any) to appear after the Data and C... |
| LBCTSWG_Header | varchar |  |  | SI | The Header (if any) to appear after the Column Hea... |
| LBCTSWG_LocationReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Location ReportPage
The ReportPage... |
| LBCTSWG_Owner | varchar |  |  | SI | Owner |
| LBCTSWG_ReferringDoctorReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Referring Doctor ReportPage
The Re... |
| LBCTSWG_Section_DR | bigint |  | FK | SI | Section
The Section under which to include this g... |
| LBCTSWG_Sequence | double |  |  | SI | Sequence
The sequence of this group on a Doctors ... |
| LBCTSWG_ThirdPartyReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] Third Party ReportPage
The ReportP... |
| LBCTSWG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSWG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSWG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q52Q1 | - |  |  | SI | Palpación |
| Q52Q2 | - |  |  | SI | Percusión |
| Q52Q4 | - |  |  | SI | Auscultación |
| Q52Q5 | - |  |  | SI | Localización |
| Q52Q6 | - |  |  | SI | Lateralidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*