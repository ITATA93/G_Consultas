# lab.QC_MaterialLotType

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMLT_ParRef | varchar | PK |  | NO | QC_MaterialLot Parent Reference |
| QCMLT_Code | varchar |  |  | NO | QC Type - (W)orksheet / (M)achine |
| QCMLT_RowID | varchar |  |  | NO | - |
| QCMLT_WsMach | varchar |  |  | NO | Worksheet / Machine Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*