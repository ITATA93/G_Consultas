# lab.CT_DoctorSpecialty

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDRS_ParRef | varchar | PK |  | NO | CT_Doctor Parent Reference |
| CTDRS_Default | varchar |  |  | SI | Default |
| CTDRS_RowID | varchar |  |  | NO | - |
| CTDRS_Specialty_DR | varchar |  | FK | NO | Specialty DR |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*