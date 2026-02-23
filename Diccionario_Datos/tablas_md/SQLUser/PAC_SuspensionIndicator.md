# SQLUser.PAC_SuspensionIndicator

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUSIND_RowId | bigint | PK |  | NO | - |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | Skin Inspection |
| Q11 | - |  |  | SI | Head to toe skin inspection, focus on overlying bo... |
| Q12 | - |  |  | SI | Identify any pressure injury that may be present o... |
| Q13 | - |  |  | SI | Assess localized pain related to tissue damage |
| Q14 | - |  |  | SI | Inspect skin under medical devices for any sign of... |
| Q15 | - |  |  | SI | Keep Moving and Repositioning |
| Q16 | - |  |  | SI | Reposition patient every two hours when in bed (mi... |
| Q17 | - |  |  | SI | Use manual handling aids, (do not drag) the patien... |
| Q18 | - |  |  | SI | Offload heels completely |
| Q19 | - |  |  | SI | Use 30-degree head tilt side lying position |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Do not use the following that may damage tissue: D... |
| Q21 | - |  |  | SI | Incontinence |
| Q22 | - |  |  | SI | Offer toilet assistance every 2 hours and as neces... |
| Q23 | - |  |  | SI | Apply moisture barrier on healthy skin area |
| Q24 | - |  |  | SI | Do not use oil-based cream with continence product... |
| Q25 | - |  |  | SI | Nutrition |
| Q26 | - |  |  | SI | If patient has nutritional deficit or high risk fo... |
| Q27 | - |  |  | SI | Carry out nutrition instruction and record supplem... |
| Q3 | - |  |  | SI | Support Surface |
| Q4 | - |  |  | SI | Patient in correct mattress |
| Q5 | - |  |  | SI | Check all mattress for Bottoming out |
| Q6 | - |  |  | SI | Do Not Use multiple layers of linen under patient |
| Q7 | - |  |  | SI | Keep linens dry free of wrinkles |
| Q8 | - |  |  | SI | Be sure patient is not lying on tubing, telephone,... |
| Q9 | - |  |  | SI | Use appropriate devices to offload pressure from l... |
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
| SUSIND_Code | varchar |  |  | NO | Code |
| SUSIND_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUSIND_CreatedDate | date |  |  | SI | Created Date |
| SUSIND_CreatedTime | time |  |  | SI | Created Time |
| SUSIND_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUSIND_Desc | varchar |  |  | NO | Description |
| SUSIND_Owner | varchar |  |  | SI | Owner |
| SUSIND_UpdatedDate | date |  |  | SI | Updated Date |
| SUSIND_UpdatedTime | time |  |  | SI | Updated Time |
| SUSIND_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*