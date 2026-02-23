# SQLUser.PAC_ReasonPregCancel

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PREGCNCL_RowId | bigint | PK |  | NO | - |
| ChildQ10DR | - |  |  | SI | Child Reference: Physical aggression |
| PREGCNCL_Code | varchar |  |  | NO | Code |
| PREGCNCL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PREGCNCL_CreatedDate | date |  |  | SI | Created Date |
| PREGCNCL_CreatedTime | time |  |  | SI | Created Time |
| PREGCNCL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PREGCNCL_DateFrom | date |  |  | SI | Date From |
| PREGCNCL_DateTo | date |  |  | SI | Date To |
| PREGCNCL_Desc | varchar |  |  | NO | Description |
| PREGCNCL_NationalCode | varchar |  |  | SI | National Code |
| PREGCNCL_Owner | varchar |  |  | SI | Owner |
| PREGCNCL_UpdatedDate | date |  |  | SI | Updated Date |
| PREGCNCL_UpdatedTime | time |  |  | SI | Updated Time |
| PREGCNCL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q09Q1 | - |  |  | SI | Date |
| Q09Q10 | - |  |  | SI | Staff |
| Q09Q2 | - |  |  | SI | Time |
| Q09Q3 | - |  |  | SI | Type |
| Q09Q4 | - |  |  | SI | Other type |
| Q09Q5 | - |  |  | SI | Situation / Trigger |
| Q09Q6 | - |  |  | SI | What happened? |
| Q09Q7 | - |  |  | SI | What did you do? |
| Q09Q8 | - |  |  | SI | Behavioural outcome |
| Q09Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*