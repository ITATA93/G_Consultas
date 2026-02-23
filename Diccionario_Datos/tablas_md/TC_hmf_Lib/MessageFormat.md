# TC_hmf_Lib.MessageFormat

**Schema:** TC_hmf_Lib
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBMSGFRM_Code | varchar |  |  | NO | Message format code |
| HMFLIBMSGFRM_DateFrom | date |  |  | SI | Date From |
| HMFLIBMSGFRM_DateTo | date |  |  | SI | Date To |
| HMFLIBMSGFRM_Desc | varchar |  |  | SI | Message format description |
| HMFLIBMSGFRM_Enabled | bit |  |  | SI | Enabled flag |
| HMFLIBMSGFRM_ExtCode | varchar |  |  | SI | Message format external code - universaly recognis... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*