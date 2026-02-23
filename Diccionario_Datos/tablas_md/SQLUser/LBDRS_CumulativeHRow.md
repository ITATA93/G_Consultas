# SQLUser.LBDRS_CumulativeHRow

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRSCHR_ParRef | bigint | PK |  | NO | The (Header) row containing this row |
| ChildQIEP48DR | - |  |  | SI | Child Reference: ACTIVIDADES EDUCATIVAS |
| LBDRSCHR_Label | varchar |  |  | SI | Label
The translated/formatted text for
  collec... |
| LBDRSCHR_Range | varchar |  |  | SI | Ranges
The text to display (if any) for the Range... |
| LBDRSCHR_RowID | varchar |  |  | NO | - |
| LBDRSCHR_RowNo | integer |  |  | SI | The row number within the cumulative header (neede... |
| LBDRSCHR_Units | varchar |  |  | SI | Units
The text to display (if any) for the Units ... |
| QIEP47Q1 | - |  |  | SI | Lugar |
| QIEP47Q2 | - |  |  | SI | Fecha |
| QIEP47Q3 | - |  |  | SI | Hora Inicio |
| QIEP47Q4 | - |  |  | SI | Hora Fin |
| QIEP47Q5 | - |  |  | SI | Responsable |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*