# lab.QC_MLTTestCodeLevelData

**Schema:** lab
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMTD_ParRef | varchar | PK |  | NO | QC_MLTTestCodeLevel Parent Reference |
| QCMTD_Active | varchar |  |  | SI | Active |
| QCMTD_Comments | varchar |  |  | SI | Comments |
| QCMTD_Date | date |  |  | NO | Date |
| QCMTD_Editable | varchar |  |  | SI | Editable |
| QCMTD_ExludeFlag | varchar |  |  | SI | Exclude Flag |
| QCMTD_QCRun | double |  |  | NO | QC Run |
| QCMTD_ReviewedDate | date |  |  | SI | Reviewed Date |
| QCMTD_ReviewedTime | time |  |  | SI | Reviewed Time |
| QCMTD_ReviewedUser_DR | varchar |  | FK | SI | Reviewed User DR |
| QCMTD_RowID | varchar |  |  | NO | - |
| QCMTD_Rule_DR | varchar |  | FK | SI | Violated Rule DR |
| QCMTD_Time | time |  |  | SI | Time |
| QCMTD_User_DR | varchar |  | FK | SI | User DR |
| QCMTD_Value | varchar |  |  | SI | Value |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*