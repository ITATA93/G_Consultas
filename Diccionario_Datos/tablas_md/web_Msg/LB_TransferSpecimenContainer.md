# web_Msg.LB_TransferSpecimenContainer

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBTRSPC_MsgParRef | varchar |  |  | SI | - |
| LBTRSPC_ParRef | bigint |  |  | SI | Parent Reference
Required by User.LBTransferSpeci... |
| LBTRSPC_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material DR |
| LBTRSPC_Received | varchar |  |  | SI | Received |
| LBTRSPC_RowID | varchar |  |  | SI | - |
| LBTRSPC_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container DR |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*