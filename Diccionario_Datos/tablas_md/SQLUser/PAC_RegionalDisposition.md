# SQLUser.PAC_RegionalDisposition

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REGDISP_RowId | bigint | PK |  | NO | - |
| ChildQ03DR | - |  |  | SI | Child Reference: Last solids intake |
| Q05Q1 | - |  |  | SI | Date |
| Q05Q2 | - |  |  | SI | Time |
| Q05Q3 | - |  |  | SI | Details |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REGDISP_Code | varchar |  |  | NO | Code |
| REGDISP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REGDISP_CreatedDate | date |  |  | SI | Created Date |
| REGDISP_CreatedTime | time |  |  | SI | Created Time |
| REGDISP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REGDISP_DateFrom | date |  |  | SI | Date From |
| REGDISP_DateTo | date |  |  | SI | Date To |
| REGDISP_Desc | varchar |  |  | NO | Description |
| REGDISP_Owner | varchar |  |  | SI | Owner |
| REGDISP_Subregion_DR | bigint |  | FK | SI | Subregion |
| REGDISP_UpdatedDate | date |  |  | SI | Updated Date |
| REGDISP_UpdatedTime | time |  |  | SI | Updated Time |
| REGDISP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*