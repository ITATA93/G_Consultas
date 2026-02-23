# SQLUser.MRC_CancerStage

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CANST_RowId | bigint | PK |  | NO | - |
| CANST_CancerType_DR | bigint |  | FK | NO | Cancer Type |
| CANST_Classification_DR | bigint |  | FK | SI | Cancer Classification System |
| CANST_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CANST_CreatedDate | date |  |  | SI | Created Date |
| CANST_CreatedTime | time |  |  | SI | Created Time |
| CANST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CANST_DateFrom | date |  |  | SI | Date From |
| CANST_DateTo | date |  |  | SI | Date To |
| CANST_Owner | varchar |  |  | SI | Code Table Owner |
| CANST_Site_DR | bigint |  | FK | SI | Body Part Site |
| CANST_UpdatedDate | date |  |  | SI | Updated Date |
| CANST_UpdatedTime | time |  |  | SI | Updated Time |
| CANST_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ01DR | - |  |  | SI | Child Reference: Egreso de Recién Nacido |
| Q02 | - |  |  | SI | Fecha de egreso madre |
| Q03 | - |  |  | SI | Estado de salud |
| Q04 | - |  |  | SI | Destino |
| Q05 | - |  |  | SI | Método Anticonceptivo |
| Q06 | - |  |  | SI | Comentarios |
| Q07 | - |  |  | SI | Entrega de Placenta (mujer pueblo originario) |
| Q08 | - |  |  | SI | Educación al Alta |
| Q09 | - |  |  | SI | Contenido |
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