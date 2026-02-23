# lab.CT_QCAMaterialLotLevel

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTQCAMLL_ParRef | varchar | PK |  | NO | CT_QCAMaterialLot Parent Reference |
| CTQCAMLL_Code | double |  |  | NO | Level Number |
| CTQCAMLL_Comments | varchar |  |  | SI | Comments |
| CTQCAMLL_Description | varchar |  |  | SI | Level Description |
| CTQCAMLL_ExpiryDate | date |  |  | SI | Expiry Date |
| CTQCAMLL_ExtendedDays | double |  |  | SI | Extended Days |
| CTQCAMLL_MarginToExpiry | double |  |  | SI | Margin To Expiry |
| CTQCAMLL_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*