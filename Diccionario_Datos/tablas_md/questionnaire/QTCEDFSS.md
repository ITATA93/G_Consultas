# questionnaire.QTCEDFSS

> Expanded Disability and Functional Status Scale

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Expanded Disability and Functional Status Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Ambulation |
| Q02 | varchar |  |  | SI | Pyramidal |
| Q03 | varchar |  |  | SI | Cerebellar |
| Q04 | varchar |  |  | SI | Brainstem |
| Q05 | varchar |  |  | SI | Sensory |
| Q06 | varchar |  |  | SI | Bowel and bladder |
| Q07 | varchar |  |  | SI | Visual |
| Q08 | varchar |  |  | SI | Cerebral |
| Q09 | varchar |  |  | SI | Other |
| Q10 | varchar |  |  | SI | Expanded Disability and Functional Status Scale is... |
| Q11 | varchar |  |  | SI | Normal ambulation |
| Q12 | varchar |  |  | SI | 1.0 - 4.5 |
| Q13 | varchar |  |  | SI | Impaired ambulation |
| Q14 | varchar |  |  | SI | 5.0 - 9.5 |
| Q15 | varchar |  |  | SI | Ambulation Score |
| Q16 | varchar |  |  | SI | Functional Systems Score |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | 1.0 - 4.5: Normal ambulation |
| Q20 | varchar |  |  | SI | 5.0 - 9.5: Impaired ambulation |
| Q21 | varchar |  |  | SI | Ambulation Score Interpretation |
| Q22 | varchar |  |  | SI | Functional Systems Score Interpretation |
| Q23 | varchar |  |  | SI | Score range of 1-40	 |
| Q24 | varchar |  |  | SI | Higher score indicates more functional disability |
| Q25 | varchar |  |  | SI | Lower score indicates less functional disability |
| Q26 | varchar |  |  | SI | Score range of 1-40: Higher score indicates more f... |
| Q27 | varchar |  |  | SI | Score range of 1-40: Lower score indicates less fu... |
| Q28 | varchar |  |  | SI | Normal functional systems |
| Q29 | varchar |  |  | SI | Fully ambulatory |
| Q30 | varchar |  |  | SI | Death due to Multiple Sclerosis |
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