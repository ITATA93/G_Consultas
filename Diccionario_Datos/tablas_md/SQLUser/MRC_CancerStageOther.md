# SQLUser.MRC_CancerStageOther

**Schema:** SQLUser
**Columnas:** 80
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OTH_ParRef | bigint | PK |  | NO | Parent Reference |
| CQ01 | - |  |  | SI | (null) |
| CQ02 | - |  |  | SI | (null) |
| CQ03 | - |  |  | SI | (null) |
| CQ04 | - |  |  | SI | (null) |
| CQ05 | - |  |  | SI | (null) |
| CQ06 | - |  |  | SI | (null) |
| CQ07 | - |  |  | SI | (null) |
| CQ08 | - |  |  | SI | (null) |
| CQ09 | - |  |  | SI | (null) |
| CQ10 | - |  |  | SI | (null) |
| OTH_Childsub | double |  |  | NO | Childsub |
| OTH_CodeTableTags | varchar |  |  | SI | List of Code Table Tags |
| OTH_CreatedDate | date |  |  | SI | Created Date |
| OTH_CreatedTime | time |  |  | SI | Created Time |
| OTH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OTH_DateFrom | date |  |  | SI | Date From |
| OTH_DateTo | date |  |  | SI | Date To |
| OTH_Desc | varchar |  |  | SI | Description |
| OTH_RowId | varchar |  |  | NO | - |
| OTH_Stage | varchar |  |  | SI | Stage |
| OTH_UpdatedDate | date |  |  | SI | Updated Date |
| OTH_UpdatedTime | time |  |  | SI | Updated Time |
| OTH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Comer |
| Q02 | - |  |  | SI | Lavarse |
| Q03 | - |  |  | SI | Vestirse |
| Q04 | - |  |  | SI | Arreglarse |
| Q05 | - |  |  | SI | Deposiciones (Valorese la semana previa) |
| Q06 | - |  |  | SI | Micción (Valorese la semana previa) |
| Q07 | - |  |  | SI | Usar el Retrete |
| Q08 | - |  |  | SI | Trasladarse |
| Q09 | - |  |  | SI | Deambular |
| Q10 | - |  |  | SI | Escalones |
| Q11 | - |  |  | SI | Puntaje |
| Q13 | - |  |  | SI | Resultado Indice Barthel |
| Q13ObsDR | - |  |  | SI | Resultado Indice Barthel DR |
| Q14 | - |  |  | SI | Fecha de Realización |
| Q15 | - |  |  | SI | Hora de Realización |
| Q16 | - |  |  | SI | Fecha/Hora de Realización |
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