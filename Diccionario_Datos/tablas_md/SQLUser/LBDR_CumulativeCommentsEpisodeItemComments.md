# SQLUser.LBDR_CumulativeCommentsEpisodeItemComments

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRCCEI_ParRef | varchar | PK |  | NO | - |
| LBDRCCEI_Comments_DR | bigint |  | FK | SI | Link to a websys.Document that stores the formated... |
| LBDRCCEI_InterpretationText_DR | bigint |  | FK | SI | Link to a websys.Document that contains the Interp... |
| LBDRCCEI_Label | varchar |  |  | SI | The Label to print with the comments.
For a TestS... |
| LBDRCCEI_RowID | varchar |  |  | NO | - |
| LBDRCCEI_Sequence | integer |  |  | SI | The Sequence of the Item (comments) within the epi... |
| Q18Q1 | - |  |  | SI | Joules |
| Q18Q2 | - |  |  | SI | Hora |
| Q18Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*