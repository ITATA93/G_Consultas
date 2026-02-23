# SQLUser.CT_RefClin

**Schema:** SQLUser
**Columnas:** 63
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTRFC_RowId | bigint | PK |  | NO | - |
| CTRFC_ActiveFlag | varchar |  |  | NO | Active Flag |
| CTRFC_Code | varchar |  |  | NO | Referral Clinic Code |
| CTRFC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTRFC_CreatedDate | date |  |  | SI | Created Date |
| CTRFC_CreatedTime | time |  |  | SI | Created Time |
| CTRFC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTRFC_DateFrom | date |  |  | SI | Date From |
| CTRFC_DateTo | date |  |  | SI | Date To |
| CTRFC_Desc | varchar |  |  | NO | Referral Clinic Description |
| CTRFC_FiscalCode | varchar |  |  | SI | Fiscal Code |
| CTRFC_Owner | varchar |  |  | SI | Owner |
| CTRFC_UpdatedDate | date |  |  | SI | Updated Date |
| CTRFC_UpdatedTime | time |  |  | SI | Updated Time |
| CTRFC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| CTRFC_VEMD | varchar |  |  | SI | VEMD |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient has used aluminium chloride hexahydrate de... |
| Q04 | - |  |  | SI | Aluminium chloride hexahydrate deodorant has been ... |
| Q05 | - |  |  | SI | Minimum of 4 months since the last injection |
| Q06 | - |  |  | SI | How long was the patient sweat free after their la... |
| Q07 | - |  |  | SI | Additional notes |
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