# SQLUser.CT_LetterTemplateExpression

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LTE_RowId | bigint | PK |  | NO | - |
| LTE_Code | varchar |  |  | NO | - |
| LTE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LTE_CreatedDate | date |  |  | SI | Created Date |
| LTE_CreatedTime | time |  |  | SI | Created Time |
| LTE_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LTE_DateFrom | date |  |  | SI | - |
| LTE_DateTo | date |  |  | SI | - |
| LTE_Desc | varchar |  |  | NO | - |
| LTE_Expression | varchar |  |  | NO | - |
| LTE_Owner | varchar |  |  | SI | Owner |
| LTE_UpdatedDate | date |  |  | SI | Updated Date |
| LTE_UpdatedTime | time |  |  | SI | Updated Time |
| LTE_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q17Q1 | - |  |  | SI | Substance |
| Q17Q2 | - |  |  | SI | Route |
| Q17Q3 | - |  |  | SI | Last taken date / time |
| Q17Q4 | - |  |  | SI | Last taken time |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*