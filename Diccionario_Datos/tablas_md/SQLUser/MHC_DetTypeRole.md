# SQLUser.MHC_DetTypeRole

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROLE_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| Q01 | - |  |  | SI | Mes |
| Q02 | - |  |  | SI | Año |
| Q03 | - |  |  | SI | N° Total de Organizaciones |
| Q04 | - |  |  | SI | Clubes de Adultos Mayores |
| Q05 | - |  |  | SI | Centros de Madres |
| Q06 | - |  |  | SI | Clubes Deportivos |
| Q07 | - |  |  | SI | Uniones Comunales de Adultos Mayores |
| Q08 | - |  |  | SI | Junta de Vecinos |
| Q09 | - |  |  | SI | Organizaciones informales |
| Q10 | - |  |  | SI | Otras organizaciones formales |
| Q11 | - |  |  | SI | N° Total de Organizaciones |
| Q12 | - |  |  | SI | Clubes de Adultos Mayores |
| Q13 | - |  |  | SI | Centros de Madres |
| Q14 | - |  |  | SI | Clubes Deportivos |
| Q15 | - |  |  | SI | Uniones Comunales de Adultos Mayores |
| Q16 | - |  |  | SI | Junta de Vecinos |
| Q17 | - |  |  | SI | Organizaciones informales |
| Q18 | - |  |  | SI | Otras organizaciones formales |
| QHR | - |  |  | SI | Establecimiento |
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
| ROLE_Childsub | double |  |  | NO | Childsub |
| ROLE_CreatedDate | date |  |  | SI | Created Date |
| ROLE_CreatedTime | time |  |  | SI | Created Time |
| ROLE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROLE_Role_DR | bigint |  | FK | SI | Des Ref CTRole |
| ROLE_RowId | varchar |  |  | NO | - |
| ROLE_UpdatedDate | date |  |  | SI | Updated Date |
| ROLE_UpdatedTime | time |  |  | SI | Updated Time |
| ROLE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*