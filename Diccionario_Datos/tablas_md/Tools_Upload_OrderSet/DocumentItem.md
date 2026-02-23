# Tools_Upload_OrderSet.DocumentItem

**Schema:** Tools_Upload_OrderSet
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| Key | varchar |  |  | SI | Type of content e.g. (NARR, ITEM, SECT) |
| Level | varchar |  |  | SI | to keep order of values from Vendor 
import build... |
| Link | varchar |  |  | SI | the content for the given key at the given level |
| Value | varchar |  |  | SI | the content for the given key at the given level |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*