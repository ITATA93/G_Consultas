# lab.HOS_HospitalPatientsTSet

**Schema:** lab
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSPT_ParRef | varchar | PK |  | NO | HOS_HospitalPatients Parent Reference |
| HOSPT_Counter | numeric |  |  | NO | Counter |
| HOSPT_HospitalRefNumber | varchar |  |  | SI | Hospital Ref Number |
| HOSPT_RowID | varchar |  |  | NO | - |
| HOSPT_SuperSet_DR | varchar |  | FK | SI | Super Set DR |
| HOSPT_TestSet_DR | varchar |  | FK | NO | Des Ref TestSet |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*