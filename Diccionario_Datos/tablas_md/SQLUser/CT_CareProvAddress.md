# SQLUser.CT_CareProvAddress

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Profesionales**. Médicos y personal de salud.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADDR_ParRef | varchar | PK |  | NO | CT_CareProv Parent Reference |
| ADDR_Address1 | varchar |  |  | SI | Address1 |
| ADDR_Address2 | varchar |  |  | SI | Address2 |
| ADDR_BestContactTime | varchar |  |  | SI | BestContactTime |
| ADDR_Childsub | double |  |  | NO | Childsub |
| ADDR_ContactFirstOn | varchar |  |  | SI | ContactFirstOn |
| ADDR_CreatedDate | date |  |  | SI | Created Date |
| ADDR_CreatedTime | time |  |  | SI | Created Time |
| ADDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADDR_DateFrom | date |  |  | SI | DateFrom |
| ADDR_DateTo | date |  |  | SI | DateTo |
| ADDR_Email | varchar |  |  | SI | Email |
| ADDR_Fax | varchar |  |  | SI | Fax |
| ADDR_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ADDR_Mobile | varchar |  |  | SI | Mobile |
| ADDR_Pager | varchar |  |  | SI | Pager |
| ADDR_Phone | varchar |  |  | SI | Phone |
| ADDR_Postcode_DR | bigint |  | FK | SI | Des Ref Postcode |
| ADDR_PrefConMethod | varchar |  |  | SI | PrefConMethod |
| ADDR_PrefMethod | varchar |  |  | SI | PrefMethod |
| ADDR_ProvNumber | varchar |  |  | SI | ProvNumber |
| ADDR_RowId | varchar |  |  | NO | - |
| ADDR_State_DR | bigint |  | FK | SI | Des Ref State |
| ADDR_Suburb_DR | bigint |  | FK | SI | Des Ref Suburb |
| ADDR_Type | varchar |  |  | SI | Type |
| ADDR_UpdatedDate | date |  |  | SI | Updated Date |
| ADDR_UpdatedTime | time |  |  | SI | Updated Time |
| ADDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Fecha |
| Q02 | - |  |  | SI | Hora |
| Q03 | - |  |  | SI | Usuario |
| Q04 | - |  |  | SI | Estado |
| Q05 | - |  |  | SI | Paciente |
| Q06 | - |  |  | SI | Recurso |
| Q07 | - |  |  | SI | Local |
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