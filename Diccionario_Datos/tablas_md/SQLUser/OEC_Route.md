# SQLUser.OEC_Route

**Schema:** SQLUser
**Columnas:** 72
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROUTE_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Sleep |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Sleep DR |
| Q03 | - |  |  | SI | Wake up |
| Q03N | - |  |  | SI | Note |
| Q05 | - |  |  | SI | Afternoon nap from |
| Q05L | - |  |  | SI | to |
| Q05N | - |  |  | SI | Note |
| Q05T | - |  |  | SI | Afternoon nap (to) |
| Q09 | - |  |  | SI | Go to sleep |
| Q09N | - |  |  | SI | Note |
| Q11 | - |  |  | SI | Sleeping habits |
| Q12 | - |  |  | SI | Sleeping rituals |
| Q13 | - |  |  | SI | Sleep medication |
| Q13ObsDR | - |  |  | SI | Sleep medication DR |
| Q13S | - |  |  | SI | Since |
| Q15 | - |  |  | SI | Date |
| Q16 | - |  |  | SI | Time |
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
| ROUTE_Code | varchar |  |  | NO | Code |
| ROUTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROUTE_CreatedDate | date |  |  | SI | Created Date |
| ROUTE_CreatedTime | time |  |  | SI | Created Time |
| ROUTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROUTE_DateFrom | date |  |  | SI | Date From |
| ROUTE_DateTo | date |  |  | SI | Date To |
| ROUTE_Desc | varchar |  |  | NO | Description |
| ROUTE_IVType | varchar |  |  | SI | IVType |
| ROUTE_Owner | varchar |  |  | SI | Owner |
| ROUTE_UpdatedDate | date |  |  | SI | Updated Date |
| ROUTE_UpdatedTime | time |  |  | SI | Updated Time |
| ROUTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*