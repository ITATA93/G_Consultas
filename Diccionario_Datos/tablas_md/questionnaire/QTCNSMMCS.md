# questionnaire.QTCNSMMCS

> Modified Mallet Classification Scale

**Schema:** questionnaire
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Mallet Classification Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Global Abduction |
| Q02 | varchar |  |  | SI | Global External Rotation |
| Q03 | varchar |  |  | SI | Hand to Neck |
| Q04 | varchar |  |  | SI | Hand to Spine |
| Q05 | varchar |  |  | SI | Hand to Mouth |
| Q06 | varchar |  |  | SI | Internal Rotation |
| Q07 | varchar |  |  | SI | The Mallet grading system is a commonly used funct... |
| Q08 | varchar |  |  | SI | Not Testable |
| Q09 | varchar |  |  | SI | Grade I |
| Q10 | varchar |  |  | SI | Grade II |
| Q11 | varchar |  |  | SI | Grade III |
| Q12 | varchar |  |  | SI | Grade IV |
| Q13 | varchar |  |  | SI | Grade V |
| Q14 | varchar |  |  | SI | Global Abduction Score |
| Q14G | varchar |  |  | SI | Global Abduction Grade |
| Q15 | varchar |  |  | SI | Global External Rotation Score |
| Q15G | varchar |  |  | SI | Global External Rotation Grade |
| Q16 | varchar |  |  | SI | Hand to Neck Score |
| Q16G | varchar |  |  | SI | Hand to Neck Grade |
| Q17 | varchar |  |  | SI | Hand to Spine Score |
| Q17G | varchar |  |  | SI | Hand to Spine Grade |
| Q18 | varchar |  |  | SI | Hand to Mouth Score |
| Q18G | varchar |  |  | SI | Hand to Mouth Grade |
| Q19 | varchar |  |  | SI | Internal Rotation Score |
| Q19G | varchar |  |  | SI | Internal Rotation Grade |
| Q20 | varchar |  |  | SI | Please refer to legend for grading |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*