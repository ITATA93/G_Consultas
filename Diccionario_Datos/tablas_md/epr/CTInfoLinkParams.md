# epr.CTInfoLinkParams

**Schema:** epr
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| CodeTableTags | varchar |  |  | SI | List of code table Tags |
| Context | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| Name | varchar |  |  | SI | - |
| Notes | varchar |  |  | SI | - |
| Value | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*