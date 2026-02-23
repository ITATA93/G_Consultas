# lab.BI_ManualPricingItems

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Business Intelligence**. Cubos y reportes analíticos. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BIMPI_ParRef | varchar | PK |  | NO | BI_ManualPricing Parent Reference |
| BIMPI_Description | varchar |  |  | SI | Description |
| BIMPI_GST | varchar |  |  | SI | GST |
| BIMPI_InitiationItem | varchar |  |  | SI | Initiation Item |
| BIMPI_Item_DR | varchar |  | FK | NO | Billing Item DR |
| BIMPI_Quantity | double |  |  | SI | Quantity |
| BIMPI_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*