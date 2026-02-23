# lab.CR_BatchLine

**Schema:** lab
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRBL_ParRef | varchar | PK |  | NO | CR_CreditBatch Parent Reference |
| CRBL_Amount | double |  |  | SI | Credit Amount |
| CRBL_AmountInCredit | double |  |  | SI | Amount In Credit |
| CRBL_AmountPatients | double |  |  | SI | Amount Patients |
| CRBL_AmountPayments | double |  |  | SI | Amount Payments |
| CRBL_BillLocation_DR | varchar |  | FK | SI | Bill Location DR |
| CRBL_Company_DR | varchar |  | FK | SI | Company DR |
| CRBL_DateOfCollection | date |  |  | SI | Date Of Collection |
| CRBL_DateOfPosting | date |  |  | SI | Date Of Posting |
| CRBL_DebtorNumber_DR | varchar |  | FK | SI | Debtor Number DR |
| CRBL_InvoiceBatches | varchar |  |  | SI | Invoice Batches |
| CRBL_Invoices | varchar |  |  | SI | Invoices |
| CRBL_Order | double |  |  | NO | Line Number |
| CRBL_ReceiptAmount | double |  |  | SI | Receipt Amount |
| CRBL_ReceiptNumber | varchar |  |  | SI | Receipt Number |
| CRBL_RowID | varchar |  |  | NO | - |
| CRBL_VisitNumber_DR | varchar |  | FK | SI | Visit Number DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*