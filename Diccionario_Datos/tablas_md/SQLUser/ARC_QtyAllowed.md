# SQLUser.ARC_QtyAllowed

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QTYAL_RowId | bigint | PK |  | NO | - |
| Q27Q1 | - |  |  | SI | Nombre del profesional |
| Q27Q2 | - |  |  | SI | Tipo Profesional |
| QTYAL_Code | varchar |  |  | NO | Code |
| QTYAL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QTYAL_CreatedDate | date |  |  | SI | Created Date |
| QTYAL_CreatedTime | time |  |  | SI | Created Time |
| QTYAL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QTYAL_Desc | varchar |  |  | NO | Description |
| QTYAL_InPat | double |  |  | SI | InPatient |
| QTYAL_OutPat | double |  |  | SI | OutPatient |
| QTYAL_Owner | varchar |  |  | SI | Owner |
| QTYAL_Period | varchar |  |  | SI | Time Period |
| QTYAL_Total | double |  |  | SI | Total |
| QTYAL_UpdatedDate | date |  |  | SI | Updated Date |
| QTYAL_UpdatedTime | time |  |  | SI | Updated Time |
| QTYAL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*