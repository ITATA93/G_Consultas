# questionnaire.QTCPSSKIN

> Pressure Injury Prevention Bundle (SSKIN)

**Schema:** questionnaire
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Pressure Injury Prevention Bundle (SSKIN)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q1 | date |  |  | SI | Date |
| Q10 | varchar |  |  | SI | Skin Inspection |
| Q11 | varchar |  |  | SI | Head to toe skin inspection, focus on overlying bo... |
| Q12 | varchar |  |  | SI | Identify any pressure injury that may be present o... |
| Q13 | varchar |  |  | SI | Assess localized pain related to tissue damage |
| Q14 | varchar |  |  | SI | Inspect skin under medical devices for any sign of... |
| Q15 | varchar |  |  | SI | Keep Moving and Repositioning |
| Q16 | varchar |  |  | SI | Reposition patient every two hours when in bed (mi... |
| Q17 | varchar |  |  | SI | Use manual handling aids, (do not drag) the patien... |
| Q18 | varchar |  |  | SI | Offload heels completely |
| Q19 | varchar |  |  | SI | Use 30-degree head tilt side lying position |
| Q2 | time |  |  | SI | Time |
| Q20 | varchar |  |  | SI | Do not use the following that may damage tissue: D... |
| Q21 | varchar |  |  | SI | Incontinence  |
| Q22 | varchar |  |  | SI | Offer toilet assistance every 2 hours and as neces... |
| Q23 | varchar |  |  | SI | Apply moisture barrier on healthy skin area |
| Q24 | varchar |  |  | SI | Do not use oil-based cream with continence product... |
| Q25 | varchar |  |  | SI | Nutrition |
| Q26 | varchar |  |  | SI | If patient has nutritional deficit or high risk fo... |
| Q27 | varchar |  |  | SI | Carry out nutrition instruction and record supplem... |
| Q3 | varchar |  |  | SI | Support Surface |
| Q4 | varchar |  |  | SI | Patient in correct mattress |
| Q5 | varchar |  |  | SI | Check all mattress for Bottoming out |
| Q6 | varchar |  |  | SI | Do Not Use multiple layers of linen under patient |
| Q7 | varchar |  |  | SI | Keep linens dry free of wrinkles |
| Q8 | varchar |  |  | SI | Be sure patient is not lying on tubing, telephone,... |
| Q9 | varchar |  |  | SI | Use appropriate devices to offload pressure from l... |
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