# lab.QC_GroupLink

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCGL_RowID | varchar | PK |  | NO | - |
| QCGL_Comments | varchar |  |  | SI | Comments |
| QCGL_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCGL_Level | varchar |  |  | NO | Level |
| QCGL_MaterialLotLevelDR | varchar |  | FK | SI | Material Lot Level DR |
| QCGL_QCType | varchar |  |  | NO | QC Type |
| QCGL_StartDate | date |  |  | NO | Start Date |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*