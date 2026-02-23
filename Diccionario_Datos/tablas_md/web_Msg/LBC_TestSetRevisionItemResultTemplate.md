# web_Msg.LBC_TestSetRevisionItemResultTemplate

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRIRT_AllowMultiple | varchar |  |  | SI | Allow Multiple |
| LBCTSRIRT_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site |
| LBCTSRIRT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| LBCTSRIRT_DateFrom | date |  |  | SI | Date From
Effective date for the record
Required... |
| LBCTSRIRT_DateTo | date |  |  | SI | Date To
Last day the record is active
Optional. ... |
| LBCTSRIRT_IncludeSpecimenDetails | varchar |  |  | SI | Include Specimen Details |
| LBCTSRIRT_LabSite_DR | bigint |  | FK | SI | Lab Site |
| LBCTSRIRT_Lesion_DR | bigint |  | FK | SI | Lesion |
| LBCTSRIRT_ParRef | varchar |  |  | SI | - |
| LBCTSRIRT_Priority_DR | bigint |  | FK | SI | Priority |
| LBCTSRIRT_RowID | varchar |  |  | SI | - |
| LBCTSRIRT_Sequence | numeric |  |  | SI | Rule Sequence |
| LBCTSRIRT_SpecimenGroup_DR | bigint |  | FK | SI | Specimen Group |
| LBCTSRIRT_Specimen_DR | bigint |  | FK | SI | Specimen |
| LBCTSRIRT_Template_DR | bigint |  | FK | SI | Letter Template |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*