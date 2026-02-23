# lab.QC_MLTTestCodeLevel

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMTL_ParRef | varchar | PK |  | NO | QC_MLTTestCode Parent Reference |
| QCMTL_CalcType | varchar |  |  | SI | Calculation Type |
| QCMTL_FixedMean | varchar |  |  | SI | Fixed Mean |
| QCMTL_FixedSD | varchar |  |  | SI | Fixed SD |
| QCMTL_FloatingMean | varchar |  |  | SI | Floating Mean |
| QCMTL_FloatingSD | varchar |  |  | SI | Floating SD |
| QCMTL_Level | varchar |  |  | NO | Level |
| QCMTL_PreviousMean | varchar |  |  | SI | Previous Mean |
| QCMTL_PreviousPeriodClosingDate | date |  |  | SI | Previous Period Closing Date |
| QCMTL_PreviousPoints | double |  |  | SI | Previous Number of Points |
| QCMTL_PreviousSD | varchar |  |  | SI | Previous SD |
| QCMTL_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*