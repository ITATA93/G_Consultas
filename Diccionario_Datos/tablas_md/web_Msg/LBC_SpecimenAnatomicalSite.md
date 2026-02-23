# web_Msg.LBC_SpecimenAnatomicalSite

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCSPAS_AnatomicalSite_DR | bigint |  | FK | SI | Anatomical Site DR |
| LBCSPAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCSPAS_DateFrom | date |  |  | SI | Effective date for record |
| LBCSPAS_DateTo | date |  |  | SI | Last day the record is active  |
| LBCSPAS_ParRef | bigint |  |  | SI | Parent Specimen DR |
| LBCSPAS_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*