# web_Msg.LB_ProtocolMaterial

**Schema:** web_Msg
**Columnas:** 36
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
| LBPTM_AddOnBy_DR | bigint |  | FK | SI | User who add unplanned |
| LBPTM_AddOnDate | date |  |  | SI | Add-on Date
Date when procedure was added unplann... |
| LBPTM_AddOnTime | time |  |  | SI | Add-on Time
Time when procedure was added unplann... |
| LBPTM_Billable | varchar |  |  | SI | Billable Flag
Indicates that this material is bil... |
| LBPTM_CompletedBy_DR | bigint |  | FK | SI | User who completed |
| LBPTM_CompletedDate | date |  |  | SI | Completed Date
Date when material was completed |
| LBPTM_CompletedTime | time |  |  | SI | Completed Time
Time when material was completed |
| LBPTM_Disposed | bit |  |  | SI | Disposed Flag |
| LBPTM_InsertAfterObservation_DR_Msg | varchar |  |  | SI | Helps determine sequence during initial insert in ... |
| LBPTM_LabSite_DR | bigint |  | FK | SI | Lab site of the protocol material |
| LBPTM_MaterialNumber | varchar |  |  | SI | Material Number |
| LBPTM_Material_DR | bigint |  | FK | SI | Observations
Material |
| LBPTM_ParRef | bigint |  |  | SI | Parent Reference |
| LBPTM_Planned | bit |  |  | SI | Planned
Is this material part of the configured p... |
| LBPTM_Printed | bit |  |  | SI | Printed
Is this material printed |
| LBPTM_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material CT Reference
Can only be used f... |
| LBPTM_ReferralLab_DR | bigint |  | FK | SI | Referral Lab Site for protocol material |
| LBPTM_RowID | varchar |  |  | SI | - |
| LBPTM_Source_DR | varchar |  | FK | SI | Source Procedure |
| LBPTM_Source_DR_Msg | varchar |  |  | SI | Source Procedure Message Object |
| LBPTM_Status | varchar |  |  | SI | Status |
| LBPTM_StorageDate | date |  |  | SI | Date Of Storage Change (Stored/Disposed/Not in Sto... |
| LBPTM_StorageTime | time |  |  | SI | Time Of Storage Change (Stored/Disposed/Not in Sto... |
| LBPTM_StoredBy_DR | bigint |  | FK | SI | User Who done Storage Change |
| LBPTM_TestSetItems | varchar |  |  | SI | Linked test set items
Results sent for this mater... |
| LBPTM_WorkArea_DR | bigint |  | FK | SI | - |
| ProtocolSequence | numeric |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*