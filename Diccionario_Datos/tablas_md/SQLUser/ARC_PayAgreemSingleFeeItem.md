# SQLUser.ARC_PayAgreemSingleFeeItem

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SF_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| Q01 | - |  |  | SI | Fecha Creación |
| Q02 | - |  |  | SI | Hora Creación |
| Q03 | - |  |  | SI | Prioridad Apoyo |
| Q04 | - |  |  | SI | Celular |
| Q05 | - |  |  | SI | Puntaje a Famlia |
| Q06 | - |  |  | SI | Clasificación |
| Q07 | - |  |  | SI | Participación grupo autoayuda |
| Q08 | - |  |  | SI | Otros Grupos / Instituciones o Grupos |
| Q09 | - |  |  | SI | Apoyo |
| Q10 | - |  |  | SI | Beneficios Programa Social |
| Q11 | - |  |  | SI | Descripción de estos |
| Q12 | - |  |  | SI | Comentarios |
| Q13 | - |  |  | SI | Mapa de Red |
| Q13TxtOnly | - |  |  | SI | Mapa de Red Plain Text Only |
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
| SF_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| SF_Childsub | double |  |  | NO | Childsub |
| SF_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SF_CreatedDate | date |  |  | SI | Created Date |
| SF_CreatedTime | time |  |  | SI | Created Time |
| SF_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SF_RowId | varchar |  |  | NO | - |
| SF_UpdatedDate | date |  |  | SI | Updated Date |
| SF_UpdatedTime | time |  |  | SI | Updated Time |
| SF_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*