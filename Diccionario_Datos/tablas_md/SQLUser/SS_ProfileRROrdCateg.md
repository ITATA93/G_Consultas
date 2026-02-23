# SQLUser.SS_ProfileRROrdCateg

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RROC_ParRef | bigint | PK |  | NO | Parent table |
| RROC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RROC_IncludeExclude | varchar |  |  | SI | Include Exclude |
| RROC_OrdCat_DR | bigint |  | FK | SI | Order Category |
| RROC_OrderSubCat_DR | bigint |  | FK | SI | Order SubCategory |
| RROC_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*