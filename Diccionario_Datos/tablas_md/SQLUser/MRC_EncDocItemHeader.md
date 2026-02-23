# SQLUser.MRC_EncDocItemHeader

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HEADER_RowId | bigint | PK |  | NO | - |
| ChildQ75DR | - |  |  | SI | Child Reference: Examen Neurológico |
| HEADER_Code | varchar |  |  | NO | code |
| HEADER_CreatedDate | date |  |  | SI | Created Date |
| HEADER_CreatedTime | time |  |  | SI | Created Time |
| HEADER_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HEADER_Desc | varchar |  |  | NO | description |
| HEADER_Owner | varchar |  |  | SI | Owner |
| HEADER_System | varchar |  |  | SI | System created |
| HEADER_UpdatedDate | date |  |  | SI | Updated Date |
| HEADER_UpdatedTime | time |  |  | SI | Updated Time |
| HEADER_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q55Q1 | - |  |  | SI | Piel |
| Q55Q2 | - |  |  | SI | Evaluación |
| Q55Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*