# SQLUser.PAC_ComplaintCategory

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CMC_RowId | bigint | PK |  | NO | - |
| CMC_Code | varchar |  |  | NO | Code |
| CMC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CMC_CreatedDate | date |  |  | SI | Created Date |
| CMC_CreatedTime | time |  |  | SI | Created Time |
| CMC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CMC_DateFrom | date |  |  | SI | Date From |
| CMC_DateTo | date |  |  | SI | Date To |
| CMC_Desc | varchar |  |  | NO | Description |
| CMC_Owner | varchar |  |  | SI | Owner |
| CMC_UpdatedDate | date |  |  | SI | Updated Date |
| CMC_UpdatedTime | time |  |  | SI | Updated Time |
| CMC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q19Q1 | - |  |  | SI | Other symptom |
| Q19Q2 | - |  |  | SI | Other symptom - Response |
| Q19Q3 | - |  |  | SI | Other symptom - Response |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*