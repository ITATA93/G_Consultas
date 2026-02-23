# SQLUser.PA_PersonScheduleItem

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ITM_ParRef | varchar | PK |  | NO | PA_PersonSchedule Parent Reference |
| ITM_Appoint_DR | varchar |  | FK | SI | Des Ref Appoint |
| ITM_ApptOffset | varchar |  |  | SI | ApptOffset |
| ITM_ApptOffsetUnit | varchar |  |  | SI | ApptOffsetUnit |
| ITM_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ITM_Childsub | double |  |  | NO | Childsub |
| ITM_ConsCateg_DR | bigint |  | FK | SI | Des Ref ConsCateg |
| ITM_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ITM_Resource_DR | bigint |  | FK | SI | Des Ref Resource |
| ITM_RowId | varchar |  |  | NO | - |
| ITM_Service_DR | bigint |  | FK | SI | Des Ref Service |
| ITM_SessType_DR | bigint |  | FK | SI | Des Ref SessType |
| ITM_WLCareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| ITM_WLHospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| ITM_WLLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| ITM_WaitListPrior_DR | bigint |  | FK | SI | Des Ref WaitListPrior |
| ITM_WaitListStat_DR | bigint |  | FK | SI | Des Ref WaitListStat |
| ITM_WaitListType_DR | bigint |  | FK | SI | Des Ref WaitListType |
| ITM_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*