# SQLUser.ORC_OperationAlias

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ALIAS_ParRef | bigint | PK |  | NO | ORC_Operation Parent Reference |
| ALIAS_Childsub | double |  |  | NO | Childsub |
| ALIAS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ALIAS_CreatedDate | date |  |  | SI | Created Date |
| ALIAS_CreatedTime | time |  |  | SI | Created Time |
| ALIAS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ALIAS_RowId | varchar |  |  | NO | - |
| ALIAS_Text | varchar |  |  | SI | Text |
| ALIAS_UpdatedDate | date |  |  | SI | Updated Date |
| ALIAS_UpdatedTime | time |  |  | SI | Updated Time |
| ALIAS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q03Q1 | - |  |  | SI | Drain type |
| Q03Q2 | - |  |  | SI | If other please specify |
| Q03Q3 | - |  |  | SI | Expiry date |
| Q03Q4 | - |  |  | SI | Lot number |
| Q03Q5 | - |  |  | SI | Site |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*