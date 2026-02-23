# lab.HOS_HospitalCTSpecimen

**Schema:** lab
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Hospital**. Configuración del establecimiento.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOSCP_ParRef | varchar | PK |  | NO | HOS_HospitalDataBase Parent Reference |
| HOSCP_HospitalCode | varchar |  |  | NO | Hospital Code |
| HOSCP_LabTrakCode_DR | varchar |  | FK | SI | LabTrak Code |
| HOSCP_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*