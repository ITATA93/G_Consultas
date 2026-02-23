# SQLUser.PAC_SMRStatus

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SMRSTAT_RowId | bigint | PK |  | NO | - |
| ChildQ17DR | - |  |  | SI | Child Reference: Pain control |
| Q15Q1 | - |  |  | SI | Micro goal |
| Q15Q2 | - |  |  | SI | Timing |
| Q15Q3 | - |  |  | SI | Outcome |
| Q15Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SMRSTAT_Code | varchar |  |  | NO | Code |
| SMRSTAT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SMRSTAT_CreatedDate | date |  |  | SI | Created Date |
| SMRSTAT_CreatedTime | time |  |  | SI | Created Time |
| SMRSTAT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SMRSTAT_Desc | varchar |  |  | NO | Description |
| SMRSTAT_Owner | varchar |  |  | SI | Owner |
| SMRSTAT_UpdatedDate | date |  |  | SI | Updated Date |
| SMRSTAT_UpdatedTime | time |  |  | SI | Updated Time |
| SMRSTAT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*