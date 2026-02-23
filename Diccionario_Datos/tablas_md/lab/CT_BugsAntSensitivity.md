# lab.CT_BugsAntSensitivity

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTBUS_ParRef | varchar | PK |  | NO | CT_BugsAntiBiotics Parent Reference |
| CTBUS_Operand | varchar |  |  | SI | Operand MIC |
| CTBUS_Operand_ETest | varchar |  |  | SI | Operand E-Test |
| CTBUS_Operand_mm | varchar |  |  | SI | Operand mm |
| CTBUS_Result_ETest | varchar |  |  | SI | Result E Test |
| CTBUS_Result_MIC | varchar |  |  | SI | Result MIC |
| CTBUS_Result_mm | varchar |  |  | SI | Result mm |
| CTBUS_RowID | varchar |  |  | NO | - |
| CTBUS_Sensitivity_DR | varchar |  | FK | NO | Sensitivity DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*