# TC_hmf_Lib.MatchDemographics

**Schema:** TC_hmf_Lib
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBDEM_Code | varchar |  |  | NO | Demographic Code |
| HMFLIBDEM_DateFrom | date |  |  | SI | Date From |
| HMFLIBDEM_DateTo | date |  |  | SI | Date To |
| HMFLIBDEM_Desc | varchar |  |  | SI | Demographic Description |
| HMFLIBDEM_Enabled | bit |  |  | SI | Enabled Flag |
| HMFLIBDEM_ExtCode | varchar |  |  | SI | Demographic External Code |
| HMFLIBDEM_PatientDR | varchar |  | FK | SI | Demographic Database field |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*