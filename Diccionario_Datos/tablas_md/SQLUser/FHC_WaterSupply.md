# SQLUser.FHC_WaterSupply

**Schema:** SQLUser
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Hogar/Familia**. Parámetros de entorno familiar.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FHCWS_RowId | bigint | PK |  | NO | - |
| FHCWS_Code | varchar |  |  | NO | Water Supply Code |
| FHCWS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| FHCWS_CreatedDate | date |  |  | SI | Created Date |
| FHCWS_CreatedTime | time |  |  | SI | Created Time |
| FHCWS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| FHCWS_DateFrom | date |  |  | NO | Date From |
| FHCWS_DateTo | date |  |  | SI | Date To |
| FHCWS_Desc | varchar |  |  | NO | Water Supply Description |
| FHCWS_NationalCode | varchar |  |  | SI | National Code |
| FHCWS_Owner | varchar |  |  | SI | Owner |
| FHCWS_UpdatedDate | date |  |  | SI | Updated Date |
| FHCWS_UpdatedTime | time |  |  | SI | Updated Time |
| FHCWS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Catheter urinary tract infection - Care bundle |
| Q02 | - |  |  | SI | Date |
| Q03 | - |  |  | SI | Time |
| Q04 | - |  |  | SI | Was hand hygiene carried out before any procedure ... |
| Q05 | - |  |  | SI | Has the need to keep the urinary catheter in place... |
| Q06 | - |  |  | SI | Was the hygiene of the urethral meatus performed d... |
| Q07 | - |  |  | SI | Has the urinary catheter been kept continuously co... |
| Q08 | - |  |  | SI | Has the drainage bag been emptied when an aseptic,... |
| Q09 | - |  |  | SI | Has the drainage bag been placed lower than the bl... |
| Q10 | - |  |  | SI | Comments |
| Q11 | - |  |  | SI | Bundle compliance percentage |
| Q12 | - |  |  | SI | % |
| Q13 | - |  |  | SI | Guidelines |
| Q14 | - |  |  | SI | 0 - 100% :  Higher percentages represent higher co... |
| Q15 | - |  |  | SI | Catheter Associated Urinary Tract Infection Care B... |
| Q16 | - |  |  | SI | Was the hygiene of the urethral meatus performed d... |
| Q17 | - |  |  | SI | All responses set to not evaluable |
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