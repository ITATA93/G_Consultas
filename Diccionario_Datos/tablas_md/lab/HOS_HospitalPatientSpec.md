# lab.HOS_HospitalPatientSpec

**Schema:** lab
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSPS_ParRef | varchar | PK |  | NO | HOS_HospitalPatients Parent Reference |
| HOSPS_RowId | varchar |  |  | NO | - |
| HOSPS_Specimen_DR | varchar |  | FK | NO | Des Ref Specimen |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*