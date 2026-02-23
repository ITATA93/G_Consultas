# questionnaire.QTCCSSST

> Supportive Care Screening Tool - Cancer Services

**Schema:** questionnaire
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Supportive Care Screening Tool - Cancer Services

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | If zero is no distress and 10 is extreme distress,... |
| Q02 | varchar |  |  | SI | 	Please indicate below, if any of the following ha... |
| Q03 | varchar |  |  | SI | Practical problems |
| Q04 | varchar |  |  | SI | Family problems |
| Q05 | varchar |  |  | SI | Emotional problems |
| Q06 | varchar |  |  | SI | Spiritual or religious concerns |
| Q07 | varchar |  |  | SI | Physical problems |
| Q08 | varchar |  |  | SI | Comments |
| Q09 | longvarbinary |  |  | SI | Patient / family member signature |
| Q09UDt | date |  |  | SI | Patient / family member signature Last Updated Dat... |
| Q09UTm | time |  |  | SI | Patient / family member signature Last Updated Tim... |
| Q10 | varchar |  |  | SI | Screening point |
| Q11 | varchar |  |  | SI | Are referrals recommended? |
| Q12 | varchar |  |  | SI | Dietetics  |
| Q13 | varchar |  |  | SI | Occupational therapy |
| Q14 | varchar |  |  | SI | Palliative care |
| Q15 | varchar |  |  | SI | Pastoral care |
| Q16 | varchar |  |  | SI | Physiotherapy |
| Q17 | varchar |  |  | SI | Psychology / psychiatry |
| Q18 | varchar |  |  | SI | Social work |
| Q19 | varchar |  |  | SI | Specialist work |
| Q20 | varchar |  |  | SI | Speech therapy |
| Q21 | varchar |  |  | SI | Reason |
| Q22 | varchar |  |  | SI | Reason |
| Q23 | varchar |  |  | SI | Reason |
| Q24 | varchar |  |  | SI | Reason |
| Q25 | varchar |  |  | SI | Reason |
| Q26 | varchar |  |  | SI | Reason |
| Q27 | varchar |  |  | SI | Reason |
| Q28 | varchar |  |  | SI | Reason |
| Q29 | varchar |  |  | SI | Reason |
| Q30 | varchar |  |  | SI | Other services |
| Q31 | varchar |  |  | SI | Patient agreed to above referral(s) being made? |
| Q32 | varchar |  |  | SI | Treating doctor aware of referral(s) being made? |
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