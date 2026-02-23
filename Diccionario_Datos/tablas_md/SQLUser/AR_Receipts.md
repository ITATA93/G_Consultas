# SQLUser.AR_Receipts

**Schema:** SQLUser
**Columnas:** 88
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARRCP_RowId | bigint | PK |  | NO | - |
| ARRCP_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ARRCP_AccountingPeriod_DR | bigint |  | FK | SI | Des Ref AccountingPeriod |
| ARRCP_AcctClsAuxInsType_DR | bigint |  | FK | SI | Des Ref AcctClsAuxInsType |
| ARRCP_AddDate | date |  |  | SI | Add Date |
| ARRCP_AddLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ARRCP_AddTime | time |  |  | SI | Add Time |
| ARRCP_AddUserID | bigint |  |  | SI | Add User ID |
| ARRCP_Admission_DR | bigint |  | FK | SI | Des Ref to PAADM |
| ARRCP_BankingListDate | date |  |  | SI | Banking List Date |
| ARRCP_BankingListNumber | varchar |  |  | SI | Banking List Number |
| ARRCP_BankingListTime | time |  |  | SI | Banking List Time |
| ARRCP_BatchNo | varchar |  |  | SI | Batch No |
| ARRCP_CancelAccountingPeriod_DR | bigint |  | FK | SI | Des Ref CancelAccountingPeriod |
| ARRCP_CancelComments | varchar |  |  | SI | Cancel Comments |
| ARRCP_CancelReason_DR | bigint |  | FK | SI | Des Ref WO Reason |
| ARRCP_CancelReceipt_DR | bigint |  | FK | SI | Des Ref CancelReceipt |
| ARRCP_CancelUser_DR | bigint |  | FK | SI | Des Ref CancelUser |
| ARRCP_CardAuth | varchar |  |  | SI | Credit Card Authorisation Number |
| ARRCP_CardDr_DR | bigint |  | FK | SI | Des Ref to ARCDR |
| ARRCP_ChequeDate | date |  |  | SI | Date of Cheque |
| ARRCP_ChequeRef | varchar |  |  | SI | Cheque Number |
| ARRCP_CloseShift_DR | bigint |  | FK | SI | Des Ref CloseShift |
| ARRCP_CommAmt | double |  |  | SI | Commission Amount |
| ARRCP_CrCardNo | varchar |  |  | SI | Credit Card Number |
| ARRCP_CrExpDate | date |  |  | SI | Credit Card Expiry Date |
| ARRCP_Date | date |  |  | NO | Receipt Date |
| ARRCP_Debtor_DR | bigint |  | FK | SI | Des Ref to ARCDR |
| ARRCP_DeposBank_DR | bigint |  | FK | SI | Des Ref to CMCBM |
| ARRCP_DepositExpDate | date |  |  | SI | Deposit Expiry Date |
| ARRCP_DepositFlag | varchar |  |  | SI | Deposit Flag |
| ARRCP_DiscAmt | double |  |  | SI | Discount Amount |
| ARRCP_DiscRate | double |  |  | SI | Discount Rate |
| ARRCP_Discount_DR | bigint |  | FK | SI | Des Ref to ARCDI |
| ARRCP_ExpPayDate | date |  |  | SI | Expected Payment Date |
| ARRCP_FinPer_DR | varchar |  | FK | SI | Financial Period - des ref to CTFP |
| ARRCP_GLBatch_DR | bigint |  | FK | SI | Des Ref GL Batch |
| ARRCP_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ARRCP_IncludedInBankRun | varchar |  |  | SI | Included In Bank Run |
| ARRCP_InitReceipt_DR | bigint |  | FK | SI | Des Ref ARReceipts, InitiatingReceipt |
| ARRCP_InsAssoc_DR | bigint |  | FK | SI | Des Ref InsAssoc |
| ARRCP_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| ARRCP_InvLocation_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ARRCP_InvalidAmt | double |  |  | SI | Invalid Amt |
| ARRCP_InvalidDate | date |  |  | SI | Invalid Date |
| ARRCP_InvalidFlag | varchar |  |  | SI | Invalid Flag |
| ARRCP_InvalidTime | time |  |  | SI | Invalid Time |
| ARRCP_InvalidUser_DR | bigint |  | FK | SI | Des Ref User |
| ARRCP_LocRcptNo | varchar |  |  | SI | Location Receipt Number |
| ARRCP_Location_DR | bigint |  | FK | NO | Des Ref to CTLOC (Rcp Department) |
| ARRCP_Number | varchar |  |  | SI | Receipt Number |
| ARRCP_OriginalPayAmount | double |  |  | SI | OriginalPayAmount |
| ARRCP_OverPaymentFlag | varchar |  |  | SI | Over Payment Flag |
| ARRCP_PAPMI_DR | bigint |  | FK | SI | Des Ref to PAPMI |
| ARRCP_PackageGroupNumber | varchar |  |  | SI | Package Group Number |
| ARRCP_PackageGroup_DR | bigint |  | FK | SI | Package Group |
| ARRCP_PackageSubGroup_DR | bigint |  | FK | SI | Package SubGroup |
| ARRCP_PayAmount | double |  |  | SI | Payment Amount |
| ARRCP_PayMode_DR | bigint |  | FK | SI | Des Ref to CTPM |
| ARRCP_PayerName | varchar |  |  | SI | Payer Name |
| ARRCP_PersonPackage_DR | varchar |  | FK | SI | Des Ref PAPersonPackage |
| ARRCP_PrintCount | double |  |  | SI | Print Count |
| ARRCP_RcFlag | varchar |  |  | SI | Archive Flag |
| ARRCP_RecvAmt | double |  |  | SI | Received Amount |
| ARRCP_RefundComments | varchar |  |  | SI | Refund Comments |
| ARRCP_RefundDate | date |  |  | SI | Refund Date |
| ARRCP_RefundLocation_DR | bigint |  | FK | SI | Des Ref RefundLocation |
| ARRCP_RefundReason_DR | bigint |  | FK | SI | Des Ref RefundReason |
| ARRCP_RefundReceipt_DR | bigint |  | FK | SI | Des Ref Receipt Refunded |
| ARRCP_RefundTime | time |  |  | SI | Refund Time |
| ARRCP_RefundUser_DR | bigint |  | FK | SI | Des Ref RefundUser |
| ARRCP_Remarks | varchar |  |  | SI | Remarks |
| ARRCP_Status | varchar |  |  | SI | Receipt Status (O - Cancelled Receipt) |
| ARRCP_SundryDebtor_DR | bigint |  | FK | SI | Des Ref SundryDebtor |
| ARRCP_Text1 | varchar |  |  | SI | Text1 |
| ARRCP_Text2 | varchar |  |  | SI | Text2 |
| ARRCP_Text3 | varchar |  |  | SI | Text3 |
| ARRCP_Text4 | varchar |  |  | SI | Text4 |
| ARRCP_Text5 | varchar |  |  | SI | Text5 |
| ARRCP_UnallocAmt | double |  |  | SI | Unallocated Amount |
| Q57Q1 | - |  |  | SI | Otro prinicipio activo |
| Q57Q2 | - |  |  | SI | Unidad de medida |
| Q57Q3 | - |  |  | SI | Fecha de Vencimiento |
| Q57Q4 | - |  |  | SI | Sospecha de excipiente |
| Q57Q5 | - |  |  | SI | Nombre de excipiente |
| Q57Q6 | - |  |  | SI | Via Administración |
| Q57Q7 | - |  |  | SI | Dosis |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*