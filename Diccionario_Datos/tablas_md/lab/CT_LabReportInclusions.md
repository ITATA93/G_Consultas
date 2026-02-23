# lab.CT_LabReportInclusions

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLRI_ParRef | varchar | PK |  | NO | CT_LabReport Parent Reference |
| CTLRI_DCode | varchar |  |  | SI | D Code |
| CTLRI_Extra | varchar |  |  | SI | 5th digit |
| CTLRI_MCode | varchar |  |  | SI | M Code |
| CTLRI_RowID | varchar |  |  | NO | - |
| CTLRI_Sequence | double |  |  | NO | Sequence |
| CTLRI_TCode | varchar |  |  | SI | T Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*