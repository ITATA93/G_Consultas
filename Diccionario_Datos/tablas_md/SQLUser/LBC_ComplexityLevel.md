# SQLUser.LBC_ComplexityLevel

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCCL_RowID | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Vital Embryo Numbers |
| LBCCL_Code | varchar |  |  | NO | Code	 |
| LBCCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCCL_ComplexityLevel | integer |  |  | SI | Complexity Level |
| LBCCL_CreatedDate | date |  |  | SI | Created Date |
| LBCCL_CreatedTime | time |  |  | SI | Created Time |
| LBCCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCCL_DateFrom | date |  |  | SI | Effective date for the record |
| LBCCL_DateTo | date |  |  | SI | Last day the record is active  |
| LBCCL_Desc | varchar |  |  | NO | Description  |
| LBCCL_Owner | varchar |  |  | SI | Owner |
| LBCCL_UpdatedDate | date |  |  | SI | Updated Date |
| LBCCL_UpdatedTime | time |  |  | SI | Updated Time |
| LBCCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Operator |
| Q03 | - |  |  | SI | Number of straws |
| Q04 | - |  |  | SI | Canister number |
| Q05 | - |  |  | SI | Pencil color |
| Q06 | - |  |  | SI | Straw tip color |
| Q07 | - |  |  | SI | Thawing |
| Q08 | - |  |  | SI | Number of embryos frozen |
| Q10 | - |  |  | SI | Number of embryos transferred |
| Q11 | - |  |  | SI | Number of embryos left |
| Q12 | - |  |  | SI | Number of straws left |
| Q13 | - |  |  | SI | Renewal date |
| Q14 | - |  |  | SI | Embryos |
| Q15 | - |  |  | SI | Date |
| Q16 | - |  |  | SI | Time |
| Q17 | - |  |  | SI | Freezing consent |
| Q18 | - |  |  | SI | Screening results checked |
| Q21 | - |  |  | SI | Embryologist |
| Q22 | - |  |  | SI | Partner's name |
| Q23 | - |  |  | SI | Location |
| Q24 | - |  |  | SI | Embryos thawed this cycle |
| Q25 | - |  |  | SI | Date |
| Q26 | - |  |  | SI | Cycle number |
| Q27 | - |  |  | SI | Egg freezing  number |
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