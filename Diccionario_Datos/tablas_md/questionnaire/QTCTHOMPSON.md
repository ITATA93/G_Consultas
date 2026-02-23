# questionnaire.QTCTHOMPSON

> Thompson Score

**Schema:** questionnaire
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Thompson Score

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Tone |
| Q02 | varchar |  |  | SI | Level of consciousness |
| Q03 | varchar |  |  | SI | Fits (Clinically apparent seizures) |
| Q04 | varchar |  |  | SI | Posture |
| Q05 | varchar |  |  | SI | Moro Reflex |
| Q06 | varchar |  |  | SI | Grasp Reflex |
| Q07 | varchar |  |  | SI | Suck Reflex |
| Q08 | varchar |  |  | SI | Respiratory Pattern |
| Q09 | varchar |  |  | SI | Fontanelle Tension |
| Q10 | varchar |  |  | SI | Score |
| Q11 | varchar |  |  | SI | Classification |
| Q12 | varchar |  |  | SI | 0 - 10 |
| Q13 | varchar |  |  | SI | Mild |
| Q14 | varchar |  |  | SI | 11 - 14 |
| Q15 | varchar |  |  | SI | Moderate |
| Q16 | varchar |  |  | SI | 15 - 22 |
| Q17 | varchar |  |  | SI | Severe |
| Q18 | varchar |  |  | SI | 0 - 10: Mild |
| Q19 | varchar |  |  | SI | 11 - 14: Moderate |
| Q20 | varchar |  |  | SI | 15 - 22: Severe |
| Q21 | varchar |  |  | SI | The Thompson encephalopathy score is a clinical sc... |
| Q22 | date |  |  | SI | Date |
| Q23 | time |  |  | SI | Time |
| Q24 | varchar |  |  | SI | Thompson C, Puterman A, Linley L, Hann F, Elst C, ... |
| Q25 | varchar |  |  | SI | The Thompson encephalopathy score is a clinical sc... |
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