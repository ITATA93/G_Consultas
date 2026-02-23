# SQLUser.LBDRSNOMED_Row

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRSNOMEDR_ParRef | bigint | PK |  | NO | The SNOMED table containing this row |
| ChildQIEP43DR | - |  |  | SI | Child Reference: QUMIOPROFILAXIS Vacuna HiB u otra |
| LBDRSNOMEDR_RowID | varchar |  |  | NO | - |
| LBDRSNOMEDR_Sequence | numeric |  |  | SI | The sequence number of the row. |
| LBDRSNOMEDR_Term | varchar |  |  | SI | The SNOMED Term and Concept, formatted as required |
| QIE41Q1 | - |  |  | SI | N° Frascos Rifampicina (0 a 4 Años) |
| QIE41Q2 | - |  |  | SI | N° Frascos Rifampicina (5 a 17 Años) |
| QIE41Q3 | - |  |  | SI | N° Frascos Rifampicina (> 18 Años) |
| QIE41Q4 | - |  |  | SI | N° Frascos Rifampicina (Gestantes) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*