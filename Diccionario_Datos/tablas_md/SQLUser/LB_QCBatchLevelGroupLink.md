# SQLUser.LB_QCBatchLevelGroupLink

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBQCBLGL_ParRef | varchar | PK |  | NO | Parent Value Group |
| LBQCBLGL_Active | varchar |  |  | SI | Active flag |
| LBQCBLGL_Closed | varchar |  |  | SI | Closed |
| LBQCBLGL_InstrumentSpecimenID | varchar |  |  | SI | QC Specimen ID (Cup position on tray) |
| LBQCBLGL_Instrument_DR | bigint |  | FK | SI | Link to instrument |
| LBQCBLGL_RowID | varchar |  |  | NO | - |
| LBQCBLGL_TestItem_DR | bigint |  | FK | SI | Link to the code table test item |
| LBQCBLGL_WorksheetCollapse | varchar |  |  | SI | Collapse worksheet rows (keep this QC and move to ... |
| LBQCBLGL_WorksheetGrid_DR | bigint |  | FK | SI | Worksheet Grid |
| LBQCBLGL_WorksheetPosition | integer |  |  | SI | Position on the worksheet, "absolute" row number |
| LBQCBLGL_Worksheet_DR | bigint |  | FK | SI | Link to worksheet |
| Q15Q1 | - |  |  | SI | Nombre |
| Q15Q2 | - |  |  | SI | Profesión |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*