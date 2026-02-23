# questionnaire.QTCCACT

> Child Asthma Control Test (CACT)

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Child Asthma Control Test (CACT)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Asthma |
| Q04 | varchar |  |  | SI | How is your asthma today? |
| Q05 | varchar |  |  | SI | How much of a problem is your asthma when you run,... |
| Q06 | varchar |  |  | SI | Does your asthma make you cough? |
| Q07 | varchar |  |  | SI | Does your asthma make you wake up during the night... |
| Q08 | varchar |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q09 | varchar |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q10 | varchar |  |  | SI | During the last 4 weeks, how many days did your ch... |
| Q11 | varchar |  |  | SI | Score |
| Q12 | varchar |  |  | SI | Classification |
| Q13 | varchar |  |  | SI | 0 - 11 |
| Q14 | varchar |  |  | SI | Very poorly controlled asthma |
| Q15 | varchar |  |  | SI | 12 - 19 |
| Q16 | varchar |  |  | SI | Poorly controlled asthma |
| Q17 | varchar |  |  | SI | 20 - 27 |
| Q18 | varchar |  |  | SI | Well controlled asthma |
| Q19 | varchar |  |  | SI | 0 - 11: Very poorly controlled asthma |
| Q20 | varchar |  |  | SI | 12 - 19: Poorly controlled asthma |
| Q21 | varchar |  |  | SI | 20 - 27: Well controlled asthma |
| Q22 | varchar |  |  | SI | The Child Asthma Control Test (CACT) is a 7-item s... |
| Q23 | varchar |  |  | SI | Guidelines |
| Q24 | varchar |  |  | SI | • Let your child respond to the first 4 questions ... |
| Q25 | varchar |  |  | SI | Complete the remaining 3 questions (5 to 7) on you... |
| Q26 | varchar |  |  | SI | Provenance Details |
| Q27 | varchar |  |  | SI | Based on the publication: |
| Q28 | varchar |  |  | SI | • Development of the Asthma Control Test: A survey... |
| Q29 | varchar |  |  | SI | • Development and cross-sectional validation of th... |
| Q30 | varchar |  |  | SI | Important information for use |
| Q31 | varchar |  |  | SI | • The GSK Asthma Control Test is for persons whom ... |
| Q32 | varchar |  |  | SI | prevention, monitoring, prediction, prognosis, tre... |
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