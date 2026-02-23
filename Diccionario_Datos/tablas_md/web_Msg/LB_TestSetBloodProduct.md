# web_Msg.LB_TestSetBloodProduct

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBBloodProduct_DR | varchar |  | FK | SI | - |
| LBTSBP_ActionStatus | varchar |  |  | SI | Action Status |
| LBTSBP_ActionStatusDate | date |  |  | SI | Date the action Status was updated |
| LBTSBP_ActionStatusTime | time |  |  | SI | Time the action Status was updated |
| LBTSBP_BloodProduct_DR | bigint |  | FK | SI | Blood Product Unit tested by this test set |
| LBTSBP_OverrideReasonComment | varchar |  |  | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_OverrideReason_DR | bigint |  | FK | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_OverrideUser_DR | bigint |  | FK | SI | [DEPRECATED]Move BP-Suitability-Rule-Override deta... |
| LBTSBP_ParRef | bigint |  |  | SI | Parent TestSet DR
Required by User.LBTestSetBlood... |
| LBTSBP_RowID | varchar |  |  | SI | - |
| LBTSBP_RulesAcknowledged | varchar |  |  | SI | A flag to indicate that the user has acknowledged ... |
| LBTSBP_Sequence | numeric |  |  | SI | Blood product sequence within the test set |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*