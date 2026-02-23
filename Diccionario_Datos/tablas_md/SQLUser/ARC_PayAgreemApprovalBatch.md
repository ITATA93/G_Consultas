# SQLUser.ARC_PayAgreemApprovalBatch

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APPRBCH_ParRef | bigint | PK |  | NO | ARC_PaymentAgreement Parent Reference |
| APPRBCH_BillingGroups | varchar |  |  | SI | Billing Groups |
| APPRBCH_BillingSubgroups | varchar |  |  | SI | Billing Subgroups |
| APPRBCH_Childsub | double |  |  | NO | Childsub |
| APPRBCH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APPRBCH_CreatedDate | date |  |  | SI | Created Date |
| APPRBCH_CreatedTime | time |  |  | SI | Created Time |
| APPRBCH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APPRBCH_DateFrom | date |  |  | SI | Date From |
| APPRBCH_DateTo | date |  |  | SI | Date To |
| APPRBCH_EpisodeType | varchar |  |  | SI | Episode Type |
| APPRBCH_GroupRequestDesc_DR | bigint |  | FK | NO | Des Ref BLCApprGroupRequestDescription - Approval ... |
| APPRBCH_Rank | double |  |  | SI | Rank |
| APPRBCH_RowId | varchar |  |  | NO | - |
| APPRBCH_UpdatedDate | date |  |  | SI | Updated Date |
| APPRBCH_UpdatedTime | time |  |  | SI | Updated Time |
| APPRBCH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Musculatura facial |
| Q02 | - |  |  | SI | Tranquilidad |
| Q03 | - |  |  | SI | Tono muscular* |
| Q04 | - |  |  | SI | Respuesta verbal** |
| Q05 | - |  |  | SI | Confortabilidad |
| Q06 | - |  |  | SI | Puntuación Escala de Campbell |
| Q07 | - |  |  | SI | *En caso de lesión medular o hemiplejía valorar el... |
| Q08 | - |  |  | SI | **Puede ser poco valorable en vía aérea artificial |
| Q09 | - |  |  | SI | La puntuación ideal es mantenerlo en 3 o menos |
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