# SQLUser.CT_OrderTimeline

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLORD_RowID | bigint | PK |  | NO | - |
| CTLORD_Code | varchar |  |  | SI | Code  |
| CTLORD_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| CTLORD_CreatedDate | date |  |  | SI | Created Date |
| CTLORD_CreatedTime | time |  |  | SI | Created Time |
| CTLORD_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTLORD_DateFrom | date |  |  | SI | Date From |
| CTLORD_DateTo | date |  |  | SI | Date To |
| CTLORD_Desc | varchar |  |  | SI | Description |
| CTLORD_OrderCategory | varchar |  |  | SI | Order Category |
| CTLORD_OrderStatuses | varchar |  |  | SI | Order Statuses |
| CTLORD_OrderSubCategory | varchar |  |  | SI | Order SubCategory |
| CTLORD_Owner | varchar |  |  | SI | Owner |
| CTLORD_UpdatedDate | date |  |  | SI | Updated Date |
| CTLORD_UpdatedTime | time |  |  | SI | Updated Time |
| CTLORD_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q27Q1 | - |  |  | SI | Drainage present |
| Q27Q2 | - |  |  | SI | Drainage description |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*