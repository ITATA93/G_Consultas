# lab.BI_ManualPricingAmounts

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Business Intelligence**. Cubos y reportes analíticos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BIMPA_ParRef | varchar | PK |  | NO | BI_ManualPricing Parent Reference |
| BIMPA_Amount | double |  |  | SI | Amount |
| BIMPA_Description | varchar |  |  | SI | Description |
| BIMPA_GST | varchar |  |  | SI | GST |
| BIMPA_InitiationItem | varchar |  |  | SI | Initiation Item |
| BIMPA_Item_DR | varchar |  | FK | NO | Billing Item DR |
| BIMPA_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*