# web_Msg.LB_WorksheetEntry

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBWSE_Episode_DR | bigint |  | FK | SI | The Lab episode for this entry row |
| LBWSE_ParRef | bigint |  |  | SI | - |
| LBWSE_QCLink_DR | varchar |  | FK | SI | Linked QC |
| LBWSE_RowID | varchar |  |  | SI | - |
| LBWSE_SequenceNumber | numeric |  |  | SI | Sort order of the worksheet entries |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*