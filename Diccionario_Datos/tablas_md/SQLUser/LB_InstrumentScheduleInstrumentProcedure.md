# SQLUser.LB_InstrumentScheduleInstrumentProcedure

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBISIP_ParRef | varchar | PK |  | NO | Parent |
| LBISIP_InstrumentProcedureID | varchar |  |  | SI | Inbound Channel ID
For indexing only |
| LBISIP_OutboundInstrumentProcedureID | varchar |  |  | SI | Outbound Channel ID
For indexing only |
| LBISIP_PendingUpload | varchar |  |  | SI | Upload Pending
Indicates the procedure should be ... |
| LBISIP_Performed | varchar |  |  | SI | Flag to indicate if procedure has been performed |
| LBISIP_Procedures | varchar |  |  | SI | The procedures to be performed |
| LBISIP_RowID | varchar |  |  | NO | - |
| LBISIP_Transmitted | varchar |  |  | SI | Flag to indicate if procedure has been transmitted |
| Q73Q1 | - |  |  | SI | Ojo |
| Q73Q10 | - |  |  | SI | Nistagmo |
| Q73Q11 | - |  |  | SI | Motilidad supranuclear |
| Q73Q2 | - |  |  | SI | Estrabismo |
| Q73Q3 | - |  |  | SI | Paresia plano vertical |
| Q73Q4 | - |  |  | SI | Paresia plano horizontal |
| Q73Q5 | - |  |  | SI | Tamaño pupilar |
| Q73Q6 | - |  |  | SI | Reflejo pupilar directo |
| Q73Q7 | - |  |  | SI | Reflejo pupilar consensuado |
| Q73Q8 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*