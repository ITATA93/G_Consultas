# SQLUser.ARC_BillingScheduleRevisionTariff

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBSCRT_ParRef | bigint | PK |  | NO | Parent BillingScheduleRevision |
| ARCBSCRT_Base | varchar |  |  | SI | Base
If the base flag is on, all the other tariff... |
| ARCBSCRT_BillRoundType | varchar |  |  | SI | Billing Rounding Type
Defines the type of Roundin... |
| ARCBSCRT_BillRoundUnit | double |  |  | SI | Billing Rounding Unit |
| ARCBSCRT_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBSCRT_CreatedDate | date |  |  | SI | Created Date |
| ARCBSCRT_CreatedTime | time |  |  | SI | Created Time |
| ARCBSCRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBSCRT_InactiveBillingItems | varchar |  |  | SI | A list of Inactive Billing Items from Base Tariff ... |
| ARCBSCRT_Manual | varchar |  |  | SI | Manual
If the manual flag is on, the tariff will ... |
| ARCBSCRT_Percentage | double |  |  | SI | Percentage |
| ARCBSCRT_RowID | varchar |  |  | NO | - |
| ARCBSCRT_Tariff_DR | bigint |  | FK | NO | Tariff |
| ARCBSCRT_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBSCRT_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBSCRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Código: |
| Q02 | - |  |  | SI | Edad |
| Q03 | - |  |  | SI | Sexo |
| Q04 | - |  |  | SI | Fecha de inicio Tratamiento |
| Q05 | - |  |  | SI | Marque con una X el casillero respectivo |
| Q06 | - |  |  | SI | Fecha de extracción |
| Q07 | - |  |  | SI | Hora |
| Q08 | - |  |  | SI | Volumen de plasma |
| Q09 | - |  |  | SI | Observación |
| Q10 | - |  |  | SI | Establecimiento |
| Q11 | - |  |  | SI | Serv. de salud |
| Q12 | - |  |  | SI | Nombre medico que solicita |
| Q13 | - |  |  | SI | FechaM |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*