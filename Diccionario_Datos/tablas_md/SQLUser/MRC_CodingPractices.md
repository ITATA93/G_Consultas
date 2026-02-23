# SQLUser.MRC_CodingPractices

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CODPR_RowId | bigint | PK |  | NO | - |
| CODPR_Code | varchar |  |  | NO | Code |
| CODPR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CODPR_CreatedDate | date |  |  | SI | Created Date |
| CODPR_CreatedTime | time |  |  | SI | Created Time |
| CODPR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CODPR_DateFrom | date |  |  | SI | Date From |
| CODPR_DateTo | date |  |  | SI | Date To |
| CODPR_Desc | varchar |  |  | NO | Description |
| CODPR_Owner | varchar |  |  | SI | Owner |
| CODPR_UpdatedDate | date |  |  | SI | Updated Date |
| CODPR_UpdatedTime | time |  |  | SI | Updated Time |
| CODPR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q173Q1 | - |  |  | SI | Item |
| Q173Q2 | - |  |  | SI | Descripción |
| Q173Q3 | - |  |  | SI | Lateralidad |
| Q173Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*