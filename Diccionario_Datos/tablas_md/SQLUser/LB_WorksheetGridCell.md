# SQLUser.LB_WorksheetGridCell

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBWGC_ParRef | bigint | PK |  | NO | Reference to the parent |
| ChildQ45DR | - |  |  | SI | Child Reference: Extremidades |
| LBWGC_Calibrator | varchar |  |  | SI | - |
| LBWGC_Column | integer |  |  | NO | The Column position of the cell |
| LBWGC_PreviousOccupant | varchar |  |  | SI | Record the previous occupant of the cell if it was... |
| LBWGC_ProtocolMaterial_DR | varchar |  | FK | SI | The Material associated with the cell |
| LBWGC_QCBatchLevelGroupLink_DR | varchar |  | FK | SI | The Quality Control Group associated with the cell |
| LBWGC_ReagentOnly | varchar |  |  | SI | - |
| LBWGC_Row | integer |  |  | NO | The Row position of the cell |
| LBWGC_RowID | varchar |  |  | NO | - |
| LBWGC_SpecimenContainer_DR | bigint |  | FK | SI | The Specimen Container associated with the cell |
| LBWGC_Voided | varchar |  |  | SI | - |
| Q39Q1 | - |  |  | SI | Palpación |
| Q39Q2 | - |  |  | SI | Percusión |
| Q39Q3 | - |  |  | SI | Auscultación |
| Q39Q4 | - |  |  | SI | Localización |
| Q39Q5 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*