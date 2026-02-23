# SQLUser.RB_ApptStatePPP

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SPPP_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| SPPP_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| SPPP_Childsub | double |  |  | NO | Childsub |
| SPPP_Date | date |  |  | SI | Date |
| SPPP_LastUpdateDate | date |  |  | SI | Last Update Date |
| SPPP_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| SPPP_LastUpdateTime | time |  |  | SI | Last Update Time |
| SPPP_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| SPPP_Remarks | varchar |  |  | SI | Remarks |
| SPPP_RowId | varchar |  |  | NO | - |
| SPPP_StatePPP_DR | bigint |  | FK | SI | Des Ref State PPP |
| SPPP_Time | time |  |  | SI | Time |
| SPPP_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*