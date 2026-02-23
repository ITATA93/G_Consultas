# SQLUser.INC_Itm

**Schema:** SQLUser
**Columnas:** 143
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCI_RowId | bigint | PK |  | NO | - |
| INCI_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCIM  |
| INCI_Account1_DR | bigint |  | FK | SI | Des Ref Account1 |
| INCI_Account_DR | bigint |  | FK | SI | Des Ref Account |
| INCI_AdhocItem | varchar |  |  | SI | Flag to indicate this is an auto-created stock ite... |
| INCI_BarCode | varchar |  |  | SI | BarCode |
| INCI_BatchReq | varchar |  |  | SI | Batch No Required |
| INCI_CTLOC_DR | bigint |  | FK | SI | Des Ref to CTLOC (Main Loc/Warehouse) |
| INCI_CTUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM (Unit of Measurement) |
| INCI_CTUOM_Purch_DR | bigint |  | FK | SI | Des Ref CTUOM (Purchasing) |
| INCI_CTVAT_DR | bigint |  | FK | SI | Des Ref to CTVAT (des ref to get VAT) |
| INCI_Code | varchar |  |  | NO | Inventory Code |
| INCI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INCI_CreatedDate | date |  |  | SI | Created Date |
| INCI_CreatedTime | time |  |  | SI | Created Time |
| INCI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCI_Desc | varchar |  |  | NO | Inventory Description |
| INCI_DirtyQty | double |  |  | SI | Dirty Qty |
| INCI_ExpReq | varchar |  |  | SI | Expiry Date Required |
| INCI_ExternalLoanDays | double |  |  | SI | Not Used |
| INCI_FinalVendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| INCI_FinanceCategory | varchar |  |  | SI | Finance Category |
| INCI_Flag1 | varchar |  |  | SI | Flag1 |
| INCI_Flag2 | varchar |  |  | SI | Flag2 |
| INCI_Flag3 | varchar |  |  | SI | Flag3 |
| INCI_Flag4 | varchar |  |  | SI | Flag4 |
| INCI_Flag5 | varchar |  |  | SI | Flag5 |
| INCI_INCCA_DR | varchar |  | FK | SI | Not Used Des Ref to INCCA (Ctrl Account) |
| INCI_INCPO_DR | bigint |  | FK | SI | Des Ref to INCPO (Stock type/ PO Type) |
| INCI_INCSC_DR | bigint |  | FK | SI | Des Ref to INCSC (Stock category) |
| INCI_INCTG_DR | bigint |  | FK | SI | Des Ref to INCTG (Stock take group) |
| INCI_InternalLoanDays | double |  |  | SI | Not Used |
| INCI_IsTrfFlag | varchar |  |  | SI | Issue Transfer Flag |
| INCI_LightSens_DR | bigint |  | FK | SI | Des Ref LightSens |
| INCI_LoanItem | varchar |  |  | SI | Not Used |
| INCI_LogQty | double |  |  | SI | Logical Quantity (Qty Available) |
| INCI_MaxQty | double |  |  | SI | Maximum Quantity (Limit of storage) |
| INCI_MinQty | double |  |  | SI | Minimum Quantity (Safety stock level) |
| INCI_NotUseFlag | varchar |  |  | SI | Not Use Flag |
| INCI_OriginalARCIM_DR | varchar |  | FK | SI | Original ARCIM Des Ref |
| INCI_Owner | varchar |  |  | SI | Owner |
| INCI_PackInstr_DR | bigint |  | FK | SI | Des Ref PackInstr |
| INCI_PrefVendor_DR | bigint |  | FK | SI | Des Ref PrefVendor |
| INCI_Remarks | varchar |  |  | SI | Remarks |
| INCI_ReordLevel | double |  |  | SI | Reorder Level (EOQ) |
| INCI_ReordQty | double |  |  | SI | Reorder Quantity (EOQ) |
| INCI_ReportingDays | varchar |  |  | SI | Reporting Days |
| INCI_SterCat_DR | bigint |  | FK | SI | Des Ref INC SterCat |
| INCI_Sterile | varchar |  |  | SI | Sterile Flag |
| INCI_StockAmtLastYear | double |  |  | SI | Stock Amt of Prev. Year |
| INCI_StockLocations | varchar |  |  | SI | Stock Locations of item |
| INCI_StockQtyLastYear | double |  |  | SI | Stock Qty of Prev. Year |
| INCI_StorageBinStatus | varchar |  |  | SI | Storage Bin Status |
| INCI_Text1 | varchar |  |  | SI | Text1 |
| INCI_Text10 | varchar |  |  | SI | Text10 |
| INCI_Text2 | varchar |  |  | SI | Text2 |
| INCI_Text3 | varchar |  |  | SI | Text3 |
| INCI_Text4 | varchar |  |  | SI | Text4 |
| INCI_Text5 | varchar |  |  | SI | Text5 |
| INCI_Text6 | varchar |  |  | SI | Text6 |
| INCI_Text7 | varchar |  |  | SI | Text7 |
| INCI_Text8 | varchar |  |  | SI | Text8 |
| INCI_Text9 | varchar |  |  | SI | Text9 |
| INCI_UnitCost | double |  |  | SI | Unit Cost |
| INCI_UpdateDate | date |  |  | SI | Update Date |
| INCI_UpdateTime | time |  |  | SI | Update Time |
| INCI_UpdateUser | bigint |  |  | SI | Update User |
| INCI_UpdatedDate | date |  |  | SI | Updated Date |
| INCI_UpdatedTime | time |  |  | SI | Updated Time |
| INCI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INCI_WardStock | varchar |  |  | SI | Ward Stock Replenishment Option |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Bundle compliance percentage |
| Q04 | - |  |  | SI | % |
| Q05 | - |  |  | SI | Has the patient been identified? |
| Q06 | - |  |  | SI | Has the correct indication of central venous acces... |
| Q07 | - |  |  | SI | Has the patient been informed about the indication... |
| Q08 | - |  |  | SI | Has all the necessary material for the procedure b... |
| Q09 | - |  |  | SI | Was the pre-procedural ultrasound study of the pat... |
| Q10 | - |  |  | SI | Was the patient positioned correctly? |
| Q11 | - |  |  | SI | Was hand hygiene performed according to protocol? |
| Q12 | - |  |  | SI | Has skin antisepsis been performed with 2% chlorhe... |
| Q13 | - |  |  | SI | Have the maximum barrier precautions been implemen... |
| Q14 | - |  |  | SI | Is the use of local anesthesia and / or sedation a... |
| Q15 | - |  |  | SI | Is venipuncture ultrasound-guided? |
| Q16 | - |  |  | SI | Has the correct intravenous position of the guide ... |
| Q17 | - |  |  | SI | Has intravascular placement of the catheter been v... |
| Q18 | - |  |  | SI | Was intra-procedural control of catheter tip posit... |
| Q19 | - |  |  | SI | Was the flush and lock of the catheter performed? |
| Q20 | - |  |  | SI | Has the catheter been closed with the needlefree c... |
| Q21 | - |  |  | SI | Has the catheter been secured with sutureless anco... |
| Q22 | - |  |  | SI | Was histoacrylic glue used to seal the insertion s... |
| Q23 | - |  |  | SI | Was it covered with transparent semi-permeable adh... |
| Q24 | - |  |  | SI | Confirmed the maintenance of the sterile field for... |
| Q25 | - |  |  | SI | Notes |
| Q26 | - |  |  | SI | Score |
| Q27 | - |  |  | SI | Classification |
| Q28 | - |  |  | SI | 0 - 100 |
| Q29 | - |  |  | SI | Higher percentages represent higher compliance to ... |
| Q30 | - |  |  | SI | 0 - 100: Higher percentages represent higher compl... |
| Q31 | - |  |  | SI | CVCs are the leading cause of device-related bacte... |
| Q32 | - |  |  | SI | The aim of the Central venous catheter CVC inserti... |
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