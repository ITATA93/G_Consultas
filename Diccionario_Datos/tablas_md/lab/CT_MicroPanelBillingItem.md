# lab.CT_MicroPanelBillingItem

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPC_ParRef | varchar | PK |  | NO | CT_MicrobiologyPanel Parent Reference |
| CTMPC_BillingItem_DR | varchar |  | FK | NO | Billing Item DR |
| CTMPC_Date | date |  |  | NO | Effective Date |
| CTMPC_Description | varchar |  |  | SI | Description |
| CTMPC_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*