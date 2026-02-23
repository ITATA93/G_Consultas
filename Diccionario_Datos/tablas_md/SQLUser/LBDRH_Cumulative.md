# SQLUser.LBDRH_Cumulative

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRHC_RowID | bigint | PK |  | NO | - |
| ChildQIC13DR | - |  |  | SI | Child Reference: DIRECCIÓN |
| LBDRHC_CumulativeColWidthLabels | integer |  |  | SI | Cumulative Label Column Width
The column width in... |
| LBDRHC_CumulativeColWidthRanges | integer |  |  | SI | Cumulative Ranges Column Width
The column width i... |
| LBDRHC_CumulativeColWidthResults | integer |  |  | SI | Cumulative Results Column Width
The column width ... |
| LBDRHC_CumulativeColWidthUnits | integer |  |  | SI | Cumulative Units Column Width
The column width in... |
| LBDRHC_CumulativeComments | bigint |  |  | SI | Cumulative Comments |
| QDIAG56Q1 | - |  |  | SI | Enfermedad Meningoc. |
| QDIAG56Q2 | - |  |  | SI | Meningitis |
| QDIAG56Q3 | - |  |  | SI | Enfermedad Invasiva Por Haemophilus Influenzae |
| QDIAG56Q4 | - |  |  | SI | Agente |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*