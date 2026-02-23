# questionnaire.QGXXXENDINT

> Endotracheal Intubation

**Schema:** questionnaire
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Endotracheal Intubation

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Indication |
| Q01N | varchar |  |  | SI | Note |
| Q03 | varchar |  |  | SI | Pre-oxygenation |
| Q03N | varchar |  |  | SI | Note |
| Q04 | varchar |  |  | SI | Rapid sequence technique |
| Q05 | varchar |  |  | SI | Pre-treatment |
| Q05N | varchar |  |  | SI | Note |
| Q06 | varchar |  |  | SI | Induction |
| Q06N | varchar |  |  | SI | Note |
| Q07 | varchar |  |  | SI | Paralytic agent |
| Q07N | varchar |  |  | SI | Note |
| Q11 | varchar |  |  | SI | Approach |
| Q11N | varchar |  |  | SI | Note |
| Q13 | varchar |  |  | SI | Visualisation / Guidance |
| Q13N | varchar |  |  | SI | Note |
| Q14 | numeric |  |  | SI | Number of attempts |
| Q15 | numeric |  |  | SI | Tube size |
| Q16 | varchar |  |  | SI | Successful |
| Q17 | varchar |  |  | SI | Placement confirmed by |
| Q17A | varchar |  |  | SI | Placement confirmed by |
| Q17N | varchar |  |  | SI | Note |
| Q18 | varchar |  |  | SI | Status |
| Q18N | varchar |  |  | SI | Note |
| Q19 | varchar |  |  | SI | Other procedure notes |
| Q24 | varchar |  |  | SI | Tube size |
| Q26 | date |  |  | SI | Date of insertion |
| Q27 | time |  |  | SI | Time of insertion |
| Q28 | date |  |  | SI | Date of removal |
| Q29 | time |  |  | SI | Time of removal |
| Q30 | varchar |  |  | SI | Type of removal |
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