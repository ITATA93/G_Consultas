# SQLUser.AR_Trans

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Cuentas por Cobrar (AR)**. Facturación y cobranza de pacientes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TR_RowId | bigint | PK |  | NO | - |
| Q16Q1 | - |  |  | SI | Procedimiento a Realizar |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TR_ARPBL_DR | bigint |  | FK | SI | Des Ref ARPBL |
| TR_ARRCA_DR | varchar |  | FK | SI | Des Ref ARRCA |
| TR_AccountPeriod_DR | bigint |  | FK | SI | Des Ref AccountPeriod |
| TR_Amount | double |  |  | SI | Amount |
| TR_BillDiscount_DR | varchar |  | FK | SI | Des Ref Bill Discount |
| TR_BillOutstand_DR | varchar |  | FK | SI | Des Ref BillOutstand |
| TR_BillWriteOff_DR | varchar |  | FK | SI | Des Ref BillWriteOff |
| TR_ChangeAmount | double |  |  | SI | ChangeAmount |
| TR_ConvertedCurrencyAmount | double |  |  | SI | ConvertedCurrencyAmount |
| TR_CurrencyAmount | double |  |  | SI | CurrencyAmount |
| TR_Date | date |  |  | SI | Date |
| TR_DiscType_DR | bigint |  | FK | SI | Des Ref DiscType |
| TR_DiscretOutsType_DR | bigint |  | FK | SI | Des Ref DiscretOutsType |
| TR_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| TR_OrgAR_Trans_DR | bigint |  | FK | SI | Des Ref AR_Trans |
| TR_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| TR_PAPER_DR | bigint |  | FK | SI | Des Ref PAPER |
| TR_ReceiptID_DR | bigint |  | FK | SI | Des Ref ReceiptID |
| TR_Time | time |  |  | SI | Time |
| TR_Type | varchar |  |  | SI | Transaction Type |
| TR_UserLocation_DR | bigint |  | FK | SI | Des Ref UserLocation |
| TR_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*