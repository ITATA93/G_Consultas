# questionnaire.QTCAHPT10MW

> Timed 10-Meter Walk Test

**Schema:** questionnaire
**Columnas:** 82
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Timed 10-Meter Walk Test

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Assistive device and/or bracing used |
| Q02 | date |  |  | SI | Date |
| Q03 | varchar |  |  | SI | Seconds to ambulate the measured portion of the wa... |
| Q04 | numeric |  |  | SI | Self-selected velocity: Trial 1 (seconds) |
| Q05 | numeric |  |  | SI | Self-selected velocity: Trial 2 (seconds) |
| Q06 | numeric |  |  | SI | Self-selected velocity: Trial 3 (seconds) |
| Q07 | varchar |  |  | SI | Self-selected velocity: Average time (seconds) |
| Q08 | numeric |  |  | SI | Fast velocity: Trial 1 (seconds) |
| Q09 | numeric |  |  | SI | Fast velocity: Trial 2 (seconds) |
| Q10 | numeric |  |  | SI | Fast velocity: Trial 3 (seconds) |
| Q11 | varchar |  |  | SI | Fast velocity: Average time (seconds) |
| Q11A | varchar |  |  | SI | Fast velocity: Average time (seconds) |
| Q12 | varchar |  |  | SI | Actual velocity: Divide length by the average seco... |
| Q12A | varchar |  |  | SI | Average fast-velocity (meters / second) |
| Q13 | varchar |  |  | SI | Average self-selected velocity (meters / second) |
| Q13A | varchar |  |  | SI | Average self-selected velocity (meters / second) |
| Q14 | varchar |  |  | SI | Average fast-velocity (meters / second) |
| Q15 | varchar |  |  | SI | Timed 10-Meter Walk Test |
| Q16 | varchar |  |  | SI | General Information |
| Q17 | varchar |  |  | SI | • Individual walks without assistance for the defi... |
| Q18 | varchar |  |  | SI | ◦ Start timing when the toes of the leading foot c... |
| Q19 | varchar |  |  | SI | ◦ Stop timing when the toes of the leading foot cr... |
| Q20 | varchar |  |  | SI | ◦ Assistive devices can be used but should be kept... |
| Q21 | varchar |  |  | SI | ◦ If physical assistance is required to walk, this... |
| Q22 | varchar |  |  | SI | • Can be performed at preferred walking speed or f... |
| Q23 | varchar |  |  | SI | ◦ Documentation should include the speed tested (p... |
| Q24 | varchar |  |  | SI | • Collect three trials and calculate the average o... |
| Q25 | varchar |  |  | SI | Set-up (derived from the reference articles) |
| Q26 | varchar |  |  | SI | • Measure and mark the walkway total length |
| Q27 | varchar |  |  | SI | • Add a mark at the point where the measured secti... |
| Q28 | varchar |  |  | SI | • Add a mark at the point where the measured secti... |
| Q29 | varchar |  |  | SI | Patient Instructions (derived from the reference a... |
| Q32 | varchar |  |  | SI | Marking measure |
| Q33 | varchar |  |  | SI | Diagram of Walkway: |
| Q34 | varchar |  |  | SI | • Normal comfortable speed: “I will say ready, set... |
| Q35 | varchar |  |  | SI | • Maximum speed trials: “I will say ready, set, go... |
| Q36 | varchar |  |  | SI | Walkway length |
| Q37 | varchar |  |  | SI | Enter 9999 for any trials patient was unable to co... |
| Q38 | time |  |  | SI | Time |
| Q39 | varchar |  |  | SI | Enter 9999 for any trials patient was unable to co... |
| Q7A | varchar |  |  | SI | Self-selected velocity: Average time (seconds) |
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