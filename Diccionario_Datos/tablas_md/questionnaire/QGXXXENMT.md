# questionnaire.QGXXXENMT

> Head and Neck Examination

**Schema:** questionnaire
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Head and Neck Examination

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Stomatitis |
| Q01N | bigint |  |  | SI | Note |
| Q01NTxtOnly | bigint |  |  | SI | Note Plain Text Only |
| Q01ObsDR | varchar |  | FK | SI | Stomatitis DR |
| Q03 | varchar |  |  | SI | Face |
| Q03N | varchar |  |  | SI | Note |
| Q03ObsDR | varchar |  | FK | SI | Face DR |
| Q05 | varchar |  |  | SI | Neck |
| Q05N | varchar |  |  | SI | Note |
| Q05ObsDR | varchar |  | FK | SI | Neck DR |
| Q07 | varchar |  |  | SI | Nose |
| Q07N | varchar |  |  | SI | Note |
| Q07ObsDR | varchar |  | FK | SI | Nose DR |
| Q09 | varchar |  |  | SI | Oral Cavity |
| Q09N | varchar |  |  | SI | Note |
| Q09ObsDR | varchar |  | FK | SI | Oral Cavity DR |
| Q11 | varchar |  |  | SI | Lips |
| Q11N | varchar |  |  | SI | Note |
| Q11ObsDR | varchar |  | FK | SI | Lips DR |
| Q13 | varchar |  |  | SI | Larynx |
| Q13N | varchar |  |  | SI | Note |
| Q13ObsDR | varchar |  | FK | SI | Larynx DR |
| Q15 | varchar |  |  | SI | Right ear |
| Q15N | varchar |  |  | SI | Note |
| Q15ObsDR | varchar |  | FK | SI | Right ear DR |
| Q17 | varchar |  |  | SI | Left ear |
| Q17N | varchar |  |  | SI | Note |
| Q17ObsDR | varchar |  | FK | SI | Left ear DR |
| Q18 | varchar |  |  | SI | Other |
| Q20 | bigint |  |  | SI | View |
| Q20TxtOnly | bigint |  |  | SI | View Plain Text Only |
| Q21 | varchar |  |  | SI | Head and face anterior |
| Q22 | varchar |  |  | SI | Eyes |
| Q22N | varchar |  |  | SI | Note |
| Q22ObsDR | varchar |  | FK | SI | Eyes DR |
| Q23 | varchar |  |  | SI | Pupil difference |
| Q23N | varchar |  |  | SI | Note |
| Q23ObsDR | varchar |  | FK | SI | Pupil difference DR |
| Q26 | varchar |  |  | SI | Neck range of motion |
| Q26N | varchar |  |  | SI | Note |
| Q26ObsDR | varchar |  | FK | SI | Neck range of motion DR |
| Q28 | varchar |  |  | SI | Thyroid Exam |
| Q28N | varchar |  |  | SI | Note |
| Q28ObsDR | varchar |  | FK | SI | Thyroid Exam DR |
| Q30 | varchar |  |  | SI | Lymph nodes |
| Q30N | varchar |  |  | SI | Note |
| Q30ObsDR | varchar |  | FK | SI | Lymph nodes DR |
| Q32 | varchar |  |  | SI | Jugular venous distention |
| Q32N | varchar |  |  | SI | Note |
| Q32ObsDR | varchar |  | FK | SI | Jugular venous distention DR |
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