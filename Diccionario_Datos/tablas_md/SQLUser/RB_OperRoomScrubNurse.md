# SQLUser.RB_OperRoomScrubNurse

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCRUB_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| SCRUB_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SCRUB_Childsub | double |  |  | NO | Childsub |
| SCRUB_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*