# SQLUser.CT_Title

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TTL_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Assessed by	 |
| Q02 | - |  |  | SI | Date assessed	 |
| Q03 | - |  |  | SI | Aerobic activity completed	 |
| Q03ObsDR | - |  |  | SI | Aerobic activity completed	 DR |
| Q04 | - |  |  | SI | Borg 20 Point Scale	 |
| Q04ObsDR | - |  |  | SI | Borg 20 Point Scale	 DR |
| Q05 | - |  |  | SI | Borg RPE scale® |
| Q05ObsDR | - |  |  | SI | Borg RPE scale® DR |
| Q06 | - |  |  | SI | Date |
| Q07 | - |  |  | SI | Time |
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
| TTL_Code | varchar |  |  | NO | Code |
| TTL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TTL_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| TTL_CreatedDate | date |  |  | SI | Created Date |
| TTL_CreatedTime | time |  |  | SI | Created Time |
| TTL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TTL_DateFrom | date |  |  | SI | Date From |
| TTL_DateTo | date |  |  | SI | Date To |
| TTL_Desc | varchar |  |  | NO | Description |
| TTL_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| TTL_Owner | varchar |  |  | SI | Owner |
| TTL_UpdatedDate | date |  |  | SI | Updated Date |
| TTL_UpdatedTime | time |  |  | SI | Updated Time |
| TTL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*