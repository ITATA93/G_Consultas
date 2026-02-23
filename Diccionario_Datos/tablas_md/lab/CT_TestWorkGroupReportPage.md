# lab.CT_TestWorkGroupReportPage

**Schema:** lab
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTWA_ParRef | varchar | PK |  | NO | CT_TestWorkGroup Parent Reference |
| CTTWA_Code | varchar |  |  | NO | Doctor/Patient Location Code |
| CTTWA_ReportPageType_DR | varchar |  | FK | SI | Report Page Type DR |
| CTTWA_RowID | varchar |  |  | NO | - |
| CTTWA_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*