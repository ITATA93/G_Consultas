# SQLUser.PAC_RubellaImmune_Status

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RUBIMSTS_RowId | bigint | PK |  | NO | - |
| ChildQ11DR | - |  |  | SI | Child Reference: Transfer recovery |
| Q9Q1 | - |  |  | SI | Micro goal |
| Q9Q2 | - |  |  | SI | Timing |
| Q9Q3 | - |  |  | SI | Outcome |
| Q9Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RUBIMSTS_Active | varchar |  |  | SI | Active |
| RUBIMSTS_Code | varchar |  |  | NO | Code |
| RUBIMSTS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RUBIMSTS_CreatedDate | date |  |  | SI | Created Date |
| RUBIMSTS_CreatedTime | time |  |  | SI | Created Time |
| RUBIMSTS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RUBIMSTS_DateFrom | date |  |  | SI | Date From |
| RUBIMSTS_DateTo | date |  |  | SI | Date To |
| RUBIMSTS_Desc | varchar |  |  | NO | Description |
| RUBIMSTS_NationalCode | varchar |  |  | SI | National code |
| RUBIMSTS_Owner | varchar |  |  | SI | Owner |
| RUBIMSTS_UpdatedDate | date |  |  | SI | Updated Date |
| RUBIMSTS_UpdatedTime | time |  |  | SI | Updated Time |
| RUBIMSTS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*