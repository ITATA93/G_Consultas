# SQLUser.ARC_InsurCoverStatus

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSCOV_RowId | bigint | PK |  | NO | - |
| ChildQ79DR | - |  |  | SI | Child Reference: Pensamiento |
| INSCOV_Code | varchar |  |  | NO | Code |
| INSCOV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| INSCOV_CreatedDate | date |  |  | SI | Created Date |
| INSCOV_CreatedTime | time |  |  | SI | Created Time |
| INSCOV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INSCOV_Desc | varchar |  |  | NO | Description |
| INSCOV_Owner | varchar |  |  | SI | Owner |
| INSCOV_UpdatedDate | date |  |  | SI | Updated Date |
| INSCOV_UpdatedTime | time |  |  | SI | Updated Time |
| INSCOV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q78Q1 | - |  |  | SI | Área |
| Q78Q2 | - |  |  | SI | Evaluación |
| Q78Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*