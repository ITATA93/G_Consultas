# lab.QC_MaterialLotLevel

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMLL_ParRef | varchar | PK |  | NO | QC_MaterialLot Parent Reference |
| QCMLL_Code | double |  |  | NO | Level Number |
| QCMLL_Comments | varchar |  |  | SI | Comments |
| QCMLL_ExpiryDate | date |  |  | SI | Expiry Date |
| QCMLL_ExtendedDays | double |  |  | SI | Extended Days |
| QCMLL_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| QCMLL_Name | varchar |  |  | SI | Level Description |
| QCMLL_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*