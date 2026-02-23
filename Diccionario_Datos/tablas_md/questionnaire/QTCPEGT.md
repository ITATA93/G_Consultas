# questionnaire.QTCPEGT

> Percutaneous Endoscopic Gastrostomy Tube (PEG)

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Percutaneous Endoscopic Gastrostomy Tube (PEG)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Insertion Record |
| Q04 | date |  |  | SI | Date of insertion |
| Q05 | time |  |  | SI | Time of insertion |
| Q06 | varchar |  |  | SI | Insertion reason |
| Q07 | varchar |  |  | SI | Other indication reason |
| Q08 | varchar |  |  | SI | Procedure method |
| Q09 | varchar |  |  | SI | Radiological insertion method |
| Q10 | varchar |  |  | SI | Insertion site |
| Q11 | varchar |  |  | SI | Type |
| Q12 | varchar |  |  | SI | Brand / Size |
| Q13 | numeric |  |  | SI | Flange to skin (cm) |
| Q14 | numeric |  |  | SI | Balloon volume (mls) |
| Q15 | varchar |  |  | SI | Aseptic technique used with appropriate skin prepa... |
| Q16 | varchar |  |  | SI | External fixation plate placed and secure |
| Q17 | varchar |  |  | SI | Dressing applied and secure |
| Q18 | varchar |  |  | SI | Position confirmed |
| Q19 | varchar |  |  | SI | Other position confirmation notes |
| Q20 | varchar |  |  | SI | Inserted by |
| Q21 | varchar |  |  | SI | PEG Assessment |
| Q23 | varchar |  |  | SI | Removal Record |
| Q24 | date |  |  | SI | Date |
| Q25 | time |  |  | SI | Time |
| Q26 | varchar |  |  | SI | Removal reason |
| Q27 | varchar |  |  | SI | Other removal reason |
| Q28 | varchar |  |  | SI | Removed by |
| Q29 | varchar |  |  | SI | Complications |
| Q30 | varchar |  |  | SI | Complications |
| Q31 | varchar |  |  | SI | Other complications notes |
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