# TC_hmf_Lib.MessageSection

**Schema:** TC_hmf_Lib
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFLIBMSGSEC_Code | varchar |  |  | NO | Message section code |
| HMFLIBMSGSEC_DateFrom | date |  |  | SI | Date From |
| HMFLIBMSGSEC_DateTo | date |  |  | SI | Date To |
| HMFLIBMSGSEC_Desc | varchar |  |  | SI | Message section description |
| HMFLIBMSGSEC_Enabled | bit |  |  | SI | Enabled flag |
| HMFLIBMSGSEC_ExtCode | varchar |  |  | SI | Message section external code |
| HMFLIBMSGSEC_FormatDR | bigint |  | FK | SI | Des ref to message format code table entry |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*