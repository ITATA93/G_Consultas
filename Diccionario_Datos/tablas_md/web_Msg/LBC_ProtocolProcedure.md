# web_Msg.LBC_ProtocolProcedure

**Schema:** web_Msg
**Columnas:** 22
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
| LBCPTP_Autocomplete | varchar |  |  | SI | Autocomplete
Indicates that this procedure is aut... |
| LBCPTP_CreatedDate | date |  |  | SI | Created Date |
| LBCPTP_CreatedTime | time |  |  | SI | Created Time |
| LBCPTP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTP_Notes | longvarchar |  |  | SI | Notes
HTMLRichText |
| LBCPTP_ParRef | bigint |  |  | SI | Parent Protocol |
| LBCPTP_Procedure_DR | bigint |  | FK | SI | Lab Procedure  |
| LBCPTP_RowID | varchar |  |  | SI | - |
| LBCPTP_Source_DR | varchar |  | FK | SI | Source Material  |
| LBCPTP_Source_DR_Msg | varchar |  |  | SI | Source Procedure Message Object  |
| LBCPTP_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTP_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*