# web_Msg.MR_MedReconciliation

**Schema:** web_Msg
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| MEDREC_Childsub | double |  |  | SI | Childsub |
| MEDREC_CommitDate | date |  |  | SI | Commit Date |
| MEDREC_CommitHospital_DR | bigint |  | FK | SI | Commit Hospital |
| MEDREC_CommitTime | time |  |  | SI | Commit Time |
| MEDREC_CommitUser_DR | bigint |  | FK | SI | Commit User |
| MEDREC_CreatedDate | date |  |  | SI | Created Date |
| MEDREC_CreatedHospital_DR | bigint |  | FK | SI | Des Ref Created Hospital |
| MEDREC_CreatedTime | time |  |  | SI | Created Time |
| MEDREC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDREC_Date | date |  |  | SI | Date |
| MEDREC_DischStatus | varchar |  |  | SI | Discharge Reconciliation Status |
| MEDREC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| MEDREC_ParRef | bigint |  |  | SI | MR_Adm Parent Reference
Required by User.MRMedRec... |
| MEDREC_Reason | varchar |  |  | SI | Reason for Reconciliation or Plan |
| MEDREC_RowId | varchar |  |  | SI | - |
| MEDREC_SnapshotDate | date |  |  | SI | Snapshot Date |
| MEDREC_SnapshotHospital_DR | bigint |  | FK | SI | Snapshot Hospital |
| MEDREC_SnapshotTime | time |  |  | SI | Snapshot Time |
| MEDREC_SnapshotUser_DR | bigint |  | FK | SI | Snapshot User |
| MEDREC_Status | varchar |  |  | SI | Reconciliation Status |
| MEDREC_Time | time |  |  | SI | Time |
| MEDREC_Type | varchar |  |  | SI | Type |
| MEDREC_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MEDREC_User_DR | bigint |  | FK | SI | Des Ref User |
| MenuSelected | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*