# questionnaire.QTCPRA

> Paediatric Rehabilitation Assessment

**Schema:** questionnaire
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Paediatric Rehabilitation Assessment

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Reason for admission |
| Q02 | varchar |  |  | SI | Comments |
| Q03 | varchar |  |  | SI | Previous functional status |
| Q04 | varchar |  |  | SI | Previous physical therapies |
| Q05 | varchar |  |  | SI | Lives with |
| Q06 | numeric |  |  | SI | Mother's number of pregnacies |
| Q07 | varchar |  |  | SI | Respiratory function |
| Q08 | varchar |  |  | SI | Nutrition |
| Q09 | varchar |  |  | SI | Non - autonomous nutrition |
| Q10 | varchar |  |  | SI | Level cof consciousness (AVPU) |
| Q10ObsDR | varchar |  | FK | SI | Level cof consciousness (AVPU) DR |
| Q11 | varchar |  |  | SI | Vision |
| Q12 | varchar |  |  | SI | Corneal reflex |
| Q13 | varchar |  |  | SI | Fixation |
| Q14 | varchar |  |  | SI | Following a target |
| Q15 | varchar |  |  | SI | Physical examination |
| Q16 | varchar |  |  | SI | Spontaneous posture |
| Q20 | varchar |  |  | SI | Musculo - skeletal deformities |
| Q21 | varchar |  |  | SI | Musculo - skeletal deformities |
| Q23 | varchar |  |  | SI | Motor skills |
| Q24 | varchar |  |  | SI | Head control |
| Q25 | varchar |  |  | SI | Trunk control |
| Q26 | varchar |  |  | SI | Hips control |
| Q27 | varchar |  |  | SI | Postural movements |
| Q28 | varchar |  |  | SI | Supine to the side |
| Q28ObsDR | varchar |  | FK | SI | Supine to the side DR |
| Q29 | varchar |  |  | SI | Supine to sitting |
| Q29ObsDR | varchar |  | FK | SI | Supine to sitting DR |
| Q30 | varchar |  |  | SI | Sitting to standing |
| Q30ObsDR | varchar |  | FK | SI | Sitting to standing DR |
| Q31 | varchar |  |  | SI | Sitting position: Level of sitting scale |
| Q32 | varchar |  |  | SI | Walking assessment |
| Q33 | varchar |  |  | SI | Gait |
| Q34 | varchar |  |  | SI | Gait analysis |
| Q35 | varchar |  |  | SI | Manipulation |
| Q36 | varchar |  |  | SI | Manipulation type |
| Q37 | varchar |  |  | SI | Devices / Aids |
| Q38 | varchar |  |  | SI | Type of devices / aids |
| Q39 | varchar |  |  | SI | Pain |
| Q40 | varchar |  |  | SI | Other issues |
| Q41 | varchar |  |  | SI | Treatment plan |
| Q42 | varchar |  |  | SI | Treatment goals |
| Q43 | varchar |  |  | SI | Treatment options |
| Q44 | varchar |  |  | SI | Family involved in treatment plan |
| Q45 | varchar |  |  | SI | Family involvement |
| Q46 | varchar |  |  | SI | Comments |
| Q47 | date |  |  | SI | Date |
| Q48 | time |  |  | SI | Time |
| Q49 | varchar |  |  | SI | Respiratory function |
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