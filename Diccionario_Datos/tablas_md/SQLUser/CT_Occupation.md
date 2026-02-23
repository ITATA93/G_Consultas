# SQLUser.CT_Occupation

**Schema:** SQLUser
**Columnas:** 26
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTOCC_RowId | bigint | PK |  | NO | - |
| CTOCC_Code | varchar |  |  | NO | Occupation Code |
| CTOCC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTOCC_CodeTranslated | varchar |  |  | SI | Code Translated (Computed) |
| CTOCC_CreatedDate | date |  |  | SI | Created Date |
| CTOCC_CreatedTime | time |  |  | SI | Created Time |
| CTOCC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTOCC_DateFrom | date |  |  | SI | Date From |
| CTOCC_DateTo | date |  |  | SI | Date To |
| CTOCC_Desc | varchar |  |  | NO | Occupation Desc. |
| CTOCC_DescTranslated | varchar |  |  | SI | Description Translated (Computed) |
| CTOCC_Owner | varchar |  |  | SI | Owner |
| CTOCC_UpdatedDate | date |  |  | SI | Updated Date |
| CTOCC_UpdatedTime | time |  |  | SI | Updated Time |
| CTOCC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ27DR | - |  |  | SI | Child Reference: Drainage assessment |
| Q26Q1 | - |  |  | SI | Status |
| Q26Q2 | - |  |  | SI | Care / Troubleshoot |
| Q26Q3 | - |  |  | SI | Site care |
| Q26Q4 | - |  |  | SI | Site condition |
| Q26Q5 | - |  |  | SI | Dressing |
| Q26Q6 | - |  |  | SI | Dressing condition |
| Q26Q7 | - |  |  | SI | Assessment date and time |
| Q26Q8 | - |  |  | SI | Assessment time |
| Q26Q9 | - |  |  | SI | Assessing care provider |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*