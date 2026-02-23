# lab.CT_TestSetXM

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSO_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSO_AutoTestItem_DR | varchar |  | FK | SI | Auto Test Item DR |
| CTTSO_Description | varchar |  |  | SI | Description |
| CTTSO_Length | numeric |  |  | SI | Length |
| CTTSO_Order | numeric |  |  | NO | Order |
| CTTSO_Reportable | varchar |  |  | SI | Reportable |
| CTTSO_RowID | varchar |  |  | NO | - |
| CTTSO_Type | varchar |  |  | SI | Type |
| CTTSO_XMField_DR | varchar |  | FK | SI | XM Field DR |
| CTTSO_xxx | varchar |  |  | SI | Viewable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*