# SQLUser.INC_ItmLoc

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Incidentes**. Reportes de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INCIL_INCI_ParRef | bigint | PK |  | NO | Des Ref To INCI |
| ChildQ65DR | - |  |  | SI | Child Reference: Motor Examination |
| INCIL_AvailQty | double |  |  | SI | Available Qty |
| INCIL_CTLOC_DR | bigint |  | FK | NO | Des Ref To CTLOC |
| INCIL_ChildSub | numeric |  |  | NO | INCIL Childsub (New Key) |
| INCIL_CreatedDate | date |  |  | SI | Created Date |
| INCIL_CreatedTime | time |  |  | SI | Created Time |
| INCIL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| INCIL_DateFrom | date |  |  | SI | DateFrom |
| INCIL_DateTo | date |  |  | SI | DateTo |
| INCIL_DefStorageBin_DR | varchar |  | FK | SI | Default Storage Bin, Des Ref CTLocStorageBin |
| INCIL_DirtyQty | double |  |  | SI | Dirty Quantity |
| INCIL_FinalVendor_DR | bigint |  | FK | SI | Des Ref Vendor |
| INCIL_FreeStorageBin | varchar |  |  | SI | Free Storage Bin |
| INCIL_INCSB_DR | bigint |  | FK | SI | Des Ref To INCSB |
| INCIL_IsTrfFlag | varchar |  |  | SI | Issue Transfer Flag |
| INCIL_LastPurchasePrice | double |  |  | SI | Last Purchase Price  |
| INCIL_LogQty | double |  |  | SI | Logical Quantity |
| INCIL_MainStore | varchar |  |  | SI | Main Store |
| INCIL_MaxQty | double |  |  | SI | Maximum Quantity (Limit of Storage) |
| INCIL_MinQty | double |  |  | SI | Minimum Quantity |
| INCIL_ReordLevel | double |  |  | SI | Reorder Level |
| INCIL_ReordQty | double |  |  | SI | Reorder Quantity |
| INCIL_RepLev | double |  |  | SI | Replenish Level |
| INCIL_RepQty | double |  |  | SI | Replenish Quantity |
| INCIL_ReservedQty | double |  |  | SI | Reserved Qty |
| INCIL_RowId | varchar |  |  | NO | - |
| INCIL_StockQtyLastYear | double |  |  | SI | Stock Qty of Prev. Year |
| INCIL_TransferUOM_DR | bigint |  | FK | SI | Des Ref UOM |
| INCIL_UnitCost | double |  |  | SI | Unit Cost |
| INCIL_UpdatedDate | date |  |  | SI | Updated Date |
| INCIL_UpdatedTime | time |  |  | SI | Updated Time |
| INCIL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| INCIL_WardStock | varchar |  |  | SI | Ward Stock Replenishment option |
| INCIL_WareHouse_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| Q66Q1 | - |  |  | SI | Tendon |
| Q66Q2 | - |  |  | SI | Right |
| Q66Q3 | - |  |  | SI | Left |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*