# SQLUser.CT_UserAppointTitle

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| USAPTL_RowId | bigint | PK |  | NO | - |
| Q00 | - |  |  | SI | View |
| Q03 | - |  |  | SI | Neck |
| Q08N | - |  |  | SI | Note |
| Q14 | - |  |  | SI | Breast |
| Q15 | - |  |  | SI | Breast general appearance |
| Q15N | - |  |  | SI | Note |
| Q15ObsDR | - |  |  | SI | Breast general appearance DR |
| Q17 | - |  |  | SI | Nipple secretion |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Nipple secretion DR |
| Q18 | - |  |  | SI | Breast normal |
| Q18N | - |  |  | SI | Note |
| Q18ObsDR | - |  |  | SI | Breast normal DR |
| Q19 | - |  |  | SI | Nipple retraction |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Nipple retraction DR |
| Q20 | - |  |  | SI | Breast symmetry |
| Q20N | - |  |  | SI | Note |
| Q20ObsDR | - |  |  | SI | Breast symmetry  DR |
| Q21 | - |  |  | SI | Breast skin |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Breast skin DR |
| Q23 | - |  |  | SI | Breast nodule |
| Q23N | - |  |  | SI | Localization |
| Q23ObsDR | - |  |  | SI | Breast nodule DR |
| Q25 | - |  |  | SI | Lymph nodes palpable |
| Q25N | - |  |  | SI | Note |
| Q25ObsDR | - |  |  | SI | Lymph nodes palpable DR |
| Q27 | - |  |  | SI | Other |
| Q30 | - |  |  | SI | Mastectomy |
| Q30N | - |  |  | SI | Note |
| Q30ObsDR | - |  |  | SI | Mastectomy DR |
| Q31 | - |  |  | SI | Scars / prior surgery |
| Q31N | - |  |  | SI | Note |
| Q31ObsDR | - |  |  | SI | Scars / prior surgery DR |
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
| USAPTL_Code | varchar |  |  | NO | Code |
| USAPTL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| USAPTL_CreatedDate | date |  |  | SI | Created Date |
| USAPTL_CreatedTime | time |  |  | SI | Created Time |
| USAPTL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| USAPTL_DateFrom | date |  |  | SI | Date From |
| USAPTL_DateTo | date |  |  | SI | Date to |
| USAPTL_Desc | varchar |  |  | NO | Description |
| USAPTL_Owner | varchar |  |  | SI | Owner |
| USAPTL_UpdatedDate | date |  |  | SI | Updated Date |
| USAPTL_UpdatedTime | time |  |  | SI | Updated Time |
| USAPTL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*