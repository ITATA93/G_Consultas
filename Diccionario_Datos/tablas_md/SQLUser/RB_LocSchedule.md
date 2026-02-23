# SQLUser.RB_LocSchedule

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LS_CTLOC_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| LS_ChildSub | double |  |  | NO | Child Sub (New Key) |
| LS_DOW_DR | double |  | FK | NO | des ref to CT DayOfWeek |
| LS_Load | double |  |  | NO | Doctor Load Default |
| LS_NoApptSession | double |  |  | NO | No of Appt per Session |
| LS_RowId | varchar |  |  | NO | - |
| LS_SessEndTime | time |  |  | NO | Session End Time |
| LS_SessStartTime | time |  |  | NO | Session Start Time |
| LS_Session | double |  |  | NO | Session |
| LS_Slot | varchar |  |  | NO | Slot Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*