# lab.QCA_GroupRun

**Schema:** lab
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCAGR_RowID | varchar | PK |  | NO | - |
| QCAGR_Comments | varchar |  |  | SI | Comments |
| QCAGR_Date | date |  |  | NO | Date |
| QCAGR_GroupCodeDR | varchar |  | FK | NO | Group Code DR |
| QCAGR_QCType | varchar |  |  | NO | QC Type |
| QCAGR_RunNumber | varchar |  |  | NO | Run Number |
| QCAGR_RunTime | time |  |  | SI | Run Time |
| QCAGR_TestCodeDR | varchar |  | FK | NO | Test Code DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*