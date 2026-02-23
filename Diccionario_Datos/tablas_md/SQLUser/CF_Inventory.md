# SQLUser.CF_Inventory

**Schema:** SQLUser
**Columnas:** 112
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración**. Parámetros de configuración del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCF_RowId1 | double | PK |  | NO | - |
| INCF_AckFlag | varchar |  |  | SI | If Acknowledge is required for Iss/Trf |
| INCF_AllowMixedTax | varchar |  |  | SI | AllowMixedTax |
| INCF_AlwaysDefaultToTransfer | varchar |  |  | SI | Always Default To Transfer |
| INCF_AutoWdRep | varchar |  |  | SI | Auto generate Ward Stk Replenishment |
| INCF_BatchReq | varchar |  |  | SI | Is Batch No Required |
| INCF_CodeCounter_DR | bigint |  | FK | SI | Des Ref CodeCounter |
| INCF_Counter | varchar |  |  | SI | Counter Policy |
| INCF_DFRetAmt | varchar |  |  | SI | Default Return Amount |
| INCF_DaysPastTransaction | double |  |  | SI | Days for Past Transaction |
| INCF_DefRecType_DR | bigint |  | FK | SI | Default Receive Type |
| INCF_DefaultAvePriceOnStRec | varchar |  |  | SI | DefaultAvePriceOnStRec |
| INCF_DelItmTransForNoStatusDrMan | varchar |  |  | SI | DelItmTransForNoStatusDrMan |
| INCF_Description | varchar |  |  | SI | Description |
| INCF_DisableOKDiffVendors | varchar |  |  | SI | Disable OK Diff Vendors |
| INCF_DocketDateMandStockRec | varchar |  |  | SI | Docket Date Mandatory on Stock Rec |
| INCF_DontUpdateStItemCode | varchar |  |  | SI | Do not Allow Update Stock Item Code |
| INCF_ExpReq | varchar |  |  | SI | Is Expiry Date Required |
| INCF_IgnoreOETax | varchar |  |  | SI | Ignore OE Tax |
| INCF_LockWaitTime | double |  |  | SI | Maxmimum locking wait time to update item |
| INCF_ModiLoginDefLoc | varchar |  |  | SI | Can modify default login location ? |
| INCF_ModiLoginDefUser | varchar |  |  | SI | Can modify Login Default ? (User Name) |
| INCF_NegStk | varchar |  |  | SI | Negative Stock |
| INCF_NoRetCollectPharmDisch | varchar |  |  | SI | Do not return Collected Pharmacy Stock for Dischar... |
| INCF_NoRetCollectPharmEmerg | varchar |  |  | SI | Do not return Collected Pharmacy Stock for Emergen... |
| INCF_NoRetCollectPharmInpat | varchar |  |  | SI | Do not return Collected Pharmacy Stock for Inpatie... |
| INCF_NoRetCollectPharmOutpat | varchar |  |  | SI | Do not return Collected Pharmacy Stock for Outpati... |
| INCF_NoSearchByAnyPart | varchar |  |  | SI | No SearchByAnyPart |
| INCF_NoUpdatePOPriceIfNoStock | varchar |  |  | SI | Prevent the update of PO Receive Price when there ... |
| INCF_OnLineInv | varchar |  |  | SI | On Line inventory update flag |
| INCF_OwnLocAck | varchar |  |  | SI | Only Receive Loc can Acknowledge Trf |
| INCF_Owner | varchar |  |  | SI | - |
| INCF_PrintForm | varchar |  |  | SI | Form Printing |
| INCF_PromptCommercialNameOnPO | varchar |  |  | SI | PromptCommercialNameOnPO |
| INCF_RecalculateReorderLevel | varchar |  |  | SI | Recalculate Reorder Level/Quantity |
| INCF_RecalculateReplenishLevel | varchar |  |  | SI | Recalculate Replenish Level/Quantity |
| INCF_RecvMoreRequest | varchar |  |  | SI | Allow to Receive More than Requested |
| INCF_RestrictDrugMOrdersByLoc | varchar |  |  | SI | RestrictDrugMOrdersByLoc |
| INCF_RestrictPObyPOType | varchar |  |  | SI | Restrict Purchase Order by Purch Order Type |
| INCF_RestrictTransferSTKGroup | varchar |  |  | SI | Restrict Stock Transfer by StockTake Group |
| INCF_ReturnNonPharmacyDiscon | varchar |  |  | SI | ReturnNonPharmacyDiscon |
| INCF_ReturnPharmStockDiscon | varchar |  |  | SI | Return Pharmacy Stock upon Discon |
| INCF_RowId | double |  |  | NO | INCF RowId |
| INCF_ShowZeroBatchesSTK | varchar |  |  | SI | Show in Zero batches in STK Screen |
| INCF_SkipNoStockItemsonAddAll | varchar |  |  | SI | Skip No Stock Items on Add All |
| INCF_StReqDoNotAllowMultItems | varchar |  |  | SI | StReqDoNotAllowMultItems |
| INCF_StTakeGDFNewWay | varchar |  |  | SI | StTakeGDFNewWay |
| INCF_StTakeNoCountQtyDefault | varchar |  |  | SI | StTakeNoCountQtyDefault |
| INCF_StTkSecondCountRequired | varchar |  |  | SI | StTkSecondCountRequired |
| INCF_StTransFormatNumber | varchar |  |  | SI | StTransFormatNumber |
| INCF_TransAckReasonMandatory | varchar |  |  | SI | Transfer Acknowledge Reason Mandatory |
| INCF_TransDecimalRestrict | varchar |  |  | SI | TransDecimalRestrict |
| INCF_UnifyTakeNAdjustment | varchar |  |  | SI | Unify Stock Take N Adjustment screens |
| INCF_UpdateARCost | varchar |  |  | SI | Update AR Item Cost Upon Receive |
| INCF_UpdateDate | date |  |  | SI | Last Update Date |
| INCF_UpdateTime | time |  |  | SI | Last Update Time |
| INCF_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| INCF_UseExternalStockSytem | varchar |  |  | SI | UseExternalStockSytem |
| INCF_UseStkLocRestrInquiry | varchar |  |  | SI | Use Stock Loc Restr for stock Inquiry |
| INCF_WardStk | varchar |  |  | SI | Ward Stock Option |
| QCHDate | - |  |  | SI | Date |
| QCHOperDepartmentDR | - |  |  | SI | OperDepartment |
| QCHOperationDR | - |  |  | SI | Operation |
| QCHPriorityDR | - |  |  | SI | Priority |
| QCHRBResourceDR | - |  |  | SI | Resource |
| QCHReasonForSuspend | - |  |  | SI | Reason for Suspend |
| QCHReasonNotReady | - |  |  | SI | Reason Not Ready |
| QCHStatus | - |  |  | SI | Status |
| QCHSurgeonDR | - |  |  | SI | Surgeon |
| QCHTime | - |  |  | SI | Time |
| QCHTransDate | - |  |  | SI | Transaction Date |
| QCHTransTime | - |  |  | SI | Transaction Time |
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