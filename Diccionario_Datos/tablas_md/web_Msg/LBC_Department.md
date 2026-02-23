# web_Msg.LBC_Department

**Schema:** web_Msg
**Columnas:** 49
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCDEP_AbnormalFlagWidth | integer |  |  | SI | Test Set Item Abnormal Flag  Column Width  |
| LBCDEP_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| LBCDEP_Code | varchar |  |  | SI | Code
Required by User.LBCDepartment. |
| LBCDEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDEP_CreatedDate | date |  |  | SI | Created Date |
| LBCDEP_CreatedTime | time |  |  | SI | Created Time |
| LBCDEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCDEP_CumulativeCommentsReportable | varchar |  |  | SI | Cummulative Comments are Reportable
  Y = print T... |
| LBCDEP_DateFrom | date |  |  | SI | Effective date for the record |
| LBCDEP_DateTo | date |  |  | SI | Last day the record is active  |
| LBCDEP_DepartmentFooterExtraText | varchar |  |  | SI | Department Footer Extra Text
Extra Text (such a P... |
| LBCDEP_DepartmentHeader | varchar |  |  | SI | Department header to be displayed in Lab Result En... |
| LBCDEP_DepartmentHeaderExtraText | varchar |  |  | SI | Department Header Extra Text
Extra Text (such a P... |
| LBCDEP_Desc | varchar |  |  | SI | Description/Name
Required by User.LBCDepartment. |
| LBCDEP_DescFontSize | integer |  |  | SI | Doctor's Report Specimen Description Font Size |
| LBCDEP_DocCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| LBCDEP_FooterClass | varchar |  |  | SI | Department Footer Class
The Zen Report which crea... |
| LBCDEP_HeaderClass | varchar |  |  | SI | Department Header Class
The Zen Report which crea... |
| LBCDEP_HideHeaderFooter | varchar |  |  | SI | Doctors Reports Hide Department Header/Footer |
| LBCDEP_IDescWidth | integer |  |  | SI | Test Set Item Description Column Width  |
| LBCDEP_IResultWidth | integer |  |  | SI | Test Set Item Result Column Width  |
| LBCDEP_LabBillCategory | varchar |  |  | SI | Lab Billing Category |
| LBCDEP_LocCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| LBCDEP_ManualPrint | varchar |  |  | SI | If this flag is set, Doctors Reports will not be t... |
| LBCDEP_Owner | varchar |  |  | SI | Owner |
| LBCDEP_PrintSeparatePage | varchar |  |  | SI | Print New Page
Start a new page in the Doctors Re... |
| LBCDEP_RangeWidth | integer |  |  | SI | Test Set Item Range Column Width  |
| LBCDEP_ReferringDoctorCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| LBCDEP_ReportCorrectedResults | varchar |  |  | SI | Display Corrected Results on Doctors Report after ... |
| LBCDEP_RowID | varchar |  |  | SI | - |
| LBCDEP_Sequence | double |  |  | SI | Print Sequence
The order of Departments in Doctor... |
| LBCDEP_SpecimenContainerDesc | varchar |  |  | SI | Department Specific Specimen Details Format
No va... |
| LBCDEP_SpecimenContainerListDesc | varchar |  |  | SI | Department Specific Specimen Details Format for li... |
| LBCDEP_SuppressSpecimens | varchar |  |  | SI | Doctors Reports Suppress Specimen Detals in Test S... |
| LBCDEP_TelephoneNumber | varchar |  |  | SI | Telephone Number |
| LBCDEP_TestMethodWidth | integer |  |  | SI | Test Set Item Test Method Column Width  |
| LBCDEP_TestSetBlankLine | varchar |  |  | SI | Blank Line after separator line after all specimen... |
| LBCDEP_TestSetSeparatorLine | varchar |  |  | SI | Separator Line after all specimens in a test set h... |
| LBCDEP_ThirdPartyCourier_DR | bigint |  | FK | SI | The default Courier to use for Lab Doctors Reports... |
| LBCDEP_UnitsWidth | integer |  |  | SI | Test Set Item Units Column Width  |
| LBCDEP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCDEP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCDEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*