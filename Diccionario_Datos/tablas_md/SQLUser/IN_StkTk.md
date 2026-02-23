# SQLUser.IN_StkTk

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INST_RowId | bigint | PK |  | NO | - |
| INST_ActiveItemsOnly | varchar |  |  | SI | Active Items Only |
| INST_AdjustmentComplete | varchar |  |  | SI | Adjustment Complete |
| INST_CTLOC_DR | bigint |  | FK | SI | Des Ref To CTLOC |
| INST_Completed | varchar |  |  | SI | Completed |
| INST_Date | date |  |  | NO | Transaction Date |
| INST_DateLastUpdated | date |  |  | SI | DateLastUpdated |
| INST_DoubleST | varchar |  |  | SI | Double Stock Take |
| INST_FrCode_DR | bigint |  | FK | SI | Des Ref to INCI |
| INST_FrGroup_DR | bigint |  | FK | SI | Des Ref to INCTG |
| INST_FrzDateLastUpdated | date |  |  | SI | DateLastUpdated |
| INST_FrzTimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INST_FrzUserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INST_INAD_DR | bigint |  | FK | SI | Des Ref Adjustment |
| INST_No | varchar |  |  | SI | Stock Take Reference Number |
| INST_Remarks | varchar |  |  | SI | Remarks |
| INST_SSUSR_DR | bigint |  | FK | NO | Des Ref to SSUSR |
| INST_Status | varchar |  |  | SI | Stock Take Batch Status |
| INST_StockTakeComplete | varchar |  |  | SI | StockTakeComplete |
| INST_StockTakeComplete2 | varchar |  |  | SI | StockTakeComplete2 |
| INST_Time | time |  |  | NO | Time |
| INST_TimeLastUpdated | time |  |  | SI | TimeLastUpdated |
| INST_ToCode_DR | bigint |  | FK | SI | Des Ref To INCI |
| INST_ToGroup_DR | bigint |  | FK | SI | Des Ref To INCTG |
| INST_UserLastUpdated_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Patient level |
| Q04 | - |  |  | SI | Guidelines |
| Q05 | - |  |  | SI | Level I |
| Q06 | - |  |  | SI | I.The person independently alternates between send... |
| Q07 | - |  |  | SI | Unfamiliar and familiar conversational partners. c... |
| Q08 | - |  |  | SI | Level II |
| Q09 | - |  |  | SI | II.The person independently alternates between sen... |
| Q10 | - |  |  | SI | The person may need extra time to understand messa... |
| Q11 | - |  |  | SI | Eventual effectiveness of the persons communicatio... |
| Q12 | - |  |  | SI | Level III |
| Q13 | - |  |  | SI | III.The person alternates between sender and recei... |
| Q14 | - |  |  | SI | Communication is not consistently effective with m... |
| Q15 | - |  |  | SI | Level IV |
| Q16 | - |  |  | SI | IV.The person does not consistently alternate send... |
| Q17 | - |  |  | SI | a) an occasionally effective sender and receiver |
| Q18 | - |  |  | SI | Level V |
| Q19 | - |  |  | SI | V.The person is limited as both a sender and a rec... |
| Q20 | - |  |  | SI | The person appears to have limited understanding o... |
| Q21 | - |  |  | SI | Reference |
| Q22 | - |  |  | SI | 1. Hidecker MJC, Paneth N, Rosenbaum PL,&nbsp |
| Q23 | - |  |  | SI | 2. Hidecker MJC, Paneth N, Rosenbaum PL,&nbsp |
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