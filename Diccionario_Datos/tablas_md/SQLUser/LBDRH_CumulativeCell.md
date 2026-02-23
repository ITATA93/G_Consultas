# SQLUser.LBDRH_CumulativeCell

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRHCC_ParRef | varchar | PK |  | NO | The row containing this cell |
| ChildQINFC25DR | - |  |  | SI | Child Reference: VACUNACIÓN |
| LBDRHCC_CellNo | integer |  |  | SI | The cell number within the row (needed because rel... |
| LBDRHCC_Indicator | varchar |  |  | SI | Result Indicator |
| LBDRHCC_IndicatorDesc | varchar |  |  | SI | Result Indicator Desc |
| LBDRHCC_ResultAbnormalFlag | varchar |  |  | SI | Calculated abnormal (external) flag for the result... |
| LBDRHCC_RowID | varchar |  |  | NO | - |
| LBDRHCC_TestSetItem_DR | varchar |  | FK | SI | Transactional DR to LBTestSetItem |
| LBDRHCC_TestSetStatus | varchar |  |  | SI | The status of the TestSet at the time an item is a... |
| LBDRHCC_Value | varchar |  |  | SI | - |
| QIC13Q1 | - |  |  | SI | Calle |
| QIC13Q2 | - |  |  | SI | Número |
| QIC13Q3 | - |  |  | SI | Depto |
| QIC13Q4 | - |  |  | SI | Provincia, Villa u Otro |
| QIC13Q5 | - |  |  | SI | Ciudad o Localidad |
| QIC13Q6 | - |  |  | SI | Comuna |
| QIC13Q7 | - |  |  | SI | Teléfono |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*