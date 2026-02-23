# SQLUser.MRC_NursingNoteCodeIntervent

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INT_ParRef | bigint | PK |  | NO | MRC_NursingNoteCodes Parent Reference |
| CQ01 | - |  |  | SI | (null) |
| CQ02 | - |  |  | SI | (null) |
| CQ03 | - |  |  | SI | (null) |
| CQ04 | - |  |  | SI | (null) |
| CQ05 | - |  |  | SI | (null) |
| CQ06 | - |  |  | SI | (null) |
| CQ07 | - |  |  | SI | (null) |
| CQ08 | - |  |  | SI | (null) |
| INT_Childsub | double |  |  | NO | Childsub |
| INT_Code | varchar |  |  | NO | Code |
| INT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INT_CreatedDate | date |  |  | SI | Created Date |
| INT_CreatedTime | time |  |  | SI | Created Time |
| INT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INT_FirstLine | varchar |  |  | SI | FirstLine |
| INT_RowId | varchar |  |  | NO | - |
| INT_Text | varchar |  |  | SI | Text |
| INT_UpdatedDate | date |  |  | SI | Updated Date |
| INT_UpdatedTime | time |  |  | SI | Updated Time |
| INT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Capacidad para usar el telefono |
| Q02 | - |  |  | SI | Ir de compras |
| Q03 | - |  |  | SI | Preparacion de la comida |
| Q04 | - |  |  | SI | Cuidar la casa |
| Q05 | - |  |  | SI | Lavado de Ropa |
| Q06 | - |  |  | SI | Medio de transporte |
| Q07 | - |  |  | SI | Responsabilidad sobre la medicacion |
| Q08 | - |  |  | SI | Capacidad de utilizar el dinero |
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