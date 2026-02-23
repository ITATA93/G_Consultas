# SQLUser.AR_RcptPayMode

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAYM_ParRef | bigint | PK |  | NO | AR_Receipts Parent Reference |
| ChildQ42DR | - |  |  | SI | Child Reference: Tabla reacción Adversa |
| PAYM_AddDate | date |  |  | SI | AddDate |
| PAYM_AddTime | time |  |  | SI | Add Time |
| PAYM_Amt | double |  |  | SI | Amount |
| PAYM_AuthorCode | varchar |  |  | SI | Author Code |
| PAYM_BankDate | date |  |  | SI | Bank Date |
| PAYM_BankPaymReferenceNumber | varchar |  |  | SI | Bank Payment Reference Number  |
| PAYM_BankSlipNo | varchar |  |  | SI | BankSlipNo |
| PAYM_BankingListDate | date |  |  | SI | Banking List Date |
| PAYM_BankingListNumber | varchar |  |  | SI | Banking List Number  |
| PAYM_BankingListTime | time |  |  | SI | Banking List Time |
| PAYM_Branch | varchar |  |  | SI | Branch |
| PAYM_CMBank_DR | bigint |  | FK | SI | Des Ref to CMBank |
| PAYM_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PAYM_CancelComments | varchar |  |  | SI | CancelComments |
| PAYM_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| PAYM_CardChequeNo | varchar |  |  | SI | Card/Cheque No |
| PAYM_CardExpiryDate | date |  |  | SI | Card Expiry Date |
| PAYM_Card_DR | bigint |  | FK | SI | Des Ref Card |
| PAYM_ChangeAmount | double |  |  | SI | Change Amount |
| PAYM_ChequeDate | date |  |  | SI | Cheque Date |
| PAYM_Childsub | double |  |  | NO | Childsub |
| PAYM_CloseShift_DR | bigint |  | FK | SI | Des Ref CloseShift |
| PAYM_ConvertedCurrencyAmount | double |  |  | SI | Converted Amount |
| PAYM_CredCardPaym_DR | bigint |  | FK | SI | Des Ref CredCardPaym |
| PAYM_CurrencyAmt | double |  |  | SI | Currency Amt |
| PAYM_CurrencyTender | double |  |  | SI | Foreign Currency Tender |
| PAYM_Currency_DR | bigint |  | FK | SI | Des Ref Currency |
| PAYM_Date | date |  |  | SI | Date |
| PAYM_DepositFlag | varchar |  |  | SI | Deposit Flag |
| PAYM_Drawer | varchar |  |  | SI | Drawer |
| PAYM_GLBatch_DR | bigint |  | FK | SI | Des Ref GLBatch |
| PAYM_GovernNo | varchar |  |  | SI | GovernNo |
| PAYM_IncludedInBankRun | varchar |  |  | SI | Included In Bank Run |
| PAYM_InvDate | date |  |  | SI | InvDate |
| PAYM_InvLoc_DR | bigint |  | FK | SI | Des Ref InvLoc |
| PAYM_InvNotes | varchar |  |  | SI | Inv Notes |
| PAYM_InvTime | time |  |  | SI | InvTime |
| PAYM_InvUser | bigint |  |  | SI | Des Ref User |
| PAYM_InvalidFlag | varchar |  |  | SI | Invalid Flag |
| PAYM_PayMode_DR | bigint |  | FK | SI | Des Ref to PayMode |
| PAYM_Reconcile | varchar |  |  | SI | Reconcile |
| PAYM_RefundComments | varchar |  |  | SI | RefundComments |
| PAYM_RefundNo | varchar |  |  | SI | RefundNo |
| PAYM_RefundReason_DR | bigint |  | FK | SI | Des Ref RefundReason |
| PAYM_Remarks | varchar |  |  | SI | Remarks |
| PAYM_RowId | varchar |  |  | NO | - |
| PAYM_Text1 | varchar |  |  | SI | Text1 |
| PAYM_Text2 | varchar |  |  | SI | Text2 |
| PAYM_Text3 | varchar |  |  | SI | Text3 |
| PAYM_Text4 | varchar |  |  | SI | Text4 |
| PAYM_Text5 | varchar |  |  | SI | Text5 |
| PAYM_UpdateDate | date |  |  | SI | UpdateDate |
| PAYM_UpdateTime | time |  |  | SI | UpdateTime |
| PAYM_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| Q14Q1 | - |  |  | SI | Tipo de Fármaco |
| Q14Q10 | - |  |  | SI | Motivo de la Prescripción |
| Q14Q2 | - |  |  | SI | Fármaco (s) |
| Q14Q3 | - |  |  | SI | Marca ® |
| Q14Q4 | - |  |  | SI | Lote |
| Q14Q5 | - |  |  | SI | Dosis |
| Q14Q6 | - |  |  | SI | Frecuencia |
| Q14Q7 | - |  |  | SI | Vía de Administración |
| Q14Q8 | - |  |  | SI | Fecha Inicio |
| Q14Q9 | - |  |  | SI | Fecha Término |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*