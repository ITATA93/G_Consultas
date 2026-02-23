# web_Msg.LB_Transfer

**Schema:** web_Msg
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTR_AutomaticSendAway | varchar |  |  | SI | Flag to indicate if the transfer was automatically... |
| LBTR_Comments | varchar |  |  | SI | Comments |
| LBTR_CourierComments | varchar |  |  | SI | Courier Comments |
| LBTR_DailyNumber | numeric |  |  | SI | Daily Counter 
Will store the daily counter betwe... |
| LBTR_DateChangedStatus | date |  |  | SI | Date latest changed status |
| LBTR_DateInit | date |  |  | SI | Date Added to Transfers list |
| LBTR_DateReceived | date |  |  | SI | Date Received |
| LBTR_DateSent | date |  |  | SI | Date Sent |
| LBTR_DestinationChangeReason_DR | bigint |  | FK | SI | Record the reason why a transfer would have their ... |
| LBTR_Episode_DR | bigint |  | FK | SI | Lab Episode
Required by User.LBTransfer. |
| LBTR_EstimatedArrivalDate | date |  |  | SI | Estimated Arrival Date |
| LBTR_EstimatedArrivalTime | time |  |  | SI | Estimated Arrival Time |
| LBTR_FinalDestination | varchar |  |  | SI | The property is the accumulation of the test sets'... |
| LBTR_FromLabSite_DR | bigint |  | FK | SI | From Lab Site |
| LBTR_Order | varchar |  |  | SI | Order |
| LBTR_PackingNumber | varchar |  |  | SI | Packing Number |
| LBTR_RowID | varchar |  |  | SI | - |
| LBTR_SPCReceiveStatus | varchar |  |  | SI | Specimen Container Receive Status
LBTransferSPCSt... |
| LBTR_ShipmentBarcoded | varchar |  |  | SI | Flag to indicate if the specimen transfer was barc... |
| LBTR_ShipmentContainerSeq | numeric |  |  | SI | Position in Shipment Container |
| LBTR_ShipmentContainer_DR | varchar |  | FK | SI | Shipment Container |
| LBTR_ShipmentSeq | numeric |  |  | SI | Position in Shipment  |
| LBTR_Shipment_DR | bigint |  | FK | SI | ShipmentO |
| LBTR_Status | varchar |  |  | SI | Transaction Status
LBTransferStatus standard type |
| LBTR_TempReceived | numeric |  |  | SI | Receive Temp |
| LBTR_TempSent | numeric |  |  | SI | Sent Temp   |
| LBTR_TestSetList | varchar |  |  | SI | Test Set List |
| LBTR_TimeChangedStatus | time |  |  | SI | Time latest changed status |
| LBTR_TimeInit | time |  |  | SI | Time Added to Transfers list |
| LBTR_TimeReceived | time |  |  | SI | Time Received |
| LBTR_TimeSent | time |  |  | SI | Time Sent |
| LBTR_ToLabSite_DR | bigint |  | FK | SI | To Lab Site  |
| LBTR_ToReferralLab_DR | bigint |  | FK | SI | To Referral Lab |
| LBTR_UserReceived_DR | bigint |  | FK | SI | Received By User |
| LBTR_UserSent_DR | bigint |  | FK | SI | Sent By User  |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| SpecimenContainer_DR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*