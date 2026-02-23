# SQLUser.SS_ProfileRROrdCategItems

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | Parent table |
| ITM_ARCIM_DR | varchar |  | FK | SI | Order Item |
| ITM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ITM_IncludeExclude | varchar |  |  | SI | Include / Exclude/ |
| ITM_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*