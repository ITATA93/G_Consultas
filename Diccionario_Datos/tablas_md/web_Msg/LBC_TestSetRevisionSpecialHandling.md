# web_Msg.LBC_TestSetRevisionSpecialHandling

**Schema:** web_Msg
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRSH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRSH_Converted | bit |  |  | SI | Converted Flag
Cannot be set via the UI |
| LBCTSRSH_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTSRSH_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTSRSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBCTSRSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBCTSRSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBCTSRSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBCTSRSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBCTSRSH_ParRef | bigint |  |  | SI | Parent Reference to LBCTestSetRevision |
| LBCTSRSH_RowID | varchar |  |  | SI | - |
| LBCTSRSH_Sequence | integer |  |  | SI | Sequence |
| LBCTSRSH_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*