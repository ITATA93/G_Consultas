# SQLUser.LBDR_OrderQuestion

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDROQ_ParRef | varchar | PK |  | NO | - |
| ChildQ85DR | - |  |  | SI | Child Reference: Introspección y Juicio |
| LBDROQ_Answer | varchar |  |  | SI | Answer |
| LBDROQ_CollectionDate | date |  |  | SI | Episode Collection Date for Sorting Purpose Only |
| LBDROQ_CollectionTime | time |  |  | SI | Episode Collection Date for Sorting Purpose Only |
| LBDROQ_EpisodeNo | varchar |  |  | SI | Episode No |
| LBDROQ_Question | varchar |  |  | SI | Question |
| LBDROQ_RowID | varchar |  |  | NO | - |
| Q84Q1 | - |  |  | SI | Características |
| Q84Q2 | - |  |  | SI | Evaluación |
| Q84Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*