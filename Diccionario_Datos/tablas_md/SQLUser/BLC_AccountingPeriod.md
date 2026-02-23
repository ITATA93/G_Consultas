# SQLUser.BLC_AccountingPeriod

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PER_RowId | bigint | PK |  | NO | - |
| PER_Code | varchar |  |  | NO | Code |
| PER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PER_CreatedDate | date |  |  | SI | Created Date |
| PER_CreatedTime | time |  |  | SI | Created Time |
| PER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PER_DateFrom | date |  |  | SI | Date From |
| PER_DateTo | date |  |  | SI | Date To |
| PER_Desc | varchar |  |  | NO | Description |
| PER_Owner | varchar |  |  | SI | Owner |
| PER_Status | varchar |  |  | SI | Status |
| PER_UpdatedDate | date |  |  | SI | Updated Date |
| PER_UpdatedTime | time |  |  | SI | Updated Time |
| PER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | El paciente ha confirmado: Nombre, apellidos y RUT... |
| Q02 | - |  |  | SI | Brazalete de identificación instalado con datos co... |
| Q03 | - |  |  | SI | Se confirmó el procedimiento a realizar con la ord... |
| Q04 | - |  |  | SI | El paciente está en ayuno |
| Q05 | - |  |  | SI | El paciente realizó la preparación indicada |
| Q06 | - |  |  | SI | Si realizó preparación&nbsp |
| Q07 | - |  |  | SI | Tiene antecedentes de alergia a medicamentos / lat... |
| Q08 | - |  |  | SI | Retiro de prótesis y/o piercings bucal |
| Q09 | - |  |  | SI | Fecha evaluación |
| Q10 | - |  |  | SI | Hora evaluación |
| Q11 | - |  |  | SI | Responsable del Registro |
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