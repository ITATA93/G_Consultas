# epr.CTIconProfileItem

**Schema:** epr
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| IconDR | bigint |  | FK | SI | - |
| IconGroupDR | bigint |  | FK | SI | Icon Profile item can be a single icon, or a group |
| InfoLinkContext | varchar |  |  | SI | InfoLink Context - StandardType for the various co... |
| InfoLinkDR | bigint |  | FK | SI | InfoLink Use with Specific Provider rather default |
| InfoLinkForPatient | bit |  |  | SI | InfoLink used for Care Provider (0) or Patient Inf... |
| InfoLinkMode | varchar |  |  | SI | InfoLink Mode - also indicated InfoLink Used |
| LinkChartBookDR | bigint |  | FK | SI | - |
| LinkComponent | varchar |  |  | SI | - |
| LinkExpression | varchar |  |  | SI | - |
| LinkItemDR | bigint |  | FK | SI | - |
| LinkUrl | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| Sequence | varchar |  |  | SI | - |
| ShowInfoPane | varchar |  |  | SI | - |
| UseCustomFunction | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*