# TC_hmf_Lib.BaseTransform

**Schema:** TC_hmf_Lib
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFBASETRM_Code | varchar |  |  | NO | Used by Perforce for generated xml file name |
| HMFBASETRM_DateFrom | date |  |  | SI | Date From |
| HMFBASETRM_DateTo | date |  |  | SI | Date To |
| HMFBASETRM_Enabled | bit |  |  | SI | Enabled flag |
| HMFBASETRM_TransformDR | bigint |  | FK | NO | Des ref to message transform code table |
| HMFBASETRM_VersionDR | varchar |  | FK | NO | Des ref to message version code table |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*