# questionnaire.QTCEDIN6

> Modified EDIN Scale

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Modified EDIN Scale

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Postmenstrual age |
| Q04 | varchar |  |  | SI | Facial activity |
| Q05 | varchar |  |  | SI | Body movements |
| Q06 | varchar |  |  | SI | Quality of sleep |
| Q07 | varchar |  |  | SI | Quality of contact with  nurses	 |
| Q08 | varchar |  |  | SI | Consolability |
| Q09 | varchar |  |  | SI | Score |
| Q10 | varchar |  |  | SI | Classification |
| Q11 | varchar |  |  | SI | 0 - 6 |
| Q12 | varchar |  |  | SI | No pain |
| Q13 | varchar |  |  | SI | 6 - 8 |
| Q14 | varchar |  |  | SI | Presence of pain; consider intervention |
| Q15 | varchar |  |  | SI | 8 - 17 |
| Q16 | varchar |  |  | SI | Moderate to severe pain |
| Q17 | varchar |  |  | SI | EDIN (Échelle Douleur Inconfort Nouveau-Né, neonat... |
| Q18 | varchar |  |  | SI | This is a sightly modified version of the scale, i... |
| Q19 | varchar |  |  | SI | The modified EDIN scale has postmenstrual age (PMA... |
| Q20 | varchar |  |  | SI | 0 - 6: No pain |
| Q21 | varchar |  |  | SI | 6 - 8: Presence of pain; consider intervention |
| Q22 | varchar |  |  | SI | 8 - 17: Moderate to severe pain |
| Q23 | varchar |  |  | SI | The EDIN6 score is the sum total of each question ... |
| Q24 | varchar |  |  | SI | Score interpretation: score range is 0-17. Scores ... |
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