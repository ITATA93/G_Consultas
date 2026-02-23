# SQLUser.OEC_TextResultType

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| TRT_RowId | bigint | PK |  | NO | - |
| ChildQ26DR | - |  |  | SI | Child Reference: Stoma care |
| Q25Q1 | - |  |  | SI | Date |
| Q25Q10 | - |  |  | SI | Care provider |
| Q25Q2 | - |  |  | SI | Stoma colour |
| Q25Q3 | - |  |  | SI | Stoma profile |
| Q25Q4 | - |  |  | SI | Skin peristomal |
| Q25Q5 | - |  |  | SI | Descriptive bowel consistency |
| Q25Q6 | - |  |  | SI | Stoma output |
| Q25Q7 | - |  |  | SI | Pain |
| Q25Q8 | - |  |  | SI | Pain score |
| Q25Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| TRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TRT_CreatedDate | date |  |  | SI | Created Date |
| TRT_CreatedTime | time |  |  | SI | Created Time |
| TRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| TRT_Desc | varchar |  |  | NO | Result Name |
| TRT_ModifyFlag | varchar |  |  | SI | ModifyFlag |
| TRT_Owner | varchar |  |  | SI | Owner |
| TRT_UpdatedDate | date |  |  | SI | Updated Date |
| TRT_UpdatedTime | time |  |  | SI | Updated Time |
| TRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*