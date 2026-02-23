# SQLUser.OE_TextResult

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Initial Assessment |
| Q02 | - |  |  | SI | I am going to ask you to identify up to three impo... |
| Q03 | - |  |  | SI | with as a result of your problem. Today, are there... |
| Q04 | - |  |  | SI | because of your problem? (Clinician: show scale to... |
| Q05 | - |  |  | SI | Follow-up Assessments |
| Q06 | - |  |  | SI | When I assessed you on (state previous assessment ... |
| Q07 | - |  |  | SI | activities from list at a time). Today, do you sti... |
| Q08 | - |  |  | SI | the list)? |
| Q09 | - |  |  | SI | Patient-specific activity scoring scheme (Point to... |
| Q10 | - |  |  | SI | 0 |
| Q11 | - |  |  | SI | 1 |
| Q12 | - |  |  | SI | 2 |
| Q13 | - |  |  | SI | 3 |
| Q14 | - |  |  | SI | 4 |
| Q15 | - |  |  | SI | 5 |
| Q16 | - |  |  | SI | 6 |
| Q17 | - |  |  | SI | 7 |
| Q18 | - |  |  | SI | 8 |
| Q19 | - |  |  | SI | 9 |
| Q20 | - |  |  | SI | 10 |
| Q21 | - |  |  | SI | Unable to perform activity |
| Q22 | - |  |  | SI | Able to perform activity at the same level as befo... |
| Q23 | - |  |  | SI | Impairment |
| Q24 | - |  |  | SI | Assessment Type |
| Q25 | - |  |  | SI | Activity 1 |
| Q26 | - |  |  | SI | Activity 2 |
| Q27 | - |  |  | SI | Activity 3 |
| Q28 | - |  |  | SI | Activity 4 |
| Q29 | - |  |  | SI | Activity 5 |
| Q30 | - |  |  | SI | Additional |
| Q31 | - |  |  | SI | Additional |
| Q32 | - |  |  | SI | Score |
| Q33 | - |  |  | SI | Score |
| Q34 | - |  |  | SI | Score |
| Q35 | - |  |  | SI | Score |
| Q36 | - |  |  | SI | Score |
| Q37 | - |  |  | SI | Score |
| Q38 | - |  |  | SI | Score |
| Q39 | - |  |  | SI | Number of activities |
| Q40 | - |  |  | SI | Total score |
| Q41 | - |  |  | SI | Minimum detectable change (90%CI) for average scor... |
| Q42 | - |  |  | SI | Minimum detectable change (90%CI) for single activ... |
| Q43 | - |  |  | SI | Date |
| Q44 | - |  |  | SI | Time |
| Q45 | - |  |  | SI | Date |
| Q46 | - |  |  | SI | Unable to perform activity&nbsp |
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
| TR_Abnormal | varchar |  |  | SI | Abnormal |
| TR_Action_DR | bigint |  | FK | SI | Des Ref Action |
| TR_CPVerified_DR | varchar |  | FK | SI | Des Ref CPVerified |
| TR_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| TR_CareProviderReported_DR | varchar |  | FK | SI | Des Ref CareProviderReported |
| TR_ClinicallySignificant | varchar |  |  | SI | ClinicallySignificant |
| TR_DMPConnexionSecrete | varchar |  |  | SI | Secret connection to DMP |
| TR_DMPDoNotSendToDMP | varchar |  |  | SI | Do not send the validated document to DMP |
| TR_DMPNoVisibilityPS | varchar |  |  | SI | Document hidden from care provider in DMP |
| TR_DMPNoVisibilityPatient | varchar |  |  | SI | Document not visible to patient in DMP |
| TR_DMPNoVisibilityRepresentantLegal | varchar |  |  | SI | Document not visible to the patient's legal repres... |
| TR_DateCreated | date |  |  | SI | Date Created |
| TR_DateRead | date |  |  | SI | Date Read |
| TR_DateTranscribed | date |  |  | SI | Date Transcribed |
| TR_DateUnread | date |  |  | SI | Date Unread |
| TR_DateUpdated | date |  |  | SI | Date Updated |
| TR_DateVerified | date |  |  | SI | Date Verified |
| TR_DistList | varchar |  |  | SI | Distribute List |
| TR_DocumentExtId | varchar |  |  | SI | External Reference Id |
| TR_DocumentName | varchar |  |  | SI | Document Name |
| TR_DocumentURL | varchar |  |  | SI | Document URL |
| TR_Document_DR | bigint |  | FK | SI | Document Object |
| TR_ExternalResultStatus | varchar |  |  | SI | External Result Status |
| TR_ForSignByCP | varchar |  |  | SI | For Sign By Care Provider |
| TR_GenericCheckbox1 | varchar |  |  | SI | Generic Checkbox 1 |
| TR_GenericCheckbox2 | varchar |  |  | SI | Generic Checkbox 2 |
| TR_GenericCheckbox3 | varchar |  |  | SI | Generic Checkbox 3 |
| TR_ImpressionDR | bigint |  | FK | SI | Impression DR |
| TR_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| TR_Loc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| TR_MSSSendToMSSPatient | varchar |  |  | SI | Send to patient secure health messaging system |
| TR_MSSSendToMSSPro | varchar |  |  | SI | Send to Care Provider secure health messaging syst... |
| TR_Message_DR | bigint |  | FK | SI | Send Result Message |
| TR_Name | varchar |  |  | SI | Name |
| TR_OEORD_DR | numeric |  | FK | SI | Des Ref OEORD |
| TR_OtherRecipients | varchar |  |  | SI | OtherRecipients |
| TR_PerformedAt_DR | bigint |  | FK | SI | Where Performed  |
| TR_ProvideCopyToPatient | varchar |  |  | SI | Provide a copy to patient |
| TR_Questionnaire | varchar |  |  | SI | Questionnaire |
| TR_ReasonSuppResult_DR | bigint |  | FK | SI | Des Ref ReasonSuppResult |
| TR_ResStat_DR | bigint |  | FK | SI | Des Ref Result Status |
| TR_ResultComments | varchar |  |  | SI | Result Comments |
| TR_ResultFlags | varchar |  |  | SI | Result Flags |
| TR_SuppressPrint | varchar |  |  | SI | Suppress Print |
| TR_TestSetComments | varchar |  |  | SI | TestSetComments |
| TR_TextResultType_DR | bigint |  | FK | SI | Des Ref TextResultType |
| TR_TimeCreated | time |  |  | SI | Time Created |
| TR_TimeRead | time |  |  | SI | Time Read |
| TR_TimeTranscribed | time |  |  | SI | Time Transcribed |
| TR_TimeUnread | time |  |  | SI | TimeUnread |
| TR_TimeUpdated | time |  |  | SI | Time Updated |
| TR_TimeVerified | time |  |  | SI | Time Verified |
| TR_Transcribed | varchar |  |  | SI | Transcribed |
| TR_UrgentResult | varchar |  |  | SI | Urgent Result |
| TR_UserCreated | bigint |  |  | SI | Des Ref SSUser |
| TR_UserRead_DR | bigint |  | FK | SI | Des Ref User Read |
| TR_UserTranscribed_DR | bigint |  | FK | SI | Des Ref UserTranscribed |
| TR_UserUnread_DR | bigint |  | FK | SI | Des Ref UserUnread |
| TR_UserUpdated_DR | bigint |  | FK | SI | Des Ref UserUpdated |
| TR_UserVerified | bigint |  |  | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*