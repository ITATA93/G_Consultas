# SQLUser.CT_LocEpisSubType

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBT_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q02 | - |  |  | SI | Sitio de Punción |
| Q03 | - |  |  | SI | N° de Punciones |
| Q04 | - |  |  | SI | Touhy N° |
| Q05 | - |  |  | SI | Punta Lápiz N° |
| Q06 | - |  |  | SI | Cateter N° |
| Q07 | - |  |  | SI | Nivel Anestésico |
| Q08 | - |  |  | SI | Calidad del Líquido Cefalo-Raquídeo |
| Q09 | - |  |  | SI | Parestesias |
| Q10 | - |  |  | SI | Descripción |
| Q11 | - |  |  | SI | Observaciones |
| Q13 | - |  |  | SI | Posición |
| QANANO | - |  |  | SI | ANANO |
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
| SUBT_Childsub | double |  |  | NO | Childsub |
| SUBT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBT_CreatedDate | date |  |  | SI | Created Date |
| SUBT_CreatedTime | time |  |  | SI | Created Time |
| SUBT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBT_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| SUBT_RowId | varchar |  |  | NO | - |
| SUBT_UpdatedDate | date |  |  | SI | Updated Date |
| SUBT_UpdatedTime | time |  |  | SI | Updated Time |
| SUBT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*