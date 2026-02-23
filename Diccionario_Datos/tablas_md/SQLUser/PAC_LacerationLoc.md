# SQLUser.PAC_LacerationLoc

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOCLAC_RowId | bigint | PK |  | NO | - |
| LOCLAC_Code | varchar |  |  | NO | Code |
| LOCLAC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOCLAC_CreatedDate | date |  |  | SI | Created Date |
| LOCLAC_CreatedTime | time |  |  | SI | Created Time |
| LOCLAC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOCLAC_DateFrom | date |  |  | SI | Date From |
| LOCLAC_DateTo | date |  |  | SI | Date To |
| LOCLAC_Desc | varchar |  |  | NO | Description |
| LOCLAC_Owner | varchar |  |  | SI | Owner |
| LOCLAC_UpdatedDate | date |  |  | SI | Updated Date |
| LOCLAC_UpdatedTime | time |  |  | SI | Updated Time |
| LOCLAC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q37Q1 | - |  |  | SI | Date |
| Q37Q2 | - |  |  | SI | Time |
| Q37Q3 | - |  |  | SI | Reassessment / Follow-Up |
| Q37Q4 | - |  |  | SI | Social worker's name |
| Q37Q5 | - |  |  | SI | Social worker's ID No |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*