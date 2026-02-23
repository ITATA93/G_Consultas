# SQLUser.BLC_CRAFTVersion

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Banco de Sangre**. Gestión de hemoderivados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRAFTV_RowId | bigint | PK |  | NO | - |
| CRAFTV_Code | varchar |  |  | NO | Code |
| CRAFTV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CRAFTV_CreatedDate | date |  |  | SI | Created Date |
| CRAFTV_CreatedTime | time |  |  | SI | Created Time |
| CRAFTV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CRAFTV_DateFrom | date |  |  | SI | Date From |
| CRAFTV_DateTo | date |  |  | SI | Date To |
| CRAFTV_Desc | varchar |  |  | NO | Description |
| CRAFTV_Owner | varchar |  |  | SI | Owner |
| CRAFTV_PaymentRate | double |  |  | SI | Payment Rate |
| CRAFTV_UpdatedDate | date |  |  | SI | Updated Date |
| CRAFTV_UpdatedTime | time |  |  | SI | Updated Time |
| CRAFTV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | ¿Tiene indicación médica del día para terapia kiné... |
| Q02 | - |  |  | SI | ¿Se encuentra hemodinámicamente estable? |
| Q03 | - |  |  | SI | ¿Paciente posee brazalete de identificación? |
| Q04 | - |  |  | SI | Si es menor de 15 años, ¿Suspención alimentación e... |
| Q05 | - |  |  | SI | Si es adulto, ¿Tipo de reposo indicado? |
| Q06 | - |  |  | SI | Si es adulto, ¿Riesgo de caídas evaluado? |
| Q07 | - |  |  | SI | Servicio de solicitud |
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