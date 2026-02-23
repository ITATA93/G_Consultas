# SQLUser.ARC_BillingItem

**Schema:** SQLUser
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ARCBI_RowID | bigint | PK |  | NO | - |
| ARCBI_BaseItem | varchar |  |  | SI | Base Item |
| ARCBI_BillingSubgroup_DR | varchar |  | FK | NO | Department/Billing Subgroup |
| ARCBI_Code | varchar |  |  | NO | Code |
| ARCBI_CodeTableTags | varchar |  |  | SI | List of code table tags |
| ARCBI_CreatedDate | date |  |  | SI | Created Date |
| ARCBI_CreatedTime | time |  |  | SI | Created Time |
| ARCBI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ARCBI_DateFrom | date |  |  | SI | Effective date for the record |
| ARCBI_DateTo | date |  |  | SI | Last day the record is active |
| ARCBI_Desc | varchar |  |  | NO | Description |
| ARCBI_ExcludeFromConing | varchar |  |  | SI | Exclude From Coning |
| ARCBI_ExcludeFromMedicare | varchar |  |  | SI | Exclude From Medicare |
| ARCBI_ExcludeInitiationItem | varchar |  |  | SI | Exclude Initiation Item |
| ARCBI_ItemMast_DR | varchar |  | FK | SI | Order Item |
| ARCBI_Owner | varchar |  |  | SI | Owner |
| ARCBI_UpdatedDate | date |  |  | SI | Updated Date |
| ARCBI_UpdatedTime | time |  |  | SI | Updated Time |
| ARCBI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ChildQ112DR | - |  |  | SI | Child Reference: Pulsos periféricos |
| Q46Q1 | - |  |  | SI | Tipo de lesión |
| Q46Q2 | - |  |  | SI | Consistencia |
| Q46Q3 | - |  |  | SI | Cantidad |
| Q46Q4 | - |  |  | SI | Tamaño |
| Q46Q5 | - |  |  | SI | Ubicación |
| Q46Q6 | - |  |  | SI | Localización topográfica |
| Q46Q7 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*