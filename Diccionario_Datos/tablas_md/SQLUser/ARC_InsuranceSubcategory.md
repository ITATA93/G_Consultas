# SQLUser.ARC_InsuranceSubcategory

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUB_ParRef | bigint | PK |  | NO | ARC_InsuranceCategory Parent Reference |
| ChildQ81DR | - |  |  | SI | Child Reference: Psicomotricidad |
| Q80Q1 | - |  |  | SI | Evaluación |
| Q80Q2 | - |  |  | SI | Comentario (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SUB_Childsub | double |  |  | NO | Childsub |
| SUB_Code | varchar |  |  | NO | Code |
| SUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUB_CreatedDate | date |  |  | SI | Created Date |
| SUB_CreatedTime | time |  |  | SI | Created Time |
| SUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUB_Desc | varchar |  |  | NO | Description |
| SUB_RowId | varchar |  |  | NO | - |
| SUB_UpdatedDate | date |  |  | SI | Updated Date |
| SUB_UpdatedTime | time |  |  | SI | Updated Time |
| SUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*