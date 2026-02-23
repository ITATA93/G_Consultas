# SQLUser.PAC_Isolation

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ISOL_RowId | bigint | PK |  | NO | - |
| ISOL_Code | varchar |  |  | NO | Code |
| ISOL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ISOL_CreatedDate | date |  |  | SI | Created Date |
| ISOL_CreatedTime | time |  |  | SI | Created Time |
| ISOL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ISOL_DateFrom | date |  |  | SI | Date From |
| ISOL_DateTo | date |  |  | SI | Date To |
| ISOL_Desc | varchar |  |  | NO | Description |
| ISOL_Owner | varchar |  |  | SI | Owner |
| ISOL_UpdatedDate | date |  |  | SI | Updated Date |
| ISOL_UpdatedTime | time |  |  | SI | Updated Time |
| ISOL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q22Q1 | - |  |  | SI | Date |
| Q22Q2 | - |  |  | SI | Time |
| Q22Q3 | - |  |  | SI | Reviewed by |
| Q22Q4 | - |  |  | SI | Frequency for review |
| Q22Q5 | - |  |  | SI | New order placed? |
| Q22Q6 | - |  |  | SI | Continue restraint? |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*