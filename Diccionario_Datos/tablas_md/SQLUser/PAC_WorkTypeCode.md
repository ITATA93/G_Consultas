# SQLUser.PAC_WorkTypeCode

**Schema:** SQLUser
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WTC_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Skin integrity of the patient during perioperative... |
| Q02 | - |  |  | SI | Have all pressure areas been checked? |
| Q03 | - |  |  | SI | Are they intact? |
| Q04 | - |  |  | SI | Specify site and description |
| Q05 | - |  |  | SI | Action taken |
| Q06 | - |  |  | SI | Comments |
| Q07 | - |  |  | SI | Body map |
| Q08 | - |  |  | SI | Pressure risk assessment prior to surgery |
| Q09 | - |  |  | SI | Were any new pressure areas or new skin breaks ide... |
| Q10 | - |  |  | SI | Specify site and description |
| Q11 | - |  |  | SI | Action taken |
| Q12 | - |  |  | SI | Comments |
| Q13 | - |  |  | SI | Pressure risk assessment post surgery |
| Q14 | - |  |  | SI | Have all pressure areas been checked? |
| Q15 | - |  |  | SI | Are they intact? |
| Q16 | - |  |  | SI | Specify site and description |
| Q17 | - |  |  | SI | Action taken |
| Q18 | - |  |  | SI | Additional information |
| Q19 | - |  |  | SI | Pressure risk assessment in recovery |
| Q20 | - |  |  | SI | Have all pressure areas been checked? |
| Q21 | - |  |  | SI | Are they intact? |
| Q22 | - |  |  | SI | Specify site and description |
| Q23 | - |  |  | SI | Action taken |
| Q24 | - |  |  | SI | Procedure name |
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
| WTC_Code | varchar |  |  | NO | Code |
| WTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WTC_CreatedDate | date |  |  | SI | Created Date |
| WTC_CreatedTime | time |  |  | SI | Created Time |
| WTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WTC_DateFrom | date |  |  | SI | Date From |
| WTC_DateTo | date |  |  | SI | Date To |
| WTC_Desc | varchar |  |  | NO | Description |
| WTC_Owner | varchar |  |  | SI | Owner |
| WTC_UpdatedDate | date |  |  | SI | Updated Date |
| WTC_UpdatedTime | time |  |  | SI | Updated Time |
| WTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*