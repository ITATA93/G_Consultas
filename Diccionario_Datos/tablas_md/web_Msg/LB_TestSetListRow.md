# web_Msg.LB_TestSetListRow

**Schema:** web_Msg
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Completed | bit |  |  | SI | - |
| EpisodeID | varchar |  |  | SI | PAAdm |
| EpisodeRowCount | integer |  |  | SI | Episode Row Count |
| ID | varchar |  |  | NO | - |
| LBCQueueID | varchar |  |  | SI | - |
| LBEP_CollectionDate | varchar |  |  | SI | - |
| LBEP_CollectionTime | varchar |  |  | SI | - |
| LBEP_ReceivedDate | varchar |  |  | SI | - |
| LBEP_ReceivedTime | varchar |  |  | SI | - |
| LBEP_RefDocDesc | varchar |  |  | SI | - |
| LBSubjectID | varchar |  |  | SI | LBSubject |
| LBTR_FromLabSite_DR | bigint |  | FK | SI | - |
| LBTR_Status | varchar |  |  | SI | - |
| LBTR_ToLabSite_DR | bigint |  | FK | SI | - |
| LBTR_ToRefLab_DR | bigint |  | FK | SI | - |
| LBTS_CollectedDate | varchar |  |  | SI | - |
| LBTS_CollectedTime | varchar |  |  | SI | - |
| LBTS_Confidential | varchar |  |  | SI | LabSite |
| LBTS_Episode_DR | bigint |  | FK | SI | LBEpisode Reference
Required by User.LBTestSet. |
| LBTS_LabSite_DR | bigint |  | FK | SI | LabSite |
| LBTS_OrdItem_DR | varchar |  | FK | SI | OrderItem Reference
Required by User.LBTestSet. |
| LBTS_Priority_DR | bigint |  | FK | SI | Calculated Test Set Priority - Do not index and do... |
| LBTS_ReceivedDate | varchar |  |  | SI | - |
| LBTS_ReceivedTime | varchar |  |  | SI | - |
| LBTS_RowID | varchar |  |  | SI | - |
| LBTS_SignificantResult | varchar |  |  | SI | - |
| LBTS_StatusResult | varchar |  |  | SI | Status of Results |
| LBTS_TestSet_DR | bigint |  | FK | SI | TestSet CodeTable Reference
Required by User.LBTe... |
| LBTS_TriggerTestSet_DR | bigint |  | FK | SI | Differential Counter Trigger Test Set |
| PAPMI_Name | varchar |  |  | SI | - |
| PAPMI_Name2 | varchar |  |  | SI | - |
| PAPMI_Name3 | varchar |  |  | SI | - |
| PatientID | varchar |  |  | SI | PAPerson |
| ReadOnly | bit |  |  | SI | - |
| RowCount | integer |  |  | SI | Row count |
| Selected | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| TSLBQ_InDate | varchar |  |  | SI | - |
| TSLBQ_InTime | varchar |  |  | SI | - |
| TSLBQ_InUser | varchar |  |  | SI | - |
| Taken | varchar |  |  | SI | User_SessionId_IP of the user that has taken the e... |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*