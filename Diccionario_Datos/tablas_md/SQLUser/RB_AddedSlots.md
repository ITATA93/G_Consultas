# SQLUser.RB_AddedSlots

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADD_RowId | bigint | PK |  | NO | - |
| ADD_ApptSchedFrom_DR | varchar |  | FK | SI | Des Ref ApptSchedFrom |
| ADD_ApptSched_DR | varchar |  | FK | SI | Des Ref Appt Sched |
| ADD_Date | date |  |  | SI | Date |
| ADD_DateFrom | date |  |  | SI | DateFrom |
| ADD_EndTime | time |  |  | SI | End Time |
| ADD_NumberOfSlots | double |  |  | SI | Number Of Slots |
| ADD_ResourceFrom_DR | bigint |  | FK | SI | Des Ref ResourceFrom |
| ADD_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| ADD_StartTime | time |  |  | SI | Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*