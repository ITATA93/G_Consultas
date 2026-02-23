# web_Msg.LB_EpisodeReportingInterface

**Schema:** web_Msg
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CareProv_DR | varchar |  | FK | SI | Care Provider |
| Clinic_DR | bigint |  | FK | SI | Clinic |
| Copies | numeric |  |  | SI | Copies |
| ID | varchar |  |  | NO | - |
| LBEPRI_Copies | numeric |  |  | SI | Number of Copies
0 = do not produce report, resul... |
| LBEPRI_EpisodeReportingMsg_DR | varchar |  | FK | SI | - |
| LBEPRI_IsAddOn | varchar |  |  | SI | Is Add-On
N = It's entered in Lab Registration
Y... |
| LBEPRI_ParRef | varchar |  |  | SI | - |
| LBEPRI_Queue_DR | bigint |  | FK | SI | External Interface Queue |
| LBEPRI_ReportMode | varchar |  |  | SI | Report Mode |
| LBEPRI_RowID | varchar |  |  | SI | - |
| LBEPRI_TestSets | varchar |  |  | SI | A list of test sets using the report interface (On... |
| Location_DR | bigint |  | FK | SI | Location |
| MarkAsDeleted | bit |  |  | SI | If the interface has got associated recepient, mar... |
| Queue_DR | bigint |  | FK | SI | Queue |
| ReadOnly | bit |  |  | SI | - |
| ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor |
| RemoveOnAccept | bit |  |  | SI | If Recepient has been changed, set the flag to 1.... |
| ReportMode | varchar |  |  | SI | Report Mode |
| SessionId | varchar |  |  | SI | - |
| ThirdParty_DR | bigint |  | FK | SI | Third Party |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*