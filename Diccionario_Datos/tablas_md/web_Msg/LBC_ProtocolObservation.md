# web_Msg.LBC_ProtocolObservation

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| Description | varchar |  |  | SI | [ Internal ] Description
The calculated procedure... |
| Hierarchy | numeric |  |  | SI | [ Internal ] Structure Hierarchy
Used to store th... |
| ID | varchar |  |  | NO | - |
| LBCPTO_CreatedDate | date |  |  | SI | Created Date |
| LBCPTO_CreatedTime | time |  |  | SI | Created Time |
| LBCPTO_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTO_Notes | varchar |  |  | SI | Notes |
| LBCPTO_Observation_DR | bigint |  | FK | SI | Lab Obserrvation |
| LBCPTO_ParRef | bigint |  |  | SI | Parent Protocol |
| LBCPTO_RowID | varchar |  |  | SI | - |
| LBCPTO_Source_DR | varchar |  | FK | SI | Source Material |
| LBCPTO_Source_DR_Msg | varchar |  |  | SI | Source Procedure Message Object  |
| LBCPTO_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTO_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTO_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*