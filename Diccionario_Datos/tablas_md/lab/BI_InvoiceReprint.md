# lab.BI_InvoiceReprint

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Business Intelligence**. Cubos y reportes analíticos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BIIR_RowID | varchar | PK |  | NO | - |
| BIIR_Date | date |  |  | NO | Date |
| BIIR_Episode_DR | varchar |  | FK | NO | Episode DR |
| BIIR_Flag | varchar |  |  | SI | Printed Flag |
| BIIR_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*