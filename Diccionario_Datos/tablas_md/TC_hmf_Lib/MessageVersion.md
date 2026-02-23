# TC_hmf_Lib.MessageVersion

**Schema:** TC_hmf_Lib
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFLIBMSGVER_ParRef | bigint | PK |  | NO | Message Format Parent Reference |
| HMFLIBMSGVER_Code | varchar |  |  | NO | Message version code |
| HMFLIBMSGVER_DateFrom | date |  |  | SI | Date From |
| HMFLIBMSGVER_DateTo | date |  |  | SI | Date To |
| HMFLIBMSGVER_Desc | varchar |  |  | SI | Message version description |
| HMFLIBMSGVER_Enabled | bit |  |  | SI | Enabled flag |
| HMFLIBMSGVER_Version | varchar |  |  | SI | Message version value |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*