# SQLUser.ORC_QuantityofLiquor

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUOFLI_RowId | bigint | PK |  | NO | - |
| Q09Q1 | - |  |  | SI | Date |
| Q09Q2 | - |  |  | SI | Time |
| Q09Q3 | - |  |  | SI | ml |
| Q09Q4 | - |  |  | SI | Overnight (ml/hr) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| QUOFLI_Code | varchar |  |  | NO | Code |
| QUOFLI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| QUOFLI_CreatedDate | date |  |  | SI | Created Date |
| QUOFLI_CreatedTime | time |  |  | SI | Created Time |
| QUOFLI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| QUOFLI_DateFrom | date |  |  | SI | Date From |
| QUOFLI_DateTo | date |  |  | SI | Date To |
| QUOFLI_Desc | varchar |  |  | NO | Description |
| QUOFLI_Owner | varchar |  |  | SI | Owner |
| QUOFLI_UpdatedDate | date |  |  | SI | Updated Date |
| QUOFLI_UpdatedTime | time |  |  | SI | Updated Time |
| QUOFLI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*