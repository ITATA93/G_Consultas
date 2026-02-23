# questionnaire.QGXXXMSD

> Shoulder dystocia

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Shoulder dystocia

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Entered retrospectively |
| Q01ObsDR | varchar |  | FK | SI | Entered retrospectively DR |
| Q02 | time |  |  | SI | Assistance requested - time |
| Q03 | time |  |  | SI | Assistance arrived - time |
| Q04 | varchar |  |  | SI | Episiotomy done |
| Q04ObsDR | varchar |  | FK | SI | Episiotomy done DR |
| Q05 | time |  |  | SI | Episiotomy time |
| Q06 | time |  |  | SI | McRoberts position - time |
| Q07 | time |  |  | SI | Suprapubic pressure applied - time |
| Q08 | time |  |  | SI | Woods' screw manoeuvre - time |
| Q09 | time |  |  | SI | Delivery of posterior shoulder - time |
| Q10 | time |  |  | SI | Moved onto all fours - time |
| Q11 | varchar |  |  | SI | Other manoeuvres |
| Q12 | varchar |  |  | SI | Midwife countersigning |
| Q13 | time |  |  | SI | Help requested - time |
| Q14 | time |  |  | SI | Emergency call - time |
| Q15 | date |  |  | SI | Delivery of head - date |
| Q16 | time |  |  | SI | Delivery of head - time |
| Q17 | date |  |  | SI | Delivery of rest of baby - date |
| Q18 | time |  |  | SI | Delivery of rest of baby - time |
| Q19 | varchar |  |  | SI | Delivery notes |
| Q20 | varchar |  |  | SI | Mothers position before and during birth |
| Q21 | numeric |  |  | SI | Time from emergency call to delivery (mins) |
| Q22 | varchar |  |  | SI | Direction head facing |
| Q22ObsDR | varchar |  | FK | SI | Direction head facing DR |
| Q23 | bit |  |  | SI | Any sign of arm weakness |
| Q24 | bit |  |  | SI | Any sign of potential bony fracture |
| Q25 | varchar |  |  | SI | Assessed by |
| Q26 | varchar |  |  | SI | Shoulder |
| Q27 | time |  |  | SI | Rubin 2 manoeuvre - time |
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