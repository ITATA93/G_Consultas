# questionnaire.QTCHSI

> Heaviness of Smoking Index (HSI)

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Heaviness of Smoking Index (HSI)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | How soon after you wake do you smoke your first ci... |
| Q04 | varchar |  |  | SI | How many cigarettes do you typically smoke per day... |
| Q05 | varchar |  |  | SI | Score |
| Q06 | varchar |  |  | SI | Classification |
| Q07 | varchar |  |  | SI | 0 - 2 |
| Q08 | varchar |  |  | SI | Low Nicotine Dependence |
| Q09 | varchar |  |  | SI | 3 - 4 |
| Q10 | varchar |  |  | SI | Medium Nicotine Dependence |
| Q11 | varchar |  |  | SI | 5 - 6 |
| Q12 | varchar |  |  | SI | High Nicotine Dependence |
| Q13 | varchar |  |  | SI | The Heaviness of Smoking Index (HSI) was developed... |
| Q14 | varchar |  |  | SI | 0 - 2: Low Nicotine Dependence |
| Q15 | varchar |  |  | SI | 3 - 4: Medium Nicotine Dependence |
| Q16 | varchar |  |  | SI | 5 - 6: High Nicotine Dependence |
| Q17 | varchar |  |  | SI | Guidelines |
| Q18 | varchar |  |  | SI | The Heaviness of Smoking Index (HSI) is a subset o... |
| Q19 | varchar |  |  | SI | The two-question HSI may be used in situations whe... |
| Q20 | varchar |  |  | SI | Dummy 1 |
| Q21 | varchar |  |  | SI | Dummy 2 |
| Q22 | varchar |  |  | SI | Dummy 3 |
| Q23 | varchar |  |  | SI | Heatherton TF; Kozlowski LT; Frecker RC; Rickert W... |
| Q24 | varchar |  |  | SI | Using self-reported time to the first cigarette of... |
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