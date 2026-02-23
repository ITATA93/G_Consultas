# questionnaire.QTCKINDER1

> KINDER 1 Falls Risk Assessment and Plan

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* KINDER 1 Falls Risk Assessment and Plan

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Presented to Emergency Department (ED) because of ... |
| Q04 | varchar |  |  | SI | Consider: syncope, seizure or loss of consciousnes... |
| Q05 | varchar |  |  | SI | Age > 70 years |
| Q06 | varchar |  |  | SI | Altered mental state |
| Q07 | varchar |  |  | SI | Consider: disorientation, impaired judgement, poor... |
| Q08 | varchar |  |  | SI | Impaired mobility |
| Q09 | varchar |  |  | SI | Consider: Ambulates or transfers with assistive de... |
| Q10 | varchar |  |  | SI | Ambulates with unsteady gait and no assistance |
| Q11 | varchar |  |  | SI | Unable to ambulate or transfer |
| Q12 | varchar |  |  | SI | Nurse judgement |
| Q13 | varchar |  |  | SI | Consider: bowel or bladder incontinence, diarrhoea... |
| Q14 | varchar |  |  | SI | Details of judgement |
| Q15 | varchar |  |  | SI | • Once an ED patient is deemed a high fall risk in... |
| Q16 | varchar |  |  | SI | • If patient does not have any fall risks identifi... |
| Q17 | varchar |  |  | SI |  If the patient falls in the ED, the patient becom... |
| Q18 | varchar |  |  | SI | • If patient is a high fall risk, fall prevention ... |
| Q19 | varchar |  |  | SI | The following section is not part of the KINDER 1 ... |
| Q20 | varchar |  |  | SI | Implement bedside safety plan |
| Q21 | varchar |  |  | SI | The following actions should be completed in all i... |
| Q22 | varchar |  |  | SI | Add falls risk against patient's alerts in TrakCar... |
| Q23 | varchar |  |  | SI | A full falls risk assessment and management plan t... |
| Q24 | varchar |  |  | SI | Consider criteria for referral to Falls and Balanc... |
| Q25 | varchar |  |  | SI | Score |
| Q26 | varchar |  |  | SI | Classification |
| Q27 | varchar |  |  | SI | 0 |
| Q28 | varchar |  |  | SI | No falls risk |
| Q29 | varchar |  |  | SI | 1 - 5 |
| Q30 | varchar |  |  | SI | High falls risk |
| Q31 | varchar |  |  | SI | 0: No falls risk |
| Q32 | varchar |  |  | SI | 1 - 5: High falls risk |
| Q33 | varchar |  |  | SI | The KINDER 1 falls risk assessment tool was design... |
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