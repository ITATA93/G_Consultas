# questionnaire.QTCNSICHS

> Intracerebral Hemorrhage (ICH) Score

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Intracerebral Hemorrhage (ICH) Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Glasgow Coma Score input |
| Q02 | varchar |  |  | SI | Age ≥ 80 years |
| Q03 | varchar |  |  | SI | ICH Volume ≥ 30ml |
| Q04 | varchar |  |  | SI | Intraventricular Hemorrhage |
| Q05 | varchar |  |  | SI | Infratentorial Origin of Hemorrhage |
| Q06 | varchar |  |  | SI | ICH score is primarily used as a clinical grading ... |
| Q07 | varchar |  |  | SI | Identifies patients with ICH who will attain funct... |
| Q08 | varchar |  |  | SI | 30-day mortality increases as the (summed) ICH sco... |
| Q09 | varchar |  |  | SI | Score 0: No mortailty |
| Q10 | varchar |  |  | SI | Score 1: 13% mortality chances |
| Q11 | varchar |  |  | SI | Score 2: 26% mortality chances |
| Q12 | varchar |  |  | SI | Score 3: 72% mortality chances |
| Q13 | varchar |  |  | SI | Score 4: 97% mortality chances |
| Q14 | varchar |  |  | SI | Score 5 - 6: 100% mortality chances |
| Q15 | varchar |  |  | SI | ICH score is primarily used as a clinical grading ... |
| Q16 | varchar |  |  | SI | This score is often used in conjunction with the F... |
| Q17 | date |  |  | SI | Date |
| Q18 | time |  |  | SI | Time |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | 1 |
| Q22 | varchar |  |  | SI | 13% mortality chances |
| Q23 | varchar |  |  | SI | 2 |
| Q24 | varchar |  |  | SI | 26% mortality chances |
| Q25 | varchar |  |  | SI | 3 |
| Q26 | varchar |  |  | SI | 72% mortality chances |
| Q27 | varchar |  |  | SI | 4 |
| Q28 | varchar |  |  | SI | 97% mortality chances |
| Q29 | varchar |  |  | SI | 5 - 6 |
| Q30 | varchar |  |  | SI | 100% mortality chances |
| Q31 | varchar |  |  | SI | 0 |
| Q32 | varchar |  |  | SI | No mortailty |
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