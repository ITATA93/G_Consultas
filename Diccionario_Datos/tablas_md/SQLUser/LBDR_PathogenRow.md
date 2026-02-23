# SQLUser.LBDR_PathogenRow

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRPR_ParRef | bigint | PK |  | NO | The Pathogen table containing this row |
| ChildQ253DR | - |  |  | SI | Child Reference: Actividades de la Vida Diaria y T... |
| LBDRPR_Antibitotic_DR | bigint |  | FK | SI | The antibiotic for the row |
| LBDRPR_Label | varchar |  |  | SI | Label
The translated/formatted text for the descr... |
| LBDRPR_RowID | varchar |  |  | NO | - |
| LBDRPR_Sequence | integer |  |  | SI | The sequence number of the row within the table (n... |
| Q251Q1 | - |  |  | SI | Evaluación |
| Q251Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*