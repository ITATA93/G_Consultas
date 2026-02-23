# SQLUser.PA_PayorApprovalRequest

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAPPREQ_RowId | bigint | PK |  | NO | - |
| PAPPREQ_Adm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| PAPPREQ_AmendInitiator | varchar |  |  | SI | Approval Request Amending Initiator - From Standar... |
| PAPPREQ_ApprReqSource_DR | bigint |  | FK | SI | Des Ref BLCApprovalRequestSource |
| PAPPREQ_ApprReqStat_DR | bigint |  | FK | SI | Des Ref BLCApprovalRequestStatus |
| PAPPREQ_ApprovReqDate | date |  |  | NO | Approval Request Date |
| PAPPREQ_ApprovReqType | varchar |  |  | SI | Approval Request Type |
| PAPPREQ_ApprovResponseDate | date |  |  | SI | Approval Response Date |
| PAPPREQ_ApprovValidUntilDate | date |  |  | SI | Approval Valid Until Date |
| PAPPREQ_ApprovalNumber | varchar |  |  | SI | Approval Number |
| PAPPREQ_ApprovedAmount | double |  |  | SI | Approved Amount |
| PAPPREQ_ApprovedBy | varchar |  |  | SI | Approved By |
| PAPPREQ_ApprovedQTY | double |  |  | SI | Approved QTY |
| PAPPREQ_CareProvClaimID | varchar |  |  | SI | Episode Care Provider Claim ID  |
| PAPPREQ_Date1 | date |  |  | SI | Date1 |
| PAPPREQ_Date2 | date |  |  | SI | Date2 |
| PAPPREQ_Date3 | date |  |  | SI | Date3 |
| PAPPREQ_Date4 | date |  |  | SI | Date4 |
| PAPPREQ_Date5 | date |  |  | SI | Date5 |
| PAPPREQ_EPrescComments | varchar |  |  | SI | E-Prescription Comments - [DEPRECATED] replaced by... |
| PAPPREQ_EPrescNumber | varchar |  |  | SI | E-Prescription Number - [DEPRECATED] replaced by U... |
| PAPPREQ_EPrescStatus | varchar |  |  | SI | E-Prescription Status - [DEPRECATED] replaced by U... |
| PAPPREQ_Eligibility_DR | varchar |  | FK | SI | Des Ref PAPersonEligibility |
| PAPPREQ_ExpectedAdmDate | date |  |  | SI | Expected Date of Admission |
| PAPPREQ_GroupRequestDesc_DR | bigint |  | FK | SI | Des Ref BLCApprGroupRequestDescription - Approval ... |
| PAPPREQ_InitialReq_DR | bigint |  | FK | SI | Deprecated - Des Ref PAPayorApprovalRequest |
| PAPPREQ_Initiator | varchar |  |  | SI | Approval Request Initiator - From Standard Type Pa... |
| PAPPREQ_LnkPreApprovalReq_DR | bigint |  | FK | SI | Linked Pre-Approval Request - Des Ref PAPayorAppro... |
| PAPPREQ_Number1 | double |  |  | SI | Number1 |
| PAPPREQ_Number2 | double |  |  | SI | Number2 |
| PAPPREQ_Number3 | double |  |  | SI | Number3 |
| PAPPREQ_Number4 | double |  |  | SI | Number4 |
| PAPPREQ_Number5 | double |  |  | SI | Number5 |
| PAPPREQ_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem |
| PAPPREQ_OrderSetRequestAmount | double |  |  | SI | Order Set Requesting Amount - Populated against th... |
| PAPPREQ_OrderingCareProvClaimID | varchar |  |  | SI | Ordering Care Provider Claim ID |
| PAPPREQ_PatInformNotes | varchar |  |  | SI | Patient Information Notes |
| PAPPREQ_PatMas_DR | bigint |  | FK | SI | Des Ref PAPatMas |
| PAPPREQ_PatientInformed | varchar |  |  | SI | Patient Informed |
| PAPPREQ_PatientTotal | double |  |  | SI | Patient Total as calculated by Best Plan procedure |
| PAPPREQ_PayorApprGroupRequest_DR | bigint |  | FK | SI | Des Ref PAPayorApprovalGroupRequest |
| PAPPREQ_PayorAuthCode | varchar |  |  | SI | Payor Authorization Code |
| PAPPREQ_Payor_DR | bigint |  | FK | SI | Payor - Des Ref ARCInsuranceType |
| PAPPREQ_Plan_DR | bigint |  | FK | SI | Plan - Des Ref ARCAuxilInsurType |
| PAPPREQ_Price | double |  |  | SI | Price as calculated by Best Plan procedure |
| PAPPREQ_PriceBeforeDisc | double |  |  | SI | Price before discount as calculated by Best Plan p... |
| PAPPREQ_QuoteItem_DR | varchar |  | FK | SI | Des Ref ARQuoteItems |
| PAPPREQ_ReasonApprReject_DR | bigint |  | FK | SI | Des Ref BLCReasonForApprovalRejection |
| PAPPREQ_RefDoctorCode | varchar |  |  | SI | External Referral Doctor Code  |
| PAPPREQ_RemainingQTY | double |  |  | SI | Quantity Remaining |
| PAPPREQ_Remarks | varchar |  |  | SI | Remarks |
| PAPPREQ_RequestAmount | double |  |  | SI | Requesting Amount |
| PAPPREQ_RequestingQTY | double |  |  | SI | Requesting Quantity |
| PAPPREQ_ServiceTax | double |  |  | SI | Service Tax Amount as calculated by Best Plan proc... |
| PAPPREQ_Text1 | varchar |  |  | SI | Text1 |
| PAPPREQ_Text2 | varchar |  |  | SI | Text2 |
| PAPPREQ_Text3 | varchar |  |  | SI | Text3 |
| PAPPREQ_Text4 | varchar |  |  | SI | Text4 |
| PAPPREQ_Text5 | varchar |  |  | SI | Text5 |
| PAPPREQ_ToothText1 | varchar |  |  | SI | Tooth Text1 |
| PAPPREQ_ToothText2 | varchar |  |  | SI | Tooth Text2 |
| PAPPREQ_ToothText3 | varchar |  |  | SI | Tooth Text3 |
| PAPPREQ_ToothText4 | varchar |  |  | SI | Tooth Text4 |
| PAPPREQ_ToothText5 | varchar |  |  | SI | Tooth Text5 |
| PAPPREQ_TrafficAccident_DR | bigint |  | FK | SI | Des Ref PATrafficAccident |
| PAPPREQ_UpdateDate | date |  |  | SI | Update Date |
| PAPPREQ_UpdateHospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| PAPPREQ_UpdateTime | time |  |  | SI | Update Time |
| PAPPREQ_UpdateUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| PAPPREQ_WaitList_DR | bigint |  | FK | SI | Des Ref PAWaitingList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*