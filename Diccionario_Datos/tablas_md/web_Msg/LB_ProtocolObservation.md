# web_Msg.LB_ProtocolObservation

**Schema:** web_Msg
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Description | varchar |  |  | SI | [ Internal ] Description
The calculated procedure... |
| Hierarchy | numeric |  |  | SI | [ Internal ] Structure Hierarchy
Used to store th... |
| ID | varchar |  |  | NO | - |
| LBPTO_AddOnBy_DR | bigint |  | FK | SI | User who add unplanned |
| LBPTO_AddOnDate | date |  |  | SI | Add-on Date
Date when procedure was added unplann... |
| LBPTO_AddOnTime | time |  |  | SI | Add-on Time
Time when procedure was added unplann... |
| LBPTO_CompletedBy_DR | bigint |  | FK | SI | User who completed |
| LBPTO_CompletedDate | date |  |  | SI | Completed Date
Date when observation was complete... |
| LBPTO_CompletedTime | time |  |  | SI | Completed Time
Time when observation was complete... |
| LBPTO_InsertAfterObservation_DR_Msg | varchar |  |  | SI | - |
| LBPTO_Note | longvarchar |  |  | SI | Standard Note against this observation
HTMLRichTe... |
| LBPTO_Observation_DR | bigint |  | FK | SI | Observation |
| LBPTO_ParRef | bigint |  |  | SI | Parent Reference |
| LBPTO_Planned | bit |  |  | SI | Planned
Is this material part of the configured p... |
| LBPTO_RowID | varchar |  |  | SI | - |
| LBPTO_Source_DR | varchar |  | FK | SI | Source Material |
| LBPTO_Source_DR_Msg | varchar |  |  | SI | Source Material Message Object  |
| LBPTO_Status | varchar |  |  | SI | Status |
| LBPTO_TestSetItem_DR | varchar |  | FK | SI | Linked test set item 
Links a test set item and i... |
| ProtocolSequence | numeric |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*