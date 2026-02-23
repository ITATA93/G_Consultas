# questionnaire.QTCUTIS

> Urinary Tract Infection (UTI) Surveillance

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Urinary Tract Infection (UTI) Surveillance

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Facilty |
| Q02 | varchar |  |  | SI | Department |
| Q03 | varchar |  |  | SI | Admission diagnosis |
| Q04 | varchar |  |  | SI | Date admitted |
| Q05 | date |  |  | SI | Date readmitted |
| Q06 | varchar |  |  | SI | Date of discharge |
| Q07 | date |  |  | SI | Date of onset |
| Q08 | varchar |  |  | SI | Admitting physician |
| Q09 | varchar |  |  | SI | Infection detected on |
| Q10 | varchar |  |  | SI | Risk Factors |
| Q11 | varchar |  |  | SI | Urinary catheter status |
| Q12 | varchar |  |  | SI | Device insertion location |
| Q13 | varchar |  |  | SI | Reason device insertion |
| Q14 | date |  |  | SI | Date of device insertion |
| Q15 | date |  |  | SI | Date of device removal |
| Q16 | varchar |  |  | SI | Event details |
| Q17 | varchar |  |  | SI | Specific event |
| Q18 | varchar |  |  | SI | Signs & Symptoms (check all that apply) |
| Q19 | varchar |  |  | SI | Any patient |
| Q20 | varchar |  |  | SI | ≤ 1 year old |
| Q21 | varchar |  |  | SI | Laboratory |
| Q22 | varchar |  |  | SI | Clinical diagnosis |
| Q23 | varchar |  |  | SI | Pathogens identified |
| Q24 | varchar |  |  | SI | Died |
| Q25 | varchar |  |  | SI | Improved |
| Q26 | varchar |  |  | SI | Hospital Acquired Infection (HAI) confirmed by the... |
| Q27 | varchar |  |  | SI | Documented by the attending physician |
| Q28 | varchar |  |  | SI | Confirmed Hospital Acquired Infection (HAI) |
| Q29 | varchar |  |  | SI | Laboratory test (See lab chart) |
| Q30 | varchar |  |  | SI | Comments |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
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