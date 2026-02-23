# SQLUser.RB_OperatingRoomSpecEquip

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EQ_ParRef | bigint | PK |  | NO | RB_OperatingRoom Parent Reference |
| EQ_APPT_DR | varchar |  | FK | SI | Des Ref APPT |
| EQ_Childsub | double |  |  | NO | Childsub |
| EQ_DateBooked | date |  |  | SI | DateBooked |
| EQ_DateRequiredTo | date |  |  | SI | Date Required To
Date to that the equipment is us... |
| EQ_DateTo | date |  |  | SI | Date To
This date is the EQDateRequiredTo + any t... |
| EQ_Duration | double |  |  | SI | Duration |
| EQ_Equip_DR | bigint |  | FK | SI | Des Ref to Equip |
| EQ_OffsetTime | time |  |  | SI | OffsetTime |
| EQ_Qty | double |  |  | SI | Quantity |
| EQ_RowId | varchar |  |  | NO | - |
| EQ_Status | varchar |  |  | SI | Starus |
| EQ_TimeBooked | time |  |  | SI | TimeBooked |
| EQ_TimeRequiredTo | time |  |  | SI | Time Required To
Time to that the equipment is us... |
| EQ_TimeTo | time |  |  | SI | Time To
This date is the EQTimeRequiredTo + any t... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*