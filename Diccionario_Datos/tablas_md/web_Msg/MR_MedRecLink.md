# web_Msg.MR_MedRecLink

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Medicamentos**. Prescripción y administración de fármacos. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| HasRestrictedLinkOrd | bit |  |  | SI | Mark this MRMedRecLink to contain LinkOrd that is ... |
| ID | varchar |  |  | NO | - |
| MRL_Childsub | double |  |  | SI | Childsub |
| MRL_ClassifiedVia_DR | bigint |  | FK | SI | Classified Via |
| MRL_Decision | varchar |  |  | SI | Decision |
| MRL_DecisionCommitted | bit |  |  | SI | Decision Committed |
| MRL_Discrepancy | varchar |  |  | SI | Discrepancy |
| MRL_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| MRL_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| MRL_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| MRL_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| MRL_ParRef | varchar |  |  | SI | MR_Adm Parent Reference
Required by User.MRMedRec... |
| MRL_RowId | varchar |  |  | SI | - |
| MRL_VarianceReason_DR | bigint |  | FK | SI | Variance Reason |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| ToBeDeleted | bit |  |  | SI | Mark this row to be deleted when the whole page is... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |
| web_Msg_MRL_ParRef | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*