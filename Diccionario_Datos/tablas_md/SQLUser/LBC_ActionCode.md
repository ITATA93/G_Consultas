# SQLUser.LBC_ActionCode

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAC_RowID | bigint | PK |  | NO | - |
| ChildQ20DR | - |  |  | SI | Child Reference: Congenital heart disease screenin... |
| LBCAC_Code | varchar |  |  | NO | Code |
| LBCAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAC_CreatedDate | date |  |  | SI | Created Date |
| LBCAC_CreatedTime | time |  |  | SI | Created Time |
| LBCAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAC_DateFrom | date |  |  | SI | Date Active From |
| LBCAC_DateTo | date |  |  | SI | Date Active To |
| LBCAC_Desc | varchar |  |  | NO | Description |
| LBCAC_LabAction | varchar |  |  | SI | Laboratory Action |
| LBCAC_Owner | varchar |  |  | SI | Owner |
| LBCAC_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAC_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Age at initial screening (hours) |
| Q04 | - |  |  | SI | Clinical assessment notes |
| Q05 | - |  |  | SI | Signature of screener |
| Q05UDt | - |  |  | SI | Signature of screener Last Updated Date |
| Q05UTm | - |  |  | SI | Signature of screener Last Updated Time |
| Q06 | - |  |  | SI | If pulse oxygen saturation is <90% in either the h... |
| Q07 | - |  |  | SI | If pulse oxygen saturation are <95% in both the ha... |
| Q08 | - |  |  | SI | If pulse oxygen saturations are ≥95% in either ext... |
| Q15 | - |  |  | SI | Name  of screener |
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