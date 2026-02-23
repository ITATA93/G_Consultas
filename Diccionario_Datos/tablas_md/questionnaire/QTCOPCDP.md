# questionnaire.QTCOPCDP

> Care During Procedure - Outpatient

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Care During Procedure - Outpatient

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | varchar |  |  | SI | Skin preparation |
| Q10 | varchar |  |  | SI | Body Map |
| Q11 | varchar |  |  | SI | Swab, needle and instrument count |
| Q12 | varchar |  |  | SI | Pre op count consultant / scrub practitioner |
| Q13 | varchar |  |  | SI | Pre op count circulating practitioner |
| Q14 | varchar |  |  | SI | Final count consultant / scrub practitioner |
| Q15 | varchar |  |  | SI | Final count circulating practitioner |
| Q16 | varchar |  |  | SI | Swabs, needles and instruments correct |
| Q17 | varchar |  |  | SI | If No, please indicate count discrepancy and actio... |
| Q18 | varchar |  |  | SI | Packs remaining in situ |
| Q19 | numeric |  |  | SI | Number |
| Q2 | varchar |  |  | SI | Irrigation fluid used |
| Q20 | varchar |  |  | SI | Type |
| Q21 | varchar |  |  | SI | Position |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
| Q24 | varchar |  |  | SI | Body map |
| Q3 | varchar |  |  | SI | Infiltration / anaesthetic type (specify) |
| Q4 | varchar |  |  | SI | Type and number of specimens (specify) |
| Q5 | varchar |  |  | SI | Diathermy plate/pad removed and site shows no adve... |
| Q6 | varchar |  |  | SI | Skin closure if applicable |
| Q7 | varchar |  |  | SI | If Other, please detail |
| Q8 | varchar |  |  | SI | Procedure performed |
| Q9 | varchar |  |  | SI | See operation note for any post procedural instruc... |
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