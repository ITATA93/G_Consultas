# SQLUser.OE_OrderItemChange

**Schema:** SQLUser
**Columnas:** 20
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Órdenes Médicas**. Solicitudes de exámenes, procedimientos, etc. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OICH_RowId | bigint | PK |  | NO | - |
| ChildQ32DR | - |  |  | SI | Child Reference: Fingers |
| OICH_Action | varchar |  |  | SI | Action  |
| OICH_NotifyUser | varchar |  |  | SI | NotifyUserOfModification    |
| OICH_OrdItemCondDesc | varchar |  |  | SI | OICHOrdItemCondDesc   |
| OICH_OrdItemDesc | varchar |  |  | SI | OrdItemDesc   |
| OICH_OrdItemShortDesc | varchar |  |  | SI | OICHOrdItemShortDesc   |
| OICH_OrdItem_DR | varchar |  | FK | SI | Des Ref OEOrdItem  |
| OICH_Reason_DR | bigint |  | FK | SI | Des Ref MRCVarianceReason  |
| OICH_UpdatedDate | date |  |  | SI | Updated Date |
| OICH_UpdatedTime | time |  |  | SI | UpdatedTime |
| OICH_UpdatedUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| Q31Q1 | - |  |  | SI | Movement |
| Q31Q2 | - |  |  | SI | Strength - Right |
| Q31Q3 | - |  |  | SI | Strength - Left |
| Q31Q4 | - |  |  | SI | AROM - Right |
| Q31Q5 | - |  |  | SI | AROM - Left |
| Q31Q6 | - |  |  | SI | PROM - Right |
| Q31Q7 | - |  |  | SI | PROM - Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*