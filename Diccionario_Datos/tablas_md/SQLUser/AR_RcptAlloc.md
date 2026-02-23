# SQLUser.AR_RcptAlloc

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARRAL_ARRCP_ParRef | bigint | PK |  | NO | Des Ref to ARRCP |
| ARRAL_1stPayFlag | varchar |  |  | SI | First Payment Flag |
| ARRAL_ARPBIL_DR | bigint |  | FK | SI | Des Ref ARPBIL - Patient Bill |
| ARRAL_ARRCA_DR | varchar |  | FK | SI | Des Ref to Refund ARRCA |
| ARRAL_Admission_DR | bigint |  | FK | SI | Des Ref to PAADM |
| ARRAL_AllocCode_DR | varchar |  | FK | SI | Allocation Code - Des Ref to ARCAC(not in use |
| ARRAL_BankingListDate | date |  |  | SI | Banking List Date |
| ARRAL_BankingListNumber | varchar |  |  | SI | Banking List Number  |
| ARRAL_BankingListTime | time |  |  | SI | Banking List Time |
| ARRAL_Bill_DR | bigint |  | FK | SI | Des Ref to ARBIL (Not in Use) |
| ARRAL_CMCBank_DR | bigint |  | FK | SI | Des Ref to CMCBank |
| ARRAL_ChildSub | numeric |  |  | NO | ARRAL Child Subscript |
| ARRAL_Deposit_DR | bigint |  | FK | SI | Deposit Type - des ref to ARCDT |
| ARRAL_DiscAmt | double |  |  | SI | Discount Amount |
| ARRAL_DiscRate | double |  |  | SI | Discount Rate |
| ARRAL_DocFeeFlag | varchar |  |  | SI | Doctor Fee Flag (Should Be a Yes/No) |
| ARRAL_GlBatchNo | varchar |  |  | SI | GL Batch Number |
| ARRAL_IncludedInBankRun | varchar |  |  | SI | Included In Bank Run |
| ARRAL_OverpayFlag | varchar |  |  | SI | Overpay Flag |
| ARRAL_PayAmt | double |  |  | SI | Payment Amount |
| ARRAL_PayMode_DR | bigint |  | FK | SI | Des Ref PayMode |
| ARRAL_PrevBal | double |  |  | SI | Previous Balance |
| ARRAL_RcFlag | varchar |  |  | SI | Archive Flag |
| ARRAL_ReasonOverpay | varchar |  |  | SI | Reason for Overpay |
| ARRAL_RecoupFlag | varchar |  |  | SI | Recoup Flag |
| ARRAL_RefundNo | varchar |  |  | SI | RefundNo |
| ARRAL_RefundReason_DR | bigint |  | FK | SI | Des Ref RefundReason |
| ARRAL_RoundAmt | double |  |  | SI | Round Amount |
| ARRAL_RowId | varchar |  |  | NO | - |
| ARRAL_Transact_DR | varchar |  | FK | SI | Transaction Code (Des Ref to ARCTC)(not in us |
| ARRAL_UpdateDate | date |  |  | SI | Update Date |
| ARRAL_UpdateTime | time |  |  | SI | Update Time |
| ARRAL_UpdateUser_DR | bigint |  | FK | SI | Des Ref Update User |
| Q41Q1 | - |  |  | SI | Nombre |
| Q41Q2 | - |  |  | SI | Relacion |
| Q41Q3 | - |  |  | SI | Edad |
| Q41Q4 | - |  |  | SI | Estudios |
| Q41Q5 | - |  |  | SI | Antecedentes de Salud Física y Mental |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*