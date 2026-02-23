# SQLUser.PAC_ReferralDiagProblemAlias

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALIAS_ParRef | bigint | PK |  | NO | PAC_ReferralDiagnosticProblem Parent Reference |
| ALIAS_Childsub | double |  |  | NO | Childsub |
| ALIAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALIAS_CreatedDate | date |  |  | SI | Created Date |
| ALIAS_CreatedTime | time |  |  | SI | Created Time |
| ALIAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALIAS_RowId | varchar |  |  | NO | - |
| ALIAS_Text | varchar |  |  | SI | Text |
| ALIAS_UpdatedDate | date |  |  | SI | Updated Date |
| ALIAS_UpdatedTime | time |  |  | SI | Updated Time |
| ALIAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ32DR | - |  |  | SI | Child Reference: Eyesight |
| Q31Q1 | - |  |  | SI | Dexterity assessment for |
| Q31Q2 | - |  |  | SI | Able to attend to peritoneal dialysis connection |
| Q31Q3 | - |  |  | SI | Able to attend to peritoneal dialysis disconnectio... |
| Q31Q4 | - |  |  | SI | Able to open gauze packaging |
| Q31Q5 | - |  |  | SI | Able to clamp  unclamp catheter lines |
| Q31Q6 | - |  |  | SI | Able to remove and replace cap |
| Q31Q7 | - |  |  | SI | Able to break phalange |
| Q31Q8 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*