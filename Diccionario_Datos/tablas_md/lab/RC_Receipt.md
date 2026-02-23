# lab.RC_Receipt

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RCPT_RowID | varchar | PK |  | NO | - |
| RCPT_AmountCash | numeric |  |  | SI | Amount Cash |
| RCPT_AmountOthers | numeric |  |  | SI | Amount Others |
| RCPT_Company_DR | varchar |  | FK | SI | Company |
| RCPT_CreditBatchLine_DR | varchar |  | FK | SI | Credit BatchLine DR |
| RCPT_Number | varchar |  |  | NO | Receipt Number |
| RCPT_PrintedDate | date |  |  | SI | Printed Date |
| RCPT_PrintedTime | time |  |  | SI | Printed Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*