# web_Msg.LB_ShipmentContainer

**Schema:** web_Msg
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBSHC_AcknowledgedBy_DR | bigint |  | FK | SI | Reference to user that acknowledges action  |
| LBSHC_CourierComment | varchar |  |  | SI | Additional user comment |
| LBSHC_Courier_DR | bigint |  | FK | SI | Reference to user |
| LBSHC_DropOffDate | date |  |  | SI | Pick-off Date |
| LBSHC_DropOffTime | time |  |  | SI | Drop-off Time |
| LBSHC_FinalDestination | varchar |  |  | SI | The property is the accumulation of the shipment c... |
| LBSHC_Number | varchar |  |  | SI | Number of the container within the shipment |
| LBSHC_ParRef | bigint |  |  | SI | Parent Reference
Required by User.LBShipmentConta... |
| LBSHC_PickUpDate | date |  |  | SI | Pick-up Date |
| LBSHC_PickUpTime | time |  |  | SI | Pick-up Time |
| LBSHC_ReceivedBy_DR | bigint |  | FK | SI | User Who Received the Specimen Container  |
| LBSHC_ReceivedDate | date |  |  | SI | Date Of Receiving |
| LBSHC_ReceivedTime | time |  |  | SI | Time Of Receiving |
| LBSHC_RowID | varchar |  |  | SI | - |
| LBSHC_ShipmentBarcoded | varchar |  |  | SI | Flag to indicate if all the specimen transfers wer... |
| LBSHC_Status | varchar |  |  | SI | Transaction Status of the Shipment Container |
| LBSHC_ToLabSite_DR | bigint |  | FK | SI | To Lab Site  |
| LBSHC_ToReferralLab_DR | bigint |  | FK | SI | Referral Lab Site |
| LBSHC_WorkAreaDateIn | date |  |  | SI | Date the specimen container was received into the ... |
| LBSHC_WorkAreaTimeIn | time |  |  | SI | Time the specimen container was received into the ... |
| LBSHC_WorkAreaUserIn_DR | bigint |  | FK | SI | Work Area User In
User that received the specimen... |
| LBSHC_WorkArea_DR | bigint |  | FK | SI | Current work area
Work area into which the specim... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*