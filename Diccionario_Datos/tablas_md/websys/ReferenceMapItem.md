# websys.ReferenceMapItem

> "Reference Map Item

**Schema:** websys
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

*Descripción original:* "Reference Map Item

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| AcceptSource | bit |  |  | SI | Accept Source
This item is exempt from the mappin... |
| ID | varchar |  |  | NO | - |
| SourceDescription | varchar |  |  | SI | Source Description |
| SourceGUID | varchar |  |  | NO | Source GUID |
| TargetDescription | varchar |  |  | SI | Target Description
Calculated based on the local ... |
| TargetGUIDs | varchar |  |  | SI | Target GUIDs |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*