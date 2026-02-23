# lab.CT_AntibioticsSensitivity

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTANS_ParRef | varchar | PK |  | NO | CT_Antibiotics Parent Reference |
| CTANS_Operand | varchar |  |  | SI | Operand MIC |
| CTANS_Operand_ETest | varchar |  |  | SI | Operand E Test |
| CTANS_Operand_mm | varchar |  |  | SI | Operand mm |
| CTANS_Result_ETest | varchar |  |  | SI | Result E Test |
| CTANS_Result_MIC | varchar |  |  | SI | Result MIC |
| CTANS_Result_mm | varchar |  |  | SI | Result mm |
| CTANS_RowID | varchar |  |  | NO | - |
| CTANS_Sensitivity_DR | varchar |  | FK | NO | Sensitivity DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*