# SQLUser.SS_GroupOrderCategory

**Schema:** SQLUser
**Columnas:** 16
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SSORD_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| SSORD_BookingOnly | varchar |  |  | SI | BookingOnly |
| SSORD_BypassReview | varchar |  |  | SI | BypassReview |
| SSORD_Childsub | double |  |  | NO | Childsub |
| SSORD_EditOnly | varchar |  |  | SI | EditOnly |
| SSORD_IncludeExclude | varchar |  |  | SI | Include Exclude |
| SSORD_OrdCat_DR | bigint |  | FK | SI | Des Ref to OrdCat |
| SSORD_OrdSubCategory | bigint |  |  | SI | Order SubCategory des ref |
| SSORD_OrderInvisbleItem | varchar |  |  | SI | Allow to Order Invisble Item |
| SSORD_OrderOnDischarge | varchar |  |  | SI | Order On Discharge |
| SSORD_OrderOnFinanceDisch | varchar |  |  | SI | OrderOnFinanceDisch |
| SSORD_OrderSets | varchar |  |  | SI | Allow to order Order Sets |
| SSORD_PermissionToReview | varchar |  |  | SI | PermissionToReview |
| SSORD_RequireAuthorisation | varchar |  |  | SI | Require Authorisation |
| SSORD_RestrictEditPermLev | varchar |  |  | SI | Restrict Edit Permission Level |
| SSORD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*