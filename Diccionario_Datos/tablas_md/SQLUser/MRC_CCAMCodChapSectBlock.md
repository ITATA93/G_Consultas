# SQLUser.MRC_CCAMCodChapSectBlock

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BLOCK_ParRef | varchar | PK |  | NO | MRC_CCAMCodChapBlock Parent Reference |
| BLOCK_Childsub | double |  |  | NO | Childsub |
| BLOCK_Code | varchar |  |  | NO | Code |
| BLOCK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BLOCK_CreatedDate | date |  |  | SI | Created Date |
| BLOCK_CreatedTime | time |  |  | SI | Created Time |
| BLOCK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BLOCK_DateFrom | date |  |  | SI | Date From |
| BLOCK_DateTo | date |  |  | SI | Date To |
| BLOCK_Desc | varchar |  |  | NO | Description |
| BLOCK_RowId | varchar |  |  | NO | - |
| BLOCK_UpdatedDate | date |  |  | SI | Updated Date |
| BLOCK_UpdatedTime | time |  |  | SI | Updated Time |
| BLOCK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ54DR | - |  |  | SI | Child Reference: Examen físico |
| Q51Q1 | - |  |  | SI | N° de días |
| Q51Q2 | - |  |  | SI | Motivo de hospitalización |
| Q51Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*