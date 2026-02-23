# questionnaire.QTCCAN

> Congenital Anomaly Notification

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Congenital Anomaly Notification

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Congenital anomaly |
| Q04 | varchar |  |  | SI | Diagnosed |
| Q05 | varchar |  |  | SI | Pregnancy gestation |
| Q06 | varchar |  |  | SI | weeks |
| Q07 | varchar |  |  | SI | days |
| Q08 | numeric |  |  | SI | Pregnancy gestation (weeks) |
| Q09 | numeric |  |  | SI | Pregnancy gestation (days) |
| Q10 | varchar |  |  | SI | Infant age |
| Q11 | varchar |  |  | SI | weeks |
| Q12 | varchar |  |  | SI | months |
| Q13 | numeric |  |  | SI | Infant age (weeks) |
| Q14 | numeric |  |  | SI | Infant age (months) |
| Q15 | varchar |  |  | SI | Fetal genetic testing |
| Q16 | varchar |  |  | SI | Other fetal genetic testing |
| Q17 | varchar |  |  | SI | Antenatal imaging |
| Q18 | varchar |  |  | SI | Other antenatal imaging |
| Q19 | varchar |  |  | SI | Fetal / Neonatal imaging |
| Q20 | varchar |  |  | SI | Other fetal / neonatal imaging |
| Q21 | varchar |  |  | SI | Fetal / Neonatal testing |
| Q22 | varchar |  |  | SI | Other fetal / neonatal testing |
| Q23 | varchar |  |  | SI | Notes |
| Q25 | varchar |  |  | SI | Notes |
| Q26 | varchar |  |  | SI | Relevant maternal / paternal history |
| Q27 | varchar |  |  | SI | Maternal environmental exposures (i.e. alcohol, dr... |
| Q28 | varchar |  |  | SI | Perinatal infection |
| Q29 | varchar |  |  | SI | Pregnancy outcome |
| Q30 | date |  |  | SI | Deceased date, if applicable |
| Q31 | varchar |  |  | SI | Transferred for care |
| Q32 | varchar |  |  | SI | Dummy1 |
| Q33 | varchar |  |  | SI | Notes |
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