# SQLUser.RB_ReviewWorkbench

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBRW_RowId | bigint | PK |  | NO | - |
| RBRW_ApptStat | varchar |  |  | SI | Hold or Rebooked |
| RBRW_Resource_DR | bigint |  | FK | SI | Des Ref RBResource |
| RBRW_SessionId | varchar |  |  | SI | Session Id |
| RB_Appointment_DR | varchar |  | FK | SI | Des Ref RBAppointment |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*