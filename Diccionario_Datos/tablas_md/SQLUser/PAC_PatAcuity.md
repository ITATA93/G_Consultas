# SQLUser.PAC_PatAcuity

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACU_RowId | bigint | PK |  | NO | - |
| ACU_Code | varchar |  |  | NO | Code |
| ACU_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACU_CreatedDate | date |  |  | SI | Created Date |
| ACU_CreatedTime | time |  |  | SI | Created Time |
| ACU_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACU_DateFrom | date |  |  | SI | Date From |
| ACU_DateTo | date |  |  | SI | Date To |
| ACU_Desc | varchar |  |  | NO | Description |
| ACU_NationalCode | varchar |  |  | SI | National Code |
| ACU_Owner | varchar |  |  | SI | Owner |
| ACU_UpdatedDate | date |  |  | SI | Updated Date |
| ACU_UpdatedTime | time |  |  | SI | Updated Time |
| ACU_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ02DR | - |  |  | SI | Child Reference: Nutritional review |
| Q04Q1 | - |  |  | SI | Date |
| Q04Q2 | - |  |  | SI | Time |
| Q04Q3 | - |  |  | SI | Bag and line changed and documented |
| Q04Q4 | - |  |  | SI | Summary of treatment plan |
| Q04Q5 | - |  |  | SI | Have treatment orders been placed? |
| Q04Q6 | - |  |  | SI | Who was present on ward round |
| Q04Q7 | - |  |  | SI | Additional comments |
| Q04Q8 | - |  |  | SI | Glycaemic control target |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*