# SQLUser.ARC_OrdSetDateOSNarrative

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OSN_ParRef | varchar | PK |  | NO | ARC_OrdSetDateOS Parent Reference |
| OSN_Active | bit |  |  | SI | Active - Only active narratives will display in th... |
| OSN_Childsub | double |  |  | NO | Childsub |
| OSN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OSN_CreatedDate | date |  |  | SI | Created Date |
| OSN_CreatedTime | time |  |  | SI | Created Time |
| OSN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OSN_DisplaySource | bit |  |  | SI | Display Source - will display Source at the end of... |
| OSN_RecommendationLevel_DR | bigint |  | FK | SI | Des Ref to Recommendation Level - will display at ... |
| OSN_RowId | varchar |  |  | NO | - |
| OSN_Source_DR | bigint |  | FK | SI | Des Ref to Source of the Narrative information |
| OSN_Stream_DR | bigint |  | FK | SI | Narrative Stream  |
| OSN_Type | varchar |  |  | SI | Narrative Type - Uses the standard type "Narrative... |
| OSN_UpdatedDate | date |  |  | SI | Updated Date |
| OSN_UpdatedTime | time |  |  | SI | Updated Time |
| OSN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Equipamiento |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*