# SQLUser.INC_ItmHosp

**Schema:** SQLUser
**Columnas:** 121
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSP_ParRef | bigint | PK |  | NO | INC_Itm Parent Reference |
| HOSP_AccountIssue_DR | bigint |  | FK | SI | Des Ref GLCAcct |
| HOSP_AccountReceive_DR | bigint |  | FK | SI | Des Ref GLCAcct |
| HOSP_BarCode | varchar |  |  | SI | BarCode |
| HOSP_BatchReq | varchar |  |  | SI | Batch Number Required |
| HOSP_CTUOMTransfer_DR | bigint |  | FK | SI | Des Ref CTUOM (Transfer) |
| HOSP_CTUOM_Purch_DR | bigint |  | FK | SI | Des Ref CTUOM (Purchasing) |
| HOSP_Childsub | double |  |  | NO | Childsub |
| HOSP_Code | varchar |  |  | SI | Inventory Code |
| HOSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOSP_CreatedDate | date |  |  | SI | Created Date |
| HOSP_CreatedTime | time |  |  | SI | Created Time |
| HOSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOSP_DateFrom | date |  |  | SI | Date From |
| HOSP_DateTo | date |  |  | SI | Date To |
| HOSP_ExpReq | varchar |  |  | SI | Expiry Date Required |
| HOSP_FinalVendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| HOSP_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| HOSP_IsTrfFlag | varchar |  |  | SI | Issue Transfer Flag |
| HOSP_LastPurchasePrice | double |  |  | SI | Last Purchase Price  |
| HOSP_LogQty | double |  |  | SI | Logical Quantity (Qty Available) |
| HOSP_MaxQty | double |  |  | SI | Maximum Quantity (Limit of storage) |
| HOSP_MinQty | double |  |  | SI | Minimum Quantity (Safety stock level) |
| HOSP_Notes | varchar |  |  | SI | Remarks |
| HOSP_ReordLevel | double |  |  | SI | Reorder Level (EOQ) |
| HOSP_ReordQty | double |  |  | SI | Reorder Quantity (EOQ) |
| HOSP_ReportingDays | varchar |  |  | SI | Reporting Days |
| HOSP_RowId | varchar |  |  | NO | - |
| HOSP_StockQtyLastYear | double |  |  | SI | Stock Qty of Prev. Year |
| HOSP_StorageBinStatus | varchar |  |  | SI | Storage Bin Status |
| HOSP_UnitCost | double |  |  | SI | Unit Cost |
| HOSP_UpdatedDate | date |  |  | SI | Updated Date |
| HOSP_UpdatedTime | time |  |  | SI | Updated Time |
| HOSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| HOSP_WardStock | varchar |  |  | SI | Ward Stock Replenishment Option |
| Q01 | - |  |  | SI | Congestive heart failure history |
| Q02 | - |  |  | SI | Hypertension history |
| Q03 | - |  |  | SI | Age ≥ 75 years |
| Q04 | - |  |  | SI | Diabetes mellitus history |
| Q05 | - |  |  | SI | Stroke or TIA symptoms previously |
| Q06 | - |  |  | SI | Stroke or thromboembolism (TE)/100 years at risk i... |
| Q07 | - |  |  | SI | STROKE OR TE/100 PERSON-YEARS |
| Q08 | - |  |  | SI | Score |
| Q09 | - |  |  | SI | Ischemic Stroke |
| Q10 | - |  |  | SI | Stroke / TIA / TE |
| Q11 | - |  |  | SI | 0 |
| Q12 | - |  |  | SI | 0.6 |
| Q13 | - |  |  | SI | 0.9 |
| Q14 | - |  |  | SI | 1 |
| Q15 | - |  |  | SI | 3 |
| Q16 | - |  |  | SI | 4.3 |
| Q17 | - |  |  | SI | 2 |
| Q18 | - |  |  | SI | 4.2 |
| Q19 | - |  |  | SI | 6.1 |
| Q20 | - |  |  | SI | 3 |
| Q21 | - |  |  | SI | 7.1 |
| Q22 | - |  |  | SI | 9.9 |
| Q23 | - |  |  | SI | 4 |
| Q24 | - |  |  | SI | 11.1 |
| Q25 | - |  |  | SI | 14.9 |
| Q26 | - |  |  | SI | 5 |
| Q27 | - |  |  | SI | 12.5 |
| Q28 | - |  |  | SI | 16.7 |
| Q29 | - |  |  | SI | 6 |
| Q30 | - |  |  | SI | 13 |
| Q31 | - |  |  | SI | 17.2 |
| Q32 | - |  |  | SI | Score |
| Q33 | - |  |  | SI | Classification |
| Q34 | - |  |  | SI | 0 |
| Q35 | - |  |  | SI | Low risk of thromboembolic event |
| Q36 | - |  |  | SI | 1-2 |
| Q37 | - |  |  | SI | Intermediate risk of thromboembolic event |
| Q38 | - |  |  | SI | 3-6 |
| Q39 | - |  |  | SI | High risk of thromboembolic event |
| Q40 | - |  |  | SI | 0: Low risk of thromboembolic event |
| Q41 | - |  |  | SI | 1-2: Intermediate risk of thromboembolic event |
| Q42 | - |  |  | SI | 3-6: High risk of thromboembolic event |
| Q43 | - |  |  | SI | The CHADS₂score is one of several risk stratificat... |
| Q44 | - |  |  | SI | Stroke or Thromboembolism (TE)/100 Years at Risk i... |
| Q45 | - |  |  | SI | Date |
| Q46 | - |  |  | SI | Time |
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