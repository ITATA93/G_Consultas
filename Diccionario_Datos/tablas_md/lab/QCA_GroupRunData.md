# lab.QCA_GroupRunData

**Schema:** lab
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCAGRD_ParRef | varchar | PK |  | NO | QC_GroupRun Parent Reference |
| QCAGRD_Comments | varchar |  |  | SI | Comments |
| QCAGRD_Editable | varchar |  |  | SI | Editable Flag |
| QCAGRD_EntryDate | date |  |  | SI | Entry Date |
| QCAGRD_EntryTime | time |  |  | SI | Entry Time |
| QCAGRD_EntryUserDR | varchar |  | FK | SI | Entry User DR |
| QCAGRD_ExcludeFlag | varchar |  |  | SI | Exclude Flag |
| QCAGRD_Level | varchar |  |  | NO | Level Number |
| QCAGRD_ReviewedDate | date |  |  | SI | Reviewed Date |
| QCAGRD_ReviewedTime | time |  |  | SI | Reviewed Time |
| QCAGRD_ReviewedUserDR | varchar |  | FK | SI | Reviewed User DR |
| QCAGRD_RowID | varchar |  |  | NO | - |
| QCAGRD_Value | varchar |  |  | SI | Value |
| QCAGRD_ViolatedRuleDR | varchar |  | FK | SI | Violated Rule DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*