# SQLUser.RB_ResEffDateSessEpisSubtype

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBEPS_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| EBEPS_EpisSubtypeDR | bigint |  | FK | SI | Des Ref CTLOC |
| RBEPS_Childsub | double |  |  | NO | Childsub |
| RBEPS_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*