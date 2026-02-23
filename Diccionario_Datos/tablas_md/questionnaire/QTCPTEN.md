# questionnaire.QTCPTEN

> Physical Therapy: Examination (Neurology)

**Schema:** questionnaire
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Physical Therapy: Examination (Neurology)

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
| Q06 | varchar |  |  | SI | Muscle length examination |
| Q07 | varchar |  |  | SI | Muscle length summary |
| Q08 | varchar |  |  | SI | Muscle tone examination |
| Q09 | varchar |  |  | SI | Muscle tone summary |
| Q10 | varchar |  |  | SI | Muscle strength examination |
| Q11 | varchar |  |  | SI | Muscle strength summary |
| Q12 | varchar |  |  | SI | Limb muscle strength |
| Q13 | varchar |  |  | SI | Left upper extremities |
| Q13ObsDR | varchar |  | FK | SI | Left upper extremities DR |
| Q14 | varchar |  |  | SI | Right upper extremities |
| Q14ObsDR | varchar |  | FK | SI | Right upper extremities DR |
| Q15 | varchar |  |  | SI | Left lower extremities |
| Q15ObsDR | varchar |  | FK | SI | Left lower extremities DR |
| Q16 | varchar |  |  | SI | Right lower extremities |
| Q16ObsDR | varchar |  | FK | SI | Right lower extremities DR |
| Q17 | varchar |  |  | SI | Static sitting balance |
| Q17ObsDR | varchar |  | FK | SI | Static sitting balance DR |
| Q18 | varchar |  |  | SI | Dynamic sitting balance |
| Q18ObsDR | varchar |  | FK | SI | Dynamic sitting balance DR |
| Q19 | varchar |  |  | SI | Static standing balance |
| Q19ObsDR | varchar |  | FK | SI | Static standing balance DR |
| Q20 | varchar |  |  | SI | Dynamic standing balance |
| Q20ObsDR | varchar |  | FK | SI | Dynamic standing balance DR |
| Q21 | varchar |  |  | SI | Sensation examination |
| Q22 | varchar |  |  | SI | Sensation summary |
| Q23 | varchar |  |  | SI | Rolling |
| Q23ObsDR | varchar |  | FK | SI | Rolling DR |
| Q24 | varchar |  |  | SI | Come to sit |
| Q24ObsDR | varchar |  | FK | SI | Come to sit DR |
| Q25 | varchar |  |  | SI | Ambulatory status |
| Q25ObsDR | varchar |  | FK | SI | Ambulatory status DR |
| Q26 | varchar |  |  | SI | Transferring |
| Q26ObsDR | varchar |  | FK | SI | Transferring DR |
| Q27 | varchar |  |  | SI | Gait pattern |
| Q27ObsDR | varchar |  | FK | SI | Gait pattern DR |
| Q28 | varchar |  |  | SI | Gait aid |
| Q28ObsDR | varchar |  | FK | SI | Gait aid DR |
| Q29 | varchar |  |  | SI | Level of assistance |
| Q29ObsDR | varchar |  | FK | SI | Level of assistance DR |
| Q30 | varchar |  |  | SI | Gait analysis summary |
| Q31 | varchar |  |  | SI | Other examination |
| Q32 | varchar |  |  | SI | To document specific examinations, please complete... |
| Q33 | varchar |  |  | SI | Examples: |
| Q34 | varchar |  |  | SI | Range of Motion |
| Q35 | varchar |  |  | SI | Manual Muscle Testing |
| Q36 | varchar |  |  | SI | Modified Tardieu Scale |
| Q37 | varchar |  |  | SI | Modified Ashworth Scale |
| Q38 | varchar |  |  | SI | Come to stand |
| Q38ObsDR | varchar |  | FK | SI | Come to stand DR |
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