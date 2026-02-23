# lab.QC_MaterialLot

**Schema:** lab
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCML_ParRef | varchar | PK |  | NO | QC_Material Parent Reference |
| QCML_CloseDate | date |  |  | SI | Close Date |
| QCML_Code | double |  |  | NO | Sequence Number |
| QCML_Comments | varchar |  |  | SI | Comments |
| QCML_CurrentLot | varchar |  |  | SI | Current Lot Y/N |
| QCML_ExpiryDate | date |  |  | SI | Expiry Date |
| QCML_ExtendedDays | double |  |  | SI | Extended Days |
| QCML_Lot | varchar |  |  | SI | Lot Number |
| QCML_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| QCML_Name | varchar |  |  | SI | Lot Description |
| QCML_OpeningDate | date |  |  | SI | Opening Date |
| QCML_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*