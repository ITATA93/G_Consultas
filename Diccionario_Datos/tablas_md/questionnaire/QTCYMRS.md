# questionnaire.QTCYMRS

> Young Mania Rating Scale (YMRS)

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Young Mania Rating Scale (YMRS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Elevated mood |
| Q04 | varchar |  |  | SI | Increased motor activity - energy |
| Q05 | varchar |  |  | SI | Sexual interest |
| Q06 | varchar |  |  | SI | Sleep |
| Q07 | varchar |  |  | SI | Irritability |
| Q08 | varchar |  |  | SI | Speech (rate and amount) |
| Q09 | varchar |  |  | SI | Language - thought disorder |
| Q10 | varchar |  |  | SI | Content |
| Q11 | varchar |  |  | SI | Disruptive - aggressive behavior |
| Q12 | varchar |  |  | SI | Appearance |
| Q13 | varchar |  |  | SI | Insight |
| Q14 | varchar |  |  | SI | • The scale is generally done by a clinician or ot... |
| Q15 | varchar |  |  | SI | • The purpose of each item is to rate the severity... |
| Q16 | varchar |  |  | SI | • The keys provided are guides. One can ignore the... |
| Q17 | varchar |  |  | SI | Scoring between the points given (whole or half po... |
| Q18 | varchar |  |  | SI | This is particularly useful when severity of a par... |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | 0 - 60 |
| Q22 | varchar |  |  | SI | Higher score indicates worse manic symptoms |
| Q23 | varchar |  |  | SI | 0 - 60: Higher score indicates worse manic symptom... |
| Q24 | varchar |  |  | SI | The Young Mania Rating Scale (YMRS) is one of the ... |
| Q25 | varchar |  |  | SI | The scale has 11 items and is based on the patient... |
| Q26 | varchar |  |  | SI | Sometimes a clinical study entry requirement of YM... |
| Q27 | varchar |  |  | SI | • There are four items that are graded on a 0 to 8... |
| Q28 | varchar |  |  | SI | These four items are given twice the weight of the... |
| Q29 | varchar |  |  | SI | • There are well described anchor points for each ... |
| Q30 | varchar |  |  | SI | They depend on the patients’ clinical features suc... |
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