# lab.BI_ReBill

**Schema:** lab
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Business Intelligence**. Cubos y reportes analíticos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BIRB_RowID | varchar | PK |  | NO | - |
| BIRB_CollectionCentre_DR | varchar |  | FK | SI | Collection Centre DR |
| BIRB_CompanyCode_DR | varchar |  | FK | SI | Company Code |
| BIRB_Date | date |  |  | NO | Date |
| BIRB_DateOfCollection | date |  |  | SI | Date Of Collection |
| BIRB_DebtorNumber_DR | varchar |  | FK | SI | Debtor Number DR |
| BIRB_Episode_DR | varchar |  | FK | NO | Episode DR |
| BIRB_Flag | varchar |  |  | SI | Flag |
| BIRB_InitiationCode_DR | varchar |  | FK | SI | Initiation Code DR |
| BIRB_InvoiceBatch_OLD | numeric |  |  | SI | BIRB_InvoiceBatch_OLD |
| BIRB_ListOfvtsRID | varchar |  |  | SI | List of vtsRIDs |
| BIRB_NewDVA | varchar |  |  | SI | New DVA |
| BIRB_NewFundNumber | varchar |  |  | SI | New Fund Number |
| BIRB_NewFundTable | varchar |  |  | SI | New Fund Table |
| BIRB_NewMedicare | varchar |  |  | SI | New Medicare |
| BIRB_NewMedicareRef | varchar |  |  | SI | New Medicare Ref |
| BIRB_NewPensioner | varchar |  |  | SI | New Pensioner |
| BIRB_NewReference | varchar |  |  | SI | New Reference |
| BIRB_PayCode_New_DR | varchar |  | FK | SI | Pay Code New DR |
| BIRB_PayCode_Old_DR | varchar |  | FK | SI | Pay Code Old DR |
| BIRB_Printed | varchar |  |  | SI | Printed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*