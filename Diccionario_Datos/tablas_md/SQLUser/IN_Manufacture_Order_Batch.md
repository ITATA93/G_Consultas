# SQLUser.IN_Manufacture_Order_Batch

**Schema:** SQLUser
**Columnas:** 17
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MOBAT_ParRef | bigint | PK |  | NO | IN_Manufacture_Order Parent Reference |
| MOBAT_Childsub | double |  |  | NO | Childsub |
| MOBAT_DemandNo | varchar |  |  | SI | Demand Number |
| MOBAT_ExpiryDate | date |  |  | SI | Expiry Date |
| MOBAT_ExtBatchNo | varchar |  |  | SI | Ext BatchNo |
| MOBAT_ExtDispenseID | varchar |  |  | SI | External DispenseID |
| MOBAT_ExtQty | double |  |  | SI | Ext Qty |
| MOBAT_INCI_DR | varchar |  | FK | SI | Des Ref INCI |
| MOBAT_INCLB_DR | varchar |  | FK | SI | Des Ref to INCLB |
| MOBAT_Price | double |  |  | SI | Price |
| MOBAT_Qty | double |  |  | SI | Quantity |
| MOBAT_RowId | varchar |  |  | NO | - |
| Q25Q1 | - |  |  | SI | Biopsy |
| Q25Q2 | - |  |  | SI | Cone |
| Q25Q3 | - |  |  | SI | Hysterectomy |
| Q25Q4 | - |  |  | SI | Laser |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*