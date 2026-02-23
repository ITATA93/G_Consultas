# websys.DSSEventItem

**Schema:** websys
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| BooleanOperator | varchar |  |  | SI | - |
| ClassProperty | varchar |  |  | SI | - |
| ComponentItem | varchar |  |  | SI | - |
| ConditionIsDate | bit |  |  | SI | - |
| ConditionValue | varchar |  |  | SI | - |
| ConditionalOperator | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | - |
| EventItemID | varchar |  |  | SI | Store other event item id which depends on the cur... |
| EventItemType | varchar |  |  | SI | - |
| GroupingCount | integer |  |  | SI | - |
| GroupingOperator | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| INTConditionValue | varchar |  |  | SI | - |
| ItemFriendlyName | varchar |  |  | SI | - |
| LeftParen | varchar |  |  | SI | - |
| MeasurementUnit | varchar |  |  | SI | - |
| MedTrakFunction | varchar |  |  | SI | - |
| RightParen | varchar |  |  | SI | - |
| Rule | bigint |  |  | SI | - |
| Sequence | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| dspEventItem | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*