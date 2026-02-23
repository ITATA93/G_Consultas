# questionnaire.QTCCRIES8

> Revised Child Impact of Events Scale (CRIES-8)

**Schema:** questionnaire
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Revised Child Impact of Events Scale (CRIES-8)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | 7. Do other things keep making you think about it?... |
| Q11 | varchar |  |  | SI | 8. Do you try not to think about it? |
| Q12 | varchar |  |  | SI | If they did not occur during that time please sele... |
| Q13 | varchar |  |  | SI | Score |
| Q14 | varchar |  |  | SI | Classification |
| Q15 | varchar |  |  | SI | 0 - 40 |
| Q16 | varchar |  |  | SI | Higher scores indicate higher PTSD symptoms |
| Q17 | varchar |  |  | SI | 0 - 40: Higher scores indicate higher PTSD symptom... |
| Q18 | varchar |  |  | SI | The Children’s Impact of Event Scale, 8-item (CRIE... |
| Q19 | varchar |  |  | SI | Intrusion score |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Avoidance score |
| Q3 | varchar |  |  | SI | Below is a list of comments made by people after s... |
| Q4 | varchar |  |  | SI | 1. Do you think about it even when you dont mean t... |
| Q5 | varchar |  |  | SI | 2. Do you try to remove it from your memory? |
| Q6 | varchar |  |  | SI | 3. Do you have waves of strong feelings about it? |
| Q7 | varchar |  |  | SI | 4. Do you stay away from reminders of it (e.g. pla... |
| Q8 | varchar |  |  | SI | 5. Do you try not talk about it? |
| Q9 | varchar |  |  | SI | 6. Do pictures about it pop into your mind? |
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