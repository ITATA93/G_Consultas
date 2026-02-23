# web_Msg.LBC_Protocol

**Schema:** web_Msg
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCPT_Code | varchar |  |  | SI | Code |
| LBCPT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCPT_CreatedDate | date |  |  | SI | Created Date |
| LBCPT_CreatedTime | time |  |  | SI | Created Time |
| LBCPT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPT_DateFrom | date |  |  | SI | Date From |
| LBCPT_DateTo | date |  |  | SI | Date To |
| LBCPT_DepartmentRestrictionList | varchar |  |  | SI | Department Restriction List |
| LBCPT_Desc | varchar |  |  | SI | Description |
| LBCPT_LabSiteRestrictionList | varchar |  |  | SI | Lab Site Restriction List |
| LBCPT_Owner | varchar |  |  | SI | Owner |
| LBCPT_RowID | varchar |  |  | SI | - |
| LBCPT_SOPCode | varchar |  |  | SI | SOP Code |
| LBCPT_SpecimenGroupList | varchar |  |  | SI | Specimen Group  |
| LBCPT_SpecimenList | varchar |  |  | SI | Specimen  |
| LBCPT_SubLevel | varchar |  |  | SI | Sub Level |
| LBCPT_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPT_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*