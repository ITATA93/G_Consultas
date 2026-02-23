# SQLUser.RB_EventTimes

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TIME_ParRef | bigint | PK |  | NO | RB_Event Parent Reference |
| TIME_AttendeeFemaleNo | double |  |  | SI | AttendeeFemaleNo |
| TIME_AttendeeMaleNo | double |  |  | SI | AttendeeMaleNo |
| TIME_CancelReason_DR | bigint |  | FK | SI | Des Ref CancelReason |
| TIME_Charge | double |  |  | SI | Charge |
| TIME_Childsub | double |  |  | NO | Childsub |
| TIME_Date | date |  |  | SI | Date |
| TIME_EventSessionData1 | varchar |  |  | SI | EventSessionData1 |
| TIME_EventSessionData2 | varchar |  |  | SI | EventSessionData2 |
| TIME_EventSessionData3 | varchar |  |  | SI | EventSessionData3 |
| TIME_EventSessionDesc | varchar |  |  | SI | Event Session Description |
| TIME_EventSubType_DR | varchar |  | FK | SI | Des Ref EventSubType |
| TIME_ItemCat_DR | bigint |  | FK | SI | Des Ref ARCItemCat |
| TIME_NoOfAttendees | double |  |  | SI | TIME_NoOfAttendees |
| TIME_PreparationTime | time |  |  | SI | Preparation Time |
| TIME_ReviewTime | time |  |  | SI | Predicted Review Time |
| TIME_RowId | varchar |  |  | NO | - |
| TIME_StartTime | time |  |  | SI | Start Time |
| TIME_Status | varchar |  |  | SI | Status |
| TIME_TransferReason_DR | bigint |  | FK | SI | Des Ref TransferReason |
| TIME_TravelTime | time |  |  | SI | Predicted Travel Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*