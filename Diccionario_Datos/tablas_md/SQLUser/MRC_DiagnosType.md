# SQLUser.MRC_DiagnosType

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DTYP_RowId | bigint | PK |  | NO | - |
| ChildQ83DR | - |  |  | SI | Child Reference: Evaluación Motivacional |
| DTYP_Code | varchar |  |  | NO | Code |
| DTYP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DTYP_CreatedDate | date |  |  | SI | Created Date |
| DTYP_CreatedTime | time |  |  | SI | Created Time |
| DTYP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DTYP_DateFrom | date |  |  | SI | DateFrom |
| DTYP_DateTo | date |  |  | SI | DateTo |
| DTYP_Desc | varchar |  |  | NO | Description |
| DTYP_NoSendToCoding | varchar |  |  | SI | No Send To Coding |
| DTYP_Owner | varchar |  |  | SI | Owner |
| DTYP_UpdatedDate | date |  |  | SI | Updated Date |
| DTYP_UpdatedTime | time |  |  | SI | Updated Time |
| DTYP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q11Q1 | - |  |  | SI | Área |
| Q11Q2 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*