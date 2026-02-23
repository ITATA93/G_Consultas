# web_Msg.LB_WorksheetEntryTestSetItem

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBWSETSI_ParRef | varchar |  |  | SI | - |
| LBWSETSI_QCStatus | varchar |  |  | SI | QC Status
The display status of a qc test item on... |
| LBWSETSI_QCTestItem_DR | varchar |  | FK | SI | - |
| LBWSETSI_RowID | varchar |  |  | SI | - |
| LBWSETSI_Sequence | double |  |  | SI | - |
| LBWSETSI_TestSetItem_DR | varchar |  | FK | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*