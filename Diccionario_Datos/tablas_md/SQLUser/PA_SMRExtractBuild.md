# SQLUser.PA_SMRExtractBuild

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMREB_RowId | bigint | PK |  | NO | - |
| SMREB_AcceptRejectDate | date |  |  | SI | AcceptRejectDate |
| SMREB_AcceptRejectHospital_DR | bigint |  | FK | SI | Des Ref AcceptRejectHospital_DR |
| SMREB_AcceptRejectTime | time |  |  | SI | AcceptRejectTime |
| SMREB_AcceptRejectUser_DR | bigint |  | FK | SI | Des Ref AcceptRejectUser |
| SMREB_BatchCount | double |  |  | SI | Batch Count |
| SMREB_BatchNumber | double |  |  | SI | Batch Number |
| SMREB_EndDate | date |  |  | SI | End Date |
| SMREB_ExtractCount | double |  |  | SI | Extract Count |
| SMREB_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| SMREB_LastSent | date |  |  | SI | Last Sent |
| SMREB_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| SMREB_LastUserHospital_DR | bigint |  | FK | SI | Des Ref LastUserHospital |
| SMREB_PAExtract_DR | bigint |  | FK | SI | Des Ref PAExtract |
| SMREB_RecordType | varchar |  |  | SI | Record Type |
| SMREB_RunDate | date |  |  | SI | Run Date |
| SMREB_RunLocation_DR | bigint |  | FK | SI | Des Ref RunLocation |
| SMREB_RunTime | time |  |  | SI | Run Time |
| SMREB_SentByUser_DR | bigint |  | FK | SI | Des Ref User |
| SMREB_StartDate | date |  |  | SI | Start Date |
| SMREB_Status | varchar |  |  | SI | Status |
| SMREB_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*