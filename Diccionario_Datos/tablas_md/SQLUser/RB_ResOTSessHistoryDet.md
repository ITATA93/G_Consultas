# SQLUser.RB_ResOTSessHistoryDet

**Schema:** SQLUser
**Columnas:** 30
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | varchar | PK |  | NO | RB_ResOTSessHistory Parent Reference |
| DET_CPActive | varchar |  |  | SI | OT session CP Active |
| DET_CPActualArrivalTime | time |  |  | SI | OT session CP Actual Arrival Time, copied from ASC... |
| DET_CPAddedDate | date |  |  | SI | OT session CP Added Date |
| DET_CPAddedTime | time |  |  | SI | OT session CP Added Time |
| DET_CPEffDtDateFrom | date |  |  | SI | Effective Date Session CP Date From |
| DET_CPEffDtDateTo | date |  |  | SI | Effective Date Session CP Date To |
| DET_CPLastUpdateDate | date |  |  | SI | OT session CP Last Update Date |
| DET_CPLastUpdateTime | time |  |  | SI | OT session CP Last Update Time |
| DET_CPLastUpdateUser_DR | bigint |  | FK | SI | OT session CP Last Update User |
| DET_CPReason_DR | bigint |  | FK | SI | OT session CP Reason For Variance  |
| DET_CPRole | varchar |  |  | SI | OT session CP Role, standard type AnaestOtherStaff... |
| DET_CPSession_DR | varchar |  | FK | SI | OT session CP Eff Date Session  |
| DET_CPStatus | varchar |  |  | SI | OT session CP Status D Deleted,S Swapped,O Overrid... |
| DET_CPType | varchar |  |  | SI | OT session CP Type, S for Surgeon, A for Anaesthet... |
| DET_CareProv_DR | varchar |  | FK | SI | OT session CP  |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_EffDtSessSetting | varchar |  |  | SI | RS Effective Date Session Setting |
| DET_NonCPAttendeeDetails | varchar |  |  | SI | Non CP Attendee Details |
| DET_OperatingStaffRole_DR | bigint |  | FK | SI | Des Ref ORC_OperatingStaffRole |
| DET_RowId | varchar |  |  | NO | - |
| DET_SPAddedDate | date |  |  | SI | OT session Specialty Added Date |
| DET_SPAddedTime | time |  |  | SI | OT session Specialty Added Time |
| DET_SPEffDtDateFrom | date |  |  | SI | Effective Date Session Specialty Date From |
| DET_SPEffDtDateTo | date |  |  | SI | Effective Date Session Specialty Date To |
| DET_SPEffDtMain | varchar |  |  | SI | Effective Date Session or OT Session override Spec... |
| DET_SPLastUpdateDate | date |  |  | SI | OT session Specialty Last Update Date |
| DET_SPLastUpdateTime | time |  |  | SI | OT session Specialty Last Update Time |
| DET_SPLastUpdateUser_DR | bigint |  | FK | SI | OT session Specialty Last Update User |
| DET_Specialty_DR | bigint |  | FK | SI | OT session Specialty Des Ref CTLoc |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*