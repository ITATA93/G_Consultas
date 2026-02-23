# SQLUser.MRC_EncEntryTypeActionRestr

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RESTR_ParRef | varchar | PK |  | NO | - |
| ChildQ54DR | - |  |  | SI | Child Reference: Examen físico |
| Q51Q1 | - |  |  | SI | N° de días |
| Q51Q2 | - |  |  | SI | Motivo de hospitalización |
| Q51Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RESTR_AgeFrom | integer |  |  | SI | Age From |
| RESTR_AgeTo | integer |  |  | SI | AgeTo |
| RESTR_Childsub | double |  |  | NO | Childsub |
| RESTR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RESTR_CreatedDate | date |  |  | SI | Created Date |
| RESTR_CreatedTime | time |  |  | SI | Created Time |
| RESTR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RESTR_RowId | varchar |  |  | NO | - |
| RESTR_Sex_DR | bigint |  | FK | SI | Des Ref Sex |
| RESTR_UpdatedDate | date |  |  | SI | Updated Date |
| RESTR_UpdatedTime | time |  |  | SI | Updated Time |
| RESTR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*