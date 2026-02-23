# SQLUser.PA_CodaExtractBuild

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXB_RowId | bigint | PK |  | NO | - |
| EXB_AccountPeriod_DR | bigint |  | FK | SI | Des Ref AccountPeriod |
| EXB_DateFrom | date |  |  | SI | Date From |
| EXB_DateRun | date |  |  | SI | DateRun |
| EXB_DateTo | date |  |  | SI | Date To |
| EXB_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| EXB_TimeRun | time |  |  | SI | TimeRun |
| EXB_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Facilty |
| Q02 | - |  |  | SI | Department |
| Q03 | - |  |  | SI | Admission diagnosis |
| Q04 | - |  |  | SI | Date admitted |
| Q05 | - |  |  | SI | Date readmitted |
| Q06 | - |  |  | SI | Date of discharge |
| Q07 | - |  |  | SI | Date of onset |
| Q08 | - |  |  | SI | Admitting physician |
| Q09 | - |  |  | SI | Infection detected on |
| Q10 | - |  |  | SI | Risk Factors |
| Q11 | - |  |  | SI | Urinary catheter status |
| Q12 | - |  |  | SI | Device insertion location |
| Q13 | - |  |  | SI | Reason device insertion |
| Q14 | - |  |  | SI | Date of device insertion |
| Q15 | - |  |  | SI | Date of device removal |
| Q16 | - |  |  | SI | Event details |
| Q17 | - |  |  | SI | Specific event |
| Q18 | - |  |  | SI | Signs & Symptoms (check all that apply) |
| Q19 | - |  |  | SI | Any patient |
| Q20 | - |  |  | SI | ≤ 1 year old |
| Q21 | - |  |  | SI | Laboratory |
| Q22 | - |  |  | SI | Clinical diagnosis |
| Q23 | - |  |  | SI | Pathogens identified |
| Q24 | - |  |  | SI | Died |
| Q25 | - |  |  | SI | Improved |
| Q26 | - |  |  | SI | Hospital Acquired Infection (HAI) confirmed by the... |
| Q27 | - |  |  | SI | Documented by the attending physician |
| Q28 | - |  |  | SI | Confirmed Hospital Acquired Infection (HAI) |
| Q29 | - |  |  | SI | Laboratory test (See lab chart) |
| Q30 | - |  |  | SI | Comments |
| Q31 | - |  |  | SI | Date |
| Q32 | - |  |  | SI | Time |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*