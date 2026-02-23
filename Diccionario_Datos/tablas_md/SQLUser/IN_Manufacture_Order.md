# SQLUser.IN_Manufacture_Order

**Schema:** SQLUser
**Columnas:** 96
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INMAN_RowId | bigint | PK |  | NO | - |
| INMAN_Amount | double |  |  | SI | Amount of Drug Manufactured |
| INMAN_Batch_No | varchar |  |  | SI | Batch No |
| INMAN_CTLOC_DR | bigint |  | FK | NO | Des Ref to CTLOC |
| INMAN_CancelReason | varchar |  |  | SI | CancelReason |
| INMAN_Date | date |  |  | NO | Date of Order |
| INMAN_DrugRegister | varchar |  |  | SI | Drug Register |
| INMAN_End_Date | date |  |  | SI | End Date of Manufacture |
| INMAN_End_Time | time |  |  | SI | End Time |
| INMAN_EnterdQty | double |  |  | SI | Quantity Entered |
| INMAN_Expire_Date | date |  |  | SI | Expire Date |
| INMAN_Expire_Time | time |  |  | SI | Expire Time |
| INMAN_INCI_DR | bigint |  | FK | NO | Des Ref to INCI |
| INMAN_INCLB_DR | varchar |  | FK | SI | Des Ref to INCLB |
| INMAN_No | varchar |  |  | NO | Order No |
| INMAN_OrigRcp_DR | varchar |  | FK | SI | Des Ref OrigRcp |
| INMAN_Qty | double |  |  | NO | Quantity to Manufacture |
| INMAN_QtyRequired | double |  |  | SI | Quantity Required |
| INMAN_RecNumber | double |  |  | SI | RecNumber |
| INMAN_Remarks | varchar |  |  | SI | Remarks |
| INMAN_Start_Date | date |  |  | SI | Start Date |
| INMAN_Start_Time | time |  |  | SI | Start_Time |
| INMAN_Status | varchar |  |  | SI | Status (Completed/Aborted) |
| INMAN_Sterile | varchar |  |  | SI | Flag Sterile |
| INMAN_UOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| INMAN_UserCompleted | varchar |  |  | SI | User Completed |
| INMAN_User_DR | bigint |  | FK | NO | Des Ref to SSU |
| Q01 | - |  |  | SI | Treatment date |
| Q03 | - |  |  | SI | Treatment type - old |
| Q07 | - |  |  | SI | Follow up date - old |
| Q08 | - |  |  | SI | Follow up no |
| Q09 | - |  |  | SI | Pregnant months |
| Q16 | - |  |  | SI | Cytology old |
| Q17 | - |  |  | SI | Other comments |
| Q18 | - |  |  | SI | Diagnosis |
| Q19 | - |  |  | SI | Abnormal features |
| Q20 | - |  |  | SI | Colposcopy diagram |
| Q21 | - |  |  | SI | Months |
| Q22 | - |  |  | SI | Extent of lesion |
| Q23 | - |  |  | SI | Plan to review old |
| Q24 | - |  |  | SI | Plan for treatment details |
| Q25 | - |  |  | SI | Plan for treatment |
| Q26 | - |  |  | SI | Treatment comments |
| Q27 | - |  |  | SI | Treatment date |
| Q28 | - |  |  | SI | Plan to review |
| Q29 | - |  |  | SI | Treatment type |
| Q30 | - |  |  | SI | Colposcopy |
| Q31 | - |  |  | SI | Directed biopsy |
| Q32 | - |  |  | SI | Follow up date |
| Q33 | - |  |  | SI | Cytology |
| Q34 | - |  |  | SI | Cytology |
| Q35 | - |  |  | SI | Colposcopy |
| Q36 | - |  |  | SI | Date |
| Q37 | - |  |  | SI | Time |
| Q38 | - |  |  | SI | Plan to review |
| Q39 | - |  |  | SI | Plan for treatment |
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