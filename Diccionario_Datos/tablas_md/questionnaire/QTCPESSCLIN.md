# questionnaire.QTCPESSCLIN

> Nurse Pessary Assessment

**Schema:** questionnaire
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Nurse Pessary Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Staff introductions made |
| Q02 | varchar |  |  | SI | Medication history |
| Q03 | varchar |  |  | SI | Add to clinical documentation of Medication Histor... |
| Q04 | varchar |  |  | SI | Any changes to medication |
| Q05 | varchar |  |  | SI | Add to clinical documentation of Current Medicatio... |
| Q06 | varchar |  |  | SI | Notes |
| Q07 | varchar |  |  | SI | Health problems |
| Q08 | varchar |  |  | SI | Add to clinical documentation of Problems |
| Q09 | varchar |  |  | SI | Any concerns / safeguarding issues |
| Q10 | varchar |  |  | SI | Notes |
| Q11 | varchar |  |  | SI | Do you experience any of the following |
| Q12 | varchar |  |  | SI | Discussed appropriateness of continued ring pessar... |
| Q13 | varchar |  |  | SI | Notes |
| Q14 | varchar |  |  | SI | Vaginal epithelium intact |
| Q15 | varchar |  |  | SI | Notes |
| Q16 | varchar |  |  | SI | Pessary re-fitted |
| Q17 | varchar |  |  | SI | Add pessary type to clinical documentation of Proc... |
| Q18 | varchar |  |  | SI | Notes |
| Q19 | numeric |  |  | SI | Pessary size |
| Q20 | numeric |  |  | SI | Pessary lot no |
| Q21 | varchar |  |  | SI | Notes |
| Q22 | varchar |  |  | SI | Chaperone |
| Q23 | varchar |  |  | SI | Notes |
| Q24 | varchar |  |  | SI | Medication history |
| Q25 | varchar |  |  | SI | Please ensure you add any relevant medication hist... |
| Q26 | varchar |  |  | SI | Any changes to medication |
| Q27 | varchar |  |  | SI | Please ensure you add any relevant medication to t... |
| Q28 | varchar |  |  | SI | Health problems |
| Q29 | varchar |  |  | SI | Please ensure you add any relevant past medical hi... |
| Q30 | varchar |  |  | SI | Pessary re-fitted |
| Q31 | varchar |  |  | SI | Please ensure you add any relevant pessary type to... |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
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