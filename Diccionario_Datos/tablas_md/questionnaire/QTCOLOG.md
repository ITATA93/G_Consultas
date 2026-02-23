# questionnaire.QTCOLOG

> The Orientation Log (O-Log)

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* The Orientation Log (O-Log)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Clock time |
| Q11 | varchar |  |  | SI | Etiology / Event |
| Q12 | varchar |  |  | SI | Pathology deficits |
| Q13 | varchar |  |  | SI | Provenance details |
| Q14 | varchar |  |  | SI | Jackson WT, Novack TA, Dowler RN. Effective serial... |
| Q15 | varchar |  |  | SI | Guidelines |
| Q16 | varchar |  |  | SI | Incorrect responses should be followed by cuing at... |
| Q17 | varchar |  |  | SI | In the place domain, hospital in any context is su... |
| Q18 | varchar |  |  | SI | In the domain of time, month, date, year, and day ... |
| Q19 | varchar |  |  | SI | However, clock time can be correct to within 30 mi... |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Patients are allowed to look at a clock without pe... |
| Q21 | varchar |  |  | SI | For situation, the patient must be oriented to bot... |
| Q22 | varchar |  |  | SI | And pathology / deficits (e.g., what kind of injur... |
| Q23 | varchar |  |  | SI | Situational responses must demonstrate awareness o... |
| Q24 | varchar |  |  | SI | Add scores down each column and plot total. |
| Q25 | varchar |  |  | SI | The Orientation Log (O-Log) is designed to be a qu... |
| Q3 | varchar |  |  | SI | City |
| Q4 | varchar |  |  | SI | Kind of place |
| Q5 | varchar |  |  | SI | Name of hospital |
| Q6 | varchar |  |  | SI | Month |
| Q7 | varchar |  |  | SI | Date |
| Q8 | varchar |  |  | SI | Year |
| Q9 | varchar |  |  | SI | Day of week |
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