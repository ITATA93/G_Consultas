# questionnaire.QTCIIEF

> "International Index of Erectile Function, Abridged (IIEF-5

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "International Index of Erectile Function, Abridged (IIEF-5

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Over the past 6 months |
| Q02 | varchar |  |  | SI | How do you rate your confidence that you could get... |
| Q03 | varchar |  |  | SI | When you had erections with sexual stimulation, ho... |
| Q04 | varchar |  |  | SI | During sexual intercourse, how often were you able... |
| Q05 | varchar |  |  | SI | During sexual intercourse, how difficult was it to... |
| Q06 | varchar |  |  | SI | When you attempted sexual intercourse, how often w... |
| Q07 | varchar |  |  | SI | Score |
| Q08 | varchar |  |  | SI | Classification |
| Q09 | varchar |  |  | SI | A self-administered tool which is an abridged five... |
| Q10 | varchar |  |  | SI | 5–7 |
| Q11 | varchar |  |  | SI | Severe erectile dysfunction |
| Q12 | varchar |  |  | SI | 8–11 |
| Q13 | varchar |  |  | SI | Moderate erectile dysfunction |
| Q14 | varchar |  |  | SI | 12–16 |
| Q15 | varchar |  |  | SI | Mild to moderate erectile dysfunction |
| Q16 | varchar |  |  | SI | 17–21 |
| Q17 | varchar |  |  | SI | Mild erectile dysfunction |
| Q18 | varchar |  |  | SI | 22–25 |
| Q19 | varchar |  |  | SI | No erectile dysfunction |
| Q20 | varchar |  |  | SI | IIEF-5 Scoring |
| Q21 | varchar |  |  | SI | The IIEF-5 score is the sum of the ordinal respons... |
| Q22 | varchar |  |  | SI | 22–25: No erectile dysfunction |
| Q23 | varchar |  |  | SI | 17–21: Mild erectile dysfunction |
| Q24 | varchar |  |  | SI | 12–16: Mild to moderate erectile dysfunction |
| Q25 | varchar |  |  | SI | 8–11: Moderate erectile dysfunction |
| Q26 | varchar |  |  | SI | 5–7: Severe erectile dysfunction |
| Q27 | date |  |  | SI | Date |
| Q28 | time |  |  | SI | Time |
| Q29 | varchar |  |  | SI | Rosen R, Cappelleri J, Smith M, Lipsky J, Peña B. ... |
| Q30 | varchar |  |  | SI | Int J Impot Res 1999;11:319–326. |
| Q31 | varchar |  |  | SI | A self-administered tool which is an abridged five... |
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