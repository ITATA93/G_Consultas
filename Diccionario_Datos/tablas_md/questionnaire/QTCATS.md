# questionnaire.QTCATS

> Audiometry Test Sheet

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Audiometry Test Sheet

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Pure-tone audiogram |
| Q02 | date |  |  | SI | Date |
| Q03 | time |  |  | SI | Time |
| Q04 | varchar |  |  | SI | Right ear |
| Q05 | varchar |  |  | SI | Right ear |
| Q06 | varchar |  |  | SI | Left ear |
| Q07 | varchar |  |  | SI | Left ear |
| Q08 | varchar |  |  | SI | Reliability |
| Q09 | varchar |  |  | SI | Masking type |
| Q10 | varchar |  |  | SI | Masking level |
| Q11 | varchar |  |  | SI | Ear |
| Q12 | varchar |  |  | SI | Speech audiometry results |
| Q13 | varchar |  |  | SI | Right ear |
| Q14 | varchar |  |  | SI | Left ear |
| Q15 | varchar |  |  | SI | Speech Reception Threshold Level |
| Q16 | varchar |  |  | SI | Speech Disc. Score % |
| Q17 | varchar |  |  | SI | Intensity of Speech Disc. |
| Q18 | varchar |  |  | SI | Masking Level of Speech Reception Threshold |
| Q19 | varchar |  |  | SI | Masking Level of Speech Disc. |
| Q20 | varchar |  |  | SI | Aided Speech Disc. Scores |
| Q21 | varchar |  |  | SI | Speech Reception Threshold Level |
| Q22 | varchar |  |  | SI | Speech Disc. Score % |
| Q23 | varchar |  |  | SI | Intensity of Speech Disc. |
| Q24 | varchar |  |  | SI | Masking Level of Speech Reception Threshold |
| Q25 | varchar |  |  | SI | Masking Level of Speech Disc. |
| Q26 | varchar |  |  | SI | Aided Speech Disc. Scores |
| Q27 | varchar |  |  | SI | Remarks & comments |
| Q28 | varchar |  |  | SI | Recommendations |
| Q29 | varchar |  |  | SI | Left Ear |
| Q30 | varchar |  |  | SI | Right Ear |
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