# SQLUser.ARC_AdmixtureRecRoute

**Schema:** SQLUser
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RECRT_ParRef | bigint | PK |  | NO | ARC_AdmixtureRecipe Parent Reference |
| ChildQ33DR | - |  |  | SI | Child Reference: Dinero y/o Valores |
| Q32Q1 | - |  |  | SI | Sin Audífonos |
| Q32Q2 | - |  |  | SI | Estado |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RECRT_Childsub | double |  |  | NO | Childsub |
| RECRT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RECRT_CreatedDate | date |  |  | SI | Created Date |
| RECRT_CreatedTime | time |  |  | SI | Created Time |
| RECRT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RECRT_Route_DR | bigint |  | FK | NO | Route |
| RECRT_RowId | varchar |  |  | NO | - |
| RECRT_UpdatedDate | date |  |  | SI | Updated Date |
| RECRT_UpdatedTime | time |  |  | SI | Updated Time |
| RECRT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*