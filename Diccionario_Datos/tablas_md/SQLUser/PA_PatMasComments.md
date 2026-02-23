# SQLUser.PA_PatMasComments

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMT_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| CMT_Childsub | double |  |  | NO | Childsub |
| CMT_Comments | varchar |  |  | SI | Comments |
| CMT_Date | date |  |  | SI | Date |
| CMT_FutureDate | date |  |  | SI | Future Date |
| CMT_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| CMT_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| CMT_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| CMT_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| CMT_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| CMT_OnHold | varchar |  |  | SI | OnHold |
| CMT_RowId | varchar |  |  | NO | - |
| CMT_ShortDesc | varchar |  |  | SI | Short Description |
| CMT_Time | time |  |  | SI | Time |
| CMT_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*