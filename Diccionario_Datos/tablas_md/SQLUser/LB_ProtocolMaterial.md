# SQLUser.LB_ProtocolMaterial

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBPTM_ParRef | bigint | PK |  | NO | Parent Reference |
| LBPTM_AddOnBy_DR | bigint |  | FK | SI | User who add unplanned |
| LBPTM_AddOnDate | date |  |  | SI | Add-on Date
Date when procedure was added unplann... |
| LBPTM_AddOnTime | time |  |  | SI | Add-on Time
Time when procedure was added unplann... |
| LBPTM_Billable | varchar |  |  | SI | Billable Flag
Indicates that this material is bil... |
| LBPTM_CompletedBy_DR | bigint |  | FK | SI | User who completed |
| LBPTM_CompletedDate | date |  |  | SI | Completed Date
Date when material was completed |
| LBPTM_CompletedTime | time |  |  | SI | Completed Time
Time when material was completed |
| LBPTM_Disposed | bit |  |  | SI | Disposed Flag |
| LBPTM_LabSite_DR | bigint |  | FK | SI | Lab site of the protocol material |
| LBPTM_MaterialNumber | varchar |  |  | SI | Material Number |
| LBPTM_Material_DR | bigint |  | FK | SI | Observations
Material |
| LBPTM_Planned | bit |  |  | SI | Planned
Is this material part of the configured p... |
| LBPTM_Printed | bit |  |  | SI | Printed
Is this material printed |
| LBPTM_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material CT Reference
Can only be used f... |
| LBPTM_ReferralLab_DR | bigint |  | FK | SI | Referral Lab Site for protocol material |
| LBPTM_RowID | varchar |  |  | NO | - |
| LBPTM_Source_DR | varchar |  | FK | SI | Source Procedure |
| LBPTM_Status | varchar |  |  | SI | Status |
| LBPTM_StorageDate | date |  |  | SI | Date Of Storage Change (Stored/Disposed/Not in Sto... |
| LBPTM_StorageTime | time |  |  | SI | Time Of Storage Change (Stored/Disposed/Not in Sto... |
| LBPTM_StoredBy_DR | bigint |  | FK | SI | User Who done Storage Change |
| LBPTM_TestSetItems | varchar |  |  | SI | Linked test set items
Results sent for this mater... |
| LBPTM_WorkArea_DR | bigint |  | FK | SI | - |
| ProtocolSequence | numeric |  |  | SI | - |
| Q01 | - |  |  | SI | Objetivo Registro |
| Q02 | - |  |  | SI | Autonomo |
| Q03 | - |  |  | SI | Total |
| Q04 | - |  |  | SI | Parcial |
| Q05 | - |  |  | SI | Se adapta bien a los cambios de temperatura |
| Q06 | - |  |  | SI | Conducta ante la fiebre |
| Q08 | - |  |  | SI | Diagnostico 1 |
| Q09 | - |  |  | SI | Diagnostico 2 |
| Q10 | - |  |  | SI | Conclusion |
| Q11 | - |  |  | SI | Temperatura |
| Q12 | - |  |  | SI | Mantiene Temperatura |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*