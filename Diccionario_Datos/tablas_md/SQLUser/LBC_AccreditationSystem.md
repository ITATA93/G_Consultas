# SQLUser.LBC_AccreditationSystem

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCAS_RowID | bigint | PK |  | NO | - |
| LBCAS_Accredited | varchar |  |  | SI | Accredited |
| LBCAS_Code | varchar |  |  | SI | Code |
| LBCAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCAS_CreatedDate | date |  |  | SI | Created Date |
| LBCAS_CreatedTime | time |  |  | SI | Created Time |
| LBCAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCAS_DateFrom | date |  |  | SI | Date From |
| LBCAS_DateTo | date |  |  | SI | Date To |
| LBCAS_Desc | varchar |  |  | SI | Description |
| LBCAS_Owner | varchar |  |  | SI | Owner |
| LBCAS_UpdatedDate | date |  |  | SI | Updated Date |
| LBCAS_UpdatedTime | time |  |  | SI | Updated Time |
| LBCAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q24Q1 | - |  |  | SI | Date |
| Q24Q2 | - |  |  | SI | Time |
| Q24Q3 | - |  |  | SI | Care provider |
| Q24Q4 | - |  |  | SI | Code |
| Q24Q5 | - |  |  | SI | Description |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*