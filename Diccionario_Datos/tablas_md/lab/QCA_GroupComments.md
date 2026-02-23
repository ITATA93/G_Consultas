# lab.QCA_GroupComments

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCAGC_RowID | varchar | PK |  | NO | - |
| QCAGC_Comments | varchar |  |  | SI | Comments |
| QCAGC_EntryDate | date |  |  | SI | Entry Date |
| QCAGC_EntryTime | time |  |  | SI | Entry Time |
| QCAGC_EntryUser_DR | varchar |  | FK | SI | Entry User |
| QCAGC_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCAGC_OrderNumber | varchar |  |  | NO | Order Number |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*