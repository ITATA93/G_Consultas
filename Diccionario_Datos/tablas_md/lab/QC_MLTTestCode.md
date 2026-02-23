# lab.QC_MLTTestCode

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Control de Calidad**. Gestión de calidad de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QCMTT_ParRef | varchar | PK |  | NO | QC_MaterialLotType Parent Reference |
| QCMTT_Active | varchar |  |  | SI | Active |
| QCMTT_RowID | varchar |  |  | NO | - |
| QCMTT_TestItemGroup_DR | varchar |  | FK | SI | Test Item Group |
| QCMTT_TestItem_DR | varchar |  | FK | NO | Test Item |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*