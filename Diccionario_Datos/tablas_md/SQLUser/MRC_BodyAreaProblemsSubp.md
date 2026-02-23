# SQLUser.MRC_BodyAreaProblemsSubp

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUBP_ParRef | varchar | PK |  | NO | MRC_BodyAreaProblems Parent Reference |
| ChildQ69DR | - |  |  | SI | Child Reference: Pupilas / Reflejos oculares |
| Q68Q1 | - |  |  | SI | Hallazgos |
| Q68Q2 | - |  |  | SI | Ubicación |
| Q68Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUBP_Childsub | double |  |  | NO | Childsub |
| SUBP_Code | varchar |  |  | NO | Code |
| SUBP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUBP_CreatedDate | date |  |  | SI | Created Date |
| SUBP_CreatedTime | time |  |  | SI | Created Time |
| SUBP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUBP_Desc | varchar |  |  | NO | Description |
| SUBP_RowId | varchar |  |  | NO | - |
| SUBP_UpdatedDate | date |  |  | SI | Updated Date |
| SUBP_UpdatedTime | time |  |  | SI | Updated Time |
| SUBP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*