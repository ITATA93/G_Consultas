# SQLUser.MR_Procedures

**Schema:** SQLUser
**Columnas:** 97
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Procedimientos**. Intervenciones realizadas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROC_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| ChildQ06DR | - |  |  | SI | Child Reference: Daily Assessment |
| PROC_AliasDiagText | varchar |  |  | SI | AliasDiagText |
| PROC_Anaesthetist_DR | varchar |  | FK | SI | Des Ref Anaesthetist |
| PROC_Appoint_DR | varchar |  | FK | SI | Des Ref Appoint |
| PROC_BodySite_DR | bigint |  | FK | SI | Des Ref OECBodySite |
| PROC_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| PROC_Childsub | double |  |  | NO | Childsub |
| PROC_ContractFlag_DR | bigint |  | FK | SI | Des Ref ContractFlag |
| PROC_CopyToEpisode_DR | bigint |  | FK | SI | Des Ref to PAAdm - Copied To Linked Episode |
| PROC_DRGRank | varchar |  |  | SI | DRG Rank |
| PROC_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| PROC_Date | date |  |  | SI | Date |
| PROC_EndDate | date |  |  | SI | End Date |
| PROC_EnteredAs | varchar |  |  | SI | EnteredAs - if Terminology link was used |
| PROC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PROC_ExternalId | varchar |  |  | SI | A reference to external systems.
Used by HealthSh... |
| PROC_FirstInset | varchar |  |  | SI | FirstInset |
| PROC_GenericCB | varchar |  |  | SI | Generic Checkbox  - This has changed from a generi... |
| PROC_GenericCareProvA_DR | varchar |  | FK | SI | Des Ref CTCP |
| PROC_GenericCareProvB_DR | varchar |  | FK | SI | Des Ref CTCP |
| PROC_ICPC2Codes_DR | bigint |  | FK | SI | Des Ref MRCICPC2Codes |
| PROC_Laterality_DR | bigint |  | FK | SI | Des Ref PACLaterality |
| PROC_MappedProc_DR | bigint |  | FK | SI | Des Ref MappedProc |
| PROC_OperCategory_DR | bigint |  | FK | SI | Des Ref OperCategory |
| PROC_OperRecord_DR | varchar |  | FK | SI | Des Ref Operation Record |
| PROC_Operation_DR | bigint |  | FK | SI | Des Ref Operation |
| PROC_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| PROC_PrimSecond | varchar |  |  | SI | Prim Second |
| PROC_ProcDate | date |  |  | SI | Proc Date |
| PROC_ProcedureActivity_DR | bigint |  | FK | SI | Des Ref ProcedureActivity |
| PROC_ProcedureNotes | varchar |  |  | SI | Procedure Notes |
| PROC_ProcedurePhase_DR | bigint |  | FK | SI | Des Ref ProcedurePhase |
| PROC_RobotUsed | varchar |  |  | SI | Robot Used |
| PROC_RowId | varchar |  |  | NO | - |
| PROC_SnomedConcept_DR | bigint |  | FK | SI | Des Ref PACSnomedConcept |
| PROC_SnomedTerms_DR | bigint |  | FK | SI | Des Ref PACSnomedTerms |
| PROC_SpecialityLoc_DR | bigint |  | FK | SI | Des Ref CTLoc |
| PROC_Time | time |  |  | SI | Time |
| PROC_TimeEnd | time |  |  | SI | TimeEnd |
| PROC_TimeStart | time |  |  | SI | TimeStart |
| PROC_Transact_DR | varchar |  | FK | SI | Des Ref Transact |
| PROC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| PROC_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Date of Insertion |
| Q02 | - |  |  | SI | Time of Insertion |
| Q03 | - |  |  | SI | Date Removed |
| Q04 | - |  |  | SI | Time Removed |
| Q05 | - |  |  | SI | Tracheostomy Notes |
| Q07 | - |  |  | SI | Size |
| Q08 | - |  |  | SI | Types |
| Q09 | - |  |  | SI | Emergency Equipment in Room |
| Q10 | - |  |  | SI | Securing Device |
| Q10ObsDR | - |  |  | SI | Securing Device DR |
| Q11 | - |  |  | SI | Inner Cannula Insitu |
| Q12 | - |  |  | SI | Date |
| Q13 | - |  |  | SI | Time |
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