# SQLUser.CT_InternatAgreem

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INAG_RowId | bigint | PK |  | NO | - |
| INAG_Code | varchar |  |  | NO | Code |
| INAG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INAG_Country_DR | bigint |  | FK | SI | Des Ref Country |
| INAG_CreatedDate | date |  |  | SI | Created Date |
| INAG_CreatedTime | time |  |  | SI | Created Time |
| INAG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INAG_Desc | varchar |  |  | NO | Description |
| INAG_Owner | varchar |  |  | SI | Owner |
| INAG_UpdatedDate | date |  |  | SI | Updated Date |
| INAG_UpdatedTime | time |  |  | SI | Updated Time |
| INAG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | (C) Caudate |
| Q02 | - |  |  | SI | (I) Insular Ribbon |
| Q03 | - |  |  | SI | (IC) Internal Capsule |
| Q04 | - |  |  | SI | (L) Lentiform nucleus |
| Q05 | - |  |  | SI | (MCA1) Anterior MCA cortex |
| Q06 | - |  |  | SI | (MCA2) MCA cortex lateral to the insular ribbon |
| Q07 | - |  |  | SI | (MCA3) Posterior MCA cortex |
| Q08 | - |  |  | SI | (MCA4) Anterior cortex immediately rostal to M1 |
| Q09 | - |  |  | SI | (MCA5) Lateral cortex immediately rostal to M3 |
| Q10 | - |  |  | SI | (MCA6) Posterior cortex immediately rostal to M3 |
| Q11 | - |  |  | SI | 95% prob of survial if ASPECTS >7 |
| Q12 | - |  |  | SI | 90% prob of poor outcome if ASPECTS <7 |
| Q13 | - |  |  | SI | 95% probability of survival |
| Q14 | - |  |  | SI | 99% probability of no SICH |
| Q15 | - |  |  | SI | Score 0 - 7 |
| Q16 | - |  |  | SI | Score 8 - 10 |
| Q17 | - |  |  | SI | 90% probability of poor outcome |
| Q18 | - |  |  | SI | Subcortical Structures |
| Q19 | - |  |  | SI | MCA Cortex |
| Q20 | - |  |  | SI | ASPECTS  is a 10-point quantitative topographic CT... |
| Q21 | - |  |  | SI | Segmental assessment of the MCA vascular territory... |
| Q22 | - |  |  | SI | No ischaemia in the MCA territory would score 10 &... |
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