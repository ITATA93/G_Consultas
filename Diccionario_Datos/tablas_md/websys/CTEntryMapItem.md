# websys.CTEntryMapItem

> "Reference Map Item

**Schema:** websys
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* "Reference Map Item

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| DateFrom | date |  |  | NO | Date From |
| DateTo | date |  |  | SI | Date To |
| ID | varchar |  |  | NO | - |
| ITEM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITEM_Owner | varchar |  |  | SI | Owner - DEPRECATED - Code Table Overrides |
| TargetCode | varchar |  |  | SI | Target Description
Calculated based on the local ... |
| TargetDescription | varchar |  |  | SI | Target Description
Calculated based on the local ... |
| TargetGUID | varchar |  |  | NO | Target GUIDs |
| VendorCode | varchar |  |  | NO | Source GUID |
| VendorDescription | varchar |  |  | SI | Source Description |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*