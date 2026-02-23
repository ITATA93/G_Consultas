# SQLUser.MHC_DetTypeOutcomeType

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTC_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| OUTC_Childsub | double |  |  | NO | Childsub |
| OUTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OUTC_CreatedDate | date |  |  | SI | Created Date |
| OUTC_CreatedTime | time |  |  | SI | Created Time |
| OUTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OUTC_OutcomeType_DR | bigint |  | FK | SI | Des Ref MHCDetentionOutcome |
| OUTC_RowId | varchar |  |  | NO | - |
| OUTC_UpdatedDate | date |  |  | SI | Updated Date |
| OUTC_UpdatedTime | time |  |  | SI | Updated Time |
| OUTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Sin Alternaciones |
| Q03 | - |  |  | SI | Disnea |
| Q04 | - |  |  | SI | Detalle |
| Q05 | - |  |  | SI | Tiraje |
| Q06 | - |  |  | SI | Ruidos Respiratorios |
| Q07 | - |  |  | SI | Tos |
| Q08 | - |  |  | SI | Secreciones |
| Q09 | - |  |  | SI | Detalle |
| Q10 | - |  |  | SI | No Expectoracion |
| Q11 | - |  |  | SI | Tabaquismo |
| Q12 | - |  |  | SI | cig/dia |
| Q13 | - |  |  | SI | Traqueotomia |
| Q14 | - |  |  | SI | Oxigenoterapia |
| Q15 | - |  |  | SI | Detalle |
| Q16 | - |  |  | SI | Diagnostico 1 |
| Q17 | - |  |  | SI | Diagnostico 2 |
| Q18 | - |  |  | SI | Conclusion |
| Q19 | - |  |  | SI | Dificultad Respiratoria |
| Q20 | - |  |  | SI | Tipo Tos |
| Q21 | - |  |  | SI | Tipo Secreción |
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