# SQLUser.MHC_TaskType

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHCTASKT_RowId | bigint | PK |  | NO | - |
| MHCTASKT_Code | varchar |  |  | NO | Code |
| MHCTASKT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| MHCTASKT_CreatedDate | date |  |  | SI | Created Date |
| MHCTASKT_CreatedTime | time |  |  | SI | Created Time |
| MHCTASKT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MHCTASKT_DateFrom | date |  |  | SI | Date From |
| MHCTASKT_DateTo | date |  |  | SI | Date To |
| MHCTASKT_Desc | varchar |  |  | NO | Description |
| MHCTASKT_DetentionOutcome_DR | bigint |  | FK | SI | Des Ref MHCDetentionOutcome |
| MHCTASKT_DetentionType_DR | bigint |  | FK | SI | Des Ref MHCDetentionType |
| MHCTASKT_DueOffsetDays | double |  |  | SI | DueOffsetDays |
| MHCTASKT_DueOffsetUnits | varchar |  |  | SI | DueOffsetUnits |
| MHCTASKT_Owner | varchar |  |  | SI | Owner |
| MHCTASKT_RecipientRole_DR | bigint |  | FK | SI | Des Ref CTRole |
| MHCTASKT_ResponsibleRole_DR | bigint |  | FK | SI | Des Ref CTRole |
| MHCTASKT_SpellTask | varchar |  |  | SI | SpellTask |
| MHCTASKT_StartOffsetDays | double |  |  | SI | StartOffsetDays |
| MHCTASKT_StartOffsetUnits | varchar |  |  | SI | StartOffsetUnits |
| MHCTASKT_SuspensionType_DR | bigint |  | FK | SI | Des Ref MHSuspensionType |
| MHCTASKT_TaskItem_DR | bigint |  | FK | SI | Des Ref epr.Task |
| MHCTASKT_TriggerEvent | varchar |  |  | SI | TriggerEvent |
| MHCTASKT_UpdatedDate | date |  |  | SI | Updated Date |
| MHCTASKT_UpdatedTime | time |  |  | SI | Updated Time |
| MHCTASKT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿A causa de sus síntomas, su trabajo se ha visto p... |
| Q02 | - |  |  | SI | ¿A causa de sus síntomas, su vida social y sus act... |
| Q03 | - |  |  | SI | ¿A causa de sus síntomas, su vida familiar y sus r... |
| Q04 | - |  |  | SI | Desde su última visita, ¿cuánto le han dificultado... |
| Q05 | - |  |  | SI | Durante la última semana, ¿qué porcentaje de apoyo... |
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