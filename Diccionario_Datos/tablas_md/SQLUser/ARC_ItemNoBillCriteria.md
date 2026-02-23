# SQLUser.ARC_ItemNoBillCriteria

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NBCR_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| NBCR_Childsub | double |  |  | NO | Childsub |
| NBCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| NBCR_CreatedDate | date |  |  | SI | Created Date |
| NBCR_CreatedTime | time |  |  | SI | Created Time |
| NBCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| NBCR_DateFrom | date |  |  | NO | Date From |
| NBCR_DateTo | date |  |  | SI | Date To |
| NBCR_EpisodeType | varchar |  |  | SI | Episode Type |
| NBCR_Epissubtype_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| NBCR_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| NBCR_Location_DR | bigint |  | FK | SI | Des Ref CTLoc |
| NBCR_RowId | varchar |  |  | NO | - |
| NBCR_UpdatedDate | date |  |  | SI | Updated Date |
| NBCR_UpdatedTime | time |  |  | SI | Updated Time |
| NBCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Terminar |
| Q02 | - |  |  | SI | Iniciar |
| Q03 | - |  |  | SI | Motivo de Aislamiento |
| Q04 | - |  |  | SI | Fecha de Inicio |
| Q05 | - |  |  | SI | Hora de Inicio |
| Q06 | - |  |  | SI | Fecha de Término |
| Q07 | - |  |  | SI | Hora de Término |
| Q08 | - |  |  | SI | Observaciones |
| Q09 | - |  |  | SI | Responsable |
| Q10 | - |  |  | SI | Responsable |
| Q11 | - |  |  | SI | Comentarios Retiro |
| Q12 | - |  |  | SI | Servicio/Unidad |
| Q13 | - |  |  | SI | Lugar Temporal |
| Q14 | - |  |  | SI | Motivo de Término Aislamiento |
| Q15 | - |  |  | SI | Aislamiento Indicado |
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