# SQLUser.PAC_Presentation

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PRES_RowId | bigint | PK |  | NO | - |
| ChildQ09DR | - |  |  | SI | Child Reference: Family / Social / Work reintegrat... |
| PRES_Code | varchar |  |  | NO | Code |
| PRES_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PRES_CreatedDate | date |  |  | SI | Created Date |
| PRES_CreatedTime | time |  |  | SI | Created Time |
| PRES_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PRES_DateFrom | date |  |  | SI | Date From |
| PRES_DateTo | date |  |  | SI | Date To |
| PRES_Desc | varchar |  |  | NO | Description |
| PRES_NationalCode | varchar |  |  | SI | National Code |
| PRES_Owner | varchar |  |  | SI | Owner |
| PRES_UpdatedDate | date |  |  | SI | Updated Date |
| PRES_UpdatedTime | time |  |  | SI | Updated Time |
| PRES_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q07Q1 | - |  |  | SI | Micro goal |
| Q07Q2 | - |  |  | SI | Timing |
| Q07Q3 | - |  |  | SI | Outcome |
| Q07Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*