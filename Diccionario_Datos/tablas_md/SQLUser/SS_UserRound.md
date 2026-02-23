# SQLUser.SS_UserRound

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RND_ParRef | bigint | PK |  | NO | SS_User Parent Reference |
| RND_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| RND_Childsub | double |  |  | NO | Childsub |
| RND_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*