# questionnaire.QTCDA

> Dental Assessment

**Schema:** questionnaire
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Dental Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | Extra Oral |
| Q04 | varchar |  |  | SI | Face |
| Q05 | varchar |  |  | SI | Symmetry/ Asymmetry |
| Q06 | varchar |  |  | SI | Profile |
| Q07 | varchar |  |  | SI | Intra Oral |
| Q08 | varchar |  |  | SI | Oral hygiene |
| Q09 | varchar |  |  | SI | Calculus |
| Q09a | varchar |  |  | SI | Calculus details |
| Q10 | varchar |  |  | SI | Stain |
| Q10a | varchar |  |  | SI | Stain Details |
| Q11 | varchar |  |  | SI | Oral mucosa |
| Q11a | varchar |  |  | SI | Abnormal oral mucosa |
| Q12 | varchar |  |  | SI | Tounge |
| Q13 | varchar |  |  | SI | Jaw relations |
| Q14 | varchar |  |  | SI | Others |
| Q15 | varchar |  |  | SI | Occlusion |
| Q16 | varchar |  |  | SI | Torus palatinus |
| Q17 | varchar |  |  | SI | Torus mandibularis |
| Q18 | varchar |  |  | SI | Palatum |
| Q19 | varchar |  |  | SI | Diastema |
| Q20 | varchar |  |  | SI | Diastema details |
| Q21 | varchar |  |  | SI | Dental anomalies |
| Q22 | varchar |  |  | SI | Anomalies details |
| Q23 | varchar |  |  | SI | Others details |
| Q24 | varchar |  |  | SI | Decay |
| Q25 | varchar |  |  | SI | Missing |
| Q26 | varchar |  |  | SI | Filling |
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