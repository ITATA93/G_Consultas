# SQLUser.PA_WaitingListNotAvailable

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| NA_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| NA_CTPCP_DR | varchar |  | FK | SI | Des Ref Care Provider |
| NA_Childsub | double |  |  | NO | Childsub |
| NA_Comments | varchar |  |  | SI | Comments |
| NA_ContactResponseDate | date |  |  | SI | ContactResponseDate |
| NA_Date | date |  |  | SI | Date |
| NA_DateDelete | date |  |  | SI | DateDelete |
| NA_DateFrom | date |  |  | SI | Date From |
| NA_DateFromProcessedFlag | varchar |  |  | SI | Date From Processed Flag |
| NA_DateTo | date |  |  | SI | Date To |
| NA_ExcludeFromWaiting | varchar |  |  | SI | Exclude From Waiting |
| NA_IndefiniteEndDate | varchar |  |  | SI | Indefinite End Date |
| NA_ProcessedFlag | varchar |  |  | SI | ProcessedFlag |
| NA_ReasonForList_DR | bigint |  | FK | SI | Des Ref ReasonForList |
| NA_Reason_DR | bigint |  | FK | SI | Des Ref Reason Not Avail |
| NA_ReviewDate | date |  |  | SI | ReviewDate |
| NA_RowId | varchar |  |  | NO | - |
| NA_SuspensionIndicator_DR | bigint |  | FK | SI | Des Ref Suspension Indicator |
| NA_Time | time |  |  | SI | Time |
| NA_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| NA_User_DR | bigint |  | FK | SI | Des Ref User |
| NA_WLType_DR | bigint |  | FK | SI | Des Ref WLType |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*