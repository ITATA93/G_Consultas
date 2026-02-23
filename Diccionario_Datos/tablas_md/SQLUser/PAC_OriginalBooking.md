# SQLUser.PAC_OriginalBooking

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ORIGBOOK_RowId | bigint | PK |  | NO | - |
| ORIGBOOK_Code | varchar |  |  | NO | Code |
| ORIGBOOK_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ORIGBOOK_CreatedDate | date |  |  | SI | Created Date |
| ORIGBOOK_CreatedTime | time |  |  | SI | Created Time |
| ORIGBOOK_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ORIGBOOK_DateFrom | date |  |  | SI | Date From |
| ORIGBOOK_DateTo | date |  |  | SI | Date To |
| ORIGBOOK_Desc | varchar |  |  | NO | Description |
| ORIGBOOK_NationalCode | varchar |  |  | SI | National code |
| ORIGBOOK_Owner | varchar |  |  | SI | Owner |
| ORIGBOOK_UpdatedDate | date |  |  | SI | Updated Date |
| ORIGBOOK_UpdatedTime | time |  |  | SI | Updated Time |
| ORIGBOOK_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q24Q1 | - |  |  | SI | Goal |
| Q24Q2 | - |  |  | SI | Time Frame |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*