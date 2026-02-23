# SQLUser.AR_CloseShift

**Schema:** SQLUser
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CLS_RowId | bigint | PK |  | NO | - |
| CLS_AmountReceived | double |  |  | SI | Amount Received |
| CLS_BankRefNumber | varchar |  |  | SI | Bank Reference Number |
| CLS_BatchRefNumber | varchar |  |  | SI | Batch Reference Number |
| CLS_CCRefAMEX | varchar |  |  | SI | CC Reference AMEX |
| CLS_CCRefNonAMEX | varchar |  |  | SI | CC Reference Non AMEX |
| CLS_CancelDate | date |  |  | SI | Cancel Date |
| CLS_CancelText | varchar |  |  | SI | CancelText |
| CLS_CancelTime | time |  |  | SI | Cancel Time |
| CLS_CancelUser_DR | bigint |  | FK | SI | Des Ref CancelUser |
| CLS_CashierCheck_DR | bigint |  | FK | SI | Des Ref CashierCheck |
| CLS_CashierClosing_DR | bigint |  | FK | SI | Des Ref CashierClosing |
| CLS_CloseDate | date |  |  | SI | Close Date |
| CLS_CloseTime | time |  |  | SI | Close Time |
| CLS_ClosingBalance | double |  |  | SI | Closing Balance |
| CLS_CreateDate | date |  |  | SI | Create Date |
| CLS_CreateTime | time |  |  | SI | Create Time |
| CLS_CreateUser_DR | bigint |  | FK | SI | Des Ref CreateUser |
| CLS_Date1 | date |  |  | SI | Date1 |
| CLS_Date2 | date |  |  | SI | Date2 |
| CLS_Date3 | date |  |  | SI | Date3 |
| CLS_Date4 | date |  |  | SI | Date4 |
| CLS_Date5 | date |  |  | SI | Date5 |
| CLS_Notes | varchar |  |  | SI | Notes |
| CLS_Number | varchar |  |  | SI | Number |
| CLS_Number1 | double |  |  | SI | Number1 |
| CLS_Number2 | double |  |  | SI | Number2 |
| CLS_Number3 | double |  |  | SI | Number3 |
| CLS_Number4 | double |  |  | SI | Number4 |
| CLS_Number5 | double |  |  | SI | Number5 |
| CLS_OpeningBalance | double |  |  | SI | Opening Balance |
| CLS_PostedToERP | varchar |  |  | SI | Posted to ERP |
| CLS_ReasonCancel_DR | bigint |  | FK | SI | Des Ref ReasonCancel |
| CLS_RecCashier_DR | bigint |  | FK | SI | Des Ref RecCashier |
| CLS_RecDate | date |  |  | SI | RecDate |
| CLS_RecLocation_DR | bigint |  | FK | SI | Des Ref Location |
| CLS_RecTimeFrom | time |  |  | SI | Rec Time From |
| CLS_RecTimeTo | time |  |  | SI | Rec Time To |
| CLS_Status | varchar |  |  | SI | Status |
| CLS_SupervisorBalanceReason | varchar |  |  | SI | Supervisor Balance Reason |
| CLS_SupervisorCloseDate | date |  |  | SI | Supervisor Close Date |
| CLS_SupervisorCloseTime | time |  |  | SI | Supervisor Close Time |
| CLS_SupervisorClosed | varchar |  |  | SI | Supervisor Closed |
| CLS_Supervisor_DR | bigint |  | FK | SI | Des Ref SSUser |
| CLS_Text1 | varchar |  |  | SI | Text1 |
| CLS_Text2 | varchar |  |  | SI | Text2 |
| CLS_Text3 | varchar |  |  | SI | Text3 |
| CLS_Text4 | varchar |  |  | SI | Text4 |
| CLS_Text5 | varchar |  |  | SI | Text5 |
| CLS_TotalCCAmtAMEX | double |  |  | SI | Total CC amount AMEX  |
| CLS_TotalCCAmtNonAMEX | double |  |  | SI | Total CC amount Non AMEX |
| CLS_TotalCommChargesAMEX | double |  |  | SI | Total commission charges AMEX |
| CLS_TotalCommChargesNonAMEX | double |  |  | SI | Total commission charges Non AMEX |
| CLS_VatAmtAMEX | double |  |  | SI | Vat Amount AMEX |
| CLS_VatAmtNonAMEX | double |  |  | SI | Vat Amount Non AMEX |
| ChildQ37DR | - |  |  | SI | Child Reference: Lista de Cuidadores |
| Q32Q1 | - |  |  | SI | Nombre y apellidos |
| Q32Q2 | - |  |  | SI | Edad |
| Q32Q3 | - |  |  | SI | Relación de parentesco |
| Q32Q4 | - |  |  | SI | Actividad principal |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*