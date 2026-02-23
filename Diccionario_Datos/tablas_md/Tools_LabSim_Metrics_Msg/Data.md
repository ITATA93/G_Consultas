# Tools_LabSim_Metrics_Msg.Data

**Schema:** Tools_LabSim_Metrics_Msg
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AuthorisationMode | varchar |  |  | SI | Authorisation Mode  |
| AuthorisedHourBlock | integer |  |  | SI | Hour Block the Test was Authorised |
| AuthorisedToPrintedEE | integer |  |  | SI | Authorised To Printed EE |
| AuthorisedToPrintedRB | integer |  |  | SI | Authorised To Printed RB |
| AuthorisedToReportStart | integer |  |  | SI | Authorised To ReportStart |
| EnteredHourBlock | integer |  |  | SI | Hour Block the Test was Entered |
| EnteredToAuthorised | integer |  |  | SI | Entered To Authorised |
| ExtInterfaceQueueDate | date |  |  | SI | Ext Interface Queue Date |
| ExtInterfaceQueueTime | time |  |  | SI | Ext Interface Queue Time |
| LBCTSRCODE | varchar |  |  | SI | Test Set Revision Code |
| LBDRBBatchDate | date |  |  | SI | Doctor Report Start Date  |
| LBDRBBatchTime | time |  |  | SI | Doctor Report Start Time |
| LBDRBPrintDate | date |  |  | SI | Report Printed Date |
| LBDRBPrintTime | time |  |  | SI | Report Printed Time |
| LBISResultReceivedDate | date |  |  | SI | Date the last result was received |
| LBISResultReceivedTime | time |  |  | SI | Time the last result was received |
| LBISScheduleDate | date |  |  | SI | Date the test was scheduled |
| LBISScheduleTime | time |  |  | SI | Time the test was scheduled |
| LBISTransmissionDate | date |  |  | SI | Date the test was transmitted last |
| LBISTransmissionTime | time |  |  | SI | Time the test was transmitted last |
| LBInstrumentScheduleID | varchar |  |  | SI | Instrument Schedule ID |
| LBTSAuthoriseDate | date |  |  | SI | AuthoriseDate |
| LBTSAuthoriseTime | time |  |  | SI | Authorise Time |
| LBTSAuthorisedByDR | bigint |  | FK | SI | User who (last) Authorised the result |
| LBTSEnteredDate | date |  |  | SI | EnteredDate |
| LBTSEnteredTime | time |  |  | SI | EnteredTime |
| LBTSOrderDate | date |  |  | SI | Order Date |
| LBTSOrderTime | time |  |  | SI | Order Time |
| LBTSReceivedDate | date |  |  | SI | Received Date |
| LBTSReceivedTime | time |  |  | SI | Received Time |
| LBTSTestSetDR | bigint |  | FK | SI | Test Set Revision ID |
| LBTestSetDR | bigint |  | FK | SI | LB Test Set ID |
| OrderToReceive | integer |  |  | SI | Order To Receive |
| OrderedHourBlock | integer |  |  | SI | Hour Block the Test was ordered |
| PrintedHourBlock | integer |  |  | SI | Hour Block the Test was Printed |
| ReceiveToEntered | integer |  |  | SI | Receive To Entered |
| ReceivedHourBlock | integer |  |  | SI | Hour Block the Test was Received |
| ReceivedToAuthorised | integer |  |  | SI | Received To Authorised |
| ReceivedToScheduled | integer |  |  | SI | Instrument: Received To Scheduled |
| ReportPrintedToExtIntQueue | integer |  |  | SI | Report Printed To External Interface Queue |
| ReportStartToReportPrinted | integer |  |  | SI | Report Start to Report Printed |
| ScheduledToTransmit | integer |  |  | SI | Instrument: Scheduled To Transmit |
| TransmitToResultReceived | integer |  |  | SI | Instrument: Transmit To Result Received |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*