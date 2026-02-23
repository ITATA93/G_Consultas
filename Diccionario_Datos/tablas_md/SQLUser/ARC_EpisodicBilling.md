# SQLUser.ARC_EpisodicBilling

**Schema:** SQLUser
**Columnas:** 55
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EPB_RowId | bigint | PK |  | NO | - |
| ChildQ70DR | - |  |  | SI | Child Reference: Extremidades Alteradas |
| EPB_BillField1 | varchar |  |  | SI | Bill Field1 |
| EPB_BillField10 | varchar |  |  | SI | Bill Field 10 |
| EPB_BillField11 | varchar |  |  | SI | Bill Field 11 |
| EPB_BillField12 | varchar |  |  | SI | Bill Field 12 |
| EPB_BillField13 | varchar |  |  | SI | Bill Field13 |
| EPB_BillField14 | varchar |  |  | SI | Bill Field14 |
| EPB_BillField15 | varchar |  |  | SI | Bill Field15 |
| EPB_BillField16 | varchar |  |  | SI | Bill Field16 |
| EPB_BillField17 | varchar |  |  | SI | Bill Field17 |
| EPB_BillField18 | varchar |  |  | SI | Bill Field18 |
| EPB_BillField19 | varchar |  |  | SI | Bill Field19 |
| EPB_BillField2 | varchar |  |  | SI | Bill Field2 |
| EPB_BillField20 | varchar |  |  | SI | BillField20 |
| EPB_BillField21 | varchar |  |  | SI | BillField21 |
| EPB_BillField22 | varchar |  |  | SI | BillField22 |
| EPB_BillField23 | varchar |  |  | SI | BillField23 |
| EPB_BillField3 | varchar |  |  | SI | Bill Field3 |
| EPB_BillField4 | varchar |  |  | SI | Bill Field4 |
| EPB_BillField5 | varchar |  |  | SI | Bill Field5 |
| EPB_BillField6 | varchar |  |  | SI | Bill Field6 |
| EPB_BillField7 | varchar |  |  | SI | Bill Field7 |
| EPB_BillField8 | varchar |  |  | SI | Bill Field8 |
| EPB_BillField9 | varchar |  |  | SI | BillField 9 |
| EPB_CreatedDate | date |  |  | SI | Created Date |
| EPB_CreatedTime | time |  |  | SI | Created Time |
| EPB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| EPB_DayOnly | varchar |  |  | SI | Day Only |
| EPB_DischDestin | varchar |  |  | SI | DischargeDestination |
| EPB_InlierDesc | varchar |  |  | SI | Inlier Desc |
| EPB_InlierPayorCode | varchar |  |  | SI | Inlier Payor Code |
| EPB_LowerLevelDesc | varchar |  |  | SI | Lower Level Desc |
| EPB_LowerLevelPayorCode | varchar |  |  | SI | Lower Level Payor Code |
| EPB_OverInlierBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EPB_OverInlierBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EPB_OverrideBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EPB_OverrideBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EPB_OverrideInlierBillGrp_DR | bigint |  | FK | SI | Des Ref ARCBillGrp |
| EPB_OverrideInlierBillSub_DR | varchar |  | FK | SI | Des Ref ARCBillSub |
| EPB_RevertPerDiemInlier | varchar |  |  | SI | Revert to Per Diem for Inlier |
| EPB_RevertPerDiemOutlier | varchar |  |  | SI | Revert to Per Diem for Outlier |
| EPB_TransferDailyDiscountRate | varchar |  |  | SI | Transfer Daily Discount Rate  |
| EPB_TransferTrimPoint | varchar |  |  | SI | Transfer Trim Point |
| EPB_UpdatedDate | date |  |  | SI | Updated Date |
| EPB_UpdatedTime | time |  |  | SI | Updated Time |
| EPB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| EPB_UpperLevelDesc | varchar |  |  | SI | Upper Level Desc |
| EPB_UpperLevelPayorCode | varchar |  |  | SI | Upper Level Payor Code |
| Q52Q1 | - |  |  | SI | Palpación |
| Q52Q2 | - |  |  | SI | Percusión |
| Q52Q4 | - |  |  | SI | Auscultación |
| Q52Q5 | - |  |  | SI | Localización |
| Q52Q6 | - |  |  | SI | Lateralidad |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*