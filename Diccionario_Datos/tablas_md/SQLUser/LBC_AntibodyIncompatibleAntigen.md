# SQLUser.LBC_AntibodyIncompatibleAntigen

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCABIA_ParRef | bigint | PK |  | NO | Parent Antibody |
| LBCABIA_CodeTableTags | varchar |  |  | SI | List of code table tags |
| LBCABIA_CreatedDate | date |  |  | SI | Created Date |
| LBCABIA_CreatedTime | time |  |  | SI | Created Time |
| LBCABIA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCABIA_IncompatibleAntigen_DR | bigint |  | FK | NO | Incompatible Antigen |
| LBCABIA_NTAction | varchar |  |  | SI | Not-Test Action |
| LBCABIA_RowID | varchar |  |  | NO | - |
| LBCABIA_RuleAction | varchar |  |  | NO | Rule Action |
| LBCABIA_UpdatedDate | date |  |  | SI | Updated Date |
| LBCABIA_UpdatedTime | time |  |  | SI | Updated Time |
| LBCABIA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q18Q1 | - |  |  | SI | Time from |
| Q18Q2 | - |  |  | SI | Time to |
| Q18Q3 | - |  |  | SI | Sensitivity |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*