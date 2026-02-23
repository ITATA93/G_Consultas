# SQLUser.ARC_OrdSetDateOS

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OS_ParRef | varchar | PK |  | NO | ARC_OrdSetDate Parent Reference |
| ChildQ09DR | - |  |  | SI | Child Reference: Equipamiento_old |
| ChildQ26DR | - |  |  | SI | Child Reference: Cirugías adicionales |
| OS_Childsub | double |  |  | NO | Childsub |
| OS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OS_CreatedDate | date |  |  | SI | Created Date |
| OS_CreatedTime | time |  |  | SI | Created Time |
| OS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OS_Number | double |  |  | SI | Number |
| OS_OrderSet_DR | varchar |  | FK | SI | Des Ref to ARCOS |
| OS_ParentSection_DR | varchar |  | FK | SI | Parent Section |
| OS_Price | double |  |  | SI | Price |
| OS_RowId | varchar |  |  | NO | - |
| OS_SelectionDefault | varchar |  |  | SI | Order Selection Default uses Standard Type 'Select... |
| OS_UpdatedDate | date |  |  | SI | Updated Date |
| OS_UpdatedTime | time |  |  | SI | Updated Time |
| OS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q24Q1 | - |  |  | SI | Profesional de la Salud |
| Q24Q2 | - |  |  | SI | Rol |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*