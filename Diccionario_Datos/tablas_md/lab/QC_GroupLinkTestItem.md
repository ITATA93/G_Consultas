# lab.QC_GroupLinkTestItem

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCGLT_ParRef | varchar | PK |  | NO | QC_GroupLink Parent Reference |
| QCGLT_CalculationType | varchar |  |  | SI | Calculation Type |
| QCGLT_Comments | varchar |  |  | SI | Comments |
| QCGLT_FloatingCV | varchar |  |  | SI | Floating CV |
| QCGLT_FloatingMean | varchar |  |  | SI | Floating mean |
| QCGLT_FloatingSD | varchar |  |  | SI | Floating SD |
| QCGLT_RowID | varchar |  |  | NO | - |
| QCGLT_TargetCV | varchar |  |  | SI | Target CV |
| QCGLT_TargetMean | varchar |  |  | SI | Target mean |
| QCGLT_TargetSD | varchar |  |  | SI | Target SD |
| QCGLT_TestItemDR | varchar |  | FK | NO | Test Code DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*