# lab.CTQC_MaterialLot

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCML_ParRef | varchar | PK |  | NO | QC_Material Parent Reference |
| CTQCML_CloseDate | date |  |  | SI | Close Date |
| CTQCML_Comments | varchar |  |  | SI | Comments |
| CTQCML_Description | varchar |  |  | SI | Lot Description |
| CTQCML_ExpiryDate | date |  |  | SI | Expiry Date |
| CTQCML_ExtendedDays | double |  |  | SI | Extended Days |
| CTQCML_Lot | varchar |  |  | SI | Lot Number |
| CTQCML_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| CTQCML_OpeningDate | date |  |  | SI | Opening Date |
| CTQCML_RowId | varchar |  |  | NO | - |
| CTQCML_Sequence | double |  |  | NO | Sequence Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*