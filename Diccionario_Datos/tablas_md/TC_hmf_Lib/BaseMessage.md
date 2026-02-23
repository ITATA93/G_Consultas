# TC_hmf_Lib.BaseMessage

**Schema:** TC_hmf_Lib
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| HMFBASEMSG_Code | varchar |  |  | NO | Used by Perforce for generated xml file name |
| HMFBASEMSG_DateFrom | date |  |  | SI | Date From |
| HMFBASEMSG_DateTo | date |  |  | SI | Date To |
| HMFBASEMSG_Enabled | bit |  |  | SI | Enabled flag |
| HMFBASEMSG_MessageDR | bigint |  | FK | NO | Des Ref to message code table |
| HMFBASEMSG_TransformDR | bigint |  | FK | SI | Des Ref to supported message version |
| HMFBASEMSG_VersionDR | varchar |  | FK | SI | Des Ref to supported message version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*