# SQLUser.RB_ResSchedule

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RS_RES_ParRef | bigint | PK |  | NO | RB_Resource Parent Reference |
| RS_ChildSub | double |  |  | NO | Child Sub (New Key) |
| RS_DOW_DR | double |  | FK | SI | Des Ref to CT DayOfWeek |
| RS_Load | double |  |  | SI | Load Level |
| RS_NoApptSession | double |  |  | SI | Number of Appointment for this session |
| RS_RowId | varchar |  |  | NO | - |
| RS_SessEndTime | time |  |  | SI | Session End Time |
| RS_SessStartTime | time |  |  | SI | Session Start Time |
| RS_Session | varchar |  |  | SI | Session |
| RS_SessionType_DR | bigint |  | FK | SI | Des Ref Session Type |
| RS_Slot | varchar |  |  | SI | Slot Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*