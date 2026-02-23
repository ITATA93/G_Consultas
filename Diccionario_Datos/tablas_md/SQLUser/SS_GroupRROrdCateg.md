# SQLUser.SS_GroupRROrdCateg

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RRCAT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| RRCAT_Childsub | double |  |  | NO | Childsub |
| RRCAT_IncludeExclude | varchar |  |  | SI | Include Exclude |
| RRCAT_OrdCat_DR | bigint |  | FK | SI | Des Ref OrdCat |
| RRCAT_OrderSubCat_DR | bigint |  | FK | SI | Des Ref OrderSubCat |
| RRCAT_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*