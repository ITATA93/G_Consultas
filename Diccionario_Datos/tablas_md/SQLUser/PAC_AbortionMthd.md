# SQLUser.PAC_AbortionMthd

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ABOM_RowId | bigint | PK |  | NO | - |
| ABOM_Code | varchar |  |  | NO | Code |
| ABOM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ABOM_CreatedDate | date |  |  | SI | Created Date |
| ABOM_CreatedTime | time |  |  | SI | Created Time |
| ABOM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ABOM_DateFrom | date |  |  | SI | DateFrom |
| ABOM_DateTo | date |  |  | SI | DateTo |
| ABOM_Desc | varchar |  |  | NO | Description |
| ABOM_Owner | varchar |  |  | SI | Owner |
| ABOM_UpdatedDate | date |  |  | SI | Updated Date |
| ABOM_UpdatedTime | time |  |  | SI | Updated Time |
| ABOM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Characteristic |
| Q04 | - |  |  | SI | General appearance |
| Q05 | - |  |  | SI | Capillary refill |
| Q06 | - |  |  | SI | Tears |
| Q07 | - |  |  | SI | Mucous membranes |
| Q08 | - |  |  | SI | Eyes |
| Q09 | - |  |  | SI | Quality of respiration |
| Q10 | - |  |  | SI | Quality of radial pulse |
| Q11 | - |  |  | SI | Skin elasticity |
| Q12 | - |  |  | SI | Heart rate |
| Q13 | - |  |  | SI | Urine output |
| Q14 | - |  |  | SI | Score interpretation |
| Q15 | - |  |  | SI | Guidelines |
| Q16 | - |  |  | SI | Score <3 corresponds to a fluid deficit of <5% bod... |
| Q17 | - |  |  | SI | Score ≥3 and <6 corresponds to a fluid deficit of ... |
| Q18 | - |  |  | SI | Estimate percentage dehydration in children with g... |
| Q19 | - |  |  | SI | Score ≥6 corresponds to a fluid deficit of >9% bod... |
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