# lab.CT_Antibiotics

**Schema:** lab
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTANT_RowId | varchar | PK |  | NO | - |
| CTANT_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTANT_Activity_DR | varchar |  | FK | SI | Activity DR |
| CTANT_AgeMax | double |  |  | SI | Maximum age for antibiotic |
| CTANT_AgeMin | double |  |  | SI | Minimum age for antibiotic |
| CTANT_Code | varchar |  |  | NO | Code |
| CTANT_DisplaySequence | numeric |  |  | SI | Display Sequence |
| CTANT_Name | varchar |  |  | SI | Name |
| CTANT_NotForPregnantFlag | varchar |  |  | SI | Not for Pregnant Flag |
| CTANT_OXOID_Code | varchar |  |  | SI | OXOID Code |
| CTANT_SpeciesAllowed | varchar |  |  | SI | Species allowed |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*