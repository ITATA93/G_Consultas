# SQLUser.MRC_ObjectiveOutcome

**Schema:** SQLUser
**Columnas:** 64
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBJOUTC_RowId | bigint | PK |  | NO | - |
| OBJOUTC_Code | varchar |  |  | NO | Code |
| OBJOUTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OBJOUTC_CreatedDate | date |  |  | SI | Created Date |
| OBJOUTC_CreatedTime | time |  |  | SI | Created Time |
| OBJOUTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OBJOUTC_DateFrom | date |  |  | SI | DateFrom |
| OBJOUTC_DateTo | date |  |  | SI | DateTo |
| OBJOUTC_Desc | varchar |  |  | NO | Description |
| OBJOUTC_Owner | varchar |  |  | SI | Owner |
| OBJOUTC_UpdatedDate | date |  |  | SI | Updated Date |
| OBJOUTC_UpdatedTime | time |  |  | SI | Updated Time |
| OBJOUTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Autonomo |
| Q03 | - |  |  | SI | Total |
| Q04 | - |  |  | SI | Parcial |
| Q05 | - |  |  | SI | Utiliza ropa comoda y adecuada |
| Q06 | - |  |  | SI | Adecuado para la edad |
| Q08 | - |  |  | SI | Diagnostico 1 |
| Q09 | - |  |  | SI | Diagnostico 2 |
| Q10 | - |  |  | SI | Conclusion |
| Q11 | - |  |  | SI | Especifique |
| Q12 | - |  |  | SI | Vestirse/Desvestirse |
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