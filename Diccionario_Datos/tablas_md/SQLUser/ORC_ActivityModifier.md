# SQLUser.ORC_ActivityModifier

**Schema:** SQLUser
**Columnas:** 18
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACTMOD_RowId | bigint | PK |  | NO | - |
| ACTMOD_Code | varchar |  |  | NO | Code |
| ACTMOD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACTMOD_CreatedDate | date |  |  | SI | Created Date |
| ACTMOD_CreatedTime | time |  |  | SI | Created Time |
| ACTMOD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACTMOD_DateFrom | date |  |  | SI | Date From |
| ACTMOD_DateTo | date |  |  | SI | Date To |
| ACTMOD_Desc | varchar |  |  | NO | Description |
| ACTMOD_Owner | varchar |  |  | SI | Owner |
| ACTMOD_UpdatedDate | date |  |  | SI | Updated Date |
| ACTMOD_UpdatedTime | time |  |  | SI | Updated Time |
| ACTMOD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ51DR | - |  |  | SI | Child Reference: Special Test 5 ( + or - ) |
| Q50Q1 | - |  |  | SI | Labral tear |
| Q50Q2 | - |  |  | SI | Left |
| Q50Q3 | - |  |  | SI | Right |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*