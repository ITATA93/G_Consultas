# SQLUser.SS_ProfileOrderCategory

**Schema:** SQLUser
**Columnas:** 19
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OC_ParRef | bigint | PK |  | NO | Parent table |
| OC_AllowAmendStatAfterDischarge | varchar |  |  | SI | Allowed To Amend Status After Financial Discharge |
| OC_BookingOnly | varchar |  |  | SI | Booking Only |
| OC_BypassReview | varchar |  |  | SI | Bypass Review |
| OC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OC_EditOnly | varchar |  |  | SI | Edit Only |
| OC_IncludeExclude | varchar |  |  | SI | Include Exclude |
| OC_OrdCat_DR | bigint |  | FK | SI | Order Category |
| OC_OrdSubCategory | bigint |  |  | SI | Order SubCategory |
| OC_OrderInvisbleItem | varchar |  |  | SI | Allow to Order Invisble Item |
| OC_OrderOnDischarge | varchar |  |  | SI | Order On Discharge |
| OC_OrderOnFinanceDisch | varchar |  |  | SI | Order On Financial Discharge |
| OC_OrderSets | varchar |  |  | SI | Allow to order Order Sets |
| OC_PermissionToReview | varchar |  |  | SI | Permission To Review |
| OC_RequireAuthorisation | varchar |  |  | SI | Require Authorisation |
| OC_RestrictEditDosingModelPermLev | varchar |  |  | SI | Restrict Edit Dosing Model Permission Level |
| OC_RestrictEditPermLev | varchar |  |  | SI | Restrict Edit Permission Level |
| OC_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*