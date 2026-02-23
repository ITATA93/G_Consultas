# SQLUser.LB_Transfer

**Schema:** SQLUser
**Columnas:** 46
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBTR_RowID | bigint | PK |  | NO | - |
| ChildQ29DR | - |  |  | SI | Child Reference: Caracterización del Consumo |
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
| LBTR_Episode_DR | bigint |  | FK | NO | Lab Episode |
| LBTR_EstimatedArrivalDate | date |  |  | SI | Estimated Arrival Date |
| LBTR_EstimatedArrivalTime | time |  |  | SI | Estimated Arrival Time |
| LBTR_FinalDestination | varchar |  |  | SI | The property is the accumulation of the test sets'... |
| LBTR_FromLabSite_DR | bigint |  | FK | SI | From Lab Site |
| LBTR_Order | varchar |  |  | SI | Order |
| LBTR_PackingNumber | varchar |  |  | SI | Packing Number |
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
| Q21Q1 | - |  |  | SI | RIT / RUC / ROL |
| Q21Q2 | - |  |  | SI | Delito Tipo |
| Q21Q3 | - |  |  | SI | Delito Causa |
| Q21Q4 | - |  |  | SI | Tribunal |
| Q21Q5 | - |  |  | SI | Sanción accesoria |
| Q21Q6 | - |  |  | SI | Sanción Ley 20.084 |
| Q21Q7 | - |  |  | SI | Duración de la sanción |
| Q21Q8 | - |  |  | SI | Delegado Responsable y Fono |
| Q21Q9 | - |  |  | SI | Programa Sename |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*