# lab.QCA_GroupLinkTestItem

**Schema:** lab
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCAGLT_ParRef | varchar | PK |  | NO | QC_GroupLink Parent Reference |
| QCAGLT_ActiveFlag | varchar |  |  | SI | Active Flag |
| QCAGLT_CalculationType | varchar |  |  | SI | Calculation Type |
| QCAGLT_Comments | varchar |  |  | SI | Comments |
| QCAGLT_DecimalPoints | varchar |  |  | SI | Decimal points |
| QCAGLT_FloatingCV | varchar |  |  | SI | Floating CV |
| QCAGLT_FloatingMean | varchar |  |  | SI | Floating mean |
| QCAGLT_FloatingSD | varchar |  |  | SI | Floating SD |
| QCAGLT_RowID | varchar |  |  | NO | - |
| QCAGLT_TargetCV | varchar |  |  | SI | Target CV |
| QCAGLT_TargetMean | varchar |  |  | SI | Target mean |
| QCAGLT_TargetSD | varchar |  |  | SI | Target SD |
| QCAGLT_TestCodeDR | varchar |  | FK | NO | Test Code DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*