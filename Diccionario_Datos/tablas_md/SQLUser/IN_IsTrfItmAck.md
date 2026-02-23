# SQLUser.IN_IsTrfItmAck

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACK_ParRef | varchar | PK |  | NO | INIT Par Ref |
| ACK_AckQty | double |  |  | SI | Acknowledge Quantity |
| ACK_ChildSub | numeric |  |  | NO | ChildSub |
| ACK_RowId | varchar |  |  | NO | - |
| ACK_TransferToStorageBin_DR | varchar |  | FK | SI | Des Ref CTLocStorageBin |
| Q01 | - |  |  | SI | Method 1 |
| Q02 | - |  |  | SI | Method 2 |
| Q03 | - |  |  | SI | Method 3 |
| Q04 | - |  |  | SI | Reading |
| Q05 | - |  |  | SI | Reading 2 |
| Q06 | - |  |  | SI | Reading 3 |
| Q07 | - |  |  | SI | Colour Vision |
| Q08 | - |  |  | SI | Stereopsis |
| Q09 | - |  |  | SI | Amler Grid |
| Q10 | - |  |  | SI | Method |
| Q11 | - |  |  | SI | OD |
| Q12 | - |  |  | SI | OS |
| Q13 | - |  |  | SI | Notes |
| Q14 | - |  |  | SI | Image Annotation |
| Q15 | - |  |  | SI | Date |
| Q16 | - |  |  | SI | Time |
| Q17 | - |  |  | SI | Method 1 |
| Q18 | - |  |  | SI | Method 2 |
| Q19 | - |  |  | SI | Method 3 |
| Q20 | - |  |  | SI | Notes |
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