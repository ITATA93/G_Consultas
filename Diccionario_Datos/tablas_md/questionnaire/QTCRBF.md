# questionnaire.QTCRBF

> Radiotherapy Booking Form

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Radiotherapy Booking Form

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Language |
| Q04 | varchar |  |  | SI | Please specify language |
| Q05 | varchar |  |  | SI | Mobility status |
| Q06 | varchar |  |  | SI | Has the patient consented for radiotherapy treatme... |
| Q07 | varchar |  |  | SI | Has the patient had previous radiotherapy treatmen... |
| Q08 | varchar |  |  | SI | Give details |
| Q09 | varchar |  |  | SI | Is the patient having concurrent chemotherapy? |
| Q10 | varchar |  |  | SI | Comments |
| Q11 | varchar |  |  | SI | Does the patient have a pacemaker? |
| Q12 | varchar |  |  | SI | Pacemakers details |
| Q13 | varchar |  |  | SI | Is dental clearance needed? |
| Q14 | varchar |  |  | SI | Details of dental clearance |
| Q15 | varchar |  |  | SI | Site of treatment |
| Q16 | varchar |  |  | SI | Treatment intent |
| Q17 | varchar |  |  | SI | Is contrast required? |
| Q18 | varchar |  |  | SI | Comments |
| Q19 | varchar |  |  | SI | Four-dimensional computed tomography scan required... |
| Q20 | varchar |  |  | SI | Scanning levels |
| Q21 | varchar |  |  | SI | Other |
| Q22 | varchar |  |  | SI | Positioning |
| Q23 | varchar |  |  | SI | Phase1 |
| Q24 | varchar |  |  | SI | Gray (Gy) |
| Q25 | varchar |  |  | SI | Number |
| Q26 | varchar |  |  | SI | Bolus |
| Q27 | varchar |  |  | SI | Phase 2 |
| Q28 | varchar |  |  | SI | Phase 3 / Boost |
| Q29 | varchar |  |  | SI | Gray (Gy) |
| Q30 | varchar |  |  | SI | Number |
| Q31 | varchar |  |  | SI | Bolus |
| Q32 | varchar |  |  | SI | Gray (Gy) |
| Q33 | varchar |  |  | SI | Number |
| Q34 | varchar |  |  | SI | Bolus |
| Q35 | varchar |  |  | SI | Remarks / Comments |
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