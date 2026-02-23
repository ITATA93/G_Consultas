# SQLUser.ARC_ItmRecLoc

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Maestro de Items**. Prestaciones, exámenes, procedimientos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCRL_RowId | varchar | PK |  | NO | - |
| ARCRL_ARCIMSub | double |  |  | NO | Subscript of ARCIM |
| ARCRL_ARCIM_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| ARCRL_CTHospitalDR | bigint |  | FK | SI | CT Hospital DR |
| ARCRL_CreatedDate | date |  |  | SI | Created Date |
| ARCRL_CreatedTime | time |  |  | SI | Created Time |
| ARCRL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCRL_DateFrom | date |  |  | SI | Date From |
| ARCRL_DateTo | date |  |  | SI | Date To |
| ARCRL_DaysOfTheWeek | varchar |  |  | SI | DaysOfTheWeek |
| ARCRL_DefaultFlag | varchar |  |  | SI | Default Flag |
| ARCRL_DispenseType | varchar |  |  | SI | Dispense Type |
| ARCRL_Function | varchar |  |  | SI | Function |
| ARCRL_OrdLoc_DR | bigint |  | FK | SI | Ordering Location |
| ARCRL_OrderPriority_DR | bigint |  | FK | SI | Des Ref OrderPriority |
| ARCRL_PRNFlag | varchar |  |  | SI | PRN Flag |
| ARCRL_RecLoc_DR | bigint |  | FK | NO | Receiving Location |
| ARCRL_Resource_DR | bigint |  | FK | SI | Equipment |
| ARCRL_Subscript | double |  |  | NO | Subscript of ARCRL |
| ARCRL_TimeFrom | time |  |  | SI | Time From |
| ARCRL_TimeTo | time |  |  | SI | Time To |
| ARCRL_UpdatedDate | date |  |  | SI | Updated Date |
| ARCRL_UpdatedTime | time |  |  | SI | Updated Time |
| ARCRL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q146Q1 | - |  |  | SI | Procedimiento a Realizar |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*