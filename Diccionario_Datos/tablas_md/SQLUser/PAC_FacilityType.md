# SQLUser.PAC_FacilityType

**Schema:** SQLUser
**Columnas:** 78
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FACIL_RowId | bigint | PK |  | NO | - |
| FACIL_Code | varchar |  |  | NO | Code |
| FACIL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FACIL_CreatedDate | date |  |  | SI | Created Date |
| FACIL_CreatedTime | time |  |  | SI | Created Time |
| FACIL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FACIL_DateFrom | date |  |  | SI | Date From |
| FACIL_DateTo | date |  |  | SI | Date To |
| FACIL_Desc | varchar |  |  | NO | Description |
| FACIL_MaxItemsPerRx | integer |  |  | SI | Maximum number of items on a prescription |
| FACIL_Owner | varchar |  |  | SI | Owner |
| FACIL_UpdatedDate | date |  |  | SI | Updated Date |
| FACIL_UpdatedTime | time |  |  | SI | Updated Time |
| FACIL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Stage of assessment |
| Q04 | - |  |  | SI | Upper limb affected |
| Q05 | - |  |  | SI | Weight bearing - lower limb right |
| Q06 | - |  |  | SI | Weight bearing - lower limb left |
| Q07 | - |  |  | SI | Gait aid |
| Q08 | - |  |  | SI | Other aid |
| Q09 | - |  |  | SI | Level of assistance required |
| Q10 | - |  |  | SI | Equipment required |
| Q11 | - |  |  | SI | Other equipment |
| Q12 | - |  |  | SI | Method of transfer |
| Q13 | - |  |  | SI | Other method |
| Q14 | - |  |  | SI | Number of staff required |
| Q15 | - |  |  | SI | Level of assistance |
| Q16 | - |  |  | SI | Equipment |
| Q17 | - |  |  | SI | Other equipment |
| Q18 | - |  |  | SI | Number of staff required |
| Q19 | - |  |  | SI | Level of assistance |
| Q20 | - |  |  | SI | Equipment |
| Q21 | - |  |  | SI | Number of staff required |
| Q22 | - |  |  | SI | Level of assistance |
| Q23 | - |  |  | SI | Number of staff required |
| Q24 | - |  |  | SI | Level of assistance |
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