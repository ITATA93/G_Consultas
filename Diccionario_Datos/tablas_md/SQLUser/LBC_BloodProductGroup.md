# SQLUser.LBC_BloodProductGroup

**Schema:** SQLUser
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCBPG_RowID | bigint | PK |  | NO | - |
| LBCBPG_ApplyABORhCheck | varchar |  |  | SI | Apply ABO / Rh Suitability Check |
| LBCBPG_ApplyAntibodyAntigenCheck | varchar |  |  | SI | Apply Blood Group Antibody / Antigen Compatibility... |
| LBCBPG_BloodIssueReportGroup_DR | bigint |  | FK | SI | Blood Issue Report Group |
| LBCBPG_Code | varchar |  |  | NO | Code |
| LBCBPG_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCBPG_Comment | varchar |  |  | SI | Comment |
| LBCBPG_ConditionallyDisableControlledIssue | varchar |  |  | SI | Determines whether to disable controlled issue in ... |
| LBCBPG_ControlledIssue | varchar |  |  | SI | Enables controlled issue for the blood product gro... |
| LBCBPG_CreatedDate | date |  |  | SI | Created Date |
| LBCBPG_CreatedTime | time |  |  | SI | Created Time |
| LBCBPG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCBPG_CrossmatchRequired | varchar |  |  | SI | Requires crossmatch |
| LBCBPG_DateFrom | date |  |  | SI | Effective date for the record |
| LBCBPG_DateTo | date |  |  | SI | Last day the record is active |
| LBCBPG_DefaultReservationPeriod | integer |  |  | SI | Default reservation period |
| LBCBPG_DefaultReservationPeriodUnit | varchar |  |  | SI | Default reservation period unit |
| LBCBPG_Desc | varchar |  |  | NO | Description |
| LBCBPG_DoseBased | varchar |  |  | SI | Dose based |
| LBCBPG_EmergencyDisableLabelVerification | varchar |  |  | SI | Disable Label Verification in Emergency or Uncross... |
| LBCBPG_EmergencyIssueBloodGroups | varchar |  |  | SI | Donation Blood Groups Allowed for Emergency Issue |
| LBCBPG_ExpirationChangeOnAuthorisation | varchar |  |  | SI | Whether the expiration date/time changes upon auth... |
| LBCBPG_Instructions | longvarchar |  |  | SI | Instructions
HTMLRichText |
| LBCBPG_IssueComment | longvarchar |  |  | SI | Issue Comment
HTMLRichText |
| LBCBPG_LabBloodIssueLabelReportGroup_DR | bigint |  | FK | SI | Only the Report linked to this Report Group will b... |
| LBCBPG_LabelVerification | varchar |  |  | SI | Label Verification In Use |
| LBCBPG_LifespanAfterAuthorisation | integer |  |  | SI | Lifespan after authorisation in the case of expira... |
| LBCBPG_LifespanAfterAuthorisationUnit | varchar |  |  | SI | Lifespan after authorisation unit in the case of e... |
| LBCBPG_MinTimeToExp | varchar |  |  | SI | Minimum time to expiry to allow issue |
| LBCBPG_MinTimeToExpUnit | varchar |  |  | SI | Minimum time to expiry to allow issue unit |
| LBCBPG_Owner | varchar |  |  | SI | Owner |
| LBCBPG_ThawConceptsApply | varchar |  |  | SI | Thaw Concepts Apply. Enables Thaw Start and End da... |
| LBCBPG_TransfusionEvent | varchar |  |  | SI | Constitutes a transfusion event
Transfusion a uni... |
| LBCBPG_UOM_DR | bigint |  | FK | SI | Units of measurement |
| LBCBPG_UpdatedDate | date |  |  | SI | Updated Date |
| LBCBPG_UpdatedTime | time |  |  | SI | Updated Time |
| LBCBPG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Date of sleep study |
| Q04 | - |  |  | SI | Apnoea-Hypopnoea Index at time of sleep study |
| Q05 | - |  |  | SI | Funding type |
| Q06 | - |  |  | SI | Type of prescription |
| Q07 | - |  |  | SI | Pressure delivery method |
| Q08 | - |  |  | SI | Equipment required |
| Q09 | - |  |  | SI | CPAP range (cm H2O) |
| Q10 | - |  |  | SI | to |
| Q11 | - |  |  | SI | CPAP (cm H2O) |
| Q12 | - |  |  | SI | Fixed pressure CPAP of (cm H2O) |
| Q13 | - |  |  | SI | Current pressure (cm H2O) |
| Q14 | - |  |  | SI | Change to new pressure (cm H2O) |
| Q15 | - |  |  | SI | Method of support |
| Q16 | - |  |  | SI | Expired positive airway pressure min (cm H2O) |
| Q17 | - |  |  | SI | Expired positive airway pressure max (cm H2O) |
| Q18 | - |  |  | SI | Inspired positive airway pressure min (cm H2O) |
| Q19 | - |  |  | SI | Inspired positive airway pressure max (cm H2O) |
| Q20 | - |  |  | SI | Back up rate |
| Q21 | - |  |  | SI | Back up rate breaths per minute |
| Q22 | - |  |  | SI | Inspiratory time (sec) |
| Q23 | - |  |  | SI | Settings |
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