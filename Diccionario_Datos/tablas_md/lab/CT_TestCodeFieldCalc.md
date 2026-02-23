# lab.CT_TestCodeFieldCalc

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTCC_ParRef | varchar | PK |  | NO | CT_TestCode Parent Reference |
| CTTCC_AlwaysCalculated | varchar |  |  | SI | Always Calculated |
| CTTCC_Calculation | varchar |  |  | SI | Calculation |
| CTTCC_IncludeNumericCodes | varchar |  |  | SI | Include Numeric Codes |
| CTTCC_Required | varchar |  |  | SI | All test items required for Calculation |
| CTTCC_RowId | varchar |  |  | NO | - |
| CTTCC_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*