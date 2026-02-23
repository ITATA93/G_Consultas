# web_Msg.LBWorkStatusFind

**Schema:** web_Msg
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| CollectedDateFrom | date |  |  | SI | Collected Date From |
| CollectedDateTo | date |  |  | SI | Collected Date To |
| CollectedTimeFrom | time |  |  | SI | Collected Time From |
| CollectedTimeTo | time |  |  | SI | Collected Time To |
| DepartmentID | varchar |  |  | SI | The id of the selected department. Used in LBWorkS... |
| Departments | varchar |  |  | SI | A comma-delimited list of the selected departments |
| FromDate | date |  |  | SI | The selected search start date. Used in LBWorkStat... |
| FromTime | time |  |  | SI | The selected search start time. Used in LBWorkStat... |
| ID | varchar |  |  | NO | - |
| IncludeFinalStatus | varchar |  |  | SI | Include summary data for test sets with a final st... |
| LabSiteID | varchar |  |  | SI | The id of the selected lab site. Used in LBWorkSta... |
| LabSites | varchar |  |  | SI | A comma-delimited list of the selected lab sites |
| ReadOnly | bit |  |  | SI | - |
| ReceivedDateFrom | date |  |  | SI | Received Date From |
| ReceivedDateTo | date |  |  | SI | Received Date To |
| ReceivedTimeFrom | time |  |  | SI | Received Time From |
| ReceivedTimeTo | time |  |  | SI | Received Time To |
| ResultStatus | varchar |  |  | SI | The id of the selected test set status. Used in LB... |
| SessionId | varchar |  |  | SI | - |
| ShowReportPending | varchar |  |  | SI | Include summary data on test sets that are still o... |
| ShowUnregistered | varchar |  |  | SI | Work that may have been received but has not been ... |
| SpecimenMaterialLabSite | varchar |  |  | SI | Specimen Material Lab Site Filter |
| TestSetList | varchar |  |  | SI | List of selected test sets as comma separated stri... |
| TestSetStatusList | varchar |  |  | SI | acts as a search filter for test sets that current... |
| TestSetStatuses | varchar |  |  | SI | A comma-delimited list of the selected test set st... |
| ToDate | date |  |  | SI | The selected search end date. Used in LBWorkStatus... |
| ToTime | time |  |  | SI | The selected search end time. Used in LBWorkStatus... |
| WorkAreaList | varchar |  |  | SI | List of selected work areas |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*