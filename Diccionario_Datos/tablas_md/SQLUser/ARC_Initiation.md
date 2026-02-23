# SQLUser.ARC_Initiation

**Schema:** SQLUser
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCINI_RowID | bigint | PK |  | NO | - |
| ARCINI_BillingDescription | varchar |  |  | SI | Billing Description |
| ARCINI_Code | varchar |  |  | NO | Code |
| ARCINI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCINI_CreatedDate | date |  |  | SI | Created Date |
| ARCINI_CreatedTime | time |  |  | SI | Created Time |
| ARCINI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCINI_DateFrom | date |  |  | SI | Effective date for the record |
| ARCINI_DateTo | date |  |  | SI | Last day the record is active |
| ARCINI_Desc | varchar |  |  | NO | Description |
| ARCINI_Inpatient | varchar |  |  | SI | Inpatient |
| ARCINI_License | varchar |  |  | SI | License |
| ARCINI_Owner | varchar |  |  | SI | Owner |
| ARCINI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCINI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCINI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ51DR | - |  |  | SI | Child Reference: Pulmón |
| Q36Q1 | - |  |  | SI | Hallazgos |
| Q36Q2 | - |  |  | SI | Ubicación |
| Q36Q3 | - |  |  | SI | Lateralidad |
| Q36Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*