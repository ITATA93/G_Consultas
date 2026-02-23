# SQLUser.LB_InstrumentScheduleInstrumentTestItem

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBISITI_ParRef | varchar | PK |  | NO | Parent |
| ChildQ61DR | - |  |  | SI | Child Reference: Cardiaco |
| LBISITI_AntibInstrumentTestItemID | varchar |  |  | SI | Inbound Antibiotic Result Instrument Test Item ID ... |
| LBISITI_AntibOutboundInstrumentTestItemID | varchar |  |  | SI | Outbound Antibiotic Order Instrument Test Item ID ... |
| LBISITI_BloodProductIDs | varchar |  |  | SI | Blood Product IDs
The blood product (donor sample... |
| LBISITI_HoldAntibioticOrder | varchar |  |  | SI | Hold antibiotic order until organism result has be... |
| LBISITI_InstrumentTestItemID | varchar |  |  | SI | Inbound Channel ID
For indexing only, copy of LBC... |
| LBISITI_OutboundInstrumentTestItemID | varchar |  |  | SI | Outbound Channel ID
For indexing only, copy of LB... |
| LBISITI_PendingUpload | varchar |  |  | SI | Pending Upload
Indicates the test item should be ... |
| LBISITI_Performed | varchar |  |  | SI | Flag to indicate if test item has been performed |
| LBISITI_PerformedOnInstrument_DR | bigint |  | FK | SI | Instrument the test item has been performed |
| LBISITI_RowID | varchar |  |  | NO | - |
| LBISITI_Status | varchar |  |  | SI | Status of the scheduled test item
Standard Type: ... |
| LBISITI_TestItem_DR | bigint |  | FK | SI | Test Item
Used for indexing which LBCTestItem the... |
| LBISITI_TestSetBloodProducts | varchar |  |  | SI | Links to blood products (donor samples) to be test... |
| LBISITI_TestSetItems | varchar |  |  | SI | The test set items to be performed |
| LBISITI_TestSetRevisionItems | varchar |  |  | SI | The test set revision items to be performed |
| LBISITI_Transmitted | varchar |  |  | SI | Flag to indicate if test item has been transmitted... |
| Q58Q1 | - |  |  | SI | Percusión |
| Q58Q2 | - |  |  | SI | Auscultación |
| Q58Q3 | - |  |  | SI | Localización |
| Q58Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*