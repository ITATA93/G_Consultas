# SQLUser.LBDRH_CumulativeRow

**Schema:** SQLUser
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRHCR_ParRef | bigint | PK |  | NO | The cumulative containing this row |
| ChildQIEP42DR | - |  |  | SI | Child Reference: QUMIOPROFILAXIS RIFAMPICINA |
| LBDRHCR_Label | varchar |  |  | SI | Label
The translated/formatted text for the descr... |
| LBDRHCR_Range | varchar |  |  | SI | Ranges
The text to display (if any) for the Norma... |
| LBDRHCR_RowID | varchar |  |  | NO | - |
| LBDRHCR_RowNo | integer |  |  | SI | The row number within the cumulative (needed becau... |
| LBDRHCR_Units | varchar |  |  | SI | Units
The text to display (if any) for the Units ... |
| QIE40Q1 | - |  |  | SI | N° Cáp. Ciprofloxacino (0 a 4 Años) |
| QIE40Q2 | - |  |  | SI | N° Cáp. Ciprofloxacino (5 a 17 Años) |
| QIE40Q3 | - |  |  | SI | N° Cáp. Ciprofloxacino (> 18 Años) |
| QIE40Q4 | - |  |  | SI | N° Cáp. Ciprofloxacino (Gestantes) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*