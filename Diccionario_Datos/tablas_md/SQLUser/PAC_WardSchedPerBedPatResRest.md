# SQLUser.PAC_WardSchedPerBedPatResRest

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BRR_ParRef | varchar | PK |  | NO | PAC_WardSchedPerBedPat Parent Reference |
| BRR_Childsub | double |  |  | NO | Childsub |
| BRR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BRR_CreatedDate | date |  |  | SI | Created Date |
| BRR_CreatedTime | time |  |  | SI | Created Time |
| BRR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BRR_Equipment_DR | bigint |  | FK | SI | Des Ref Equipment    |
| BRR_RowId | varchar |  |  | NO | - |
| BRR_UpdatedDate | date |  |  | SI | Updated Date |
| BRR_UpdatedTime | time |  |  | SI | Updated Time |
| BRR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date of 12 week classification |
| Q02 | - |  |  | SI | Date of 24 week classification |
| Q03 | - |  |  | SI | Site |
| Q04 | - |  |  | SI | Ischemia |
| Q05 | - |  |  | SI | Neuropathy |
| Q06 | - |  |  | SI | Bacterial Infection 	 |
| Q07 | - |  |  | SI | Area |
| Q08 | - |  |  | SI | Depth |
| Q09 | - |  |  | SI | 0 - 2 : |
| Q10 | - |  |  | SI | 3 - 6 : |
| Q11 | - |  |  | SI | Score |
| Q12 | - |  |  | SI | Classification |
| Q13 | - |  |  | SI | Less Severe Ulcer |
| Q14 | - |  |  | SI | Severe Ulcer |
| Q15 | - |  |  | SI | SINBAD Ulcer Classification is simple score based ... |
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