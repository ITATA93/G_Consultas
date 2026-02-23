# SQLUser.ORC_O2DeliveryModeEndo

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| O2DEMO_RowId | bigint | PK |  | NO | - |
| O2DEMO_Code | varchar |  |  | NO | Code |
| O2DEMO_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| O2DEMO_CreatedDate | date |  |  | SI | Created Date |
| O2DEMO_CreatedTime | time |  |  | SI | Created Time |
| O2DEMO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| O2DEMO_DateFrom | date |  |  | SI | Date From |
| O2DEMO_DateTo | date |  |  | SI | Date To |
| O2DEMO_Desc | varchar |  |  | NO | Description |
| O2DEMO_Owner | varchar |  |  | SI | Owner |
| O2DEMO_UpdatedDate | date |  |  | SI | Updated Date |
| O2DEMO_UpdatedTime | time |  |  | SI | Updated Time |
| O2DEMO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Diet type	 |
| Q01a | - |  |  | SI | Diet Types |
| Q02 | - |  |  | SI | Texture |
| Q02a | - |  |  | SI | Texture |
| Q03 | - |  |  | SI | Fluid type	 |
| Q04 | - |  |  | SI | Fluid restriction	 |
| Q05 | - |  |  | SI | Religious considerations |
| Q06 | - |  |  | SI | Supervision |
| Q06a | - |  |  | SI | Supervision |
| Q07 | - |  |  | SI | Trays |
| Q07a | - |  |  | SI | Trays |
| Q08 | - |  |  | SI | Diet restrictions	 |
| Q09 | - |  |  | SI | Other |
| Q10 | - |  |  | SI | Date |
| Q11 | - |  |  | SI | Time |
| Q12 | - |  |  | SI | Modified Fluids |
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