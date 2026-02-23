# TC_hmf_Lib.MessageTransform

**Schema:** TC_hmf_Lib
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBMSGTRM_Class | varchar |  |  | SI | Transformation class |
| HMFLIBMSGTRM_Code | varchar |  |  | SI | Message transformation code |
| HMFLIBMSGTRM_DateFrom | date |  |  | SI | Date From |
| HMFLIBMSGTRM_DateTo | date |  |  | SI | Date To |
| HMFLIBMSGTRM_Desc | varchar |  |  | SI | Message transformation description |
| HMFLIBMSGTRM_Enabled | bit |  |  | SI | Enabled flag |
| HMFLIBMSGTRM_FormatDR | bigint |  | FK | SI | Des ref to message format that the transformation ... |
| HMFLIBMSGTRM_Type | varchar |  |  | SI | Transformation type |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*