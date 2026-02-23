# SQLUser.RB_OperRoomSurgeonAssistant

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SURG_ParREf | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| SURG_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SURG_Childsub | double |  |  | NO | Childsub |
| SURG_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*