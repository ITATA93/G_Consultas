# web_Msg.LB_QCBatchLevelGroupLink

**Schema:** web_Msg
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBQCBLGL_Active | varchar |  |  | SI | Active flag |
| LBQCBLGL_InstrumentSpecimenID | varchar |  |  | SI | QC Specimen ID (Cup position on tray) |
| LBQCBLGL_Instrument_DR | bigint |  | FK | SI | Link to instrument |
| LBQCBLGL_ParRef | varchar |  |  | SI | Parent Value Group
Required by User.LBQCBatchLeve... |
| LBQCBLGL_RowID | varchar |  |  | SI | - |
| LBQCBLGL_TestItem_DR | bigint |  | FK | SI | Link to the code table test item |
| LBQCBLGL_WorksheetCollapse | varchar |  |  | SI | Collapse worksheet rows (keep this QC and move to ... |
| LBQCBLGL_WorksheetGrid_DR | bigint |  | FK | SI | Worksheet Grid |
| LBQCBLGL_WorksheetPosition | integer |  |  | SI | Position on the worksheet, "absolute" row number |
| LBQCBLGL_Worksheet_DR | bigint |  | FK | SI | Link to worksheet |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*