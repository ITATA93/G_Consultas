# SQLUser.ARC_PackageGroupSubGroup

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACKGRPSUB_ParRef | bigint | PK |  | NO | ARC_PackageGroup Parent Reference |
| PACKGRPSUB_Childsub | double |  |  | NO | Childsub |
| PACKGRPSUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACKGRPSUB_Comments | varchar |  |  | SI | Comments |
| PACKGRPSUB_CreatedDate | date |  |  | SI | Created Date |
| PACKGRPSUB_CreatedTime | time |  |  | SI | Created Time |
| PACKGRPSUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACKGRPSUB_DateFrom | date |  |  | SI | DateFrom |
| PACKGRPSUB_DateTo | date |  |  | SI | DateTo |
| PACKGRPSUB_PackSubGroup_DR | bigint |  | FK | SI | Des Ref ARCPackageSubGroup |
| PACKGRPSUB_Rank | integer |  |  | SI | Rank |
| PACKGRPSUB_RowId | varchar |  |  | NO | - |
| PACKGRPSUB_UpdatedDate | date |  |  | SI | Updated Date |
| PACKGRPSUB_UpdatedTime | time |  |  | SI | Updated Time |
| PACKGRPSUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Paciente |
| Q02 | - |  |  | SI | Apoderado |
| Q03 | - |  |  | SI | ¿Usa inhalador estacional? |
| Q04 | - |  |  | SI | Nombre: |
| Q05 | - |  |  | SI | ¿Durante el último año ha presentado alguna patolo... |
| Q06 | - |  |  | SI | ¿Cuál/es? |
| Q07 | - |  |  | SI | ¿Recibió indicaciones escritas antes de iniciar su... |
| Q08 | - |  |  | SI | Comentarios |
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