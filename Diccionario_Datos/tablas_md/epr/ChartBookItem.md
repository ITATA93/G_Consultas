# epr.ChartBookItem

**Schema:** epr
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ChartBookDR | bigint |  | FK | NO | - |
| ChartDR | bigint |  | FK | NO | - |
| ChartPosition | varchar |  |  | SI | - |
| ChartSequence | double |  |  | SI | - |
| ConditionalExpression | varchar |  |  | SI | Conditionally display chart |
| DateFrom | date |  |  | SI | - |
| DateTo | date |  |  | SI | - |
| EPRPrintHideNoData | bit |  |  | SI | Hide chart in EPR Print if no data |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*