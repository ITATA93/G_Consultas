# questionnaire.QTCKOOSPS

> KOOS-Physical Function Shortform (KOOS-PS)

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* KOOS-Physical Function Shortform (KOOS-PS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | The questions concern the patient's level of funct... |
| Q04 | varchar |  |  | SI | please indicate the degree of difficulty the patie... |
| Q05 | varchar |  |  | SI | last week  |
| Q06 | varchar |  |  | SI | due to his/her knee problem. |
| Q07 | varchar |  |  | SI | Rising from bed |
| Q08 | varchar |  |  | SI | Putting on socks / stockings |
| Q09 | varchar |  |  | SI | Rising from sitting |
| Q10 | varchar |  |  | SI | Bending to floor |
| Q11 | varchar |  |  | SI | Twisting / Pivoting on your injured knee |
| Q12 | varchar |  |  | SI | Kneeling |
| Q13 | varchar |  |  | SI | Squatting |
| Q14 | varchar |  |  | SI | Each item is scored from 0 to 4, with 0 representi... |
| Q15 | varchar |  |  | SI | KOOS-PS scale scores are transformed so the KOOS-P... |
| Q16 | varchar |  |  | SI | extreme difficulty (0)  |
| Q17 | varchar |  |  | SI | to  |
| Q18 | varchar |  |  | SI | no difficulty (100). |
| Q19 | varchar |  |  | SI | Score |
| Q20 | varchar |  |  | SI | Classification |
| Q21 | varchar |  |  | SI | 0 - 100 |
| Q22 | varchar |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
| Q23 | varchar |  |  | SI | 0 - 100: Scores range from 0 to 100 with a score o... |
| Q24 | varchar |  |  | SI | No difficulty |
| Q25 | varchar |  |  | SI | 0: Extreme difficulty |
| Q26 | varchar |  |  | SI | 100: No difficulty |
| Q27 | varchar |  |  | SI | The Knee Injury and Osteoarthritis Outcome Score (... |
| Q28 | varchar |  |  | SI | KOOS-PS Score |
| Q29 | varchar |  |  | SI | KOOS-PS Score |
| Q30 | varchar |  |  | SI | KOOS Score (Display only) |
| Q31 | varchar |  |  | SI | Scores range from 0 to 100 with a score of 0 indic... |
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