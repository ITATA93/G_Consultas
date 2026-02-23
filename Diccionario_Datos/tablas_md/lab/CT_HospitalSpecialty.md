# lab.CT_HospitalSpecialty

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTHOA_ParRef | varchar | PK |  | NO | CT_Hospital Parent Reference |
| CTHOA_Default | varchar |  |  | SI | Default |
| CTHOA_RowID | varchar |  |  | NO | - |
| CTHOA_Specialty_DR | varchar |  | FK | NO | Specialty DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*