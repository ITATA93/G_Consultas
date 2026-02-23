# SQLUser.LBDRH_CumulativeHCell

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRHCHC_ParRef | varchar | PK |  | NO | The (Header) row containing this cell |
| ChildQIEP40DR | - |  |  | SI | Child Reference: GRUPOS ESPECÍFICOS |
| LBDRHCHC_CellNo | integer |  |  | SI | The cell number within the row (needed because rel... |
| LBDRHCHC_RowID | varchar |  |  | NO | - |
| LBDRHCHC_Value | varchar |  |  | SI | - |
| Q25Q1 | - |  |  | SI | Vacunación Hib |
| Q25Q2 | - |  |  | SI | N° Dosis Hib |
| Q25Q3 | - |  |  | SI | Fecha Vacuna Hib |
| Q25Q4 | - |  |  | SI | Vacunación Neumocóccica |
| Q25Q5 | - |  |  | SI | N° Dosis Neumocóccica |
| Q25Q6 | - |  |  | SI | Fecha Vacuna Neumocóccica |
| Q25Q7 | - |  |  | SI | Otros |
| Q25Q8 | - |  |  | SI | N° Dosis Otros |
| Q25Q9 | - |  |  | SI | Fecha Otros |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*