# lab.CT_LabReportTests

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLRT_ParRef | varchar | PK |  | NO | CT_LabReport Parent Reference |
| CTLRT_CCR_codes | varchar |  |  | SI | Cervical registry codes |
| CTLRT_RowID | varchar |  |  | NO | - |
| CTLRT_TestSet_DR | varchar |  | FK | NO | Test Set DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*