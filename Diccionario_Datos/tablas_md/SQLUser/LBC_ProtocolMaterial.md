# SQLUser.LBC_ProtocolMaterial

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Laboratorio**. Parámetros del módulo de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCPTM_ParRef | bigint | PK |  | NO | Parent Protocol |
| LBCPTM_CreatedDate | date |  |  | SI | Created Date |
| LBCPTM_CreatedTime | time |  |  | SI | Created Time |
| LBCPTM_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCPTM_Material_DR | bigint |  | FK | SI | Lab Material  |
| LBCPTM_Notes | varchar |  |  | SI | Notes |
| LBCPTM_PrintLabel | varchar |  |  | SI | Print Labels |
| LBCPTM_RowID | varchar |  |  | NO | - |
| LBCPTM_SnomedTerm_DR | bigint |  | FK | SI | SNOMED Code |
| LBCPTM_Source_DR | varchar |  | FK | SI | Source Procedure |
| LBCPTM_UpdatedDate | date |  |  | SI | Updated Date |
| LBCPTM_UpdatedTime | time |  |  | SI | Updated Time |
| LBCPTM_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q169Q1 | - |  |  | SI | Inmunización que protege contra |
| Q169Q2 | - |  |  | SI | Número de Dosis |
| Q169Q3 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*