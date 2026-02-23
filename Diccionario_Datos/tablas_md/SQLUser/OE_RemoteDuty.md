# SQLUser.OE_RemoteDuty

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REMOD_RowId | bigint | PK |  | NO | - |
| ChildQ71DR | - |  |  | SI | Child Reference: Special Test (+ or - ) |
| Q70Q1 | - |  |  | SI | Muscle |
| Q70Q2 | - |  |  | SI | Strength Left |
| Q70Q3 | - |  |  | SI | Strength Right |
| Q70Q4 | - |  |  | SI | Resisted Isometric Test |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REMOD_CareprovText | varchar |  |  | SI | Free Text CareProvider/Caller placing the order |
| REMOD_ContactNoText | varchar |  |  | SI | Contact Number |
| REMOD_DMOSeenByDate | date |  |  | SI | Seen By DMO Date |
| REMOD_DMOSeenByTime | time |  |  | SI | Seen By DMO Time |
| REMOD_HospNotifDate | date |  |  | SI | Hospital Notified Date |
| REMOD_HospNotifTime | time |  |  | SI | Hospital Notified Time |
| REMOD_OEORI_DR | varchar |  | FK | NO | OEOrdItem DR |
| REMOD_PlaceOfOrder | varchar |  |  | SI | Free Text Location placing the order |
| REMOD_PlanCallBackBy_DR | bigint |  | FK | SI | Planned Call Back By |
| REMOD_PlanCallBackDate | date |  |  | SI | Planned Call Back Date |
| REMOD_PlanCallBackTime | time |  |  | SI | Planned Call Back Time |
| REMOD_RecCareProvText | varchar |  |  | SI | Recieving Consultant Free Text |
| REMOD_RecCareProv_DR | varchar |  | FK | SI | Receiving Consultant |
| REMOD_ReferPrio_DR | bigint |  | FK | SI | Referral Priority |
| REMOD_Remarks | varchar |  |  | SI | Other Details / Remarks |
| REMOD_RetAcceptDate | date |  |  | SI | Retrieval Accepted Date |
| REMOD_RetAcceptTime | time |  |  | SI | Retrieval Accepted Time |
| REMOD_RetArriveDestDate | date |  |  | SI | Retrieval Arrival Date at Destination |
| REMOD_RetArriveDestTime | time |  |  | SI | Retrieval Arrival Time at Destination |
| REMOD_RetDepartBaseDate | date |  |  | SI | Retrieval Departed Date from Base |
| REMOD_RetDepartBaseTime | time |  |  | SI | Retrieval Departed Time from Base |
| REMOD_RetDepartDestDate | date |  |  | SI | Retrieval Departed Date from Destination |
| REMOD_RetDepartDestTime | time |  |  | SI | Retrieval Departed Time from Destination |
| REMOD_RetETABaseDate | date |  |  | SI | Retrieval Estimated Date of Arrival back at base (... |
| REMOD_RetETABaseTime | time |  |  | SI | Retrieval Estimated Time of Arrival back at base (... |
| REMOD_RetPlanDate | date |  |  | SI | Retrieval Planned Date |
| REMOD_RetPlanTime | time |  |  | SI | Retrieval Planned Time |
| REMOD_RetPrio_DR | bigint |  | FK | SI | Retrieval Priority |
| REMOD_RetTransp_DR | bigint |  | FK | SI | Retrieval Transport |
| REMOD_TransferLoc_DR | bigint |  | FK | SI | Transfer Location |
| REMOD_Triaged | varchar |  |  | SI | Triaged / Ready for MO Review |
| REMOD_Type | varchar |  |  | NO | Remote Duty Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*