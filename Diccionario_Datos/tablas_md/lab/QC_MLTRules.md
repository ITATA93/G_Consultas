# lab.QC_MLTRules

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMTR_ParRef | varchar | PK |  | NO | QC_MaterialLotType Parent Reference |
| QCMTR_Colour | varchar |  |  | SI | Colour |
| QCMTR_Comments | varchar |  |  | SI | Comments |
| QCMTR_Order | double |  |  | NO | Order Number |
| QCMTR_RowID | varchar |  |  | NO | - |
| QCMTR_Rules_DR | varchar |  | FK | SI | Rules DR |
| QCMTR_Status | varchar |  |  | SI | Status |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*