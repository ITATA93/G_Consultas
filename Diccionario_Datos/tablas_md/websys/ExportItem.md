# websys.ExportItem

> Data Export Framer - Items

**Schema:** websys
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* Data Export Framer - Items

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| ChildExport | bigint |  |  | SI | - |
| ChildExportSelection | varchar |  |  | SI | - |
| CustomCode | varchar |  |  | SI | - |
| FieldReference | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InUse | bit |  |  | SI | - |
| IndexOn | bit |  |  | SI |  also require working array, transformations etc |
| IsStatutoryCode | bit |  |  | SI | - |
| LocalCheckStyle | varchar |  |  | SI | Local Check code - COS code to return error and se... |
| LocalCheckTooltip | varchar |  |  | SI | - |
| Name | varchar |  |  | SI | - |
| Transformation | varchar |  |  | SI | - |
| WorkingArrayIndex | varchar |  |  | SI | - |
| WorkingArrayName | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*