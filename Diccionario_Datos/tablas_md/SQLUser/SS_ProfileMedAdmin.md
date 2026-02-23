# SQLUser.SS_ProfileMedAdmin

**Schema:** SQLUser
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSPMED_ParRef | bigint | PK |  | NO | Parent  |
| SSPMED_AdminRoute | varchar |  |  | SI | Admin Routes |
| SSPMED_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SSPMED_CreatedDate | date |  |  | SI | Created Date |
| SSPMED_CreatedTime | time |  |  | SI | Created Time |
| SSPMED_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SSPMED_RowID | varchar |  |  | NO | - |
| SSPMED_SchemaGroup | varchar |  |  | SI | Schema Groups |
| SSPMED_UpdatedDate | date |  |  | SI | Updated Date |
| SSPMED_UpdatedTime | time |  |  | SI | Updated Time |
| SSPMED_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*