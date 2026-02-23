# SQLUser.LBDR_SNOMED

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRSNOMED_RowID | bigint | PK |  | NO | - |
| ChildQ83DR | - |  |  | SI | Child Reference: Pensamiento |
| LBDRSNOMED_HeaderText | varchar |  |  | SI | Table Header Text
The text to appear above the ta... |
| Q82Q1 | - |  |  | SI | Características |
| Q82Q2 | - |  |  | SI | Evaluación |
| Q82Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*