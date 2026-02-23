# SQLUser.RB_Attendance

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ATT_RowId | bigint | PK |  | NO | - |
| ATT_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| ATT_Comments | varchar |  |  | SI | Comments |
| ATT_Date | date |  |  | SI | Date |
| ATT_FirstAttendance | varchar |  |  | SI | FirstAttendance |
| ATT_Outcome | varchar |  |  | SI | Outcome |
| ATT_PAAdm_DR | bigint |  | FK | SI | Des Ref PAAdm |
| ATT_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPMI |
| ATT_Payor_DR | bigint |  | FK | SI | Des Ref Payor |
| ATT_Plan_DR | bigint |  | FK | SI | Des Ref Plan |
| ATT_Priority | varchar |  |  | SI | Priority |
| ATT_Time | time |  |  | SI | Time |
| ATT_UpdateDate | date |  |  | SI | UpdateDate |
| ATT_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| ATT_UpdateTime | time |  |  | SI | UpdateTime |
| ATT_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*