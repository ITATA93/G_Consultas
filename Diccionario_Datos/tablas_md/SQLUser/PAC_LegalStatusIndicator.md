# SQLUser.PAC_LegalStatusIndicator

**Schema:** SQLUser
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LSTI_RowId | bigint | PK |  | NO | - |
| LSTI_Code | varchar |  |  | NO | Code |
| LSTI_CreatedDate | date |  |  | SI | Created Date |
| LSTI_CreatedTime | time |  |  | SI | Created Time |
| LSTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LSTI_DateFrom | date |  |  | SI | DateFrom |
| LSTI_DateTo | date |  |  | SI | DateTo |
| LSTI_Desc | varchar |  |  | NO | Description |
| LSTI_NationalCode | varchar |  |  | SI | NationalCode |
| LSTI_UpdatedDate | date |  |  | SI | Updated Date |
| LSTI_UpdatedTime | time |  |  | SI | Updated Time |
| LSTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Number of times out of bed |
| Q01ObsDR | - |  |  | SI | Number of times out of bed DR |
| Q02 | - |  |  | SI | Incontinent |
| Q02ObsDR | - |  |  | SI | Incontinent DR |
| Q02a | - |  |  | SI | Comments |
| Q03 | - |  |  | SI | Able to call for assistance |
| Q03ObsDR | - |  |  | SI | Able to call for assistance DR |
| Q03a | - |  |  | SI | Comments |
| Q04 | - |  |  | SI | Wandering / Restless |
| Q04ObsDR | - |  |  | SI | Wandering / Restless DR |
| Q04a | - |  |  | SI | Comments |
| Q05 | - |  |  | SI | Agitated |
| Q05ObsDR | - |  |  | SI | Agitated DR |
| Q05a | - |  |  | SI | Comments |
| Q06 | - |  |  | SI | Settled with encouragement |
| Q06ObsDR | - |  |  | SI | Settled with encouragement DR |
| Q06a | - |  |  | SI | Comments |
| Q07 | - |  |  | SI | Aggressive |
| Q07ObsDR | - |  |  | SI | Aggressive DR |
| Q07a | - |  |  | SI | Comments |
| Q08 | - |  |  | SI | Tearful / Low in mood |
| Q08ObsDR | - |  |  | SI | Tearful / Low in mood DR |
| Q08a | - |  |  | SI | Comments |
| Q09 | - |  |  | SI | Lying Awake |
| Q09ObsDR | - |  |  | SI | Lying Awake DR |
| Q09a | - |  |  | SI | Comments |
| Q10 | - |  |  | SI | Hallucinating |
| Q10ObsDR | - |  |  | SI | Hallucinating DR |
| Q10a | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Notes |
| Q12 | - |  |  | SI | Additional Notes |
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