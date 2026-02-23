# questionnaire.QTCCHADS2

> CHADS₂Risk Score

**Schema:** questionnaire
**Columnas:** 87
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* CHADS₂Risk Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Congestive heart failure history |
| Q02 | varchar |  |  | SI | Hypertension history |
| Q03 | varchar |  |  | SI | Age ≥ 75 years |
| Q04 | varchar |  |  | SI | Diabetes mellitus history |
| Q05 | varchar |  |  | SI | Stroke or TIA symptoms previously |
| Q06 | varchar |  |  | SI | Stroke or thromboembolism (TE)/100 years at risk i... |
| Q07 | varchar |  |  | SI | STROKE OR TE/100 PERSON-YEARS |
| Q08 | varchar |  |  | SI | Score |
| Q09 | varchar |  |  | SI | Ischemic Stroke |
| Q10 | varchar |  |  | SI | Stroke / TIA / TE |
| Q11 | varchar |  |  | SI | 0 |
| Q12 | varchar |  |  | SI | 0.6 |
| Q13 | varchar |  |  | SI | 0.9 |
| Q14 | varchar |  |  | SI | 1 |
| Q15 | varchar |  |  | SI | 3 |
| Q16 | varchar |  |  | SI | 4.3 |
| Q17 | varchar |  |  | SI | 2 |
| Q18 | varchar |  |  | SI | 4.2 |
| Q19 | varchar |  |  | SI | 6.1 |
| Q20 | varchar |  |  | SI | 3 |
| Q21 | varchar |  |  | SI | 7.1 |
| Q22 | varchar |  |  | SI | 9.9 |
| Q23 | varchar |  |  | SI | 4 |
| Q24 | varchar |  |  | SI | 11.1 |
| Q25 | varchar |  |  | SI | 14.9 |
| Q26 | varchar |  |  | SI | 5 |
| Q27 | varchar |  |  | SI | 12.5 |
| Q28 | varchar |  |  | SI | 16.7 |
| Q29 | varchar |  |  | SI | 6 |
| Q30 | varchar |  |  | SI | 13 |
| Q31 | varchar |  |  | SI | 17.2 |
| Q32 | varchar |  |  | SI | Score |
| Q33 | varchar |  |  | SI | Classification |
| Q34 | varchar |  |  | SI | 0 |
| Q35 | varchar |  |  | SI | Low risk of thromboembolic event |
| Q36 | varchar |  |  | SI | 1-2 |
| Q37 | varchar |  |  | SI | Intermediate risk of thromboembolic event |
| Q38 | varchar |  |  | SI | 3-6 |
| Q39 | varchar |  |  | SI | High risk of thromboembolic event |
| Q40 | varchar |  |  | SI | 0: Low risk of thromboembolic event |
| Q41 | varchar |  |  | SI | 1-2: Intermediate risk of thromboembolic event |
| Q42 | varchar |  |  | SI | 3-6: High risk of thromboembolic event |
| Q43 | varchar |  |  | SI | The CHADS₂score is one of several risk stratificat... |
| Q44 | varchar |  |  | SI | Stroke or Thromboembolism (TE)/100 Years at Risk i... |
| Q45 | date |  |  | SI | Date |
| Q46 | time |  |  | SI | Time |
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