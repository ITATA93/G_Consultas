# SQLUser.MRC_EncEntryTypeSection

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ESECT_ParRef | bigint | PK |  | NO | Parent Reference |
| ESECT_Childsub | double |  |  | NO | Childsub |
| ESECT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ESECT_CreatedDate | date |  |  | SI | Created Date |
| ESECT_CreatedTime | time |  |  | SI | Created Time |
| ESECT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ESECT_DateFrom | date |  |  | SI | Date From |
| ESECT_DateTo | date |  |  | SI | Date To |
| ESECT_RowId | varchar |  |  | NO | - |
| ESECT_Section_DR | bigint |  | FK | SI | Section |
| ESECT_Sequence | integer |  |  | SI | Sequence |
| ESECT_UpdatedDate | date |  |  | SI | Updated Date |
| ESECT_UpdatedTime | time |  |  | SI | Updated Time |
| ESECT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Presencial |
| Q02 | - |  |  | SI | Telefónico |
| Q03 | - |  |  | SI | Via mail |
| Q04 | - |  |  | SI | Nombre supervisor |
| Q05 | - |  |  | SI | Empresa |
| Q06 | - |  |  | SI | Fecha |
| Q07 | - |  |  | SI | Ritmo de trabajo (cantidad de trabajo realizado) |
| Q08 | - |  |  | SI | Calidad del trabajo realizado |
| Q09 | - |  |  | SI | Respuestas a ordenes y solicitudes |
| Q10 | - |  |  | SI | Responsabilidades |
| Q11 | - |  |  | SI | Puntualidad |
| Q12 | - |  |  | SI | Ausentabilidad (en caso de no presentar faltas la ... |
| Q13 | - |  |  | SI | Tolerancia a la frustración (Como califica la acti... |
| Q14 | - |  |  | SI | Iniciativa |
| Q15 | - |  |  | SI | Como califica la motivación del trabajador hacia l... |
| Q16 | - |  |  | SI | Como califica la relación del trabajador con compa... |
| Q17 | - |  |  | SI | Como califica la relación del trabajador con su je... |
| Q18 | - |  |  | SI | Presentacion personal |
| Q19 | - |  |  | SI | Independencia en el desempeño de su trabajo |
| Q20 | - |  |  | SI | Observaciones |
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