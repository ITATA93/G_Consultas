# lab.CR_CreditBatch

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRBT_RowID | varchar | PK |  | NO | - |
| CRBT_AmountTotal | double |  |  | SI | Amount Total |
| CRBT_AuditCode_DR | varchar |  | FK | SI | Audit Code DR |
| CRBT_AuditNumber | double |  |  | SI | Audit Number |
| CRBT_BankingCode_DR | varchar |  | FK | SI | Banking Code |
| CRBT_Code | varchar |  |  | NO | Batch number |
| CRBT_CreditType_DR | varchar |  | FK | SI | Credit Type |
| CRBT_DateOfAudit | date |  |  | SI | Audit Date |
| CRBT_DateOfCreation | date |  |  | SI | Batch Date |
| CRBT_DateOfPosting | date |  |  | SI | Date Of Posting |
| CRBT_Lines | numeric |  |  | SI | Number of lines |
| CRBT_Status | varchar |  |  | SI | Batch Status |
| CRBT_SuppressPrintReceipts | varchar |  |  | SI | Suppress Print Receipts |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*