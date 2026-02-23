# SQLUser.PAC_RefTemplateAgeSex

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGESEX_ParRef | bigint | PK |  | NO | PAC_RefTemplate Parent Reference |
| AGESEX_AgeFrom | double |  |  | SI | AgeFrom |
| AGESEX_AgeTo | double |  |  | SI | AgeTo |
| AGESEX_Childsub | double |  |  | NO | Childsub |
| AGESEX_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGESEX_CreatedDate | date |  |  | SI | Created Date |
| AGESEX_CreatedTime | time |  |  | SI | Created Time |
| AGESEX_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGESEX_DaysFrom | double |  |  | SI | AgeFrom |
| AGESEX_DaysTo | double |  |  | SI | AgeTo |
| AGESEX_MonthFrom | double |  |  | SI | AgeFrom |
| AGESEX_MonthTo | double |  |  | SI | AgeTo |
| AGESEX_RowId | varchar |  |  | NO | - |
| AGESEX_Sex_DR | bigint |  | FK | SI | Des Ref CTSex |
| AGESEX_UpdatedDate | date |  |  | SI | Updated Date |
| AGESEX_UpdatedTime | time |  |  | SI | Updated Time |
| AGESEX_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ14DR | - |  |  | SI | Child Reference: General notes |
| Q13Q1 | - |  |  | SI | Date |
| Q13Q2 | - |  |  | SI | Topic |
| Q13Q3 | - |  |  | SI | Evaluation |
| Q13Q4 | - |  |  | SI | Plan |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*