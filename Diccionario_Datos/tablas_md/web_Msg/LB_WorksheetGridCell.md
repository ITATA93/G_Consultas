# web_Msg.LB_WorksheetGridCell

**Schema:** web_Msg
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBWGC_Calibrator | varchar |  |  | SI | - |
| LBWGC_Column | integer |  |  | SI | The Column position of the cell
Required by User.... |
| LBWGC_ParRef | bigint |  |  | SI | Reference to the parent |
| LBWGC_PreviousOccupant | varchar |  |  | SI | Record the previous occupant of the cell if it was... |
| LBWGC_ProtocolMaterial_DR | varchar |  | FK | SI | The Material associated with the cell |
| LBWGC_QCBatchLevelGroupLink_DR | varchar |  | FK | SI | The Quality Control Group associated with the cell |
| LBWGC_ReagentOnly | varchar |  |  | SI | - |
| LBWGC_Row | integer |  |  | SI | The Row position of the cell
Required by User.LBW... |
| LBWGC_RowID | varchar |  |  | SI | - |
| LBWGC_SpecimenContainer_DR | bigint |  | FK | SI | The Specimen Container associated with the cell |
| LBWGC_Voided | varchar |  |  | SI | - |
| QCLinkMsg | varchar |  |  | SI | The Quality Control Group Link message object - te... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*