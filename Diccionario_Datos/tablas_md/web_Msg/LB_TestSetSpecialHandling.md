# web_Msg.LB_TestSetSpecialHandling

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Exámenes de Laboratorio**. Solicitudes y resultados.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBRQTSSHRowID | varchar |  |  | SI | - |
| LBTSSH_HideForCollection | varchar |  |  | SI | Hide for Collection |
| LBTSSH_HideForProcessing | varchar |  |  | SI | Hide for Processing |
| LBTSSH_HideForReceive | varchar |  |  | SI | Hide for Receive |
| LBTSSH_HideForStorage | varchar |  |  | SI | Hide for Storage |
| LBTSSH_HideForTransfers | varchar |  |  | SI | Hide for Transfers |
| LBTSSH_ParRef | bigint |  |  | SI | - |
| LBTSSH_RowID | varchar |  |  | SI | - |
| LBTSSH_SpecialHandling_DR | bigint |  | FK | SI | Special Handling Instructions |
| LBTestSetMsg_DR | varchar |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*