# SQLUser.OEC_SpeedFlowRate

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SFR_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Evaluation |
| Q01 | - |  |  | SI | Stoma Type |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Stoma Type DR |
| Q02 | - |  |  | SI | Stoma since |
| Q02N | - |  |  | SI | Note |
| Q03 | - |  |  | SI | Stoma Permanence |
| Q03ObsDR | - |  |  | SI | Stoma Permanence DR |
| Q06 | - |  |  | SI | Diameter top/down (cm) |
| Q07 | - |  |  | SI | Diameter right / left (cm) |
| Q08 | - |  |  | SI | Drainage / Material |
| Q08N | - |  |  | SI | Note |
| Q10 | - |  |  | SI | Note |
| Q10TxtOnly | - |  |  | SI | Note Plain Text Only |
| Q14 | - |  |  | SI | Date |
| Q15 | - |  |  | SI | Time |
| Q16 | - |  |  | SI | Removal date |
| Q17 | - |  |  | SI | Stoma formation date |
| Q18 | - |  |  | SI | Reason for stoma formation |
| Q19 | - |  |  | SI | Stoma formation |
| Q20 | - |  |  | SI | Stents present |
| Q21 | - |  |  | SI | Rod present |
| Q22 | - |  |  | SI | Stoma width (mm) |
| Q23 | - |  |  | SI | Stoma length (mm) |
| Q24 | - |  |  | SI | Stoma protrusion length (mm) |
| Q3N | - |  |  | SI | Note |
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
| SFR_Code | varchar |  |  | NO | Code |
| SFR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SFR_CreatedDate | date |  |  | SI | Created Date |
| SFR_CreatedTime | time |  |  | SI | Created Time |
| SFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SFR_Desc | varchar |  |  | NO | Description |
| SFR_Owner | varchar |  |  | SI | Owner |
| SFR_UpdatedDate | date |  |  | SI | Updated Date |
| SFR_UpdatedTime | time |  |  | SI | Updated Time |
| SFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*