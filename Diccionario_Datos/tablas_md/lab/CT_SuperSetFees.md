# lab.CT_SuperSetFees

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSSF_ParRef | varchar | PK |  | NO | CT_SuperSet Parent Reference |
| CTSSF_BillingDescription | varchar |  |  | SI | Billing Description |
| CTSSF_BillingItem_DR | varchar |  | FK | NO | Billing Item DR |
| CTSSF_EffDate | date |  |  | NO | Effective Date |
| CTSSF_Group | varchar |  |  | SI | Group |
| CTSSF_NumberOfItems | double |  |  | SI | Number Of Items |
| CTSSF_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*