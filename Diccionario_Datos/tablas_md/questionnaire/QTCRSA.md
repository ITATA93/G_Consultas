# questionnaire.QTCRSA

> Respiratory Symptom Assessment

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Respiratory Symptom Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Symptom Assessment |
| Q04 | varchar |  |  | SI | Cough |
| Q05 | varchar |  |  | SI | Other cough notes |
| Q06 | varchar |  |  | SI | Sputum |
| Q07 | varchar |  |  | SI | Other sputum notes |
| Q08 | varchar |  |  | SI | Sputum amount |
| Q09 | varchar |  |  | SI | Shortness of Breath (SOB) |
| Q10 | varchar |  |  | SI | Other SOB notes |
| Q11 | varchar |  |  | SI | Client able to walk |
| Q12 | varchar |  |  | SI | Dyspnoea Severity (Modified Medical Research Counc... |
| Q12ObsDR | varchar |  | FK | SI | Dyspnoea Severity (Modified Medical Research Counc... |
| Q13 | varchar |  |  | SI | Sleeping |
| Q14 | varchar |  |  | SI | Other sleeping notes |
| Q15 | varchar |  |  | SI | Symptom assessment notes |
| Q16 | varchar |  |  | SI | Medications / Medication Devices |
| Q17 | varchar |  |  | SI | Observe inhaler / device technique at each visit |
| Q18 | varchar |  |  | SI | Review of current inhalers conducted |
| Q19 | varchar |  |  | SI | Inhaler observation and review notes |
| Q20 | varchar |  |  | SI | Distance walked |
| Q21 | varchar |  |  | SI | Information / Education and Support |
| Q22 | varchar |  |  | SI | Topics covered |
| Q23 | varchar |  |  | SI | Other topics covered |
| Q24 | varchar |  |  | SI | Support network |
| Q25 | varchar |  |  | SI | Other support |
| Q26 | varchar |  |  | SI | Information / Education and support notes |
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