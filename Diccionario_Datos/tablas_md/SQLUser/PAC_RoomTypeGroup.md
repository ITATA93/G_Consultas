# SQLUser.PAC_RoomTypeGroup

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ROOMTG_RowId | bigint | PK |  | NO | - |
| ChildQ9DR | - |  |  | SI | Child Reference: Recovery / improvement of  motor ... |
| Q7Q1 | - |  |  | SI | Micro goal |
| Q7Q2 | - |  |  | SI | Timing |
| Q7Q3 | - |  |  | SI | Outcome |
| Q7Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| ROOMTG_Code | varchar |  |  | NO | Code |
| ROOMTG_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ROOMTG_CreatedDate | date |  |  | SI | Created Date |
| ROOMTG_CreatedTime | time |  |  | SI | Created Time |
| ROOMTG_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ROOMTG_DateFrom | date |  |  | SI | Date From |
| ROOMTG_DateTo | date |  |  | SI | Date To |
| ROOMTG_Desc | varchar |  |  | NO | Description |
| ROOMTG_InsType_DR | bigint |  | FK | SI | Des Ref Insurance Type |
| ROOMTG_Owner | varchar |  |  | SI | Owner |
| ROOMTG_RoomTypes | varchar |  |  | SI | Room Types |
| ROOMTG_UpdatedDate | date |  |  | SI | Updated Date |
| ROOMTG_UpdatedTime | time |  |  | SI | Updated Time |
| ROOMTG_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*