# lab.CT_TestSetItems

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSD_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSD_BillingDescription | varchar |  |  | SI | Billing Description |
| CTTSD_BillingItem_DR | varchar |  | FK | NO | Des Ref Billing Item Number |
| CTTSD_EffDate | date |  |  | NO | Effective Date |
| CTTSD_Group | varchar |  |  | SI | Group |
| CTTSD_MultipleConditions | varchar |  |  | SI | Multiple Conditions |
| CTTSD_NumberOfItems | double |  |  | SI | Number Of Items |
| CTTSD_Operator | varchar |  |  | SI | Operator |
| CTTSD_RowId | varchar |  |  | NO | - |
| CTTSD_TestItem_DR | varchar |  | FK | SI | Data Item DR |
| CTTSD_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*