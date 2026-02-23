# questionnaire.QTCCOPDAT

> COPD Assessment Test (CAT)

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* COPD Assessment Test (CAT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Cough score |
| Q04 | varchar |  |  | SI | I never cough (0) |
| Q05 | varchar |  |  | SI | I cough all the time (5) |
| Q06 | varchar |  |  | SI | Phlegm score |
| Q07 | varchar |  |  | SI | I have no phlegm (mucus) on my chest at all (0) |
| Q08 | varchar |  |  | SI | My chest is full of phlegm (mucus) (5) |
| Q09 | varchar |  |  | SI | Chest tightness score |
| Q10 | varchar |  |  | SI | My chest does not feel tight at all (0) |
| Q11 | varchar |  |  | SI | My chest feels very tight (5) |
| Q12 | varchar |  |  | SI | Shortness of breath score  |
| Q13 | varchar |  |  | SI | When I walk up a hill or a flight of stairs I am n... |
| Q14 | varchar |  |  | SI | When I walk up a hill or a flight of stairs I am c... |
| Q15 | varchar |  |  | SI | Activities at home score  |
| Q16 | varchar |  |  | SI | I am not limited to doing any activities at home (... |
| Q17 | varchar |  |  | SI | I am completely limited to doing all activities at... |
| Q18 | varchar |  |  | SI | Leave my home score |
| Q19 | varchar |  |  | SI | I am confident leaving my home despite my lung con... |
| Q20 | varchar |  |  | SI | I am not confident leaving my home at all because ... |
| Q21 | varchar |  |  | SI | Sleep score |
| Q22 | varchar |  |  | SI | I sleep soundly (0) |
| Q23 | varchar |  |  | SI | I do not sleep soundly because of my lung conditio... |
| Q24 | varchar |  |  | SI | Energy score |
| Q25 | varchar |  |  | SI | I have lots of energy (0) |
| Q26 | varchar |  |  | SI | I have no energy at all (5) |
| Q27 | varchar |  |  | SI | 0 - 40 |
| Q28 | varchar |  |  | SI | Higher score indicates higher impact that COPD is ... |
| Q29 | varchar |  |  | SI | Score |
| Q30 | varchar |  |  | SI | Classification |
| Q31 | varchar |  |  | SI | The COPD Assessment Test (CAT) is a questionnaire ... |
| Q32 | varchar |  |  | SI | It is designed to measure the impact of COPD on a ... |
| Q33 | varchar |  |  | SI | 0 - 40: Higher score indicates higher impact that ... |
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