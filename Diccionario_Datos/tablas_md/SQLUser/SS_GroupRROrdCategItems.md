# SQLUser.SS_GroupRROrdCategItems

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | SS_GroupRROrdCateg Parent Reference |
| ITM_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_IncludeExclude | varchar |  |  | SI | Include / Exclude/ |
| ITM_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*