# lab.CT_MicroPanelItemsSensitiv

**Schema:** lab
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTMPD_ParRef | varchar | PK |  | NO | CT_MicrobiologyPanelItems Parent Reference |
| CTMPD_Operand | varchar |  |  | SI | Operand MIC |
| CTMPD_Operand_ETest | varchar |  |  | SI | Operand E Test |
| CTMPD_Operand_mm | varchar |  |  | SI | Operand mm |
| CTMPD_Result_ETest | varchar |  |  | SI | Result E Test |
| CTMPD_Result_MIC | varchar |  |  | SI | Result MIC |
| CTMPD_Result_mm | varchar |  |  | SI | Result mm |
| CTMPD_RowID | varchar |  |  | NO | - |
| CTMPD_Sensitivity_DR | varchar |  | FK | NO | Sensitivity DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*