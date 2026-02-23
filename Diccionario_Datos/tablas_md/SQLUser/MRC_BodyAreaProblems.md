# SQLUser.MRC_BodyAreaProblems

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PROB_ParRef | bigint | PK |  | NO | MRC_BodyArea Parent Reference |
| ChildQ68DR | - |  |  | SI | Child Reference: Ojos |
| PROB_Childsub | double |  |  | NO | Childsub |
| PROB_Code | varchar |  |  | NO | Code |
| PROB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PROB_CreatedDate | date |  |  | SI | Created Date |
| PROB_CreatedTime | time |  |  | SI | Created Time |
| PROB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PROB_Desc | varchar |  |  | NO | Description |
| PROB_Explanation | varchar |  |  | SI | Explanation |
| PROB_RowId | varchar |  |  | NO | - |
| PROB_UpdatedDate | date |  |  | SI | Updated Date |
| PROB_UpdatedTime | time |  |  | SI | Updated Time |
| PROB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q46Q1 | - |  |  | SI | Tipo de lesión |
| Q46Q2 | - |  |  | SI | Consistencia |
| Q46Q3 | - |  |  | SI | Cantidad |
| Q46Q4 | - |  |  | SI | Tamaño |
| Q46Q5 | - |  |  | SI | Ubicación |
| Q46Q6 | - |  |  | SI | Localización topográfica |
| Q46Q7 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*