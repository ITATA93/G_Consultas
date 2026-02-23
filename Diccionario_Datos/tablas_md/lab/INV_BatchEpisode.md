# lab.INV_BatchEpisode

**Schema:** lab
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Inventario**. Gestión de stock y bodega.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INVBP_ParRef | varchar | PK |  | NO | INV_Batch Parent Reference |
| INVBP_Amount | double |  |  | SI | Amount Billed |
| INVBP_AmountGST | double |  |  | SI | Amount GST |
| INVBP_AmountGSTFree | double |  |  | SI | Amount GST Free |
| INVBP_AmountGSTTaxable | double |  |  | SI | Amount GST Taxable |
| INVBP_Company_DR | varchar |  | FK | SI | Company DR |
| INVBP_DateOfCollection | date |  |  | SI | Date Of Collection |
| INVBP_DateOfCreation | date |  |  | SI | Date Of Creation |
| INVBP_DebtorNumber_DR | varchar |  | FK | SI | Debtor Number DR |
| INVBP_Episode_DR | varchar |  | FK | NO | Episode DR |
| INVBP_PendingPaymentReport | varchar |  |  | SI | Pending Payment Report |
| INVBP_PendingProcessReport | varchar |  |  | SI | Pending Process Report |
| INVBP_RebillFlags | varchar |  |  | SI | Rebill Flags |
| INVBP_RowID | varchar |  |  | NO | - |
| INVBP_Sequence | numeric |  |  | SI | Sequence number |
| INVBP_UniqueNumber | varchar |  |  | SI | Unique number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*