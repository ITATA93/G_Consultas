# SQLUser.OEC_Interval

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Entry Orders**. Tipos y estados de órdenes.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INT_RowId | bigint | PK |  | NO | - |
| INT_Code | varchar |  |  | NO | Code |
| INT_CreatedDate | date |  |  | SI | Created Date |
| INT_CreatedTime | time |  |  | SI | Created Time |
| INT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INT_Desc | varchar |  |  | NO | Description |
| INT_UpdatedDate | date |  |  | SI | Updated Date |
| INT_UpdatedTime | time |  |  | SI | Updated Time |
| INT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q08Q1 | - |  |  | SI | Item |
| Q08Q2 | - |  |  | SI | 1st Count |
| Q08Q3 | - |  |  | SI | Complete |
| Q08Q4 | - |  |  | SI | Incomplete |
| Q08Q5 | - |  |  | SI | Final Count |
| Q08Q6 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*