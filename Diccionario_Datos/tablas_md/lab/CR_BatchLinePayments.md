# lab.CR_BatchLinePayments

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CRBLA_ParRef | varchar | PK |  | NO | CR_BatchLine Parent Reference |
| CRBLA_Amount | double |  |  | SI | Amount of Credit |
| CRBLA_Bank_DR | varchar |  | FK | SI | Bank |
| CRBLA_CardExpiry | varchar |  |  | SI | Card Expiry Date |
| CRBLA_CreditCard_DR | varchar |  | FK | SI | Credit Card |
| CRBLA_DrawerAuth | varchar |  |  | SI | Drawer Auth |
| CRBLA_Order | numeric |  |  | NO | Order number |
| CRBLA_ReferenceDate | date |  |  | SI | Reference Date |
| CRBLA_ReferenceNumber | varchar |  |  | SI | Cheque/Card Number/Reference number |
| CRBLA_RowID | varchar |  |  | NO | - |
| CRBLA_Type | varchar |  |  | SI | Type of credit |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*