# SQLUser.CT_HealthCareRegion

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HCR_RowId | bigint | PK |  | NO | - |
| HCR_Code | varchar |  |  | NO | Code |
| HCR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HCR_CreatedDate | date |  |  | SI | Created Date |
| HCR_CreatedTime | time |  |  | SI | Created Time |
| HCR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HCR_DateFrom | date |  |  | SI | Date From |
| HCR_DateTo | date |  |  | SI | Date To |
| HCR_Desc | varchar |  |  | NO | Description |
| HCR_Owner | varchar |  |  | SI | Owner |
| HCR_UpdatedDate | date |  |  | SI | Updated Date |
| HCR_UpdatedTime | time |  |  | SI | Updated Time |
| HCR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q162Q1 | - |  |  | SI | Service |
| Q162Q2 | - |  |  | SI | Other service |
| Q162Q3 | - |  |  | SI | Contact name |
| Q162Q4 | - |  |  | SI | Contact details |
| Q162Q5 | - |  |  | SI | Notified of admission |
| Q162Q6 | - |  |  | SI | Date |
| Q162Q7 | - |  |  | SI | Time |
| Q162Q8 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*