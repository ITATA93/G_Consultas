# SQLUser.PAC_SNAPCareType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SNAPCT_RowId | bigint | PK |  | NO | - |
| ChildQ19DR | - |  |  | SI | Child Reference: Fall prevention |
| Q17Q1 | - |  |  | SI | Micro goal |
| Q17Q2 | - |  |  | SI | Timing |
| Q17Q3 | - |  |  | SI | Outcome |
| Q17Q4 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SNAPCT_Code | varchar |  |  | NO | Code |
| SNAPCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SNAPCT_ConvertedScore | varchar |  |  | SI | Display Converted Score |
| SNAPCT_CreatedDate | date |  |  | SI | Created Date |
| SNAPCT_CreatedTime | time |  |  | SI | Created Time |
| SNAPCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SNAPCT_DateFrom | date |  |  | SI | Date From |
| SNAPCT_DateTo | date |  |  | SI | Date To |
| SNAPCT_Desc | varchar |  |  | NO | Description |
| SNAPCT_NationalCode | varchar |  |  | SI | National Code |
| SNAPCT_Owner | varchar |  |  | SI | Owner |
| SNAPCT_UpdatedDate | date |  |  | SI | Updated Date |
| SNAPCT_UpdatedTime | time |  |  | SI | Updated Time |
| SNAPCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*