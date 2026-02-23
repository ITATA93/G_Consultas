# SQLUser.PAC_RefReasonNotSubs

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFRNS_RowId | bigint | PK |  | NO | - |
| ChildQ9DR | - |  |  | SI | Child Reference: Exit site condition |
| Q8Q1 | - |  |  | SI | Date |
| Q8Q2 | - |  |  | SI | Taken for |
| Q8Q3 | - |  |  | SI | Result |
| Q8Q4 | - |  |  | SI | Treatment |
| Q8Q5 | - |  |  | SI | Comment |
| Q8Q6 | - |  |  | SI | Taken by |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| REFRNS_Code | varchar |  |  | NO | Code |
| REFRNS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| REFRNS_CreatedDate | date |  |  | SI | Created Date |
| REFRNS_CreatedTime | time |  |  | SI | Created Time |
| REFRNS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| REFRNS_DateFrom | date |  |  | SI | Date From |
| REFRNS_DateTo | date |  |  | SI | Date To |
| REFRNS_Desc | varchar |  |  | NO | Description |
| REFRNS_Owner | varchar |  |  | SI | Owner |
| REFRNS_UpdatedDate | date |  |  | SI | Updated Date |
| REFRNS_UpdatedTime | time |  |  | SI | Updated Time |
| REFRNS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*