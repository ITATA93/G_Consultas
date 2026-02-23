# SQLUser.PAC_Reason_for_Leave

**Schema:** SQLUser
**Columnas:** 23
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFL_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Restlessness |
| Q10Q1 | - |  |  | SI | Date |
| Q10Q10 | - |  |  | SI | Staff |
| Q10Q2 | - |  |  | SI | Time |
| Q10Q3 | - |  |  | SI | Type |
| Q10Q4 | - |  |  | SI | Other type |
| Q10Q5 | - |  |  | SI | Situation / Trigger |
| Q10Q6 | - |  |  | SI | What happened? |
| Q10Q7 | - |  |  | SI | What did you do? |
| Q10Q8 | - |  |  | SI | Behavioural outcome |
| Q10Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RFL_Code | varchar |  |  | NO | Code |
| RFL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RFL_CreatedDate | date |  |  | SI | Created Date |
| RFL_CreatedTime | time |  |  | SI | Created Time |
| RFL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RFL_Desc | varchar |  |  | NO | Description |
| RFL_Owner | varchar |  |  | SI | Owner |
| RFL_UpdatedDate | date |  |  | SI | Updated Date |
| RFL_UpdatedTime | time |  |  | SI | Updated Time |
| RFL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*