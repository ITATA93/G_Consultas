# lab.INV_Batch

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Inventario**. Gestión de stock y bodega.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INVB_RowID | varchar | PK |  | NO | - |
| INVB_Amount | double |  |  | SI | Amount |
| INVB_BillingLocation_DR | varchar |  | FK | SI | Billing Location_DR |
| INVB_ClaimID | varchar |  |  | SI | Claim ID |
| INVB_CompanyCode_DR | varchar |  | FK | SI | Company Code DR |
| INVB_DateOfCreation | date |  |  | SI | Date Of Creation |
| INVB_DateOfTransmission | date |  |  | SI | Date Of Transmission |
| INVB_Number | numeric |  |  | NO | Batch Number |
| INVB_PayCode_DR | varchar |  | FK | NO | Pay Code DR |
| INVB_PendingPaymentReport | varchar |  |  | SI | Pending Payment Report |
| INVB_PendingProcessReport | varchar |  |  | SI | Pending Process Report |
| INVB_PendingTransmission | varchar |  |  | SI | - |
| INVB_ProviderNumber | varchar |  |  | SI | Provider number |
| INVB_Provider_DR | varchar |  | FK | SI | Provider DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*