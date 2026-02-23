# SQLUser.MR_ProceduresActivModif

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Procedimientos**. Intervenciones realizadas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTMOD_ParRef | varchar | PK |  | NO | MR_Procedures Parent Reference |
| ACTMOD_ActivModif_DR | bigint |  | FK | SI | Des Ref ORCActivityModifier |
| ACTMOD_Childsub | double |  |  | NO | Childsub |
| ACTMOD_RowId | varchar |  |  | NO | - |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Staff Name |
| Q06Q4 | - |  |  | SI | Check |
| Q06Q5 | - |  |  | SI | Actions |
| Q06Q6 | - |  |  | SI | Daily Assessment Notes |
| Q06Q7 | - |  |  | SI | Cuff Pressure |
| Q06Q8 | - |  |  | SI | Leak Volume |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*