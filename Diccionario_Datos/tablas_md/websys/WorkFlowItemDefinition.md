# websys.WorkFlowItemDefinition

**Schema:** websys
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Caption | varchar |  |  | SI | - |
| Chart | bigint |  |  | SI | - |
| ChartBook | bigint |  |  | SI | - |
| Component | bigint |  |  | SI | - |
| Deprecated | bit |  |  | SI | - |
| Description | varchar |  |  | NO | - |
| DisplayChart | bigint |  |  | SI | - |
| DoNotDisplay | bit |  |  | SI | - |
| Name | varchar |  |  | NO | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| ShortDescription | varchar |  |  | SI | - |
| Url | varchar |  |  | NO | - |
| Worklist | bigint |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*