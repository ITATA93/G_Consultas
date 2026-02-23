# SQLUser.ORC_Intubation_Size

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORINT_RowId | bigint | PK |  | NO | - |
| ChildQ88DR | - |  |  | SI | Child Reference: Nutrition Focused Physical Findin... |
| ORINT_Code | varchar |  |  | NO | Code |
| ORINT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORINT_CreatedDate | date |  |  | SI | Created Date |
| ORINT_CreatedTime | time |  |  | SI | Created Time |
| ORINT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORINT_DateFrom | date |  |  | SI | Date From |
| ORINT_DateTo | date |  |  | SI | Date To |
| ORINT_Desc | varchar |  |  | NO | Description |
| ORINT_ETT | varchar |  |  | SI | Checkbox for ETT Restriction |
| ORINT_LMA | varchar |  |  | SI | Checkbox for LMA Restriction |
| ORINT_Owner | varchar |  |  | SI | Owner |
| ORINT_UpdatedDate | date |  |  | SI | Updated Date |
| ORINT_UpdatedTime | time |  |  | SI | Updated Time |
| ORINT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q103Q1 | - |  |  | SI | Nutritional diagnosis |
| Q103Q2 | - |  |  | SI | Related to |
| Q103Q3 | - |  |  | SI | As evidenced by |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*