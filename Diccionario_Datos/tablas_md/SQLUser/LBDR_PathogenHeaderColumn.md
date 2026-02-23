# SQLUser.LBDR_PathogenHeaderColumn

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRPHC_ParRef | varchar | PK |  | NO | The (Header) row containing this cell |
| ChildQ251DR | - |  |  | SI | Child Reference: Evaluación Motivacional |
| LBDRPHC_Label | varchar |  |  | SI | The text to appear at the top of the column
This ... |
| LBDRPHC_PathogenLegend | varchar |  |  | SI | This text to appear as a footer in the table. |
| LBDRPHC_RowID | varchar |  |  | NO | - |
| LBDRPHC_Sequence | integer |  |  | SI | The seq number for pathogens within the row (neede... |
| Q250Q1 | - |  |  | SI | Evaluación |
| Q250Q2 | - |  |  | SI | Comentario (texto Libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*