# SQLUser.ARC_OrdSetDateNarrative

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DATEN_ParRef | varchar | PK |  | NO | ARC_OrdSets Parent Reference |
| ChildQ24DR | - |  |  | SI | Child Reference: Staff Quirúrgico |
| DATEN_Active | bit |  |  | SI | Active - Only active narratives will display in th... |
| DATEN_Childsub | double |  |  | NO | Childsub |
| DATEN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DATEN_CreatedDate | date |  |  | SI | Created Date |
| DATEN_CreatedTime | time |  |  | SI | Created Time |
| DATEN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DATEN_DisplaySource | bit |  |  | SI | Display Source - will display Source at the end of... |
| DATEN_RecommendationLevel_DR | bigint |  | FK | SI | Des Ref to Recommendation Level - will display at ... |
| DATEN_RowId | varchar |  |  | NO | - |
| DATEN_Source_DR | bigint |  | FK | SI | Des Ref to Source of the Narrative information |
| DATEN_Stream_DR | bigint |  | FK | SI | Narrative Stream  |
| DATEN_Type | varchar |  |  | SI | Narrative Type - Uses the standard type "Narrative... |
| DATEN_UpdatedDate | date |  |  | SI | Updated Date |
| DATEN_UpdatedTime | time |  |  | SI | Updated Time |
| DATEN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q15Q1 | - |  |  | SI | Equipamiento |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*