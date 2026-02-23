# questionnaire.QTCMSA

> Musculoskeletal Assessment

**Schema:** questionnaire
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Musculoskeletal Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Neck |
| Q02 | varchar |  |  | SI | Notes |
| Q03 | varchar |  |  | SI | Neck Range of Motion (ROM) |
| Q04 | varchar |  |  | SI | Right |
| Q05 | varchar |  |  | SI | Left |
| Q06 | varchar |  |  | SI | Flexion |
| Q07 | varchar |  |  | SI | Extension |
| Q08 | varchar |  |  | SI | Neck Tightness |
| Q09 | varchar |  |  | SI | Right |
| Q10 | varchar |  |  | SI | Left |
| Q11 | varchar |  |  | SI | Neck Tenderness |
| Q12 | varchar |  |  | SI | Right |
| Q13 | varchar |  |  | SI | Focal tenderness in right |
| Q14 | varchar |  |  | SI | Left |
| Q15 | varchar |  |  | SI | Focal tenderness in left |
| Q16 | varchar |  |  | SI | Comments |
| Q17 | varchar |  |  | SI | Spine |
| Q18 | varchar |  |  | SI | Kyphosis |
| Q19 | varchar |  |  | SI | Scoliosis |
| Q20 | varchar |  |  | SI | Convex side of scoliosis |
| Q21 | varchar |  |  | SI | Scoliosis location |
| Q22 | varchar |  |  | SI | Lordosis |
| Q23 | varchar |  |  | SI | Iliac Crests (IC) |
| Q24 | numeric |  |  | SI | IC elevation (cm) |
| Q25 | varchar |  |  | SI | Sacroiliac tenderness right |
| Q26 | varchar |  |  | SI | Sacroiliac tenderness left |
| Q27 | varchar |  |  | SI | Sacroiliac pain maneuvers |
| Q28 | varchar |  |  | SI | Comments |
| Q29 | varchar |  |  | SI | Flexion |
| Q30 | varchar |  |  | SI | Flexion ROM |
| Q31 | numeric |  |  | SI | Distance (cm) |
| Q32 | varchar |  |  | SI | Pain with flexion |
| Q33 | varchar |  |  | SI | Extension |
| Q34 | varchar |  |  | SI | ROM restriction |
| Q35 | varchar |  |  | SI | Pain with extension |
| Q36 | varchar |  |  | SI | Paraspinals tenderness right |
| Q37 | varchar |  |  | SI | Paraspinals tenderness left |
| Q38 | varchar |  |  | SI | Rhomboids and lumborum tenderness left |
| Q39 | varchar |  |  | SI | General |
| Q40 | varchar |  |  | SI | Upper extremities (bilateral) |
| Q41 | varchar |  |  | SI | Upper extremity right |
| Q42 | varchar |  |  | SI | Upper extremity left |
| Q43 | varchar |  |  | SI | Lower extremities (bilateral) |
| Q44 | varchar |  |  | SI | Lower extremity right |
| Q45 | varchar |  |  | SI | Lower extremity left |
| Q46 | varchar |  |  | SI | Comments |
| Q47 | varchar |  |  | SI | Rhomboids and lumborum tenderness right |
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