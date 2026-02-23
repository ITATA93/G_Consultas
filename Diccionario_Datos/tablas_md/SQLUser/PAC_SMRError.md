# SQLUser.PAC_SMRError

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMRERR_RowId | bigint | PK |  | NO | - |
| ChildQ15DR | - |  |  | SI | Child Reference: Stairs recovery |
| Q13Q1 | - |  |  | SI | Micro goal |
| Q13Q2 | - |  |  | SI | Timing |
| Q13Q3 | - |  |  | SI | Outcome |
| Q13Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SMRERR_Code | varchar |  |  | NO | Code |
| SMRERR_CreatedDate | date |  |  | SI | Created Date |
| SMRERR_CreatedTime | time |  |  | SI | Created Time |
| SMRERR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SMRERR_Desc | varchar |  |  | NO | Description |
| SMRERR_Display | varchar |  |  | SI | Display |
| SMRERR_UpdatedDate | date |  |  | SI | Updated Date |
| SMRERR_UpdatedTime | time |  |  | SI | Updated Time |
| SMRERR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*