# questionnaire.QTCEA

> Emergency Assessment

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Emergency Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Brought in by |
| Q02 | varchar |  |  | SI | From |
| Q03 | varchar |  |  | SI | From (other) |
| Q04 | bit |  |  | SI | Accompanied by family |
| Q05 | varchar |  |  | SI | Initial Assessment |
| Q06 | varchar |  |  | SI | Mental status |
| Q06ObsDR | varchar |  | FK | SI | Mental status DR |
| Q07 | varchar |  |  | SI | Behaviour |
| Q07ObsDR | varchar |  | FK | SI | Behaviour DR |
| Q08 | varchar |  |  | SI | Skin |
| Q08ObsDR | varchar |  | FK | SI | Skin DR |
| Q09 | varchar |  |  | SI | Head - Wounds |
| Q09ObsDR | varchar |  | FK | SI | Head - Wounds DR |
| Q10 | varchar |  |  | SI | Pupil Reaction (R) |
| Q10ObsDR | varchar |  | FK | SI | Pupil Reaction (R) DR |
| Q11 | varchar |  |  | SI | Pupil Reaction (L) |
| Q11ObsDR | varchar |  | FK | SI | Pupil Reaction (L) DR |
| Q12 | varchar |  |  | SI | Chest - Wounds |
| Q12ObsDR | varchar |  | FK | SI | Chest - Wounds DR |
| Q13 | varchar |  |  | SI | Chest - Paradoxical movements |
| Q13ObsDR | varchar |  | FK | SI | Chest - Paradoxical movements DR |
| Q14 | varchar |  |  | SI | Breath sounds (R) |
| Q14ObsDR | varchar |  | FK | SI | Breath sounds (R) DR |
| Q15 | varchar |  |  | SI | Breath sounds (L) |
| Q15ObsDR | varchar |  | FK | SI | Breath sounds (L) DR |
| Q16 | varchar |  |  | SI | Abdomen - Wounds |
| Q16ObsDR | varchar |  | FK | SI | Abdomen - Wounds DR |
| Q17 | varchar |  |  | SI | Abdomen distended |
| Q17ObsDR | varchar |  | FK | SI | Abdomen distended DR |
| Q18 | varchar |  |  | SI | Abdomen bowel sounds |
| Q18ObsDR | varchar |  | FK | SI | Abdomen bowel sounds DR |
| Q19 | varchar |  |  | SI | Abdomen - Rigidity |
| Q19ObsDR | varchar |  | FK | SI | Abdomen - Rigidity DR |
| Q20 | varchar |  |  | SI | Extremities - Wounds / deformities |
| Q20ObsDR | varchar |  | FK | SI | Extremities - Wounds / deformities DR |
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