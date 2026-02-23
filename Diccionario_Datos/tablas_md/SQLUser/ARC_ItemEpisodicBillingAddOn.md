# SQLUser.ARC_ItemEpisodicBillingAddOn

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADD_ParRef | varchar | PK |  | NO | ARC_EpisodicBilling Parent Reference |
| ADD_Childsub | double |  |  | NO | Childsub |
| ADD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADD_CreatedDate | date |  |  | SI | Created Date |
| ADD_CreatedTime | time |  |  | SI | Created Time |
| ADD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADD_DateFrom | double |  |  | SI | Date From |
| ADD_DateTo | double |  |  | SI | Date To |
| ADD_Description | varchar |  |  | SI | Add On Description  |
| ADD_InlierAddon | double |  |  | SI | Inlier Addon |
| ADD_InlierPayorCode | varchar |  |  | SI | Inlier Payor Code  |
| ADD_OutlierAddon | double |  |  | SI | Outlier Addon |
| ADD_OutlierPayorCode | varchar |  |  | SI | Outlier Payor Code  |
| ADD_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| ADD_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| ADD_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| ADD_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| ADD_RowId | varchar |  |  | NO | - |
| ADD_ShortInlierAddon | double |  |  | SI | Short Inlier Addon |
| ADD_ShortInlierPayorCode | varchar |  |  | SI | ShortInlier Payor Code  |
| ADD_UpdatedDate | date |  |  | SI | Updated Date |
| ADD_UpdatedTime | time |  |  | SI | Updated Time |
| ADD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha de Ingreso |
| Q02 | - |  |  | SI | Hora de Ingreso |
| Q03 | - |  |  | SI | Nombre del Profesional |
| Q04 | - |  |  | SI | Tipo de Profesional |
| Q05 | - |  |  | SI | Servicio/Unidad del Paciente |
| Q06 | - |  |  | SI | Control de Ingreso |
| Q07 | - |  |  | SI | Nombre del Paciente |
| Q08 | - |  |  | SI | Observación |
| Q09 | - |  |  | SI | Apellido Parteno del Paciente |
| Q10 | - |  |  | SI | Apellido Materno del Paciente |
| Q11 | - |  |  | SI | Motivo Control de Acceso |
| Q12 | - |  |  | SI | IP Nombre Equipo del profesional |
| Q13 | - |  |  | SI | Grupo Seguridad Profesional |
| Q14 | - |  |  | SI | Local del Profesional |
| Q15 | - |  |  | SI | Código Local del Profesional |
| Q16 | - |  |  | SI | Establecimiento del Profesional |
| Q17 | - |  |  | SI | Establecimiento del Paciente |
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