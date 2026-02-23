# SQLUser.BLC_ApprGroupRequestDescription

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APGRPDSC_RowId | bigint | PK |  | NO | - |
| APGRPDSC_Code | varchar |  |  | NO | Code |
| APGRPDSC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APGRPDSC_CreatedDate | date |  |  | SI | Created Date |
| APGRPDSC_CreatedTime | time |  |  | SI | Created Time |
| APGRPDSC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APGRPDSC_DateFrom | date |  |  | SI | Date From |
| APGRPDSC_DateTo | date |  |  | SI | Date To |
| APGRPDSC_Default | varchar |  |  | SI | Default Flag |
| APGRPDSC_Desc | varchar |  |  | NO | Description |
| APGRPDSC_Owner | varchar |  |  | SI | Owner |
| APGRPDSC_UpdatedDate | date |  |  | SI | Updated Date |
| APGRPDSC_UpdatedTime | time |  |  | SI | Updated Time |
| APGRPDSC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | Antes que el paciente abandone el box |
| Q04 | - |  |  | SI | Enfermería Confirma |
| Q05 | - |  |  | SI | 1. Respiración correcta del paciente |
| Q06 | - |  |  | SI | 2. Desconecta endoscopia para desinfección, previo... |
| Q07 | - |  |  | SI | 3. Correcta identificación de las muestra biológic... |
| Q08 | - |  |  | SI | Previa al alta |
| Q09 | - |  |  | SI | 4. Educa y Entrega |
| Q10 | - |  |  | SI | Instrucciones sobre el inicio de la deglución e in... |
| Q11 | - |  |  | SI | Informe e Indicaciones del examen realizado |
| Q12 | - |  |  | SI | Paciente se retira acompañado |
| Q13 | - |  |  | SI | Responsable del registro |
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