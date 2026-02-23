# SQLUser.RB_ResEffDateSessionVar

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VAR_ParRef | varchar | PK |  | NO | RB_ResEffDateSession Parent Reference |
| VAR_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| VAR_Childsub | double |  |  | NO | Childsub |
| VAR_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| VAR_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| VAR_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| VAR_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| VAR_ReasonForVariance_DR | bigint |  | FK | SI | Des Ref ReasonForVariance |
| VAR_RowId | varchar |  |  | NO | - |
| VAR_SessDate | date |  |  | SI | SessDate |
| VAR_TimeArrived | time |  |  | SI | Time Arrived |
| VAR_TimeDeparted | time |  |  | SI | Time Departed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*