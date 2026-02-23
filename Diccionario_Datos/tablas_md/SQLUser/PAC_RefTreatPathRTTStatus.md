# SQLUser.PAC_RefTreatPathRTTStatus

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Estados posibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RTPRTT_RowId | bigint | PK |  | NO | - |
| Q04Q1 | - |  |  | SI | Persons present |
| Q04Q2 | - |  |  | SI | Other person present |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| RTPRTT_Code | varchar |  |  | NO | Code |
| RTPRTT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RTPRTT_CreatedDate | date |  |  | SI | Created Date |
| RTPRTT_CreatedTime | time |  |  | SI | Created Time |
| RTPRTT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RTPRTT_DateFrom | date |  |  | SI | Date From |
| RTPRTT_DateTo | date |  |  | SI | Date To |
| RTPRTT_Desc | varchar |  |  | NO | Description |
| RTPRTT_NationalCode | varchar |  |  | SI | National Code |
| RTPRTT_Owner | varchar |  |  | SI | Owner |
| RTPRTT_Rank | integer |  |  | SI | Rank |
| RTPRTT_Significance | double |  |  | SI | Significance |
| RTPRTT_UpdatedDate | date |  |  | SI | Updated Date |
| RTPRTT_UpdatedTime | time |  |  | SI | Updated Time |
| RTPRTT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*