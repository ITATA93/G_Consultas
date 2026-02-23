# questionnaire.QTCNSFUNCS

> Functional Outcome in patients with Primary Intracerebral Hemorrhage (FUNC) Score

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Functional Outcome in patients with Primary Intracerebral Hemorrhage (FUNC) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Age (years) |
| Q02 | varchar |  |  | SI | Intracerebral Hemorrhage (ICH) volume (cm³) |
| Q03 | varchar |  |  | SI | ICH location |
| Q04 | varchar |  |  | SI | Glasgow Coma Scale (GCS) Score |
| Q05 | varchar |  |  | SI | Pre-ICH cognitive impairment  |
| Q06 | varchar |  |  | SI | The FUNC score is a clinical tool used at hospital... |
| Q08 | varchar |  |  | SI | FUNC Score categories and percent achieving functi... |
| Q09 | varchar |  |  | SI | Score 0-4: 0% |
| Q10 | varchar |  |  | SI | Score 5-7: 29% |
| Q11 | varchar |  |  | SI | Score 8: 48% |
| Q12 | varchar |  |  | SI | Score 9-10: 75% |
| Q13 | varchar |  |  | SI | Score 11: 95% |
| Q14 | varchar |  |  | SI | Functional Outcome in Patients with Primary Intrac... |
| Q15 | date |  |  | SI | Date |
| Q16 | time |  |  | SI | Time |
| Q17 | varchar |  |  | SI | Score |
| Q18 | varchar |  |  | SI | Classification |
| Q19 | varchar |  |  | SI | 0 - 4 |
| Q20 | varchar |  |  | SI | 0% achieving functional independence at 90 days |
| Q21 | varchar |  |  | SI | 5 - 7 |
| Q22 | varchar |  |  | SI | 29% achieving functional independence at 90 days |
| Q23 | varchar |  |  | SI | 8 |
| Q24 | varchar |  |  | SI | 48% achieving functional independence at 90 days |
| Q25 | varchar |  |  | SI | 9 - 10 |
| Q26 | varchar |  |  | SI | 75% achieving functional independence at 90 days |
| Q27 | varchar |  |  | SI | 11 |
| Q28 | varchar |  |  | SI | 95% achieving functional independence at 90 days |
| Q29 | varchar |  |  | SI | 0 - 4: 0% achieving functional independence at 90 ... |
| Q30 | varchar |  |  | SI | 5 - 7: 0% achieving functional independence at 90 ... |
| Q31 | varchar |  |  | SI | 8: 48% achieving functional independence at 90 day... |
| Q32 | varchar |  |  | SI | 9 - 10: 75% achieving functional independence at 9... |
| Q33 | varchar |  |  | SI | 11: 95% achieving functional independence at 90 da... |
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