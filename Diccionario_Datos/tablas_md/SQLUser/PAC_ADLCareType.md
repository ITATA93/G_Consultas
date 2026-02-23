# SQLUser.PAC_ADLCareType

**Schema:** SQLUser
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ADLCT_RowId | bigint | PK |  | NO | - |
| ADLCT_Code | varchar |  |  | NO | Code |
| ADLCT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ADLCT_ConvertToFIM | varchar |  |  | SI | Convert To FIM |
| ADLCT_CreatedDate | date |  |  | SI | Created Date |
| ADLCT_CreatedTime | time |  |  | SI | Created Time |
| ADLCT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ADLCT_DateFrom | date |  |  | SI | Date From |
| ADLCT_DateTo | date |  |  | SI | Date To |
| ADLCT_Desc | varchar |  |  | NO | Description |
| ADLCT_NationalCode | varchar |  |  | SI | National Code |
| ADLCT_Owner | varchar |  |  | SI | Owner |
| ADLCT_UpdatedDate | date |  |  | SI | Updated Date |
| ADLCT_UpdatedTime | time |  |  | SI | Updated Time |
| ADLCT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q46Q1 | - |  |  | SI | Date |
| Q46Q2 | - |  |  | SI | Time |
| Q46Q3 | - |  |  | SI | Note |
| Q46Q4 | - |  |  | SI | Actions |
| Q46Q5 | - |  |  | SI | Drain Check |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*