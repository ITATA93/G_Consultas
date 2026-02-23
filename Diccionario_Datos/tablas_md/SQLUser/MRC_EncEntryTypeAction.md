# SQLUser.MRC_EncEntryTypeAction

**Schema:** SQLUser
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EACT_ParRef | bigint | PK |  | NO | OEC_ConsultCateg Parent Reference |
| ChildQ51DR | - |  |  | SI | Child Reference: Hospitalizaciones durante el emba... |
| EACT_Action_DR | bigint |  | FK | SI | configurable action.  |
| EACT_Childsub | double |  |  | NO | Childsub |
| EACT_Code | varchar |  |  | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| EACT_CreatedDate | date |  |  | SI | Created Date |
| EACT_CreatedTime | time |  |  | SI | Created Time |
| EACT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EACT_DateFrom | date |  |  | SI | Date From |
| EACT_DateTo | date |  |  | SI | Date To |
| EACT_DefaultAction | bit |  |  | SI | default action |
| EACT_Desc | varchar |  |  | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_DocItemHeader_DR | bigint |  | FK | SI | Header |
| EACT_DocType_DR | bigint |  | FK | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_Filter | varchar |  |  | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_Location_DR | bigint |  | FK | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_Owner | varchar |  |  | SI | Owner - DEPRECATED by Code Table Overrides |
| EACT_RowId | varchar |  |  | NO | - |
| EACT_Section_DR | varchar |  | FK | SI | Section |
| EACT_SecurityGroup_DR | bigint |  | FK | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| EACT_Seq | integer |  |  | SI | - |
| EACT_UpdatedDate | date |  |  | SI | Updated Date |
| EACT_UpdatedTime | time |  |  | SI | Updated Time |
| EACT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| EACT_WorkFlow_DR | bigint |  | FK | SI | [DEPRECATED]TC-97374- item moved to MRCEncounterAc... |
| Q32Q1 | - |  |  | SI | Fecha de aborto |
| Q32Q2 | - |  |  | SI | Tipo de aborto |
| Q32Q3 | - |  |  | SI | Comentario |
| Q32Q4 | - |  |  | SI | Tipo de Aborto |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*