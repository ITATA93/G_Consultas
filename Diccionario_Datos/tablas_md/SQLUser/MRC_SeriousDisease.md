# SQLUser.MRC_SeriousDisease

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SD_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | En el Establecimiento |
| Q04 | - |  |  | SI | Comuna de |
| Q05 | - |  |  | SI | Nombre |
| Q06 | - |  |  | SI | RUT |
| Q07 | - |  |  | SI | Nombre Completo 2 |
| Q08 | - |  |  | SI | RUT 2 |
| Q09 | - |  |  | SI | Parentesco con el Paciente |
| Q10 | - |  |  | SI | Observaciones |
| Q11 | - |  |  | SI | GES 1 |
| Q12 | - |  |  | SI | GES 2 |
| Q13 | - |  |  | SI | Motivo |
| Q14 | - |  |  | SI | Apellido Paterno |
| Q15 | - |  |  | SI | Apellido Materno |
| Q16 | - |  |  | SI | Identificación del Paciente |
| Q17 | - |  |  | SI | Identificación en caso de que quien rechaza repres... |
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
| SD_Code | varchar |  |  | NO | Code |
| SD_CreatedDate | date |  |  | SI | Created Date |
| SD_CreatedTime | time |  |  | SI | Created Time |
| SD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SD_Desc | varchar |  |  | NO | Description |
| SD_UpdatedDate | date |  |  | SI | Updated Date |
| SD_UpdatedTime | time |  |  | SI | Updated Time |
| SD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*