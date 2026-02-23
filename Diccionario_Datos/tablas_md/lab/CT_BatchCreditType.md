# lab.CT_BatchCreditType

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBT_RowID | varchar | PK |  | NO | - |
| CTBT_ActiveFlag | varchar |  |  | SI | Type |
| CTBT_Audit_DR | varchar |  | FK | SI | Audit code |
| CTBT_BankingSlip | varchar |  |  | SI | Banking Slip |
| CTBT_Code | varchar |  |  | NO | Batch Credit Type |
| CTBT_Desc | varchar |  |  | SI | Description |
| CTBT_Receipt | varchar |  |  | SI | Receipt |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*