# lab.CT_PrinterTypesVariables

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTPRV_ParRef | varchar | PK |  | NO | CT_PrinterTypes Parent Reference |
| CTPRV_Code | varchar |  |  | SI | Printer Type Specific Code |
| CTPRV_RowID | varchar |  |  | NO | - |
| CTPRV_Variable_DR | varchar |  | FK | NO | Variable |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*