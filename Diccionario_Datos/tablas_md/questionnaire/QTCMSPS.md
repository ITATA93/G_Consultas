# questionnaire.QTCMSPS

> The Modified SAD PERSONS

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Modified SAD PERSONS

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Organized or serious attempt (well thought-out pla... |
| Q11 | varchar |  |  | SI | No social supports (no close family, friends, job,... |
| Q12 | varchar |  |  | SI | Stated future intent (determined to repeat attempt... |
| Q13 | varchar |  |  | SI | Score |
| Q14 | varchar |  |  | SI | Classification |
| Q15 | varchar |  |  | SI | ≥6 |
| Q16 | varchar |  |  | SI | High suicide risk, need psychiatry directed hospit... |
| Q17 | varchar |  |  | SI | &lt;6 |
| Q18 | varchar |  |  | SI | May be safe to discharge, depending on circumstanc... |
| Q19 | varchar |  |  | SI | Provenance details |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | The modified SAD PERSONS score is a modification b... |
| Q21 | varchar |  |  | SI | 1. Hockberger RS, Rothstein RJ. Assessment of suic... |
| Q22 | varchar |  |  | SI | 2. Patterson WM, Dohn HH, Bird J, Patterson GA. Ev... |
| Q23 | varchar |  |  | SI | The modified SAD PERSONS score is a modification b... |
| Q3 | varchar |  |  | SI | Sex |
| Q4 | varchar |  |  | SI | Age |
| Q5 | varchar |  |  | SI | Depression or hopelessness (admits to depression o... |
| Q6 | varchar |  |  | SI | Previous attempts or psychiatric care (previous in... |
| Q7 | varchar |  |  | SI | Excessive alcohol or drug use (stigmata of chronic... |
| Q8 | varchar |  |  | SI | Rational thinking loss (organic brain syndrome or&... |
| Q9 | varchar |  |  | SI | Separated, divorced or widowed |
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