# SQLUser.RB_SesSchedule

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBSS_RowId | varchar | PK |  | NO | - |
| RBSS_ChildSub | double |  |  | NO | Child Sub |
| RBSS_DOW_DR | double |  | FK | SI | Des Ref to CTDOW |
| RBSS_Date | date |  |  | SI | Schedule Date |
| RBSS_JobId | double |  |  | NO | Job Id |
| RBSS_Load | double |  |  | NO | Load Level |
| RBSS_NoApptSlot | double |  |  | NO | Number of Appointments/Slot |
| RBSS_NoSlots | double |  |  | SI | Number of Slots/Session |
| RBSS_SessionNo | varchar |  |  | NO | Session Number |
| RBSS_SessionType_DR | bigint |  | FK | SI | Des Ref SessionType |
| RBSS_SlotLength | double |  |  | NO | Length of Each Slot in Minutes |
| RBSS_TimeEnd | time |  |  | NO | Session End Time |
| RBSS_TimeStart | time |  |  | NO | Session Start Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*