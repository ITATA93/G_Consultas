# SQLUser.LBDRS_Cumulative

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRSC_RowID | bigint | PK |  | NO | - |
| ChildQIEP44DR | - |  |  | SI | Child Reference: TOTALES |
| LBDRSC_TestSetList | varchar |  |  | SI | Comma-list of LBCTestSetRevision IDs included in t... |
| QIE42Q1 | - |  |  | SI | Vacuna HiB u otra (0 a 4 Años) |
| QIE42Q2 | - |  |  | SI | Vacuna HiB u otra (5 a 17 Años) |
| QIE42Q3 | - |  |  | SI | Vacuna HiB u otra (> 18 Años) |
| QIE42Q4 | - |  |  | SI | Vacuna HiB u otra (Gestantes) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*