# questionnaire.QTCCFCS

> Communication Function Classification System (CFCS) For Individuals With Cerebral Palsy

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Communication Function Classification System (CFCS) For Individuals With Cerebral Palsy

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Patient level |
| Q04 | varchar |  |  | SI | Guidelines |
| Q05 | varchar |  |  | SI | Level I |
| Q06 | varchar |  |  | SI | I.The person independently alternates between send... |
| Q07 | varchar |  |  | SI | Unfamiliar and familiar conversational partners. c... |
| Q08 | varchar |  |  | SI | Level II |
| Q09 | varchar |  |  | SI | II.The person independently alternates between sen... |
| Q10 | varchar |  |  | SI | The person may need extra time to understand messa... |
| Q11 | varchar |  |  | SI | Eventual effectiveness of the persons communicatio... |
| Q12 | varchar |  |  | SI | Level III |
| Q13 | varchar |  |  | SI | III.The person alternates between sender and recei... |
| Q14 | varchar |  |  | SI | Communication is not consistently effective with m... |
| Q15 | varchar |  |  | SI | Level IV |
| Q16 | varchar |  |  | SI | IV.The person does not consistently alternate send... |
| Q17 | varchar |  |  | SI | a) an occasionally effective sender and receiver; ... |
| Q18 | varchar |  |  | SI | Level V |
| Q19 | varchar |  |  | SI | V.The person is limited as both a sender and a rec... |
| Q20 | varchar |  |  | SI | The person appears to have limited understanding o... |
| Q21 | varchar |  |  | SI | Reference |
| Q22 | varchar |  |  | SI | 1. Hidecker MJC, Paneth N, Rosenbaum PL,&nbsp;et a... |
| Q23 | varchar |  |  | SI | 2. Hidecker MJC, Paneth N, Rosenbaum PL,&nbsp;et a... |
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