# SQLUser.PAC_RefTreatPathCompleteReason

**Schema:** SQLUser
**Columnas:** 110
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTPCR_RowId | bigint | PK |  | NO | - |
| ChildQ04DR | - |  |  | SI | Child Reference: Training details |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Training day number |
| Q05 | - |  |  | SI | Training modality |
| Q06 | - |  |  | SI | Notes |
| Q07 | - |  |  | SI | Continuous Ambulatory Peritoneal Dialysis System (... |
| Q08 | - |  |  | SI | Continuous Ambulatory Peritoneal Dialysis (CAPD) s... |
| Q09 | - |  |  | SI | Other CAPD system |
| Q10 | - |  |  | SI | Exchange |
| Q11 | - |  |  | SI | Volume drained (mL) |
| Q12 | - |  |  | SI | Fill volume (mL) |
| Q13 | - |  |  | SI | Exchange 1 |
| Q14 | - |  |  | SI | Exchange 2 |
| Q15 | - |  |  | SI | Exchange 3 |
| Q16 | - |  |  | SI | Exchange 4 |
| Q17 | - |  |  | SI | Exchange 1 |
| Q18 | - |  |  | SI | Exchange 1 - Volume drained (mL) |
| Q19 | - |  |  | SI | Exchange 1 - Fill volume (mL) |
| Q20 | - |  |  | SI | Exchange 2 |
| Q21 | - |  |  | SI | Exchange 2 - Volume drained (mL) |
| Q22 | - |  |  | SI | Exchange 2 - Fill volume (mL) |
| Q23 | - |  |  | SI | Exchange 3 |
| Q24 | - |  |  | SI | Exchange 3 - Volume drained (mL) |
| Q25 | - |  |  | SI | Exchange 3 - Fill volume (mL) |
| Q26 | - |  |  | SI | Exchange 4 |
| Q27 | - |  |  | SI | Exchange 4 - Volume drained (mL) |
| Q28 | - |  |  | SI | Exchange 4 - Fill volume (mL) |
| Q29 | - |  |  | SI | CAPD training notes |
| Q30 | - |  |  | SI | Automated Peritoneal Dialysis System (APD) |
| Q31 | - |  |  | SI | Automated Peritoneal Dialysis system |
| Q32 | - |  |  | SI | Other APD system |
| Q33 | - |  |  | SI | Number of cycles |
| Q34 | - |  |  | SI | APD - Fill volume (mL) |
| Q35 | - |  |  | SI | APD - Ultrafiltration (mL) |
| Q36 | - |  |  | SI | Glucose used |
| Q37 | - |  |  | SI | Last fill (mL) |
| Q38 | - |  |  | SI | APD training notes |
| Q39 | - |  |  | SI | Exchange 1 |
| Q40 | - |  |  | SI | Exchange 1 - Volume drained (mL) |
| Q41 | - |  |  | SI | Exchange 1 - Fill volume (mL) |
| Q42 | - |  |  | SI | Exchange 2 |
| Q43 | - |  |  | SI | Exchange 2 - Volume drained (mL) |
| Q44 | - |  |  | SI | Exchange 2 - Fill volume (mL) |
| Q45 | - |  |  | SI | Exchange 3 |
| Q46 | - |  |  | SI | Exchange 3 - Volume drained (mL) |
| Q47 | - |  |  | SI | Exchange 3 - Fill volume (mL) |
| Q48 | - |  |  | SI | Exchange 4 |
| Q49 | - |  |  | SI | Exchange 4 - Volume drained (mL) |
| Q50 | - |  |  | SI | Exchange 4 - Fill volume (mL) |
| Q51 | - |  |  | SI | Glucose used |
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
| RTPCR_Code | varchar |  |  | NO | Code |
| RTPCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTPCR_CreatedDate | date |  |  | SI | Created Date |
| RTPCR_CreatedTime | time |  |  | SI | Created Time |
| RTPCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTPCR_DateFrom | date |  |  | SI | Date From |
| RTPCR_DateTo | date |  |  | SI | Date To |
| RTPCR_DefaultPathwayComp | varchar |  |  | SI | Default Reason for Pathway Completion |
| RTPCR_DefaultStageComp | varchar |  |  | SI | Default Reason for Stage Completion |
| RTPCR_Desc | varchar |  |  | NO | Description |
| RTPCR_NationalCode | varchar |  |  | SI | National Code |
| RTPCR_Owner | varchar |  |  | SI | Owner |
| RTPCR_RTTStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| RTPCR_TreatmentPathway | varchar |  |  | SI | TreatmentPathway |
| RTPCR_TreatmentStage | varchar |  |  | SI | TreatmentStage |
| RTPCR_UpdatedDate | date |  |  | SI | Updated Date |
| RTPCR_UpdatedTime | time |  |  | SI | Updated Time |
| RTPCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*