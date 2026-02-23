# SQLUser.ARC_SurchIncremental

**Schema:** SQLUser
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCR_ParRef | bigint | PK |  | NO | ARC_SurchargeCode Parent Reference |
| INCR_AmtPerMinute | double |  |  | SI | Amount Per Block |
| INCR_AuxInstype_DR | bigint |  | FK | SI | Des Ref AuxInstype |
| INCR_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| INCR_Childsub | double |  |  | NO | Childsub |
| INCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCR_CreatedDate | date |  |  | SI | Created Date |
| INCR_CreatedTime | time |  |  | SI | Created Time |
| INCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCR_DateFrom | date |  |  | SI | Date From |
| INCR_DateTo | date |  |  | SI | Date To |
| INCR_EpisodeSubType_DR | bigint |  | FK | SI | Des Ref EpisodeSubType |
| INCR_FixedTimeAmt | double |  |  | SI | First Time Block |
| INCR_FixedTimeBlock | double |  |  | SI | Fixed Time Block |
| INCR_Hourly | varchar |  |  | SI | Hourly |
| INCR_IncremTime | double |  |  | SI | Increment Time |
| INCR_IncrementPrice | double |  |  | SI | Increment Price |
| INCR_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| INCR_RoomType_DR | bigint |  | FK | SI | Des Ref RoomType |
| INCR_RowId | varchar |  |  | NO | - |
| INCR_Tariff_DR | bigint |  | FK | SI | Des Ref Tariff |
| INCR_TimeFrom | double |  |  | SI | Time From |
| INCR_TimeUntil | double |  |  | SI | Time Until |
| INCR_UpdatedDate | date |  |  | SI | Updated Date |
| INCR_UpdatedTime | time |  |  | SI | Updated Time |
| INCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | RUT / ID Paciente |
| Q02 | - |  |  | SI | Nombre |
| Q03 | - |  |  | SI | Apellido Paterno |
| Q04 | - |  |  | SI | Apellido Materno |
| Q05 | - |  |  | SI | Establecimiento |
| Q06 | - |  |  | SI | Fecha de Registro |
| Q07 | - |  |  | SI | Iniciales de AC |
| Q08 | - |  |  | SI | Iniciales de Profesional |
| Q09 | - |  |  | SI | Fecha Inicio Programa |
| Q10 | - |  |  | SI | Fecha Término Programa (9 meses después) |
| Q11 | - |  |  | SI | Áreas |
| Q12 | - |  |  | SI | Área #2 |
| Q13 | - |  |  | SI | Razón porque elige esta área: |
| Q14 | - |  |  | SI | Personas involucradas y responsabilidades |
| Q15 | - |  |  | SI | Lugares |
| Q16 | - |  |  | SI | Tiempo |
| Q17 | - |  |  | SI | Recursos necesarios |
| Q18 | - |  |  | SI | Otros |
| Q19 | - |  |  | SI | Potenciales obstáculos y estrategias de abordaje |
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