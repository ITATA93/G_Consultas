# SQLUser.AR_PrelimBatchComm

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PBCMT_ParRef | bigint | PK |  | NO | AR_PrelimBatch Parent Reference |
| PBCMT_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL - Not Used |
| PBCMT_BatchStatus | varchar |  |  | SI | Batch Status At the time comment was entered. |
| PBCMT_Childsub | double |  |  | NO | Childsub |
| PBCMT_Comments | varchar |  |  | SI | Comments |
| PBCMT_Date | date |  |  | SI | Date |
| PBCMT_FutureDate | date |  |  | SI | Future Date |
| PBCMT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| PBCMT_LastUpdateDate | date |  |  | SI | LastUpateDate |
| PBCMT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| PBCMT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| PBCMT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| PBCMT_OnHold | varchar |  |  | SI | OnHold |
| PBCMT_RowId | varchar |  |  | NO | - |
| PBCMT_ShortDesc | varchar |  |  | SI | Short Description |
| PBCMT_Time | time |  |  | SI | Time |
| PBCMT_User_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Fecha Evaluación |
| Q02 | - |  |  | SI | Hora Evaluación |
| Q03 | - |  |  | SI | PREGUNTA SORPRESA: Se sorprendería si esta persona... |
| Q04 | - |  |  | SI | NECESIDADES PALIATIVAS: La persona, los profesiona... |
| Q05 | - |  |  | SI | PÉRDIDA FUNCIONAL: Impresión clínica de deterioro ... |
| Q06 | - |  |  | SI | PÉRDIDA NUTRICIONAL: Impresión clínica de deterior... |
| Q07 | - |  |  | SI | MULTI-MORLIDITAT: &gt |
| Q08 | - |  |  | SI | USO DE RECURSOS: &gt |
| Q09 | - |  |  | SI | ENFERMEDAD AVANZADA: Criterios de severidad y/o pr... |
| Q10 | - |  |  | SI | Comentarios |
| Q11 | - |  |  | SI | Resultado Necpal |
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