# SQLUser.LBDR_PathogenHeader

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRPH_ParRef | bigint | PK |  | NO | The Pathogen table containing this header row |
| ChildQ250DR | - |  |  | SI | Child Reference: Sexualidad |
| LBDRPH_Label | varchar |  |  | SI | Label
The translated/formatted text for the Colum... |
| LBDRPH_RowID | varchar |  |  | NO | - |
| LBDRPH_Sequence | integer |  |  | SI | The sequence number of the row within the header (... |
| Q85Q1 | - |  |  | SI | Características |
| Q85Q2 | - |  |  | SI | Evaluación |
| Q85Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*