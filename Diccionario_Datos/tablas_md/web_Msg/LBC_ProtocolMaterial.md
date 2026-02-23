# web_Msg.LBC_ProtocolMaterial

**Schema:** web_Msg
**Columnas:** 23
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
| LBCPTM_CreatedDate | date |  |  | SI | Created Date |
| LBCPTM_CreatedTime | time |  |  | SI | Created Time |
| LBCPTM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTM_Material_DR | bigint |  | FK | SI | Lab Material  |
| LBCPTM_Notes | varchar |  |  | SI | Notes |
| LBCPTM_ParRef | bigint |  |  | SI | Parent Protocol |
| LBCPTM_PrintLabel | varchar |  |  | SI | Print Labels |
| LBCPTM_RowID | varchar |  |  | SI | - |
| LBCPTM_SnomedTerm_DR | bigint |  | FK | SI | SNOMED Code |
| LBCPTM_Source_DR | varchar |  | FK | SI | Source Procedure |
| LBCPTM_Source_DR_Msg | varchar |  |  | SI | Source Procedure Message Object |
| LBCPTM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| Sequence | numeric |  |  | SI | [ Internal ] Structure Sequence
Used to store the... |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*