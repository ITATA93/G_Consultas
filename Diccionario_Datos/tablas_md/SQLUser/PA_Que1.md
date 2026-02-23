# SQLUser.PA_Que1

**Schema:** SQLUser
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUE1_RowID | bigint | PK |  | NO | - |
| QUE1_ArrivalDate | date |  |  | SI | Arrival Date |
| QUE1_ArrivalTime | time |  |  | SI | Arrival Time |
| QUE1_ArrivalToken | varchar |  |  | SI | Arrival Token |
| QUE1_CareProviderDR | varchar |  | FK | SI | Des Ref CTCP |
| QUE1_DateAccepted | date |  |  | SI | Date Accepted |
| QUE1_DateCollected | date |  |  | SI | Date Collected |
| QUE1_DatePacked | date |  |  | SI | Date Packed |
| QUE1_DateUnCollect | date |  |  | SI | DateUnCollect |
| QUE1_DepartmentLoc_DR | bigint |  | FK | SI | Des Ref CTLOC |
| QUE1_DepartureDate | date |  |  | SI | Departure Date |
| QUE1_DepartureTime | time |  |  | SI | Departure Time |
| QUE1_EPrescNote | varchar |  |  | SI | e-Prescription Notes |
| QUE1_EndDate | date |  |  | SI | EndDate |
| QUE1_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| QUE1_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| QUE1_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| QUE1_No | double |  |  | SI | Queue 1 No |
| QUE1_OrderDep_DR | bigint |  | FK | SI | Des Ref OrderDep |
| QUE1_PAADM_DR | bigint |  | FK | SI | Des Ref PAADM |
| QUE1_PBSPrintHistory_DR | bigint |  | FK | SI | PBS Prescription Print History |
| QUE1_PBSPrinted | varchar |  |  | SI | PBS Prescription Printed |
| QUE1_PharmStatus | varchar |  |  | SI | Pharmacy Status |
| QUE1_PrescNo | varchar |  |  | SI | Prescription No |
| QUE1_Priority | varchar |  |  | SI | Priority |
| QUE1_StartDate | date |  |  | SI | StartDate |
| QUE1_TimeAccepted | time |  |  | SI | Time Accepted |
| QUE1_TimeCollected | time |  |  | SI | Time Collected |
| QUE1_TimePacked | time |  |  | SI | Time Packed |
| QUE1_TimeUnCollect | time |  |  | SI | TimeUnCollect |
| QUE1_TransDate | date |  |  | SI | Transaction Date |
| QUE1_TransTime | time |  |  | SI | Transaction Time |
| QUE1_UserAccepted | varchar |  |  | SI | UserAccepted |
| QUE1_UserAccepted_DR | bigint |  | FK | SI | Des Ref User |
| QUE1_WaitingStatus | varchar |  |  | SI | Waiting Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*