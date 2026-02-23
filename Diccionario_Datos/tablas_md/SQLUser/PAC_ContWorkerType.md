# SQLUser.PAC_ContWorkerType

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| WORKT_RowId | bigint | PK |  | NO | - |
| ChildQ58DR | - |  |  | SI | Child Reference: Procedure details |
| Q57Q1 | - |  |  | SI | Name |
| Q57Q2 | - |  |  | SI | Role |
| Q57Q3 | - |  |  | SI | Other role |
| Q57Q4 | - |  |  | SI | Presence |
| Q57Q5 | - |  |  | SI | Other presence |
| Q57Q6 | - |  |  | SI | Arrival time |
| Q57Q7 | - |  |  | SI | Comments |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| WORKT_Code | varchar |  |  | NO | Code |
| WORKT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| WORKT_CreatedDate | date |  |  | SI | Created Date |
| WORKT_CreatedTime | time |  |  | SI | Created Time |
| WORKT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| WORKT_DateFrom | date |  |  | SI | Date From |
| WORKT_DateTo | date |  |  | SI | Date To |
| WORKT_Desc | varchar |  |  | NO | Description |
| WORKT_Owner | varchar |  |  | SI | Owner |
| WORKT_UpdatedDate | date |  |  | SI | Updated Date |
| WORKT_UpdatedTime | time |  |  | SI | Updated Time |
| WORKT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*