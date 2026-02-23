# SQLUser.PA_SocHist

**Schema:** SQLUser
**Columnas:** 46
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SCH_PAPMI_ParRef | bigint | PK |  | NO | Des Ref to PAPMI |
| SCH_AlcoholFlag | varchar |  |  | SI | Drinker Flag |
| SCH_ApproxOnsetDate | varchar |  |  | SI | ApproxOnsetDate |
| SCH_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| SCH_ChildSub | numeric |  |  | NO | Social History ChildSub |
| SCH_Comments | varchar |  |  | SI | Comments |
| SCH_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| SCH_Date | date |  |  | SI | Date |
| SCH_Desc | varchar |  |  | SI | Description |
| SCH_DuratDays | double |  |  | SI | Duration in Days |
| SCH_DuratMonth | double |  |  | SI | Duration in Month |
| SCH_DuratYear | double |  |  | SI | Duration in Year |
| SCH_Duration | varchar |  |  | SI | Duration |
| SCH_DurationDesc | varchar |  |  | SI | DurationDesc |
| SCH_EndCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| SCH_EndCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit]  |
| SCH_EndCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| SCH_EndCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| SCH_EndCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| SCH_EndCalcDateBase | date |  |  | SI | date calculated date is based on |
| SCH_EndDate | date |  |  | SI | EndDate |
| SCH_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| SCH_ExerDuration | double |  |  | SI | Duration For Each Exercise |
| SCH_ExerWeek | double |  |  | SI | Time Of Exercise Per Week |
| SCH_ExternalID | varchar |  |  | SI | ExternalID |
| SCH_HabitCeased | varchar |  |  | SI | HabitCeased |
| SCH_HabitsQty_DR | varchar |  | FK | SI | Des Ref to MRCHabitsQty |
| SCH_Habits_DR | bigint |  | FK | SI | Des Ref to MRCHabits |
| SCH_InActive | varchar |  |  | SI | InActive |
| SCH_NoHistoryOf | varchar |  |  | SI | NoHistoryOf |
| SCH_OnsetCalcDateAge | integer |  |  | SI | Calculated date "at the age of" |
| SCH_OnsetCalcDateAgeUnit | varchar |  |  | SI | Calculated date units "at the age of [num] [unit]  |
| SCH_OnsetCalcDateAgo | varchar |  |  | SI | Calculated date ago or from "[num] [unit] ago on/f... |
| SCH_OnsetCalcDateAgoNum | integer |  |  | SI | Calculated date number of units "[num] [unit] ago ... |
| SCH_OnsetCalcDateAgoUnit | varchar |  |  | SI | Calculated date units "[num] [unit] ago/from" |
| SCH_OnsetCalcDateBase | date |  |  | SI | date calculated date is based on |
| SCH_OnsetDate | date |  |  | SI | Onset Date |
| SCH_RcFlag | varchar |  |  | SI | Archived Flag |
| SCH_RowId | varchar |  |  | NO | - |
| SCH_SmokerFlag | varchar |  |  | SI | Smoker Flag |
| SCH_SocDate | date |  |  | SI | Date |
| SCH_Time | time |  |  | SI | Time |
| SCH_UpdateDate | date |  |  | SI | UpdateDate |
| SCH_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| SCH_UpdateTime | time |  |  | SI | UpdateTime |
| SCH_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*