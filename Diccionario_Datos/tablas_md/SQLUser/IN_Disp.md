# SQLUser.IN_Disp

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INDS_RowId | bigint | PK |  | NO | - |
| INDS_Completed | varchar |  |  | SI | Completed |
| INDS_Date | date |  |  | NO | Date Of Disposal |
| INDS_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INDS_Hospital_DR | bigint |  | FK | SI | Des Ref to CTHospital |
| INDS_No | varchar |  |  | SI | Disposal Reference No |
| INDS_ReasonAdjustment | bigint |  |  | SI | Des REf ReasonAdjustment |
| INDS_Remarks | varchar |  |  | SI | Remarks |
| INDS_SSUSR_DR | bigint |  | FK | NO | Des Ref To SSUSR |
| INDS_StOutType_DR | bigint |  | FK | SI | Des Ref StockOutType |
| INDS_Time | time |  |  | NO | Disposal Time |
| INDS_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INDS_Type | varchar |  |  | SI | Transaction Type |
| Q07 | - |  |  | SI | The Clinical, or partial, Mayo Score uses the thre... |
| Q1 | - |  |  | SI | Stool frequency |
| Q2 | - |  |  | SI | Rectal bleeding |
| Q3 | - |  |  | SI | Physician rating of disease activity |
| Q4 | - |  |  | SI | Date |
| Q5 | - |  |  | SI | Time |
| Q6 | - |  |  | SI | Score |
| Q8 | - |  |  | SI | The Clinical, or partial, Mayo Score uses the thre... |
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