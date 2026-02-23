# epr.CTWorklistItemDef

**Schema:** epr
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Deprecated | bit |  |  | SI | - |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| ReasonDeprecated | varchar |  |  | SI | - |
| WITComponentDR | bigint |  | FK | SI | - |
| WITDefaultParamsDR | bigint |  | FK | SI | - |
| WITDesc | varchar |  |  | NO | - |
| WITName | varchar |  |  | NO | - |
| WITParamComponentDR | bigint |  | FK | SI | - |
| WITUrl | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*