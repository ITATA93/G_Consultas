# questionnaire.QTCMRSS

> Modified Rodnan Skin Score (mRSS)

**Schema:** questionnaire
**Columnas:** 93
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified Rodnan Skin Score (mRSS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Fingers - Right |
| Q04 | varchar |  |  | SI | Fingers - Left |
| Q05 | varchar |  |  | SI | Hand - Right |
| Q06 | varchar |  |  | SI | Hand - Left |
| Q07 | varchar |  |  | SI | Forearm - Right |
| Q08 | varchar |  |  | SI | Forearm - Left |
| Q09 | varchar |  |  | SI | Upper arm - Right |
| Q10 | varchar |  |  | SI | Upper arm - Left |
| Q11 | varchar |  |  | SI | Face |
| Q12 | varchar |  |  | SI | Anterior chest |
| Q13 | varchar |  |  | SI | Abdomen |
| Q14 | varchar |  |  | SI | Thigh - Right |
| Q15 | varchar |  |  | SI | Thigh - Left |
| Q16 | varchar |  |  | SI | Leg - Right |
| Q17 | varchar |  |  | SI | Leg - Left |
| Q18 | varchar |  |  | SI | Feet - Right |
| Q19 | varchar |  |  | SI | Feet - Left |
| Q20 | varchar |  |  | SI | Notes |
| Q21 | varchar |  |  | SI | Score |
| Q22 | varchar |  |  | SI | Modified Rodnan Skin Score score range 0 to 51. Hi... |
| Q23 | varchar |  |  | SI | Right |
| Q24 | varchar |  |  | SI | Left |
| Q25 | varchar |  |  | SI | Fingers |
| Q26 | varchar |  |  | SI | Hand |
| Q27 | varchar |  |  | SI | Forearm |
| Q28 | varchar |  |  | SI | Upper arm |
| Q29 | varchar |  |  | SI | Thigh |
| Q30 | varchar |  |  | SI | Leg |
| Q31 | varchar |  |  | SI | Feet |
| Q34 | varchar |  |  | SI | Right |
| Q35 | varchar |  |  | SI | Right |
| Q36 | varchar |  |  | SI | Right |
| Q37 | varchar |  |  | SI | Right |
| Q38 | varchar |  |  | SI | Right |
| Q39 | varchar |  |  | SI | Left |
| Q40 | varchar |  |  | SI | Face |
| Q41 | varchar |  |  | SI | Anterior chest |
| Q42 | varchar |  |  | SI | Abdomen |
| Q43 | varchar |  |  | SI | Right |
| Q44 | varchar |  |  | SI | Right |
| Q45 | varchar |  |  | SI | Left |
| Q46 | varchar |  |  | SI | Left |
| Q47 | varchar |  |  | SI | Left |
| Q48 | varchar |  |  | SI | Left |
| Q49 | varchar |  |  | SI | Left |
| Q50 | varchar |  |  | SI | Left |
| Q51 | varchar |  |  | SI | Left |
| Q52 | varchar |  |  | SI | Right |
| Q53 | varchar |  |  | SI | Annotated image |
| Q54 | varchar |  |  | SI | (Khanna D, Furst DE, Clements PJ, et al. Standardi... |
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