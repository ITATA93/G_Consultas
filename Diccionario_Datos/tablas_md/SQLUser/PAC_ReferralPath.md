# SQLUser.PAC_ReferralPath

**Schema:** SQLUser
**Columnas:** 86
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFPATH_RowId | bigint | PK |  | NO | - |
| ChildQ22DR | - |  |  | SI | Child Reference: PEG assessment |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Insertion Record |
| Q04 | - |  |  | SI | Date of insertion |
| Q05 | - |  |  | SI | Time of insertion |
| Q06 | - |  |  | SI | Insertion reason |
| Q07 | - |  |  | SI | Other indication reason |
| Q08 | - |  |  | SI | Procedure method |
| Q09 | - |  |  | SI | Radiological insertion method |
| Q10 | - |  |  | SI | Insertion site |
| Q11 | - |  |  | SI | Type |
| Q12 | - |  |  | SI | Brand / Size |
| Q13 | - |  |  | SI | Flange to skin (cm) |
| Q14 | - |  |  | SI | Balloon volume (mls) |
| Q15 | - |  |  | SI | Aseptic technique used with appropriate skin prepa... |
| Q16 | - |  |  | SI | External fixation plate placed and secure |
| Q17 | - |  |  | SI | Dressing applied and secure |
| Q18 | - |  |  | SI | Position confirmed |
| Q19 | - |  |  | SI | Other position confirmation notes |
| Q20 | - |  |  | SI | Inserted by |
| Q21 | - |  |  | SI | PEG Assessment |
| Q23 | - |  |  | SI | Removal Record |
| Q24 | - |  |  | SI | Date |
| Q25 | - |  |  | SI | Time |
| Q26 | - |  |  | SI | Removal reason |
| Q27 | - |  |  | SI | Other removal reason |
| Q28 | - |  |  | SI | Removed by |
| Q29 | - |  |  | SI | Complications |
| Q30 | - |  |  | SI | Complications |
| Q31 | - |  |  | SI | Other complications notes |
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
| REFPATH_Code | varchar |  |  | NO | Code |
| REFPATH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFPATH_CreatedDate | date |  |  | SI | Created Date |
| REFPATH_CreatedTime | time |  |  | SI | Created Time |
| REFPATH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFPATH_DateFrom | date |  |  | SI | Date From |
| REFPATH_DateTo | date |  |  | SI | Date To |
| REFPATH_Desc | varchar |  |  | NO | Description |
| REFPATH_NationalCode | varchar |  |  | SI | National Code |
| REFPATH_Owner | varchar |  |  | SI | Owner |
| REFPATH_Subregion_DR | bigint |  | FK | SI | Subregion |
| REFPATH_UpdatedDate | date |  |  | SI | Updated Date |
| REFPATH_UpdatedTime | time |  |  | SI | Updated Time |
| REFPATH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*