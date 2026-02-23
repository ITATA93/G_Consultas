# SQLUser.LBC_TestSetRevision

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTSR_RowID | bigint | PK |  | NO | - |
| ChildQ06DR | - |  |  | SI | Child Reference: Clasificación de los Factores Bio... |
| LBCTSR_AllowBulkValidation | varchar |  |  | SI | Allow Bulk Validation |
| LBCTSR_AllowLinking | varchar |  |  | SI | Same Test Set |
| LBCTSR_AlternateCode | varchar |  |  | SI | Alternate Code |
| LBCTSR_AlternateDescription | varchar |  |  | SI | Alternate Description |
| LBCTSR_AttentionExceptionQueue_DR | bigint |  | FK | SI | Attention / Exception Queue of the test set |
| LBCTSR_CareProviderReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] ReportPage for CareProvider 
The R... |
| LBCTSR_Code | varchar |  |  | NO | Code |
| LBCTSR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSR_CodeTranslated | varchar |  |  | SI | Code Translated |
| LBCTSR_Confidential | varchar |  |  | SI | Confidential
Indicates that this test set is conf... |
| LBCTSR_CreatedDate | date |  |  | SI | Created Date |
| LBCTSR_CreatedTime | time |  |  | SI | Created Time |
| LBCTSR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTSR_CrossSpecimenTest | varchar |  |  | SI | Cross Specimen Test
All matching specimen contain... |
| LBCTSR_Cumulative | varchar |  |  | SI | Cumulative Test Set
  N = Never include this Test... |
| LBCTSR_CumulativeCommentsReportable | varchar |  |  | SI | Cummulative Comments are Reportable
  Y = print T... |
