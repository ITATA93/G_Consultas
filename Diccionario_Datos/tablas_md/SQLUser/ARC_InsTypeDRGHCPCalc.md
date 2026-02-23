# SQLUser.ARC_InsTypeDRGHCPCalc

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Seguros**. Planes y convenios. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRGHCP_ParRef | bigint | PK |  | NO | ARC_InsuranceType Parent Reference |
| ChildQ39DR | - |  |  | SI | Child Reference: Abdomen y dorso |
| DRGHCP_AddOnOrdItem_DR | varchar |  | FK | SI | Des Ref ARCItmMast |
| DRGHCP_AddOnPaymentPerc | double |  |  | SI | Add On Payment %  |
| DRGHCP_AddOnPharmPaymentPerc | double |  |  | SI | Add On Pharmacy Payment %  |
| DRGHCP_Childsub | double |  |  | NO | Childsub |
| DRGHCP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DRGHCP_Contract_DR | bigint |  | FK | SI | Des Ref BLCContractDetails |
| DRGHCP_CreatedDate | date |  |  | SI | Created Date |
| DRGHCP_CreatedTime | time |  |  | SI | Created Time |
| DRGHCP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DRGHCP_DateFrom | date |  |  | SI | Date From |
| DRGHCP_DateTo | date |  |  | SI | Date To |
| DRGHCP_HighCostLimitAmount | double |  |  | SI | High Cost Limit Amount |
| DRGHCP_LimPerOIAddOnOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Limit Per Order Item Add-On It... |
| DRGHCP_LimPerOIContract_DR | bigint |  | FK | SI | Limit Per Order Item contract, Des Ref BLCContract... |
| DRGHCP_LimPerOILimAmount | double |  |  | SI | Limit Per Order Item Limit Amount |
| DRGHCP_LimPerOIPaymentPerc | double |  |  | SI | Limit Per Order Item Payment %  |
| DRGHCP_LimSumOIAddOnOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Limit Per Sum of Order Items A... |
| DRGHCP_LimSumOIContract_DR | bigint |  | FK | SI | Limit Per Sum of Order Items contract, Des Ref BLC... |
| DRGHCP_LimSumOILimAmount | double |  |  | SI | Limit Per Sum of Order Items Limit Amount |
| DRGHCP_LimSumOIPaymentPerc | double |  |  | SI | Limit Per Sum of Order Items Payment %  |
| DRGHCP_PharmAddOnOrdItem_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Pharmacy Add-On Item |
| DRGHCP_PharmContract_DR | bigint |  | FK | SI | Pharmacy contract, Des Ref BLCContractDetails |
| DRGHCP_PharmHighCostLimAmount | double |  |  | SI | Pharmacy High Cost Limit Amount |
| DRGHCP_PostOffice_DR | bigint |  | FK | SI | Des Ref ARCPostOffice |
| DRGHCP_RowId | varchar |  |  | NO | - |
| DRGHCP_SurgHighCostContract_DR | bigint |  | FK | SI | Surgical High Cost contract, Des Ref BLCContractDe... |
| DRGHCP_SurgHighCostLimAmount | double |  |  | SI | Surgical High Cost Limit Amount |
| DRGHCP_SurgHighCostOrdItm_DR | varchar |  | FK | SI | Des Ref ARCItmMast, Surgical High Cost Add-On Item |
| DRGHCP_SurgHighCostPaymentPerc | double |  |  | SI | Surgical High Cost Payment %  |
| DRGHCP_UpdatedDate | date |  |  | SI | Updated Date |
| DRGHCP_UpdatedTime | time |  |  | SI | Updated Time |
| DRGHCP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q35Q1 | - |  |  | SI | Percusión |
| Q35Q2 | - |  |  | SI | Auscultación |
| Q35Q3 | - |  |  | SI | Localización |
| Q35Q4 | - |  |  | SI | Comentario |
| QUESParRefDR | - |  |  | SI | Parent Reference |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*