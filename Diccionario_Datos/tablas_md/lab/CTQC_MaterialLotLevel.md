# lab.CTQC_MaterialLotLevel

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCMLL_ParRef | varchar | PK |  | NO | QC_MaterialLot Parent Reference |
| CTQCMLL_Code | double |  |  | NO | Level Number |
| CTQCMLL_Comments | varchar |  |  | SI | Comments |
| CTQCMLL_Description | varchar |  |  | SI | Level Description |
| CTQCMLL_ExpiryDate | date |  |  | SI | Expiry Date |
| CTQCMLL_ExtendedDays | double |  |  | SI | Extended Days |
| CTQCMLL_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| CTQCMLL_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*