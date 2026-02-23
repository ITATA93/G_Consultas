# SQLUser.OEC_Action

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACT_RowId | bigint | PK |  | NO | - |
| ACT_Code | varchar |  |  | NO | Code |
| ACT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACT_CreatedDate | date |  |  | SI | Created Date |
| ACT_CreatedTime | time |  |  | SI | Created Time |
| ACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACT_DateFrom | date |  |  | SI | Date From |
| ACT_DateTo | date |  |  | SI | Date To |
| ACT_Desc | varchar |  |  | NO | Description |
| ACT_Owner | varchar |  |  | SI | Owner |
| ACT_UpdatedDate | date |  |  | SI | Updated Date |
| ACT_UpdatedTime | time |  |  | SI | Updated Time |
| ACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Vital Signs |
| Q02 | - |  |  | SI | Ambulation |
| Q02a | - |  |  | SI | Patient is NOT ready for discharge! (The Ambulatio... |
| Q03 | - |  |  | SI | Nausea & Vomiting |
| Q03a | - |  |  | SI | Patient is NOT ready for discharge! (The Nausea & ... |
| Q04 | - |  |  | SI | Pain |
| Q04a | - |  |  | SI | Patient is NOT ready for discharge! (The Pain scor... |
| Q05 | - |  |  | SI | Bleeding |
| Q05a | - |  |  | SI | Patient is NOT ready for discharge! (The Bleeding ... |
| Q06 | - |  |  | SI | Intake |
| Q06a | - |  |  | SI | Patient is NOT ready for discharge! (The Intake sc... |
| Q07 | - |  |  | SI | The MPADSS questionnaire is used for same day surg... |
| Q14 | - |  |  | SI | The Patient must score a total of 9 or more |
| Q15 | - |  |  | SI | The Vital Signs score is not less than 2 |
| Q16 | - |  |  | SI | None of the other questions score a zero |
| Q1a | - |  |  | SI | Patient is NOT ready for discharge! (The Vital Sig... |
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