# lab.CT_BugGroupAntSensitivity

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBGS_ParRef | varchar | PK |  | NO | CT_Bugs_Group_Antibiotics Parent Reference |
| CTBGS_Operand | varchar |  |  | SI | Operand MIC |
| CTBGS_Operand_ETest | varchar |  |  | SI | Operand E-Test |
| CTBGS_Operand_mm | varchar |  |  | SI | Operand mm |
| CTBGS_Result_ETest | varchar |  |  | SI | Result E Test |
| CTBGS_Result_MIC | varchar |  |  | SI | Result MIC |
| CTBGS_Result_mm | varchar |  |  | SI | Result mm |
| CTBGS_RowID | varchar |  |  | NO | - |
| CTBGS_Sensitivity_DR | varchar |  | FK | NO | Sensitivity DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*