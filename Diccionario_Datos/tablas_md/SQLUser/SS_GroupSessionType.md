# SQLUser.SS_GroupSessionType

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SESS_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SESS_Childsub | double |  |  | NO | Childsub |
| SESS_RowId | varchar |  |  | NO | - |
| SESS_SessionType_DR | bigint |  | FK | SI | Des Ref SessionType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*