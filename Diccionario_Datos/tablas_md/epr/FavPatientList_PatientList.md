# epr.FavPatientList_PatientList

**Schema:** epr
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| FavPatientList | bigint | PK |  | NO | Parent reference |
| ID | varchar |  |  | NO | - |
| PatientList | varchar |  |  | SI | PatientList |
| element_key | varchar |  |  | NO | PatientList array key |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*