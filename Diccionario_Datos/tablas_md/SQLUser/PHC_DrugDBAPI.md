# SQLUser.PHC_DrugDBAPI

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Farmacia Clínica**. Validación farmacéutica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| API_RowId | bigint | PK |  | NO | - |
| API_AvailabilityMethod | varchar |  |  | SI | ClassMethod to be called for API-Availability (wil... |
| API_CallMethod | varchar |  |  | NO | ClassMethod to be called for API (e.g. ##class(Reg... |
| API_CheckType | varchar |  |  | NO | CheckType e.g. DoseRange,DRINT,GENINT,AGESEX.. (St... |
| API_Code | varchar |  |  | NO | Code |
| API_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| API_Comment | varchar |  |  | SI | Comment  |
| API_ConfirmNA | varchar |  |  | SI | Confirmation on non Availability required |
| API_CreatedDate | date |  |  | SI | Created Date |
| API_CreatedTime | time |  |  | SI | Created Time |
| API_CreatedUser_DR | bigint |  | FK | SI | Created User |
| API_DateFrom | date |  |  | SI | Date From |
| API_DateTo | date |  |  | SI | Date To |
| API_Desc | varchar |  |  | NO | Description |
| API_ExternalMono | varchar |  |  | SI | Use External Monograph instead internal Y/N |
| API_ExternalMonoInfoPane | varchar |  |  | SI | When Use External Monograph use InfoPane Y/N |
| API_ExternalMonoURL | varchar |  |  | SI | URL of External Monograph |
| API_InfoPaneSize | integer |  |  | SI | Size for Infopane in % |
| API_ListSupport | varchar |  |  | SI | If API supports LastInList Flag then it get's call... |
| API_NotAvailableMsg | varchar |  |  | SI | Message shown if the API does not exists |
| API_Owner | varchar |  |  | SI | Owner |
| API_TestModeIP | varchar |  |  | SI | comma seperated list to limit the API to certain I... |
| API_UpdatedDate | date |  |  | SI | Updated Date |
| API_UpdatedTime | time |  |  | SI | Updated Time |
| API_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*