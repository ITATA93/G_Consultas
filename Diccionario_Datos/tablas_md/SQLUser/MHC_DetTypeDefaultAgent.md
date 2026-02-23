# SQLUser.MHC_DetTypeDefaultAgent

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AGN_ParRef | bigint | PK |  | NO | MHC_DetentionType Parent Reference |
| AGN_Childsub | double |  |  | NO | Childsub |
| AGN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AGN_CreatedDate | date |  |  | SI | Created Date |
| AGN_CreatedTime | time |  |  | SI | Created Time |
| AGN_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AGN_DefaultAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| AGN_Role_DR | bigint |  | FK | SI | Des Ref CTRole |
| AGN_RowId | varchar |  |  | NO | - |
| AGN_UpdatedDate | date |  |  | SI | Updated Date |
| AGN_UpdatedTime | time |  |  | SI | Updated Time |
| AGN_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ05DR | - |  |  | SI | Child Reference: Equipos y Familiares Que Efectuar... |
| Q01Q1 | - |  |  | SI | Programa |
| Q01Q2 | - |  |  | SI | Profesional |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*