# questionnaire.QTCCHAS

> Clarke Hypoglycaemia Awareness Survey

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Clarke Hypoglycaemia Awareness Survey

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | 1. Select the category that best describes you |
| Q04 | varchar |  |  | SI | 2. Have you lost some of the symptoms that used to... |
| Q05 | varchar |  |  | SI | 3. In the past six months how often have you had m... |
| Q06 | varchar |  |  | SI | (Episodes where you might feel confused, disorient... |
| Q07 | varchar |  |  | SI | 4. In the past how often have you had severe hypog... |
| Q08 | varchar |  |  | SI | (Episodes where you were unconscious or had a seiz... |
| Q09 | varchar |  |  | SI | 5. How often in the last month have you had readin... |
| Q10 | varchar |  |  | SI | 6. How often in the last month have you had readin... |
| Q11 | varchar |  |  | SI | Compare patient responses to questions 5 and 6 |
| Q12 | varchar |  |  | SI | 7. How low does your blood sugar go before you fee... |
| Q13 | varchar |  |  | SI | 8. To what extent can you tell by your symptoms th... |
| Q14 | varchar |  |  | SI | The survey assesses hypoglycaemia awareness and is... |
| Q15 | varchar |  |  | SI | • For people who have been on insulin for many yea... |
| Q16 | varchar |  |  | SI | • After a severe hypoglycaemic event |
| Q17 | varchar |  |  | SI | • After a crash |
| Q18 | varchar |  |  | SI | • A = Awareness |
| Q19 | varchar |  |  | SI | • R = Reduced awareness |
| Q20 | varchar |  |  | SI | • U = Unaware |
| Q21 | varchar |  |  | SI | • Four or more 'R' responses implies reduced hypog... |
| Q22 | varchar |  |  | SI | • 'U' response (12 or more severe hypoglycaemic ep... |
| Q23 | varchar |  |  | SI | • For question 5 and 6, one 'R' response is given ... |
| Q24 | varchar |  |  | SI | Score |
| Q25 | varchar |  |  | SI | Classification |
| Q26 | varchar |  |  | SI | 0 - 3 |
| Q27 | varchar |  |  | SI | Aware |
| Q28 | varchar |  |  | SI | 4 - 7 |
| Q29 | varchar |  |  | SI | Reduced awareness |
| Q30 | varchar |  |  | SI | >= 20 |
| Q31 | varchar |  |  | SI | Unaware |
| Q32 | varchar |  |  | SI | The Clarke Hypoglycaemia Awareness Survey comprise... |
| Q33 | varchar |  |  | SI | It also examines the glycaemic threshold for, and ... |
| Q34 | varchar |  |  | SI | Scoring |
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