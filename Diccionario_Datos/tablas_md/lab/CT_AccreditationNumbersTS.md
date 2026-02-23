# lab.CT_AccreditationNumbersTS

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTACNT_ParRef | double | PK |  | NO | CT_AccreditationNumbers Parent Reference |
| CTACNTS_AccreditationNo | varchar |  |  | SI | Accreditation Number |
| CTACNTS_EndDate | date |  |  | SI | End Date |
| CTACNTS_StartDate | date |  |  | SI | Start Date |
| CTACNTS_TestSet_DR | varchar |  | FK | NO | Test Set DR |
| CTACNTS_Type | varchar |  |  | SI | Type |
| ID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*