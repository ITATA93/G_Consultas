# SQLUser.MRC_ShortStayReason

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SHSTR_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Peso |
| Q01ObsDR | - |  |  | SI | Peso DR |
| Q02 | - |  |  | SI | Talla |
| Q02ObsDR | - |  |  | SI | Talla DR |
| Q03 | - |  |  | SI | Índice de masa corporal (IMC) |
| Q04 | - |  |  | SI | Circunferencia Craneana |
| Q04ObsDR | - |  |  | SI | Circunferencia Craneana DR |
| Q05 | - |  |  | SI | Percentil Peso Edad Gestacional |
| Q05ObsDR | - |  |  | SI | Percentil Peso Edad Gestacional DR |
| Q06 | - |  |  | SI | Percentil Talla Edad Gestacional |
| Q06ObsDR | - |  |  | SI | Percentil Talla Edad Gestacional DR |
| Q07 | - |  |  | SI | Percentil Circunferencia Craneana Edad Gestacional |
| Q07ObsDR | - |  |  | SI | Percentil Circunferencia Craneana Edad Gestacional... |
| Q08 | - |  |  | SI | Percentil Indice Ponderal Edad Gestacional |
| Q08ObsDR | - |  |  | SI | Percentil Indice Ponderal Edad Gestacional DR |
| Q10 | - |  |  | SI | (**) El cálculo automático trabaja entre 24 a 42 s... |
| Q11 | - |  |  | SI | kg |
| Q12 | - |  |  | SI | cm |
| Q13 | - |  |  | SI | cm |
| Q14 | - |  |  | SI | Semanas (**) |
| QEG | - |  |  | SI | Edad Gestacional |
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
| SHSTR_Code | varchar |  |  | NO | Code |
| SHSTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SHSTR_CreatedDate | date |  |  | SI | Created Date |
| SHSTR_CreatedTime | time |  |  | SI | Created Time |
| SHSTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SHSTR_DateFrom | date |  |  | SI | Date From |
| SHSTR_DateTo | date |  |  | SI | Date To |
| SHSTR_Desc | varchar |  |  | NO | Description |
| SHSTR_Owner | varchar |  |  | SI | Owner |
| SHSTR_UpdatedDate | date |  |  | SI | Updated Date |
| SHSTR_UpdatedTime | time |  |  | SI | Updated Time |
| SHSTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*