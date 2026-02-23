# SQLUser.LBDR_Pathogens

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRP_RowID | bigint | PK |  | NO | - |
| ChildQ79DR | - |  |  | SI | Child Reference: Conducta Motora |
| Footnote | varchar |  |  | SI | Footer String to be added at the end of table. |
| Q78Q1 | - |  |  | SI | Características |
| Q78Q2 | - |  |  | SI | Evaluación |
| Q78Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*