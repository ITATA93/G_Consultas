# SQLUser.RB_SlotLabelOverride

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SLO_RowId | bigint | PK |  | NO | - |
| SLO_DOW_DR | double |  | FK | SI | Des Ref DOW |
| SLO_EndTime | time |  |  | SI | End Time |
| SLO_RBSession_DR | varchar |  | FK | SI | Des REf RBSession |
| SLO_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| SLO_SessionLabels | varchar |  |  | SI | Session Labels |
| SLO_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*