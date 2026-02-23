# lab.QC_GroupComments

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCGC_RowID | varchar | PK |  | NO | - |
| QCGC_Comments | varchar |  |  | SI | Comments |
| QCGC_EntryDate | date |  |  | SI | Entry Date |
| QCGC_EntryTime | time |  |  | SI | Entry Date |
| QCGC_EntryUser_DR | varchar |  | FK | SI | Entry User |
| QCGC_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCGC_OrderNumber | varchar |  |  | NO | Order Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*