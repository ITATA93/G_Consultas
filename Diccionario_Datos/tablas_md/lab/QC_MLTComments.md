# lab.QC_MLTComments

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMTC_ParRef | varchar | PK |  | NO | QC_MaterialLotType Parent Reference |
| QCMTC_Comments | varchar |  |  | SI | Comments |
| QCMTC_Date | date |  |  | SI | Date |
| QCMTC_Order | double |  |  | NO | Order |
| QCMTC_RowID | varchar |  |  | NO | - |
| QCMTC_Time | time |  |  | SI | Time |
| QCMTC_User_DR | varchar |  | FK | SI | User DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*