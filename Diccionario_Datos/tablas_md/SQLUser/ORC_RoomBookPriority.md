# SQLUser.ORC_RoomBookPriority

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Órdenes**. Parámetros de órdenes médicas.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RBP_RowId | bigint | PK |  | NO | - |
| ChildQ38DR | - |  |  | SI | Child Reference: Procedure Observations |
| Q29Q1 | - |  |  | SI | Intervention |
| Q29Q2 | - |  |  | SI | Location |
| Q29Q3 | - |  |  | SI | Location other |
| Q29Q4 | - |  |  | SI | Number of samples |
| Q29Q5 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RBP_Code | varchar |  |  | NO | Code |
| RBP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RBP_CreatedDate | date |  |  | SI | Created Date |
| RBP_CreatedTime | time |  |  | SI | Created Time |
| RBP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RBP_DateFrom | date |  |  | SI | Date From |
| RBP_DateTo | date |  |  | SI | Date To |
| RBP_Desc | varchar |  |  | NO | Description |
| RBP_Order | varchar |  |  | SI | Sequence Order |
| RBP_Owner | varchar |  |  | SI | Owner |
| RBP_TargetTime | integer |  |  | SI | Priority Target Time (min) |
| RBP_UpdatedDate | date |  |  | SI | Updated Date |
| RBP_UpdatedTime | time |  |  | SI | Updated Time |
| RBP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*