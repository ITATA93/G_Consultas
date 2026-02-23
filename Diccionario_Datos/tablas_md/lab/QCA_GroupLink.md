# lab.QCA_GroupLink

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Relación entre entidades.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCAGL_RowID | varchar | PK |  | NO | - |
| QCAGL_Comments | varchar |  |  | SI | Comments |
| QCAGL_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCAGL_Level | varchar |  |  | NO | Level |
| QCAGL_MaterialLotLevelDR | varchar |  | FK | SI | Material Lot Level DR |
| QCAGL_QCType | varchar |  |  | NO | QC Type |
| QCAGL_StartDate | date |  |  | NO | Start Date |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*