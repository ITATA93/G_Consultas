# SQLUser.MRC_CCAMCodChapSect

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SECT_ParRef | bigint | PK |  | NO | MRC_CCAMCodChap Parent Reference |
| ChildQ51DR | - |  |  | SI | Child Reference: Hospitalizaciones durante el emba... |
| Q32Q1 | - |  |  | SI | Fecha de aborto |
| Q32Q3 | - |  |  | SI | Comentario |
| Q32Q4 | - |  |  | SI | Tipo de Aborto |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SECT_Childsub | double |  |  | NO | Childsub |
| SECT_Code | varchar |  |  | NO | Code |
| SECT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SECT_CreatedDate | date |  |  | SI | Created Date |
| SECT_CreatedTime | time |  |  | SI | Created Time |
| SECT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SECT_DateFrom | date |  |  | SI | Date From |
| SECT_DateTo | date |  |  | SI | Date To |
| SECT_Desc | varchar |  |  | NO | Description |
| SECT_RowId | varchar |  |  | NO | - |
| SECT_UpdatedDate | date |  |  | SI | Updated Date |
| SECT_UpdatedTime | time |  |  | SI | Updated Time |
| SECT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*