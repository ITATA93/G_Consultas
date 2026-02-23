# web_Msg.LB_ReagentSession

**Schema:** web_Msg
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBRS_ReagentBatch_DR | bigint |  | FK | SI | - |
| LBRS_TestSetRevisionReagent_DR | varchar |  | FK | SI | - |
| LBRS_TestSetRevision_DR | bigint |  | FK | SI | - |
| LBRS_Worksheet_DR | bigint |  | FK | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*