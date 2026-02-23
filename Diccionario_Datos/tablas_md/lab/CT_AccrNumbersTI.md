# lab.CT_AccrNumbersTI

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTACNTI_ParRef | double | PK |  | NO | CT_AccreditationNumbers Parent Reference |
| CTACNTI_AccreditationNo | varchar |  |  | SI | Accreditation Number |
| CTACNTI_EndDate | date |  |  | SI | End Date |
| CTACNTI_RowID | varchar |  |  | NO | - |
| CTACNTI_StartDate | date |  |  | SI | Start Date |
| CTACNTI_TestItem_DR | varchar |  | FK | NO | Test Item DR |
| CTACNTS_Type | varchar |  |  | SI | Type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*