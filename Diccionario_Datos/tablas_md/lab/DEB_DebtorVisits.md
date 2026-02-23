# lab.DEB_DebtorVisits

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEBVI_ParRef | varchar | PK |  | NO | DEB_Debtor Parent Reference |
| DEBVI_AmountInvoiced | double |  |  | SI | Amount Invoiced |
| DEBVI_AmountOutstanding | double |  |  | SI | Amount Outstanding |
| DEBVI_Comments | varchar |  |  | SI | Comments |
| DEBVI_DateOfCollection | date |  |  | NO | Date Of Collection |
| DEBVI_DateOfInvoice | date |  |  | SI | Date Of Invoice |
| DEBVI_DateOfSuppress | date |  |  | SI | Date Of Suppress |
| DEBVI_DebtorAction_DR | varchar |  | FK | SI | Debtor Action |
| DEBVI_Episode_DR | varchar |  | FK | NO | Des Ref Episode |
| DEBVI_Invoice_DR | varchar |  | FK | SI | Invoice DR |
| DEBVI_RowId | varchar |  |  | NO | - |
| DEBVI_SuppressDays | numeric |  |  | SI | Suppress Days |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*