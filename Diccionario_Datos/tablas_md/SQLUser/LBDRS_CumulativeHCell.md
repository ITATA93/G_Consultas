# SQLUser.LBDRS_CumulativeHCell

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRSCHC_ParRef | varchar | PK |  | NO | The (Header) row containing this cell |
| ChildQIEP47DR | - |  |  | SI | Child Reference: VISITA EPIDEMIOLÓGICA |
| LBDRSCHC_CellNo | integer |  |  | SI | The cell number within the row (needed because rel... |
| LBDRSCHC_RowID | varchar |  |  | NO | - |
| LBDRSCHC_Value | varchar |  |  | SI | - |
| QIEP44Q1 | - |  |  | SI | Total N° Contactos |
| QIEP44Q2 | - |  |  | SI | Total N° Cáp. Ciprofloxacino |
| QIEP44Q3 | - |  |  | SI | Total N° Frascos Rifampicina |
| QIEP44Q4 | - |  |  | SI | Total Vacuna HiB u Otra |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*