# SQLUser.MRC_DRGCodesVersion

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VER_ParRef | bigint | PK |  | NO | MRC_DRGCodes Parent Reference |
| ChildQ36DR | - |  |  | SI | Child Reference: Oídos |
| Q34Q1 | - |  |  | SI | Hallazgo |
| Q34Q2 | - |  |  | SI | Ubicación |
| Q34Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| VER_Childsub | double |  |  | NO | Childsub |
| VER_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| VER_CreatedDate | date |  |  | SI | Created Date |
| VER_CreatedTime | time |  |  | SI | Created Time |
| VER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| VER_RowId | varchar |  |  | NO | - |
| VER_UpdatedDate | date |  |  | SI | Updated Date |
| VER_UpdatedTime | time |  |  | SI | Updated Time |
| VER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| VER_Version_DR | bigint |  | FK | SI | Des Ref Version |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*