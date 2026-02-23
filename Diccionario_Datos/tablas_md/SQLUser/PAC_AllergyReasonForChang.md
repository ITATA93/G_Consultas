# SQLUser.PAC_AllergyReasonForChang

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALRFC_RowId | bigint | PK |  | NO | - |
| ALRFC_Code | varchar |  |  | NO | Code |
| ALRFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALRFC_CreatedDate | date |  |  | SI | Created Date |
| ALRFC_CreatedTime | time |  |  | SI | Created Time |
| ALRFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALRFC_DateFrom | date |  |  | SI | Date From |
| ALRFC_DateTo | date |  |  | SI | Date To |
| ALRFC_Desc | varchar |  |  | NO | Description |
| ALRFC_Owner | varchar |  |  | SI | Owner |
| ALRFC_UpdatedDate | date |  |  | SI | Updated Date |
| ALRFC_UpdatedTime | time |  |  | SI | Updated Time |
| ALRFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Respiratory equipment funding supplied by |
| Q04 | - |  |  | SI | Other funding |
| Q05 | - |  |  | SI | Equipment supplied by |
| Q06 | - |  |  | SI | Other supplier |
| Q07 | - |  |  | SI | Equipment Available / In Use |
| Q08 | - |  |  | SI | Portable concentrator |
| Q09 | - |  |  | SI | Type |
| Q10 | - |  |  | SI | Electricity generator |
| Q11 | - |  |  | SI | Nebuliser |
| Q12 | - |  |  | SI | Non invasive therapy (continuous positive airway p... |
| Q13 | - |  |  | SI | Prevention and Plans |
| Q14 | - |  |  | SI | Treatment plan in place |
| Q15 | - |  |  | SI | Exercise plan / Rehabilitation program in place |
| Q16 | - |  |  | SI | Vaccinations up to date |
| Q17 | - |  |  | SI | Prevention and plan notes |
| Q18 | - |  |  | SI | Safety Topics Discussed |
| Q19 | - |  |  | SI | Reinforce / Discuss the following safety issues at... |
| Q20 | - |  |  | SI | If smoking noted, notify respiratory nurse immedia... |
| Q21 | - |  |  | SI | Trip hazard from oxygen tubing |
| Q22 | - |  |  | SI | Fire risk from naked flames |
| Q23 | - |  |  | SI | Including candles, cigarettes, matches, lighters, ... |
| Q24 | - |  |  | SI | No oil based products |
| Q25 | - |  |  | SI | Use only water based products on face, nose |
| Q26 | - |  |  | SI | Single socket power cords for concentrator |
| Q27 | - |  |  | SI | Do not use double adaptors or extension cords |
| Q28 | - |  |  | SI | Safety notes |
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