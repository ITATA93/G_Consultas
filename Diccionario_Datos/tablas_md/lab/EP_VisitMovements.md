# lab.EP_VisitMovements

**Schema:** lab
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Episodio**. Registros de episodios clínicos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VISMV_ParRef | varchar | PK |  | NO | EP_VisitNumber Parent Reference |
| VISMV_DateReceived | date |  |  | SI | Date Received |
| VISMV_DateSent | date |  |  | SI | Date Sent |
| VISMV_EstimatedArrivalDate | date |  |  | SI | Estimated Arrival Date |
| VISMV_EstimatedArrivalTime | time |  |  | SI | Estimated Arrival Time |
| VISMV_FromUserSite_DR | varchar |  | FK | SI | From User Site DR |
| VISMV_Order | varchar |  |  | NO | Order |
| VISMV_PackingNumber | varchar |  |  | SI | Packing Number |
| VISMV_RowID | varchar |  |  | NO | - |
| VISMV_Status | varchar |  |  | SI | Status |
| VISMV_TempDispatchC | numeric |  |  | SI | Temp Dispatch C |
| VISMV_TempReceiveC | numeric |  |  | SI | Temp Receive C |
| VISMV_TimeReceived | time |  |  | SI | Time Received |
| VISMV_TimeSent | time |  |  | SI | Time Sent |
| VISMV_ToReferralLab_DR | varchar |  | FK | SI | To Referral Lab DR |
| VISMV_ToUserSite_DR | varchar |  | FK | SI | To User Site DR |
| VISMV_UserReceived_DR | varchar |  | FK | SI | User Received DR |
| VISMV_UserSent_DR | varchar |  | FK | SI | User Sent DR |
| VISMV_xxx1 | varchar |  |  | SI | vtsRID DR |
| VISMV_xxx2 | varchar |  |  | SI | Specimen Containers |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*