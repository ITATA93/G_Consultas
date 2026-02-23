# SQLUser.PA_PersonPackageDet

**Schema:** SQLUser
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | varchar | PK |  | NO | PA_PersonPackage Parent Reference |
| DET_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DET_ARCOS_DR | varchar |  | FK | SI | Des Ref ARCOS |
| DET_ChargeDifferential | varchar |  |  | SI | Charge Differential |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_ExclProportionCalc | varchar |  |  | SI | Exclude for Proportion Calculation |
| DET_ExcludePriorities | varchar |  |  | SI | Exclude Priorities |
| DET_FixedProportionAmount | double |  |  | SI | Fixed Proportion Amount |
| DET_GroupSubGroupLimit | double |  |  | SI | Group/Sub Group Limit Amount |
| DET_LimitQty | double |  |  | SI | LimitQty |
| DET_MainOrder | varchar |  |  | SI | MainOrder |
| DET_Optional | varchar |  |  | SI | Optional |
| DET_OrdItemOrdSetPackPrice | double |  |  | SI | Order Item/Order Set Package Price |
| DET_OrdItemOrdSetPrice | double |  |  | SI | Order Item/Order Set Price |
| DET_OrdItemOrdSetQtyCons | double |  |  | SI | Order Item/Order Quantity Consumed |
| DET_OrderItemLimit | double |  |  | SI | Order Item Limit Amount |
| DET_OrderItemLimitPrice | double |  |  | SI | Order Item Limit Price |
| DET_PackageOrderItemPrice | double |  |  | SI | Package Order Item Price |
| DET_PerNewborn | varchar |  |  | SI | Per Newborn |
| DET_PriceOverLimit | double |  |  | SI | PriceOverLimit |
| DET_PriceUnderLimit | double |  |  | SI | PriceUnderLimit |
| DET_RowId | varchar |  |  | NO | - |
| DET_Text1 | varchar |  |  | SI | Text1 |
| DET_Text2 | varchar |  |  | SI | Text2 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*