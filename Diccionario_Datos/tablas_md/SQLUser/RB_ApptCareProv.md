# SQLUser.RB_ApptCareProv

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**RB Module**. Funcionalidad de módulos Rich Browser.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DOC_ParRef | varchar | PK |  | NO | RB_Appointment Parent Reference |
| DOC_CareProv_DR | varchar |  | FK | SI | Des Ref Appt CareProv |
| DOC_Childsub | double |  |  | NO | Childsub |
| DOC_Date | date |  |  | SI | Date |
| DOC_LastUpdateDate | date |  |  | SI | Last Update Date |
| DOC_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| DOC_LastUpdateTime | time |  |  | SI | Last Update Time |
| DOC_LastUpdateUser_DR | bigint |  | FK | SI | Last Update User |
| DOC_Remarks | varchar |  |  | SI | Remarks |
| DOC_RowId | varchar |  |  | NO | - |
| DOC_Time | time |  |  | SI | Time |
| DOC_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*