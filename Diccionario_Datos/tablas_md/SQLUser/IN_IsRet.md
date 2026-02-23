# SQLUser.IN_IsRet

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INIR_RowId | bigint | PK |  | NO | - |
| INIR_Completed | varchar |  |  | SI | Completed |
| INIR_Date | date |  |  | SI | Date |
| INIR_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INIR_INIT_DR | bigint |  | FK | SI | Des Ref INIT |
| INIR_No | varchar |  |  | SI | Return No |
| INIR_Time | time |  |  | SI | Time |
| INIR_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INIR_User_DR | bigint |  | FK | SI | Des Ref User |
| Q02 | - |  |  | SI | Drains Insitu |
| Q03 | - |  |  | SI | EVD |
| Q04 | - |  |  | SI | Codman Micro |
| Q05 | - |  |  | SI | SDD |
| Q06 | - |  |  | SI | EVD Date Inserted |
| Q07 | - |  |  | SI | Codmn Micro Date inserted |
| Q08 | - |  |  | SI | SDD Date Inserted |
| Q09 | - |  |  | SI | ICP Catheter levelled and zeroed |
| Q10 | - |  |  | SI | Date Inserted |
| Q11 | - |  |  | SI | EVD |
| Q12 | - |  |  | SI | SDD |
| Q13 | - |  |  | SI | Codman Micro |
| Q14 | - |  |  | SI | Lumbar Drain Date Inserted |
| Q15 | - |  |  | SI | Lumbar Drain |
| Q16 | - |  |  | SI | Lumbar Drain |
| Q17 | - |  |  | SI | Drain Condition |
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