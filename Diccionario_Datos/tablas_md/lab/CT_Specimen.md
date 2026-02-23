# lab.CT_Specimen

**Schema:** lab
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Especialidades**. Especialidades médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTSPE_RowId | varchar | PK |  | NO | - |
| CTSPE_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTSPE_Code | varchar |  |  | NO | Code |
| CTSPE_DayBookLaboratories | varchar |  |  | SI | DayBook Laboratories |
| CTSPE_Desc | varchar |  |  | SI | Description |
| CTSPE_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTSPE_Medtrak_1 | varchar |  |  | SI | Medtrak field 1 |
| CTSPE_Medtrak_2 | varchar |  |  | SI | Medtrak field 2 |
| CTSPE_Module | varchar |  |  | SI | Module |
| CTSPE_TCode_DR | varchar |  | FK | SI | SNOMED TCode DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*