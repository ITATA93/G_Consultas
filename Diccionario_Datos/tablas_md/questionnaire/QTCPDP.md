# questionnaire.QTCPDP

> Peritoneal Dialysis Prescription

**Schema:** questionnaire
**Columnas:** 83
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Peritoneal Dialysis Prescription

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Prescription type	 |
| Q02 | varchar |  |  | SI | Peritoneal dialysis type |
| Q03 | numeric |  |  | SI | Target weight (empty)	 |
| Q04 | numeric |  |  | SI | Number of exchanges	 |
| Q05 | numeric |  |  | SI | Total volume (ml) |
| Q06 | varchar |  |  | SI | Type of peritoneal dialysis solutions	 |
| Q07 | numeric |  |  | SI | APD target weight (empty)	 |
| Q08 | varchar |  |  | SI | Target (Nocturnal Intermittent Peritoneal Dialysis... |
| Q09 | numeric |  |  | SI | If on TIDAL, specify %	 |
| Q10 | numeric |  |  | SI | Duration of night therapy	 |
| Q11 | numeric |  |  | SI | Volume / Solution of last fill	 |
| Q12 | numeric |  |  | SI | Total volume	 |
| Q13 | varchar |  |  | SI | Additional day fill (specify)	 |
| Q14 | numeric |  |  | SI | Target empty weight (kg) |
| Q15 | numeric |  |  | SI | Comments |
| Q16 | date |  |  | SI | Date of prescription |
| Q17 | varchar |  |  | SI | Prescription type |
| Q18 | numeric |  |  | SI | Days off dialysis |
| Q19 | varchar |  |  | SI | Comments |
| Q20 | varchar |  |  | SI | APD modality |
| Q21 | numeric |  |  | SI | Fill volume (ml) |
| Q22 | numeric |  |  | SI | Comments |
| Q23 | numeric |  |  | SI | Number of cycles |
| Q24 | numeric |  |  | SI | Comments |
| Q25 | numeric |  |  | SI | Therapy time (hr) |
| Q26 | numeric |  |  | SI | Comments |
| Q27 | varchar |  |  | SI | Last fill |
| Q28 | varchar |  |  | SI | Last fill concentration |
| Q29 | numeric |  |  | SI | Last fill volume (ml) |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | numeric |  |  | SI | Last fill dwell time (hr) |
| Q32 | varchar |  |  | SI | Comments |
| Q33 | varchar |  |  | SI | Daytime cycle |
| Q34 | varchar |  |  | SI | Daytime cycle concentration |
| Q35 | numeric |  |  | SI | Daytime cycle volume (ml) |
| Q36 | varchar |  |  | SI | Comments |
| Q37 | numeric |  |  | SI | Daytime cycle dwell time (hr) |
| Q38 | varchar |  |  | SI | Comments |
| Q39 | varchar |  |  | SI | Additional details |
| Q40 | varchar |  |  | SI | Comments |
| Q41 | date |  |  | SI | Date |
| Q42 | time |  |  | SI | Time |
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