# SQLUser.MR_SystemReview

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SYSR_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| Q01 | - |  |  | SI | Patient Description |
| Q02 | - |  |  | SI | For patients < 16 years old. |
| Q03 | - |  |  | SI | Useful to use over time to track disease progressi... |
| Q04 | - |  |  | SI | Score 100 - 80: Able to carry on normal activity |
| Q05 | - |  |  | SI | Score 70 - 50: Mild to moderate restriction. |
| Q06 | - |  |  | SI | Score 40 - 0: Moderate to severe restriction. |
| Q07 | - |  |  | SI | Uses parent description of child’s activity to ass... |
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
| SYSR_BodyAreaProblemsSubp_DR | varchar |  | FK | SI | Des Ref BodyAreaProblemsSubp  |
| SYSR_BodyAreaProblems_DR | varchar |  | FK | SI | Des Ref BodyAreaProblems  |
| SYSR_BodyArea_DR | bigint |  | FK | SI | Des Ref BodyArea  |
| SYSR_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SYSR_CareAim_DR | bigint |  | FK | SI | Des Ref CareAim |
| SYSR_Childsub | double |  |  | NO | Childsub |
| SYSR_Date | date |  |  | SI | Date |
| SYSR_Desc | varchar |  |  | SI | Description |
| SYSR_EndDate | date |  |  | SI | EndDate |
| SYSR_Laterality_DR | bigint |  | FK | SI | Des Ref Laterality |
| SYSR_MRCBodSysProbSub | varchar |  |  | SI | Des Ref MRCBodSysProbSub |
| SYSR_MRCBodySysPrStat_DR | bigint |  | FK | SI | Des Ref to MRCBodySysPrStat |
| SYSR_MRCBodySysProb_DR | varchar |  | FK | SI | Des Ref to MRCBodySysProb |
| SYSR_MRCBodySys_DR | bigint |  | FK | SI | Des Ref to MRCBodySys |
| SYSR_ReviewDate | date |  |  | SI | ReviewDate |
| SYSR_RowId | varchar |  |  | NO | - |
| SYSR_Time | time |  |  | SI | Time |
| SYSR_UpdateDate | date |  |  | SI | UpdateDate |
| SYSR_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| SYSR_UpdateTime | time |  |  | SI | UpdateTime |
| SYSR_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*