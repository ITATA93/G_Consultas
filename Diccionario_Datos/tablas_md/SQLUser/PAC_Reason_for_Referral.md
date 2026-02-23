# SQLUser.PAC_Reason_for_Referral

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFR_RowId | bigint | PK |  | NO | - |
| ChildQ12DR | - |  |  | SI | Child Reference: Psychotic Symptoms |
| Q11Q1 | - |  |  | SI | Date |
| Q11Q10 | - |  |  | SI | Staff |
| Q11Q2 | - |  |  | SI | Time |
| Q11Q3 | - |  |  | SI | Type |
| Q11Q4 | - |  |  | SI | Other type |
| Q11Q5 | - |  |  | SI | Situation / Trigger |
| Q11Q6 | - |  |  | SI | What happened? |
| Q11Q7 | - |  |  | SI | What did you do? |
| Q11Q8 | - |  |  | SI | Behavioural outcome |
| Q11Q9 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFR_Code | varchar |  |  | NO | Code |
| REFR_CreatedDate | date |  |  | SI | Created Date |
| REFR_CreatedTime | time |  |  | SI | Created Time |
| REFR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFR_Desc | varchar |  |  | NO | Description |
| REFR_UpdatedDate | date |  |  | SI | Updated Date |
| REFR_UpdatedTime | time |  |  | SI | Updated Time |
| REFR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*