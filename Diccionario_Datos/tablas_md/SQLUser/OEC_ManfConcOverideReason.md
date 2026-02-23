# SQLUser.OEC_ManfConcOverideReason

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CORM_RowId | bigint | PK |  | NO | - |
| CORM_Code | varchar |  |  | NO | Code |
| CORM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CORM_CreatedDate | date |  |  | SI | Created Date |
| CORM_CreatedTime | time |  |  | SI | Created Time |
| CORM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CORM_DateFrom | date |  |  | SI | Date From |
| CORM_DateTo | date |  |  | SI | Date To |
| CORM_Desc | varchar |  |  | NO | Description |
| CORM_Owner | varchar |  |  | SI | Owner |
| CORM_UpdatedDate | date |  |  | SI | Updated Date |
| CORM_UpdatedTime | time |  |  | SI | Updated Time |
| CORM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Right Eye |
| Q02 | - |  |  | SI | Left Eye |
| Q03 | - |  |  | SI | Redness |
| Q04 | - |  |  | SI | redness 2 |
| Q05 | - |  |  | SI | Discharge |
| Q06 | - |  |  | SI | Discharge 2 |
| Q07 | - |  |  | SI | Swelling |
| Q08 | - |  |  | SI | Contact lens |
| Q09 | - |  |  | SI | Swelling 2 |
| Q10 | - |  |  | SI | Contact lens 2 |
| Q11 | - |  |  | SI | Glasses |
| Q12 | - |  |  | SI | Glasses 2 |
| Q13 | - |  |  | SI | Prosthesis |
| Q14 | - |  |  | SI | Prosthesis 2 |
| Q15 | - |  |  | SI | Eye patch |
| Q16 | - |  |  | SI | Eye patch |
| Q17 | - |  |  | SI | Shield |
| Q18 | - |  |  | SI | Shield 2 |
| Q19 | - |  |  | SI | Notes |
| Q20 | - |  |  | SI | Lid Swelling |
| Q21 | - |  |  | SI | Date |
| Q22 | - |  |  | SI | Time |
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