# SQLUser.PAC_BedMobility

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BM_RowId | bigint | PK |  | NO | - |
| BM_Code | varchar |  |  | NO | Code |
| BM_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BM_CreatedDate | date |  |  | SI | Created Date |
| BM_CreatedTime | time |  |  | SI | Created Time |
| BM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BM_DateFrom | date |  |  | SI | Date From |
| BM_DateTo | date |  |  | SI | Date To |
| BM_Desc | varchar |  |  | NO | Description |
| BM_NationCode | varchar |  |  | SI | National Code |
| BM_NumericVal | double |  |  | SI | Numeric Value |
| BM_Owner | varchar |  |  | SI | Owner |
| BM_UpdatedDate | date |  |  | SI | Updated Date |
| BM_UpdatedTime | time |  |  | SI | Updated Time |
| BM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ70DR | - |  |  | SI | Child Reference: Tracheostomy tube assessment |
| Q06Q1 | - |  |  | SI | Date |
| Q06Q2 | - |  |  | SI | Time |
| Q06Q3 | - |  |  | SI | Staff Name |
| Q06Q4 | - |  |  | SI | Check |
| Q06Q5 | - |  |  | SI | Actions |
| Q06Q6 | - |  |  | SI | Daily Assessment Notes |
| Q06Q7 | - |  |  | SI | Cuff Pressure |
| Q06Q8 | - |  |  | SI | Leak Volume |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*