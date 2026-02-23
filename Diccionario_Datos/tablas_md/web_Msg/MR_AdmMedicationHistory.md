# web_Msg.MR_AdmMedicationHistory

**Schema:** web_Msg
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ExternalDataRetrieved | bit |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| MEDHISTMRADMID | varchar |  |  | SI | This Property is not stored.  Only needed for RowI... |
| MEDHIST_CreatedDate | date |  |  | SI | Created Date |
| MEDHIST_CreatedHospital_DR | bigint |  | FK | SI | Des Ref Created Hospital |
| MEDHIST_CreatedTime | time |  |  | SI | Created Time |
| MEDHIST_CreatedUser_DR | bigint |  | FK | SI | Created User |
| MEDHIST_NoMedHistory | varchar |  |  | SI | Patient Reports No Medication History |
| MEDHIST_PrimarySource_DR | bigint |  | FK | SI | Des Ref PHCMedHistInformSource |
| MEDHIST_ReasonForCorrection_DR | bigint |  | FK | SI | Reason for Correction |
| MEDHIST_RowId | varchar |  |  | SI | - |
| MEDHIST_SecondarySources | varchar |  |  | SI | Secondary Sources |
| MEDHIST_Status | varchar |  |  | SI | Status |
| MEDHIST_UpdateDate | date |  |  | SI | UpdateDate |
| MEDHIST_UpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MEDHIST_UpdateTime | time |  |  | SI | UpdateTime |
| MEDHIST_UpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| MenuSelected | varchar |  |  | SI | todo |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*