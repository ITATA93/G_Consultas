# SQLUser.PAC_SNAPPhases

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNAPPH_RowId | bigint | PK |  | NO | - |
| ChildQ21DR | - |  |  | SI | Child Reference: Family / Social / Work reintegrat... |
| Q5Q1 | - |  |  | SI | Micro goal |
| Q5Q2 | - |  |  | SI | Timing |
| Q5Q3 | - |  |  | SI | Outcome |
| Q5Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNAPPH_Code | varchar |  |  | NO | Code |
| SNAPPH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNAPPH_CreatedDate | date |  |  | SI | Created Date |
| SNAPPH_CreatedTime | time |  |  | SI | Created Time |
| SNAPPH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNAPPH_DateFrom | date |  |  | SI | Date From |
| SNAPPH_DateTo | date |  |  | SI | Date To |
| SNAPPH_Desc | varchar |  |  | NO | Description |
| SNAPPH_Owner | varchar |  |  | SI | Owner |
| SNAPPH_UpdatedDate | date |  |  | SI | Updated Date |
| SNAPPH_UpdatedTime | time |  |  | SI | Updated Time |
| SNAPPH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*