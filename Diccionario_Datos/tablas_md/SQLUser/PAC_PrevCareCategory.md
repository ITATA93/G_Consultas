# SQLUser.PAC_PrevCareCategory

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPREV_RowID | bigint | PK |  | NO | - |
| PACPREV_Code | varchar |  |  | NO | Code |
| PACPREV_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPREV_CreatedDate | date |  |  | SI | Created Date |
| PACPREV_CreatedTime | time |  |  | SI | Created Time |
| PACPREV_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPREV_DateFrom | date |  |  | SI | Date From |
| PACPREV_DateTo | date |  |  | SI | Date To |
| PACPREV_Desc | varchar |  |  | NO | Description |
| PACPREV_Owner | varchar |  |  | SI | Owner |
| PACPREV_UpdatedDate | date |  |  | SI | Updated Date |
| PACPREV_UpdatedTime | time |  |  | SI | Updated Time |
| PACPREV_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| PACPREV_Vaccination | bit |  |  | SI | Vaccination Checkbox |
| Q05Q1 | - |  |  | SI | Micro goal |
| Q05Q2 | - |  |  | SI | Timing |
| Q05Q3 | - |  |  | SI | Outcome |
| Q05Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*