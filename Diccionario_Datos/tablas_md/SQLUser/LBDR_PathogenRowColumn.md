# SQLUser.LBDR_PathogenRowColumn

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRPRC_ParRef | varchar | PK |  | NO | The row containing this column |
| ChildQ78DR | - |  |  | SI | Child Reference: Aspecto Físico General |
| LBDRPRC_Colour | varchar |  |  | SI | Sensitivity Colour |
| LBDRPRC_ResistantMIC | varchar |  |  | SI | Resistant MIC |
| LBDRPRC_ResultMIC | varchar |  |  | SI | Result MIC |
| LBDRPRC_RowID | varchar |  |  | NO | - |
| LBDRPRC_SensitiveMIC | varchar |  |  | SI | Sensitive MIC |
| LBDRPRC_Sensitivity | varchar |  |  | SI | The translated formatted value of the sensitivity |
| LBDRPRC_Sequence | integer |  |  | SI | The sequence number for the column, so these sort ... |
| Q253Q1 | - |  |  | SI | Evaluación |
| Q253Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*