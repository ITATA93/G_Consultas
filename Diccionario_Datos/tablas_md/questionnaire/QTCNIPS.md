# questionnaire.QTCNIPS

> Neonatal Infant Pain Scale (NIPS)

**Schema:** questionnaire
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Neonatal Infant Pain Scale (NIPS)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Recommended for children less than 1 year old |
| Q02 | varchar |  |  | SI | Facial Expression |
| Q03 | varchar |  |  | SI | Cry |
| Q04 | varchar |  |  | SI | Breathing Pattern |
| Q05 | varchar |  |  | SI | Arms |
| Q06 | varchar |  |  | SI | Legs |
| Q07 | varchar |  |  | SI | State of Arousal |
| Q08 | varchar |  |  | SI | 0-2 = mild to no pain |
| Q09 | varchar |  |  | SI | 3-4 = mild to moderate pain |
| Q10 | varchar |  |  | SI | >4 = severe pain |
| Q11 | varchar |  |  | SI | Intervention |
| Q12 | varchar |  |  | SI | None |
| Q13 | varchar |  |  | SI | Non-pharmacological intervention with a reassessme... |
| Q14 | varchar |  |  | SI | Non-pharmacological intervention and possibly a ph... |
| Q15 | varchar |  |  | SI | Total pain scores range from 0-7. The suggested in... |
| Q16 | varchar |  |  | SI | and agitation, however, the non-pharmacological in... |
| Q17 | varchar |  |  | SI | (i.e. changing the wet diaper, feeding the infant,... |
| Q18 | varchar |  |  | SI | 0-2 = mild to no pain |
| Q19 | varchar |  |  | SI | 3-4 = mild to moderate pain |
| Q20 | varchar |  |  | SI | >4 = severe pain |
| Q21 | date |  |  | SI | Date |
| Q22 | time |  |  | SI | Time |
| Q23 | varchar |  |  | SI | Type of assessment |
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