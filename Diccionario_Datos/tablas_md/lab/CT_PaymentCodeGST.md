# lab.CT_PaymentCodeGST

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPCI_ParRef | varchar | PK |  | NO | CT_PaymentCode Parent Reference |
| CTPCI_Date | date |  |  | NO | Start Date |
| CTPCI_GST_BillingItem_DR | varchar |  | FK | SI | GST Billing Item DR |
| CTPCI_GST_Description | varchar |  |  | SI | GST Description |
| CTPCI_GST_Percent | double |  |  | SI | GST Percent |
| CTPCI_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*