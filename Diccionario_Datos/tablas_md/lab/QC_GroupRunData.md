# lab.QC_GroupRunData

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCGRD_ParRef | varchar | PK |  | NO | QC_GroupRun Parent Reference |
| QCGRD_Comments | varchar |  |  | SI | Comments |
| QCGRD_Editable | varchar |  |  | SI | Editable Flag |
| QCGRD_EntryDate | date |  |  | SI | Entry Date |
| QCGRD_EntryTime | time |  |  | SI | Entry Time |
| QCGRD_EntryUser | varchar |  |  | SI | Entry User |
| QCGRD_ExcludeFlag | varchar |  |  | SI | Exclude Flag |
| QCGRD_Level | varchar |  |  | NO | Level Number |
| QCGRD_ReviewedDate | date |  |  | SI | Reviewed Date |
| QCGRD_ReviewedTime | time |  |  | SI | Reviewed Time |
| QCGRD_ReviewedUser | varchar |  |  | SI | Reviewed User |
| QCGRD_RowID | varchar |  |  | NO | - |
| QCGRD_Value | varchar |  |  | SI | Value |
| QCGRD_ViolatedRuleDR | varchar |  | FK | SI | Violated Rule DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*