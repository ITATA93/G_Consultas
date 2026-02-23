# lab.CT_LabReportExclusions

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLRE_ParRef | varchar | PK |  | NO | CT_LabReport Parent Reference |
| CTLRE_DCodes | varchar |  |  | SI | D Codes |
| CTLRE_Extra | varchar |  |  | SI | 5th digits |
| CTLRE_MCodes | varchar |  |  | SI | M Codes |
| CTLRE_RowID | varchar |  |  | NO | - |
| CTLRE_Sequence | double |  |  | NO | Sequence |
| CTLRE_TCodes | varchar |  |  | SI | T Codes |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*