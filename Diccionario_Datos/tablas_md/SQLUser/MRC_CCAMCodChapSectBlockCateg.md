# SQLUser.MRC_CCAMCodChapSectBlockCateg

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CATEG_ParRef | varchar | PK |  | NO | MRC_CCAMCodChapBlock Parent Reference |
| CATEG_Childsub | double |  |  | NO | Childsub |
| CATEG_Code | varchar |  |  | NO | Code |
| CATEG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CATEG_CreatedDate | date |  |  | SI | Created Date |
| CATEG_CreatedTime | time |  |  | SI | Created Time |
| CATEG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CATEG_DateFrom | date |  |  | SI | Date From |
| CATEG_DateTo | date |  |  | SI | Date To |
| CATEG_Desc | varchar |  |  | NO | Description |
| CATEG_RowId | varchar |  |  | NO | - |
| CATEG_UpdatedDate | date |  |  | SI | Updated Date |
| CATEG_UpdatedTime | time |  |  | SI | Updated Time |
| CATEG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q54Q1 | - |  |  | SI | Ex. físico |
| Q54Q2 | - |  |  | SI | Resultado |
| Q54Q3 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*