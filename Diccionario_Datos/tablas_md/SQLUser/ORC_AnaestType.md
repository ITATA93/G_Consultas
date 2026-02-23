# SQLUser.ORC_AnaestType

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ANTYPE_RowId | bigint | PK |  | NO | - |
| ANTYPE_Code | varchar |  |  | NO | Code |
| ANTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ANTYPE_CreatedDate | date |  |  | SI | Created Date |
| ANTYPE_CreatedTime | time |  |  | SI | Created Time |
| ANTYPE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ANTYPE_DateFrom | date |  |  | SI | Date From |
| ANTYPE_DateTo | date |  |  | SI | Date To |
| ANTYPE_Desc | varchar |  |  | NO | Description |
| ANTYPE_Owner | varchar |  |  | SI | Owner |
| ANTYPE_UpdatedDate | date |  |  | SI | Updated Date |
| ANTYPE_UpdatedTime | time |  |  | SI | Updated Time |
| ANTYPE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Assistive device and/or bracing used |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Seconds to ambulate the measured portion of the wa... |
| Q04 | - |  |  | SI | Self-selected velocity: Trial 1 (seconds) |
| Q05 | - |  |  | SI | Self-selected velocity: Trial 2 (seconds) |
| Q06 | - |  |  | SI | Self-selected velocity: Trial 3 (seconds) |
| Q07 | - |  |  | SI | Self-selected velocity: Average time (seconds) |
| Q08 | - |  |  | SI | Fast velocity: Trial 1 (seconds) |
| Q09 | - |  |  | SI | Fast velocity: Trial 2 (seconds) |
| Q10 | - |  |  | SI | Fast velocity: Trial 3 (seconds) |
| Q11 | - |  |  | SI | Fast velocity: Average time (seconds) |
| Q11A | - |  |  | SI | Fast velocity: Average time (seconds) |
| Q12 | - |  |  | SI | Actual velocity: Divide length by the average seco... |
| Q12A | - |  |  | SI | Average fast-velocity (meters / second) |
| Q13 | - |  |  | SI | Average self-selected velocity (meters / second) |
| Q13A | - |  |  | SI | Average self-selected velocity (meters / second) |
| Q14 | - |  |  | SI | Average fast-velocity (meters / second) |
| Q15 | - |  |  | SI | Timed 10-Meter Walk Test |
| Q16 | - |  |  | SI | General Information |
| Q17 | - |  |  | SI | • Individual walks without assistance for the defi... |
| Q18 | - |  |  | SI | ◦ Start timing when the toes of the leading foot c... |
| Q19 | - |  |  | SI | ◦ Stop timing when the toes of the leading foot cr... |
| Q20 | - |  |  | SI | ◦ Assistive devices can be used but should be kept... |
| Q21 | - |  |  | SI | ◦ If physical assistance is required to walk, this... |
| Q22 | - |  |  | SI | • Can be performed at preferred walking speed or f... |
| Q23 | - |  |  | SI | ◦ Documentation should include the speed tested (p... |
| Q24 | - |  |  | SI | • Collect three trials and calculate the average o... |
| Q25 | - |  |  | SI | Set-up (derived from the reference articles) |
| Q26 | - |  |  | SI | • Measure and mark the walkway total length |
| Q27 | - |  |  | SI | • Add a mark at the point where the measured secti... |
| Q28 | - |  |  | SI | • Add a mark at the point where the measured secti... |
| Q29 | - |  |  | SI | Patient Instructions (derived from the reference a... |
| Q32 | - |  |  | SI | Marking measure |
| Q33 | - |  |  | SI | Diagram of Walkway: |
| Q34 | - |  |  | SI | • Normal comfortable speed: “I will say ready, set... |
| Q35 | - |  |  | SI | • Maximum speed trials: “I will say ready, set, go... |
| Q36 | - |  |  | SI | Walkway length |
| Q37 | - |  |  | SI | Enter 9999 for any trials patient was unable to co... |
| Q38 | - |  |  | SI | Time |
| Q39 | - |  |  | SI | Enter 9999 for any trials patient was unable to co... |
| Q7A | - |  |  | SI | Self-selected velocity: Average time (seconds) |
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