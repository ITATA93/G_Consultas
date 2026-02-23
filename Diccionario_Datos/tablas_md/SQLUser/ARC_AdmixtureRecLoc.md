# SQLUser.ARC_AdmixtureRecLoc

**Schema:** SQLUser
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | ARC_AdmixtureRecipe Parent Reference |
| ChildQ31DR | - |  |  | SI | Child Reference: Lentes |
| LOC_AvailQty | double |  |  | SI | Available Qty |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref To CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LOC_CreatedDate | date |  |  | SI | Created Date |
| LOC_CreatedTime | time |  |  | SI | Created Time |
| LOC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LOC_DateFrom | date |  |  | SI | DateFrom |
| LOC_DateTo | date |  |  | SI | DateTo |
| LOC_DirtyQty | double |  |  | SI | Dirty Quantity |
| LOC_FreeStorageBin | varchar |  |  | SI | Free Storage Bin |
| LOC_INCSB_DR | bigint |  | FK | SI | Des Ref To INCSB |
| LOC_IsTrfFlag | varchar |  |  | SI | Issue Transfer Flag |
| LOC_LogQty | double |  |  | SI | Logical Quantity |
| LOC_MaxQty | double |  |  | SI | Maximum Quantity (Limit of Storage) |
| LOC_MinQty | double |  |  | SI | Minimum Quantity |
| LOC_RepLev | double |  |  | SI | Replenish Level |
| LOC_RepQty | double |  |  | SI | Replenish Quantity |
| LOC_ReservedQty | double |  |  | SI | Reserved Qty |
| LOC_RowId | varchar |  |  | NO | - |
| LOC_UpdatedDate | date |  |  | SI | Updated Date |
| LOC_UpdatedTime | time |  |  | SI | Updated Time |
| LOC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LOC_WardStock | varchar |  |  | SI | Ward Stock Replenishment option |
| LOC_WareHouse_DR | bigint |  | FK | SI | Des Ref to CTLOC |
| Q30Q1 | - |  |  | SI | Sin Prótesis Dental |
| Q30Q2 | - |  |  | SI | Ubicación Prótesis |
| Q30Q3 | - |  |  | SI | Estado |
| Q30Q4 | - |  |  | SI | Tipo de Prótesis |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*