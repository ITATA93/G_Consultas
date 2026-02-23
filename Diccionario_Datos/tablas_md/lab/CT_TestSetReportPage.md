# lab.CT_TestSetReportPage

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTSN_ParRef | varchar | PK |  | NO | CT_TestSet Parent Reference |
| CTTSN_Code | varchar |  |  | NO | Doctor/Patient Location Code |
| CTTSN_CourierRun_DR | varchar |  | FK | SI | Courier Run |
| CTTSN_ReportPageType_DR | varchar |  | FK | SI | Report Page Type DR |
| CTTSN_RowID | varchar |  |  | NO | - |
| CTTSN_Type | varchar |  |  | NO | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*