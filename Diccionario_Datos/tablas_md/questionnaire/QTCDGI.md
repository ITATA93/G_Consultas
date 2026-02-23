# questionnaire.QTCDGI

> Dynamic Gait Index

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dynamic Gait Index

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Instructions - Walk at your normal speed from here... |
| Q04 | varchar |  |  | SI | 1. Gait level surface |
| Q05 | varchar |  |  | SI | Instructions - Begin walking at your normal pace (... |
| Q06 | varchar |  |  | SI | 2. Change in gait speed |
| Q07 | varchar |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q08 | varchar |  |  | SI | Keep looking to the right until I tell you, ''look... |
| Q09 | varchar |  |  | SI | Keep your head to the left until I tell you ''look... |
| Q10 | varchar |  |  | SI | 3. Gait with horizontal head turns |
| Q11 | varchar |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q12 | varchar |  |  | SI | Keep looking up until I tell you, ''look down'', t... |
| Q13 | varchar |  |  | SI | 4. Gait with vertical head turns |
| Q14 | varchar |  |  | SI | Instructions - Begin walking at your normal pace. ... |
| Q15 | varchar |  |  | SI | 5. Gait and pivot turn |
| Q16 | varchar |  |  | SI | Instructions - Begin walking at your normal speed.... |
| Q17 | varchar |  |  | SI | 6. Step over obstacle |
| Q18 | varchar |  |  | SI | Instructions - Begin walking at normal speed. When... |
| Q19 | varchar |  |  | SI | When you come to the second cone (6 ft / 1.8 m pas... |
| Q20 | varchar |  |  | SI | 7. Step around obstacles |
| Q21 | varchar |  |  | SI | Instructions - Walk up these stairs as you would a... |
| Q22 | varchar |  |  | SI | 8. Steps |
| Q23 | varchar |  |  | SI | Notes |
| Q24 | varchar |  |  | SI | Herdman SJ. Vestibular Rehabilitation. 2nd ed. Phi... |
| Q25 | varchar |  |  | SI | Shumway-Cook A, Woollacott M. Motor Control Theory... |
| Q26 | varchar |  |  | SI | Whitney SL, Marchetti GF, Schade A, Wrisley DM. Th... |
| Q27 | varchar |  |  | SI | Equipment needed - Box (Shoebox), Cones (2), Stair... |
| Q28 | varchar |  |  | SI | Completion time: 15 min |
| Q29 | varchar |  |  | SI | Scoring - A four-point ordinal scale, ranging from... |
| Q30 | varchar |  |  | SI | Grading - Mark the lowest category that applies. |
| Q31 | varchar |  |  | SI | The Dynamic Gait Index was developed to assess the... |
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