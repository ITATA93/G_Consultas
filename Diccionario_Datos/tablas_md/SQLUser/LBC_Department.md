# SQLUser.LBC_Department

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCDEP_RowID | bigint | PK |  | NO | - |
| LBCDEP_AbnormalFlagWidth | integer |  |  | SI | Test Set Item Abnormal Flag  Column Width  |
| LBCDEP_AccreditationNumber | varchar |  |  | SI | Accreditation Number |
| LBCDEP_Code | varchar |  |  | NO | Code |
| LBCDEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCDEP_CodeTranslated | varchar |  |  | SI | Code Translated |
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
| LBCDEP_Desc | varchar |  |  | NO | Description/Name |
| LBCDEP_DescFontSize | integer |  |  | SI | Doctor's Report Specimen Description Font Size |
| LBCDEP_DescTranslated | varchar |  |  | SI | Desc Translated |
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
| Q01 | - |  |  | SI | Déficit motor en brazo |
| Q02 | - |  |  | SI | Propiocepción (ojo cerrado) : localizar pulgar afe... |
| Q03 | - |  |  | SI | Equilibrio |
| Q04 | - |  |  | SI | Puntuación test Mental (SPMSQ de Pfeiffer) |
| Q05 | - |  |  | SI | Resultado de escala Orpington |
| Q05ObsDR | - |  |  | SI | Resultado de escala Orpington DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*