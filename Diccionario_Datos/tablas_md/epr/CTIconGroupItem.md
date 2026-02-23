# epr.CTIconGroupItem

**Schema:** epr
**Columnas:** 13
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
| LinkChartBookDR | bigint |  | FK | SI | - |
| LinkComponent | bigint |  |  | SI | - |
| LinkExpression | varchar |  |  | SI | - |
| LinkItemDR | bigint |  | FK | SI | - |
| LinkUrl | varchar |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| Sequence | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*