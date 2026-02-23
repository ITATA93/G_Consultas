# SQLUser.PAC_CustomExtract

**Schema:** SQLUser
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CUSTEXT_RowId | bigint | PK |  | NO | - |
| CUSTEXT_Code | varchar |  |  | NO | Code |
| CUSTEXT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CUSTEXT_CreatedDate | date |  |  | SI | Created Date |
| CUSTEXT_CreatedTime | time |  |  | SI | Created Time |
| CUSTEXT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CUSTEXT_DeleteScript | varchar |  |  | SI | Delete Script |
| CUSTEXT_Desc | varchar |  |  | NO | Description |
| CUSTEXT_ExtractScript | varchar |  |  | SI | Extract Script |
| CUSTEXT_Owner | varchar |  |  | SI | Owner |
| CUSTEXT_UpdatedDate | date |  |  | SI | Updated Date |
| CUSTEXT_UpdatedTime | time |  |  | SI | Updated Time |
| CUSTEXT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Check the following items |
| Q04 | - |  |  | SI | Patient ID band in situ and correct |
| Q05 | - |  |  | SI | Blood loss in theatre documented on fluid balance ... |
| Q06 | - |  |  | SI | Indwelling catheter in situ |
| Q07 | - |  |  | SI | IV fluid therapy ordered |
| Q08 | - |  |  | SI | Pain management ordered |
| Q09 | - |  |  | SI | Antiemetics ordered |
| Q10 | - |  |  | SI | Antibiotics ordered |
| Q11 | - |  |  | SI | Post op x-ray ordered |
| Q12 | - |  |  | SI | Post op bloods ordered |
| Q13 | - |  |  | SI | Wound drain present |
| Q14 | - |  |  | SI | Intact dressing |
| Q15 | - |  |  | SI | Review neurovascular status of affected limb |
| Q16 | - |  |  | SI | Notes |
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