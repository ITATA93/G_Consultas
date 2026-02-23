# lab.QC_GroupRun

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCGR_RowID | varchar | PK |  | NO | - |
| QCGR_Comments | varchar |  |  | SI | Comments |
| QCGR_Date | date |  |  | NO | Date |
| QCGR_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCGR_Run | varchar |  |  | NO | Run |
| QCGR_RunTime | time |  |  | SI | Run Time |
| QCGR_TestItemDR | varchar |  | FK | NO | Test Code DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*