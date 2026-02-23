# lab.JOU_Journal

**Schema:** lab
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| JOU_ROWID | varchar | PK |  | NO | - |
| JOU_AlternateAddress1 | varchar |  |  | SI | Alternate Address1 |
| JOU_AlternateAddress2 | varchar |  |  | SI | Alternate Address2 |
| JOU_AlternateAddress3_Suburb | varchar |  |  | SI | Alternate Address3 Suburb |
| JOU_AlternateAddress4_State | varchar |  |  | SI | Alternate Address4 State |
| JOU_AlternateAddress5_PostCode | varchar |  |  | SI | Alternate Address5 Post Code |
| JOU_AlternatePayee | varchar |  |  | SI | Alternate Payee |
| JOU_Amount | double |  |  | SI | Amount |
| JOU_AmountGST | double |  |  | SI | Amount GST |
| JOU_AmountGSTFree | double |  |  | SI | Amount GST Free |
| JOU_AmountGSTTaxable | double |  |  | SI | Amount GST Taxable |
| JOU_AmountInDebtor | double |  |  | SI | Debtor Amount Calc |
| JOU_BillLocation_DR | varchar |  | FK | SI | Billing Location DR |
| JOU_Comment | varchar |  |  | SI | Comment |
| JOU_Company_DR | varchar |  | FK | SI | Company |
| JOU_Date | date |  |  | NO | Date |
| JOU_DateOfCollection | date |  |  | SI | Date Of Collection |
| JOU_DebtorNewBalance | double |  |  | SI | Debtor New Balance |
| JOU_DebtorNumber_DR | varchar |  | FK | SI | Debtor Number DR |
| JOU_DebtorOldBalance | double |  |  | SI | Debtor Old Balance |
| JOU_Episode_DR | varchar |  | FK | NO | Episode_DR |
| JOU_Invoice | varchar |  |  | SI | Invoice |
| JOU_JournalCode_DR | varchar |  | FK | NO | Journal Code |
| JOU_Order | varchar |  |  | NO | Order number |
| JOU_Printed | varchar |  |  | SI | Printed |
| JOU_User_DR | varchar |  | FK | SI | User_DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*