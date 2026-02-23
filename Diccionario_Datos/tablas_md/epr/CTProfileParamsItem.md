# epr.CTProfileParamsItem

**Schema:** epr
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| Collapse | bit |  |  | SI | - |
| CombineSameItems | bit |  |  | SI | - |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| DispOrdEnteredinError | bit |  |  | SI | - |
| DisplayObsGroupComment | bit |  |  | SI | - |
| DisplayPrefs | varchar |  |  | SI | - |
| ExcludeAdminRoute | bit |  |  | SI | - |
| ExcludeOrderItems | bit |  |  | SI | - |
| ExcludeSubCat | bit |  |  | SI | - |
| Graph | bigint |  |  | SI | - |
| GroupBy | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| ITM2PRNFlagOnly | varchar |  |  | SI | filter on OEOrdItem2->ITM2PRNFlag 
for OR [Orders... |
| ItemDesc | varchar |  |  | SI | - |
| ItemType | varchar |  |  | NO | - |
| PPParameters | varchar |  |  | SI | - |
| PPType | varchar |  |  | SI | PPType is the PARENTS profile type.   (currently o... |
| Sequence | varchar |  |  | SI | - |
| ShowEnteredInError | bit |  |  | SI | - |
| SortBy | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*