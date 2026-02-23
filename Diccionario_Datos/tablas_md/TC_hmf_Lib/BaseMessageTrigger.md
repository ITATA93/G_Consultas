# TC_hmf_Lib.BaseMessageTrigger

**Schema:** TC_hmf_Lib
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare HMF**. Framework de mensajería y procesamiento de Health Messages.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HMFBASEMSGTRG_ParRef | bigint | PK |  | NO | Trigger Event Parent Reference |
| HMFBASEMSGTRG_Action | varchar |  |  | SI | Trigger action (insert/update/delete) |
| HMFBASEMSGTRG_Code | varchar |  |  | NO | Used by Perforce for generated xml file name |
| HMFBASEMSGTRG_DateFrom | date |  |  | SI | Date From |
| HMFBASEMSGTRG_DateTo | date |  |  | SI | Date To |
| HMFBASEMSGTRG_Enabled | bit |  |  | SI | Enabled flag |
| HMFBASEMSGTRG_FormatDR | bigint |  | FK | NO | Des Ref to message format code table |
| HMFBASEMSGTRG_MessageDR | bigint |  | FK | SI | Des Ref to message code table |
| HMFBASEMSGTRG_MessageExpression | varchar |  |  | SI | Conditional Message Expression that returns the De... |
| HMFBASEMSGTRG_Screenform | varchar |  |  | SI | Trigger screen |
| ID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*