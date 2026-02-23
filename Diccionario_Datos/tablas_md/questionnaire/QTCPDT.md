# questionnaire.QTCPDT

> Peritoneal Dialysis Training

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Training

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | numeric |  |  | SI | Training day number |
| Q05 | varchar |  |  | SI | Training modality |
| Q06 | varchar |  |  | SI | Notes |
| Q07 | varchar |  |  | SI | Continuous Ambulatory Peritoneal Dialysis System (... |
| Q08 | varchar |  |  | SI | Continuous Ambulatory Peritoneal Dialysis (CAPD) s... |
| Q09 | varchar |  |  | SI | Other CAPD system  |
| Q10 | varchar |  |  | SI | Exchange |
| Q11 | varchar |  |  | SI | Volume drained (mL) |
| Q12 | varchar |  |  | SI | Fill volume (mL) |
| Q13 | varchar |  |  | SI | Exchange 1 |
| Q14 | varchar |  |  | SI | Exchange 2 |
| Q15 | varchar |  |  | SI | Exchange 3 |
| Q16 | varchar |  |  | SI | Exchange 4 |
| Q17 | varchar |  |  | SI | Exchange 1 |
| Q18 | numeric |  |  | SI | Exchange 1 - Volume drained (mL) |
| Q19 | numeric |  |  | SI | Exchange 1 - Fill volume (mL) |
| Q20 | varchar |  |  | SI | Exchange 2 |
| Q21 | numeric |  |  | SI | Exchange 2 - Volume drained (mL) |
| Q22 | numeric |  |  | SI | Exchange 2 - Fill volume (mL) |
| Q23 | varchar |  |  | SI | Exchange 3 |
| Q24 | numeric |  |  | SI | Exchange 3 - Volume drained (mL) |
| Q25 | numeric |  |  | SI | Exchange 3 - Fill volume (mL) |
| Q26 | varchar |  |  | SI | Exchange 4 |
| Q27 | numeric |  |  | SI | Exchange 4 - Volume drained (mL) |
| Q28 | numeric |  |  | SI | Exchange 4 - Fill volume (mL) |
| Q29 | varchar |  |  | SI | CAPD training notes |
| Q30 | varchar |  |  | SI | Automated Peritoneal Dialysis System (APD) |
| Q31 | varchar |  |  | SI | Automated Peritoneal Dialysis system |
| Q32 | varchar |  |  | SI | Other APD system |
| Q33 | numeric |  |  | SI | Number of cycles |
| Q34 | numeric |  |  | SI | APD - Fill volume (mL) |
| Q35 | numeric |  |  | SI | APD - Ultrafiltration (mL) |
| Q36 | varchar |  |  | SI | Glucose used |
| Q37 | numeric |  |  | SI | Last fill (mL) |
| Q38 | varchar |  |  | SI | APD training notes |
| Q39 | varchar |  |  | SI | Exchange 1 |
| Q40 | varchar |  |  | SI | Exchange 1 - Volume drained (mL) |
| Q41 | varchar |  |  | SI | Exchange 1 - Fill volume (mL) |
| Q42 | varchar |  |  | SI | Exchange 2 |
| Q43 | varchar |  |  | SI | Exchange 2 - Volume drained (mL) |
| Q44 | varchar |  |  | SI | Exchange 2 - Fill volume (mL) |
| Q45 | varchar |  |  | SI | Exchange 3 |
| Q46 | varchar |  |  | SI | Exchange 3 - Volume drained (mL) |
| Q47 | varchar |  |  | SI | Exchange 3 - Fill volume (mL) |
| Q48 | varchar |  |  | SI | Exchange 4 |
| Q49 | varchar |  |  | SI | Exchange 4 - Volume drained (mL) |
| Q50 | varchar |  |  | SI | Exchange 4 - Fill volume (mL) |
| Q51 | varchar |  |  | SI | Glucose used |
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