| LBCTSR_CustomLayout | varchar |  |  | SI | Custom Report Layout
This property indicates that... |
| LBCTSR_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSR_DefaultChartType | varchar |  |  | SI | Default Chart Type for Result Graph |
| LBCTSR_DefaultDFTVerificationQueues | varchar |  |  | SI | Default DFT Verification Workflow of the test set |
| LBCTSR_DefaultReadOnlyQueues | varchar |  |  | SI | [DEPRECATED]TC-46012[/DEPRECATED] Default Read-Onl... |
| LBCTSR_DefaultVerificationQueues | varchar |  |  | SI | Default Verification Workflow of the test set |
| LBCTSR_Department_DR | bigint |  | FK | NO | The Department the TestSet belongs to |
| LBCTSR_Desc | varchar |  |  | NO | Description
HTMLTextBox |
| LBCTSR_DescTranslated | varchar |  |  | SI | Desc Translated |
| LBCTSR_DisplayAlias | bigint |  |  | SI | Display Alias
The alias which is used to refer to... |
| LBCTSR_DocCourier_DR | bigint |  | FK | SI | Courier to use for this TestSet to send reports to... |
| LBCTSR_EnteredOnlyQueue_DR | bigint |  | FK | SI | Entered Only Queue
Optional verification queue th... |
| LBCTSR_ExcludeFromFinals | varchar |  |  | SI | Flag if this TestSet should be excluded from check... |
| LBCTSR_ExcludeSex | varchar |  |  | SI | Exclude Sex
This test set may not be performed on... |
| LBCTSR_FooterClass | varchar |  |  | SI | TestSet Footer Class
The Zen Report which creates... |
| LBCTSR_HeaderClass | varchar |  |  | SI | TestSet Header Class
The Zen Report which creates... |
| LBCTSR_LocCourier_DR | bigint |  | FK | SI | Courier to use for this TestSet to send reports to... |
| LBCTSR_LocationReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] ReportPage for Location
The Report... |
| LBCTSR_ManualPrint | varchar |  |  | SI | Manual Print
Flag to show if Doctors Reports for ... |
| LBCTSR_ManualQueues | varchar |  |  | SI | If this property is set the test can only be manua... |
| LBCTSR_ManualSpecimenEntry | varchar |  |  | SI | Manual Specimen Entry |
| LBCTSR_Materials | varchar |  |  | SI | Perform on material
If set all test set items of ... |
| LBCTSR_MultipleAllowed | varchar |  |  | SI | Multiple Allowed
This property indicates whether ... |
| LBCTSR_Number | varchar |  |  | NO | Revision Number |
| LBCTSR_Owner | varchar |  |  | SI | Owner |
| LBCTSR_ParRef | bigint |  |  | NO | - |
| LBCTSR_PlotMultipleCharts | varchar |  |  | SI | Plot multiple charts by default
Flag to indicate ... |
| LBCTSR_ReceivedOnlyQueue_DR | bigint |  | FK | SI | Received Only Queue |
| LBCTSR_ReferringDoctorCourier_DR | bigint |  | FK | SI | Courier to use for this TestSet to send reports to... |
| LBCTSR_ReferringDoctorReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] ReportPage for Referring Doctor
Th... |
| LBCTSR_ReportGroup_DR | bigint |  | FK | SI | This property can contain a reference to a report ... |
| LBCTSR_RequireApprovalForNotPerformed | varchar |  |  | SI | Require Approval for Not Performed |
| LBCTSR_ReturnToReceivedOnlyQueue | varchar |  |  | SI | Send back to Received Only Queue on Removal of Res... |
| LBCTSR_RevisionCode | varchar |  |  | SI | Revision Code |
| LBCTSR_RevisionDesc | varchar |  |  | SI | Revision Description
HTMLTextBox#n |
| LBCTSR_Section_DR | bigint |  | FK | SI | Print Section
The Section (if any) within Dept, u... |
| LBCTSR_Sequence | double |  |  | SI | Sequence
The sequence to print/Display the TestSe... |
| LBCTSR_ShowCancerCodes | varchar |  |  | SI | Flag to indicate if Cancer Codes for the departmen... |
| LBCTSR_ShowSnomedCodes | varchar |  |  | SI | Flag to indicate if Snomed Code List is to be disp... |
| LBCTSR_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| LBCTSR_SuppressResultColumnHeaders | varchar |  |  | SI | Doctors Reports Suppress Result Column Headers |
| LBCTSR_SuppressResultForExternalResultInterface | varchar |  |  | SI | Suppress Result for External Result Interface |
| LBCTSR_SuppressSpecimens | varchar |  |  | SI | Doctors Reports Suppress Specimen Detals in Test S... |
| LBCTSR_TestSetFooterExtraText | varchar |  |  | SI | TestSet Footer Extra Text
Extra Text to add to th... |
| LBCTSR_TestSetHeaderExtraText | varchar |  |  | SI | TestSet Header Extra Text
Extra Text to add to th... |
| LBCTSR_ThirdPartyCourier_DR | bigint |  | FK | SI | Courier to use for this TestSet to send reports to... |
| LBCTSR_ThirdPartyReportPage_DR | bigint |  | FK | SI | [ DEPRECATED ] ReportPage for Third Party
The Rep... |
| LBCTSR_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTSR_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTSR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCTSR_ValidateAfterFirstInstrumentResult | varchar |  |  | SI | Validate Test Set after receipt of first instrumen... |
| LBCTSR_WorkGroup_DR | bigint |  | FK | SI | WorkGroup
The WorkGroup (if any) that the TestSet... |
| LBCTSR_WorksheetAllocation | varchar |  |  | SI | Worksheet Allocation
Optional. Indicates whether ... |
| Q01 | - |  |  | SI | Equipo Responsable |
| Q02 | - |  |  | SI | Fecha de cierre del Estudio de Familia |
| Q07 | - |  |  | SI | Síntesis de la dinámica Familiar |
| Q08 | - |  |  | SI | Genograma |
| Q09 | - |  |  | SI | Ecomapa |
| Q10 | - |  |  | SI | Apgar Familiar |
| Q11 | - |  |  | SI | Círculo Familiar |
| Q12 | - |  |  | SI | Otro, Especificar |
| Q13 | - |  |  | SI | Acerca de la estructura y dinámica familiardel cas... |
| Q14 | - |  |  | SI | Subsistemas Observados |
| Q15 | - |  |  | SI | Comportamiento del Poder, Autoridad y Jerarquías e... |
| Q16 | - |  |  | SI | Coaliciones o Alianzas |
| Q17 | - |  |  | SI | Límites |
| Q18 | - |  |  | SI | Comunicación |
| Q19 | - |  |  | SI | Roles significativo |
| Q20 | - |  |  | SI | Normas o Reglas Observadas en la Familia |
| Q21 | - |  |  | SI | Dinámica Familiar |
| Q22 | - |  |  | SI | Ciclo Vital del caso índice |
| Q23 | - |  |  | SI | Ciclo Vital Familiar |
| Q24 | - |  |  | SI | Estructura Familiar |
| Q25 | - |  |  | SI | Acerca de la Estructura y Dinámica Familiar del Ca... |
| Q26 | - |  |  | SI | Breve Síntesis de la historia Familiar |
| Q28 | - |  |  | SI | Motivo del Estudio de la Familia |
| Q29 | - |  |  | SI | Identificación del Caso |
| Q30 | - |  |  | SI | Identificación de la Familia |
| Q31 | - |  |  | SI | Tipo de Familia |
| Q32 | - |  |  | SI | N° de Ficha Familia |
| Q33 | - |  |  | SI | Territorio |
| Q34 | - |  |  | SI | Círculo Familiar y Ecomapa |
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