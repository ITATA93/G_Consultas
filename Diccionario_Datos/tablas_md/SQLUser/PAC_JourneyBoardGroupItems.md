# SQLUser.PAC_JourneyBoardGroupItems

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| JBGRPITM_ParRef | bigint | PK |  | NO | PAC_JourneyBoardGroup Parent Reference |
| JBGRPITM_AddNew | varchar |  |  | SI | Can add new  |
| JBGRPITM_Childsub | double |  |  | NO | Childsub |
| JBGRPITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| JBGRPITM_DateFrom | date |  |  | SI | Date From |
| JBGRPITM_DateTo | date |  |  | SI | Date To |
| JBGRPITM_Item_DR | bigint |  | FK | SI | Des Ref Journey Board Item |
| JBGRPITM_RowId | varchar |  |  | NO | - |
| JBGRPITM_Seq | integer |  |  | SI | Sequence of displaying |
| Q01 | - |  |  | SI | Neck |
| Q02 | - |  |  | SI | Notes |
| Q03 | - |  |  | SI | Neck Range of Motion (ROM) |
| Q04 | - |  |  | SI | Right |
| Q05 | - |  |  | SI | Left |
| Q06 | - |  |  | SI | Flexion |
| Q07 | - |  |  | SI | Extension |
| Q08 | - |  |  | SI | Neck Tightness |
| Q09 | - |  |  | SI | Right |
| Q10 | - |  |  | SI | Left |
| Q11 | - |  |  | SI | Neck Tenderness |
| Q12 | - |  |  | SI | Right |
| Q13 | - |  |  | SI | Focal tenderness in right |
| Q14 | - |  |  | SI | Left |
| Q15 | - |  |  | SI | Focal tenderness in left |
| Q16 | - |  |  | SI | Comments |
| Q17 | - |  |  | SI | Spine |
| Q18 | - |  |  | SI | Kyphosis |
| Q19 | - |  |  | SI | Scoliosis |
| Q20 | - |  |  | SI | Convex side of scoliosis |
| Q21 | - |  |  | SI | Scoliosis location |
| Q22 | - |  |  | SI | Lordosis |
| Q23 | - |  |  | SI | Iliac Crests (IC) |
| Q24 | - |  |  | SI | IC elevation (cm) |
| Q25 | - |  |  | SI | Sacroiliac tenderness right |
| Q26 | - |  |  | SI | Sacroiliac tenderness left |
| Q27 | - |  |  | SI | Sacroiliac pain maneuvers |
| Q28 | - |  |  | SI | Comments |
| Q29 | - |  |  | SI | Flexion |
| Q30 | - |  |  | SI | Flexion ROM |
| Q31 | - |  |  | SI | Distance (cm) |
| Q32 | - |  |  | SI | Pain with flexion |
| Q33 | - |  |  | SI | Extension |
| Q34 | - |  |  | SI | ROM restriction |
| Q35 | - |  |  | SI | Pain with extension |
| Q36 | - |  |  | SI | Paraspinals tenderness right |
| Q37 | - |  |  | SI | Paraspinals tenderness left |
| Q38 | - |  |  | SI | Rhomboids and lumborum tenderness left |
| Q39 | - |  |  | SI | General |
| Q40 | - |  |  | SI | Upper extremities (bilateral) |
| Q41 | - |  |  | SI | Upper extremity right |
| Q42 | - |  |  | SI | Upper extremity left |
| Q43 | - |  |  | SI | Lower extremities (bilateral) |
| Q44 | - |  |  | SI | Lower extremity right |
| Q45 | - |  |  | SI | Lower extremity left |
| Q46 | - |  |  | SI | Comments |
| Q47 | - |  |  | SI | Rhomboids and lumborum tenderness right |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*