# SQLUser.IN_StkTkItm

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSTI_INST_ParRef | bigint | PK |  | NO | Des Ref To INST |
| INSTI_BatchNo | varchar |  |  | SI | BatchNo |
| INSTI_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INSTI_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM |
| INSTI_ChildSub | numeric |  |  | NO | INSTI Childsub (New Key) |
| INSTI_Count1Date | date |  |  | SI | Stock Count Date(1) |
| INSTI_Count1Person_DR | bigint |  | FK | SI | Des Ref to SSUSR |
| INSTI_Count1Qty | double |  |  | SI | Stock Count Quantity(1) |
| INSTI_Count1Time | time |  |  | SI | Stock Count Time(1) |
| INSTI_Count2Date | date |  |  | SI | Count Date(2) |
| INSTI_Count2Person_DR | bigint |  | FK | SI | Count User(2) |
| INSTI_Count2Qty | double |  |  | SI | Count Quantity(2) |
| INSTI_Count2Time | time |  |  | SI | Count Time(2) |
| INSTI_ExpiryDate | date |  |  | SI | ExpiryDate |
| INSTI_FreezeDate | date |  |  | SI | Date When Freeze Stock |
| INSTI_FreezeQty | double |  |  | SI | Quantity when Freeze Stock |
| INSTI_FreezeTime | time |  |  | SI | Time when Freeze Stock |
| INSTI_INADI_DR | varchar |  | FK | SI | Des Ref INADI |
| INSTI_INCI_DR | bigint |  | FK | SI | Des Ref INCI |
| INSTI_INCLB_DR | varchar |  | FK | NO | Des Ref to INCLB |
| INSTI_Remarks | varchar |  |  | SI | Remarks |
| INSTI_RowId | varchar |  |  | NO | - |
| INSTI_Status | varchar |  |  | SI | Status-(F)reeze,(E)ntered,(V)ariance,(A)dj |
| INSTI_StockBarCode | varchar |  |  | SI | Stock BarCode |
| INSTI_StockCode | varchar |  |  | SI | Stock Code |
| INSTI_StockDesc | varchar |  |  | SI | Stock Desc |
| INSTI_Variance1 | double |  |  | SI | Stock Take Variance(1) |
| INSTI_Variance2 | double |  |  | SI | Variance(2) |
| Q01 | - |  |  | SI | This feature is usually obtained from a family mem... |
| Q02 | - |  |  | SI | Is there evidence of an acute change in mental sta... |
| Q03 | - |  |  | SI | Did the (abnormal) behavior fluctuate during the d... |
| Q04 | - |  |  | SI | Did the patient have difficulty focusing attention... |
| Q05 | - |  |  | SI | Was the patient’s thinking disorganized or incoher... |
| Q06 | - |  |  | SI | Overall, how would you rate this patient’s level o... |
| Q07 | - |  |  | SI | The diagnosis of delirium by CAM requires the pres... |
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