# SQLUser.IN_POItm

**Schema:** SQLUser
**Columnas:** 32
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IN_PO | bigint | PK |  | NO | IN_PO Parent Reference |
| INPOI_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| INPOI_CTUOM_DR | bigint |  | FK | NO | Des Ref to CTUOM |
| INPOI_Childsub | double |  |  | NO | INPOI Childsub(New Key) |
| INPOI_CommItems_DR | bigint |  | FK | SI | Des Ref CommItems |
| INPOI_ConfirmedQtyUponXF | double |  |  | SI | ConfirmedQtyUponXF |
| INPOI_Date | date |  |  | NO | Date Needed |
| INPOI_DateApproved | date |  |  | SI | Date Approved |
| INPOI_Deliv_Qty | double |  |  | SI | Delivered Qty |
| INPOI_Disc | double |  |  | SI | Discount Rate |
| INPOI_GrossAmt | double |  |  | SI | Gross Amount |
| INPOI_INCGR_DR | bigint |  | FK | SI | Des Ref Goods receive type |
| INPOI_INCI_DR | bigint |  | FK | NO | Des Ref to INCI |
| INPOI_OutsQty | double |  |  | SI | Outstanding Quantity |
| INPOI_PreVATAmount | double |  |  | SI | Pre VAT Amount |
| INPOI_Pur_Qty | double |  |  | SI | Purchase Qty |
| INPOI_Remarks | varchar |  |  | SI | Remarks |
| INPOI_Req_Qty | double |  |  | NO | Requested Quantity |
| INPOI_StockCostApprovedQty | double |  |  | SI | Stock Cost for Approved Quantity |
| INPOI_TaxAmount | double |  |  | SI | Tax Amount |
| INPOI_TaxAmountApprovedQty | double |  |  | SI | Tax Amount for Approved Quantity |
| INPOI_TimeApproved | time |  |  | SI | TimeApproved |
| INPOI_TotalPriceApprovedQty | double |  |  | SI | Total Price for Approved Quantity |
| INPOI_UnitCost | double |  |  | NO | Unit Cost |
| INPOI_UserApproved_DR | bigint |  | FK | SI | Des Ref User |
| INPOI_VendorContract_DR | bigint |  | FK | SI | Des Ref to INCVendorContract |
| IN_POItm | varchar |  |  | NO | - |
| Q07Q1 | - |  |  | SI | Imágenes atípicas |
| Q07Q2 | - |  |  | SI | Cambios |
| Q07Q3 | - |  |  | SI | Topografía de la imagen cervical |
| Q07Q4 | - |  |  | SI | Comentarios |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*