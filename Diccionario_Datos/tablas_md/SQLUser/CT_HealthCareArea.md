# SQLUser.CT_HealthCareArea

**Schema:** SQLUser
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HCA_RowId | bigint | PK |  | NO | - |
| ChildQ162DR | - |  |  | SI | Child Reference: Adult Pre-Admission Services |
| HCA_Code | varchar |  |  | NO | Code |
| HCA_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HCA_CreatedDate | date |  |  | SI | Created Date |
| HCA_CreatedTime | time |  |  | SI | Created Time |
| HCA_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HCA_DateFrom | date |  |  | SI | Date From |
| HCA_DateTo | date |  |  | SI | Date To |
| HCA_Desc | varchar |  |  | NO | Description |
| HCA_HCR_DR | bigint |  | FK | SI | Des Ref HCR |
| HCA_InsuranceType_DR | bigint |  | FK | SI | Des Ref ARCInsuranceType |
| HCA_Owner | varchar |  |  | SI | Owner |
| HCA_UpdatedDate | date |  |  | SI | Updated Date |
| HCA_UpdatedTime | time |  |  | SI | Updated Time |
| HCA_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Service |
| Q2 | - |  |  | SI | Other service |
| Q3 | - |  |  | SI | Contact name |
| Q4 | - |  |  | SI | Contact details |
| Q5 | - |  |  | SI | Notified of admission |
| Q6 | - |  |  | SI | Date |
| Q7 | - |  |  | SI | Time |
| Q8 | - |  |  | SI | Notes |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*