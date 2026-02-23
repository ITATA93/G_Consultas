# SQLUser.MR_NursingNotes

**Schema:** SQLUser
**Columnas:** 147
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NOT_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| NOT_ActionComments | varchar |  |  | SI | ActionComments  |
| NOT_ActionTakenDate | date |  |  | SI | ActionTakenDate |
| NOT_ActionTakenTime | time |  |  | SI | Action Taken Time |
| NOT_ActivityDate | date |  |  | SI | Document(Activity) Date. Used by HealthShare for T... |
| NOT_ActivityTime | time |  |  | SI | Document(Activity) Time. Used by HealthShare for T... |
| NOT_AddWorkList | varchar |  |  | SI | Add Work List |
| NOT_AdmApptDate | date |  |  | SI | AdmApptDate |
| NOT_AdmApptTime | time |  |  | SI | AdmApptTime |
| NOT_Appoint_DR | varchar |  | FK | SI | Des Ref Appoint |
| NOT_CPType_DR | bigint |  | FK | SI | Care Provider Type |
| NOT_Childsub | double |  |  | NO | Childsub |
| NOT_ClinNoteSens_DR | bigint |  | FK | SI | Des Ref ClinNoteSens |
| NOT_ClinNotesCat_DR | bigint |  | FK | SI | Des Ref to ClinNotesCat |
| NOT_ClinNotesSubType_DR | varchar |  | FK | SI | Des Ref to ClinNotesSubType |
| NOT_ClinNotesType_DR | bigint |  | FK | SI | Des Ref ClinNotesType |
| NOT_ClinicalNotesToGateway | varchar |  |  | SI | ClinicalNotesToGateway |
| NOT_Comments1 | varchar |  |  | SI | Comments 1 |
| NOT_Comments2 | varchar |  |  | SI | Comments 2 |
| NOT_Comments3 | varchar |  |  | SI | Comments 3 |
| NOT_Comments4 | varchar |  |  | SI | Comments 4 |
| NOT_Consent | varchar |  |  | SI | Consent |
| NOT_CopyToGP | varchar |  |  | SI | CopyToGP |
| NOT_CreateDate | date |  |  | SI | CreateDate |
| NOT_CreateTime | time |  |  | SI | CreateTime |
| NOT_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| NOT_Date | date |  |  | SI | Date |
| NOT_DateAuth | date |  |  | SI | Date Auth |
| NOT_DocumentName | varchar |  |  | SI | Document Name |
| NOT_DocumentURL | varchar |  |  | SI | Document URL |
| NOT_Document_DR | bigint |  | FK | SI | Document Object |
| NOT_EditCP_DR | varchar |  | FK | SI | Des Ref EditCP |
| NOT_EnteredCareProv_DR | varchar |  | FK | SI | Des Ref EnteredCareProv |
| NOT_EnteredLoc_DR | bigint |  | FK | SI | Entered Location |
| NOT_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| NOT_EventStatus_DR | bigint |  | FK | SI | Des Ref to EventStatus |
| NOT_ExternalId | varchar |  |  | SI | ExternalId (HS) |
| NOT_ExternalRef | varchar |  |  | SI | External Reference Id |
| NOT_FamilyBooking | varchar |  |  | SI | FamilyBooking |
| NOT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| NOT_IncidentDate | date |  |  | SI | Incident Date |
| NOT_IncidentTime | time |  |  | SI | Incident Time |
| NOT_IncidentType_DR | bigint |  | FK | SI | Des Ref to IncidentType |
| NOT_IncludedForDischSum | varchar |  |  | SI | IncludedForDischSum |
| NOT_MethodOfConduct_DR | bigint |  | FK | SI | Des Ref RBCMethodOfConduct |
| NOT_Notes | varchar |  |  | SI | Notes |
| NOT_Notes1 | varchar |  |  | SI | Notes1 |
| NOT_NotesHTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| NOT_NotesHTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| NOT_NurseId_DR | varchar |  | FK | SI | Nurse Id Des Ref to CTCP |
| NOT_OEOrdItem_DR | varchar |  | FK | SI | Des Ref to OEOrdItem |
| NOT_OtherRecipNameAddress | varchar |  |  | SI | OtherRecipNameAddress |
| NOT_RTFNotes | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| NOT_RTFNotes1 | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| NOT_ReadyForCoding | varchar |  |  | SI | ReadyForCoding |
| NOT_ReasonForCorrection_DR | bigint |  | FK | SI | Des Ref ReasonForCorrection |
| NOT_RowId | varchar |  |  | NO | - |
| NOT_SecondUser_DR | bigint |  | FK | SI | Des Ref SecondUser |
| NOT_Status_DR | bigint |  | FK | SI | Des Ref Status |
| NOT_Time | time |  |  | SI | Time |
| NOT_TimeAuth | time |  |  | SI | Time Auth |
| NOT_UserAuth_DR | bigint |  | FK | SI | Des Ref UserAuth |
| NOT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Was the fall unassisted or assisted? |
| Q02 | - |  |  | SI | Was the fall observed? |
| Q03 | - |  |  | SI | Who observed the fall? |
| Q04 | - |  |  | SI | Did the patient sustain a physical injury as a res... |
| Q04a | - |  |  | SI | Comment |
| Q05 | - |  |  | SI | What type of injury was sustained? CHECK ONE |
| Q05a | - |  |  | SI | Other |
| Q07 | - |  |  | SI | Prior to the fall, what was the patient doing or t... |
| Q07a | - |  |  | SI | Other |
| Q08 | - |  |  | SI | Prior to the fall, was a fall risk assessment docu... |
| Q09 | - |  |  | SI | Was the patient determined to be at increased risk... |
| Q09a | - |  |  | SI | Other |
| Q10 | - |  |  | SI | At the time of the fall, were any of the following... |
| Q11 | - |  |  | SI | Which of the following were in place and being use... |
| Q11a | - |  |  | SI | Other |
| Q15 | - |  |  | SI | At time of the fall, was the patient on medication... |
| Q16 | - |  |  | SI | Was the medication considered to have contributed ... |
| Q17 | - |  |  | SI | Did restraints, bedrails, or other physical device... |
| Q20 | - |  |  | SI | Date of Fall |
| Q21 | - |  |  | SI | Time of Fall |
| Q22 | - |  |  | SI | Location of Fall |
| Q23 | - |  |  | SI | Was the patient confused / dizzy? |
| Q24 | - |  |  | SI | Has the patient previously fallen in hospital? |
| Q24a | - |  |  | SI | Number of falls |
| Q25 | - |  |  | SI | Clinical assessment completed by doctor |
| Q25a | - |  |  | SI | Date |
| Q25b | - |  |  | SI | Time |
| Q25c | - |  |  | SI | Reason |
| Q26 | - |  |  | SI | Review Falls Risk Assessment? |
| Q26a | - |  |  | SI | Date |
| Q26b | - |  |  | SI | Time |
| Q26c | - |  |  | SI | Reason |
| Q27 | - |  |  | SI | Falls alarm required? |
| Q27a | - |  |  | SI | Date |
| Q27b | - |  |  | SI | Time |
| Q27c | - |  |  | SI | Reason |
| Q28 | - |  |  | SI | Does the patient need a low-rise bed? |
| Q29 | - |  |  | SI | Incident report completed? |
| Q29a | - |  |  | SI | Incident form number |
| Q30 | - |  |  | SI | Patient's relatives informed |
| Q30a | - |  |  | SI | Reason |
| Q31 | - |  |  | SI | Follow-up Care |
| Q32 | - |  |  | SI | Incident Details |
| Q33 | - |  |  | SI | Follow-up |
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