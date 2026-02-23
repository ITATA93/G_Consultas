# questionnaire.QTCPTEO

> Physical Therapy: Examination (Orthopaedic)

**Schema:** questionnaire
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physical Therapy: Examination (Orthopaedic)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | I have reviewed updated physician's order and rela... |
| Q04 | varchar |  |  | SI | General appearance |
| Q05 | varchar |  |  | SI | Level of consciousness |
| Q05ObsDR | varchar |  | FK | SI | Level of consciousness DR |
| Q06 | varchar |  |  | SI | Range of motion examination |
| Q07 | varchar |  |  | SI | Range of motion summary |
| Q08 | varchar |  |  | SI | Accessory movement examination |
| Q09 | varchar |  |  | SI | Accessory movement summary |
| Q10 | varchar |  |  | SI | Palpation examination |
| Q11 | varchar |  |  | SI | Palpation summary |
| Q12 | varchar |  |  | SI | Muscle strength examination |
| Q13 | varchar |  |  | SI | Muscle strength summary |
| Q14 | varchar |  |  | SI | Rolling |
| Q14ObsDR | varchar |  | FK | SI | Rolling DR |
| Q15 | varchar |  |  | SI | Come to sit  |
| Q15ObsDR | varchar |  | FK | SI | Come to sit  DR |
| Q16 | varchar |  |  | SI | Come to stand  |
| Q16ObsDR | varchar |  | FK | SI | Come to stand  DR |
| Q17 | varchar |  |  | SI | Ambulatory status |
| Q17ObsDR | varchar |  | FK | SI | Ambulatory status DR |
| Q18 | varchar |  |  | SI | Transferring |
| Q18ObsDR | varchar |  | FK | SI | Transferring DR |
| Q19 | varchar |  |  | SI | Sensation examination |
| Q20 | varchar |  |  | SI | Sensation summary |
| Q21 | varchar |  |  | SI | Other examination summary |
| Q22 | varchar |  |  | SI | To document specific examinations, please complete... |
| Q23 | varchar |  |  | SI | Examples: |
| Q24 | varchar |  |  | SI | Range of Motion |
| Q25 | varchar |  |  | SI | Manual Muscle Testing |
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