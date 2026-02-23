# lab.CT_QCAMaterialLot

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCAML_ParRef | varchar | PK |  | NO | CT_QCAMaterial Parent Reference |
| CTQCAML_CloseDate | date |  |  | SI | Close Date |
| CTQCAML_Comments | varchar |  |  | SI | Comments |
| CTQCAML_Description | varchar |  |  | SI | Lot Description |
| CTQCAML_ExpiryDate | date |  |  | SI | Expiry Date |
| CTQCAML_ExtendedDays | double |  |  | SI | Extended Days |
| CTQCAML_Lot | varchar |  |  | SI | Lot Number |
| CTQCAML_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| CTQCAML_OpeningDate | date |  |  | SI | Opening Date |
| CTQCAML_RowId | varchar |  |  | NO | - |
| CTQCAML_Sequence | double |  |  | NO | Sequence Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*