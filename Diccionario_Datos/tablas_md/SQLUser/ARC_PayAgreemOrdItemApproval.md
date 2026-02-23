# SQLUser.ARC_PayAgreemOrdItemApproval

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OIAPPR_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| OIAPPR_BillingGroups | varchar |  |  | SI | Billing Groups |
| OIAPPR_BillingSubgroups | varchar |  |  | SI | Billing Subgroups |
| OIAPPR_Childsub | double |  |  | NO | Childsub |
| OIAPPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OIAPPR_CreatedDate | date |  |  | SI | Created Date |
| OIAPPR_CreatedTime | time |  |  | SI | Created Time |
| OIAPPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OIAPPR_DateFrom | date |  |  | SI | Date From |
| OIAPPR_DateTo | date |  |  | SI | Date To |
| OIAPPR_DischBillingGroups | varchar |  |  | SI | Discharge Billing Groups |
| OIAPPR_DischBillingSubgroups | varchar |  |  | SI | Discharge Billing Subgroups |
| OIAPPR_DischargeMed | varchar |  |  | SI | [DEPRECATED]Replaced by OIAPPRDischBillingGroups,O... |
| OIAPPR_EpisodeType | varchar |  |  | SI | Episode Type |
| OIAPPR_MinimumDuration | integer |  |  | SI | Minimum Duration (Days) |
| OIAPPR_OrderSet | varchar |  |  | SI | Order Set |
| OIAPPR_Rank | double |  |  | SI | Rank |
| OIAPPR_RowId | varchar |  |  | NO | - |
| OIAPPR_UpdatedDate | date |  |  | SI | Updated Date |
| OIAPPR_UpdatedTime | time |  |  | SI | Updated Time |
| OIAPPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Profundidad de las Quemaduras |
| Q02 | - |  |  | SI | Destrucción de la Piel |
| Q03 | - |  |  | SI | Aspecto Clínico |
| Q04 | - |  |  | SI | Dolor |
| Q05 | - |  |  | SI | Evolución |
| Q06 | - |  |  | SI | Curación por |
| Q07 | - |  |  | SI | Resultado estético |
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