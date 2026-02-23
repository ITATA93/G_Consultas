# SQLUser.LBDRH_CumulativeHRow

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRHCHR_ParRef | bigint | PK |  | NO | The cumulative containing this header row |
| ChildQIEP41DR | - |  |  | SI | Child Reference: QUIMIOPROFILAXIS CIPROFLOXACINO |
| LBDRHCHR_Label | varchar |  |  | SI | Label
The translated/formatted text for
  collec... |
| LBDRHCHR_Range | varchar |  |  | SI | Ranges
The text to display (if any) for the Range... |
| LBDRHCHR_RowID | varchar |  |  | NO | - |
| LBDRHCHR_RowNo | integer |  |  | SI | The row number within the cumulative header (neede... |
| LBDRHCHR_Units | varchar |  |  | SI | Units
The text to display (if any) for the Units ... |
| QIEP40Q1 | - |  |  | SI | Grupos |
| QIEP40Q2 | - |  |  | SI | N° de Contactos 0 a 4 Años |
| QIEP40Q3 | - |  |  | SI | N° de Contactos 5 a 17 Años |
| QIEP40Q4 | - |  |  | SI | N° de Contactos > 18 Años |
| QIEP40Q5 | - |  |  | SI | N° de Contactos Gestantes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*