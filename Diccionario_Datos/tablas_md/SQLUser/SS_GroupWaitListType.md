# SQLUser.SS_GroupWaitListType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WLT_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| WLT_Childsub | double |  |  | NO | Childsub |
| WLT_RowId | varchar |  |  | NO | - |
| WLT_WaitListType_DR | bigint |  | FK | SI | Des Ref WaitListType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*