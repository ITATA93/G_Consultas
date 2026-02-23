# questionnaire.QTCEVG

> Extravasation Grading

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Extravasation Grading

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Grading Scale |
| Q02 | varchar |  |  | SI | Skin Colour |
| Q03 | varchar |  |  | SI | Skin Temperature |
| Q04 | varchar |  |  | SI | Skin Integrity |
| Q05 | varchar |  |  | SI | Absent |
| Q06 | varchar |  |  | SI | Normal |
| Q07 | varchar |  |  | SI | Normal |
| Q08 | varchar |  |  | SI | Unbroken |
| Q09 | varchar |  |  | SI | Oedema |
| Q10 | varchar |  |  | SI | Pink |
| Q11 | varchar |  |  | SI | Warm |
| Q12 | varchar |  |  | SI | Blistered |
| Q13 | varchar |  |  | SI | Non-pitting |
| Q14 | varchar |  |  | SI | Red |
| Q15 | varchar |  |  | SI | Hot |
| Q16 | varchar |  |  | SI | Superficial skin loss |
| Q17 | varchar |  |  | SI | Pitting |
| Q18 | varchar |  |  | SI | Blanched centre |
| Q19 | varchar |  |  | SI | Tissue loss exposing subcutaneous tissue |
| Q20 | varchar |  |  | SI | Blackened |
| Q21 | varchar |  |  | SI | Tissue loss muscle / bone / exposure, deep crater ... |
| Q22 | varchar |  |  | SI | Mobility |
| Q23 | varchar |  |  | SI | Pain |
| Q24 | varchar |  |  | SI | Fever |
| Q25 | varchar |  |  | SI | Grading Scale |
| Q26 | varchar |  |  | SI | 0 |
| Q27 | varchar |  |  | SI | 1 |
| Q28 | varchar |  |  | SI | 2 |
| Q29 | varchar |  |  | SI | 3 |
| Q30 | varchar |  |  | SI | 4 |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
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