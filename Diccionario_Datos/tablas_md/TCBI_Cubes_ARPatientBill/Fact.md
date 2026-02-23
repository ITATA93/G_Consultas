# TCBI_Cubes_ARPatientBill.Fact

**Schema:** TCBI_Cubes_ARPatientBill
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1027410310 | varchar |  |  | SI | Dimension: Dx1027410310<br/>
Source: ARPBLBillDat... |
| Dx1150163006 | varchar |  |  | SI | Dimension: Dx1150163006<br/>
Source: ARPBLBillDat... |
| Dx1157904680 | varchar |  |  | SI | Dimension: Dx1157904680<br/>
Source: ARPBLBillDat... |
| Dx1342763201 | varchar |  |  | SI | Dimension: Dx1342763201<br/>
Source: ARPBLClaimRA... |
| Dx1373223449 | varchar |  |  | SI | Dimension: Dx1373223449<br/>
Source: ARPBLDateCan... |
| Dx1435304751 | varchar |  |  | SI | Dimension: Dx1435304751<br/>
Source: ARPBLBillDat... |
| Dx1439189969 | varchar |  |  | SI | Dimension: Dx1439189969<br/>
Source: ARPBLClaimRA... |
| Dx1576009719 | varchar |  |  | SI | Dimension: Dx1576009719<br/>
Source: ARPBLBillDat... |
| Dx1819089351 | varchar |  |  | SI | Dimension: Dx1819089351<br/>
Source: ARPBLBillDat... |
| Dx1900529449 | varchar |  |  | SI | Dimension: Dx1900529449<br/>
Source: ARPBLDatePri... |
| Dx2105322749 | varchar |  |  | SI | Dimension: Dx2105322749<br/>
Source: ARPBLClaimRA... |
| Dx2115163773 | varchar |  |  | SI | Dimension: Dx2115163773<br/>
Source: ARPBLDateSta... |
| Dx2133820983 | varchar |  |  | SI | Dimension: Dx2133820983<br/>
Source: ARPBLDateCan... |
| Dx2335420922 | varchar |  |  | SI | Dimension: Dx2335420922<br/>
Source: ARPBLDatePri... |
| Dx2396888539 | varchar |  |  | SI | Dimension: Dx2396888539<br/>
Source: ARPBLDatePri... |
| Dx2442481326 | varchar |  |  | SI | Dimension: Dx2442481326<br/>
Source: ARPBLClaimRA... |
| Dx2640536559 | varchar |  |  | SI | Dimension: Dx2640536559<br/>
Source: ARPBLDateSta... |
| Dx2645435770 | varchar |  |  | SI | Dimension: Dx2645435770<br/>
Source: ARPBLDatePri... |
| Dx2807203371 | varchar |  |  | SI | Dimension: Dx2807203371<br/>
Source: ARPBLDateCan... |
| Dx2984847659 | varchar |  |  | SI | Dimension: Dx2984847659<br/>
Source: ARPBLClaimRA... |
| Dx3110396284 | varchar |  |  | SI | Dimension: Dx3110396284<br/>
Source: ARPBLBillDat... |
| Dx3174062154 | varchar |  |  | SI | Dimension: Dx3174062154<br/>
Source: ARPBLDateCan... |
| Dx332003926 | varchar |  |  | SI | Dimension: Dx332003926<br/>
Source: ARPBLDateStat... |
| Dx346195175 | varchar |  |  | SI | Dimension: Dx346195175<br/>
Source: ARPBLDateStat... |
| Dx3564791415 | varchar |  |  | SI | Dimension: Dx3564791415<br/>
Source: ARPBLDatePri... |
| Dx3684530206 | varchar |  |  | SI | Dimension: Dx3684530206<br/>
Source: ARPBLBillDat... |
| Dx402709768 | varchar |  |  | SI | Dimension: Dx402709768<br/>
Source: ARPBLDateStat... |
| Dx4068722854 | varchar |  |  | SI | Dimension: Dx4068722854<br/>
Source: ARPBLDateCan... |
| Dx407709727 | varchar |  |  | SI | Dimension: Dx407709727<br/>
Source: ARPBLBillDate... |
| Dx4090662885 | varchar |  |  | SI | Dimension: Dx4090662885<br/>
Source: ARPBLClaimRA... |
| Dx4280293381 | varchar |  |  | SI | Dimension: Dx4280293381<br/>
Source: ARPBLDateSta... |
| Dx930388557 | varchar |  |  | SI | Dimension: Dx930388557<br/>
Source: ARPBLBillDate... |
| DxARPBLBillDateFrom | date |  |  | SI | Dimension: DxARPBLBillDateFrom<br/>
Source: ARPBL... |
| DxARPBLBillDateFromFxYear | varchar |  |  | SI | Dimension: DxARPBLBillDateFromFxYear<br/>
Source:... |
| DxARPBLBillDateTo | date |  |  | SI | Dimension: DxARPBLBillDateTo<br/>
Source: ARPBLBi... |
| DxARPBLBillDateToFxYear | varchar |  |  | SI | Dimension: DxARPBLBillDateToFxYear<br/>
Source: A... |
| DxARPBLClaimRADateSettle | date |  |  | SI | Dimension: DxARPBLClaimRADateSettle<br/>
Source: ... |
| DxARPBLDateCancelled | date |  |  | SI | Dimension: DxARPBLDateCancelled<br/>
Source: ARPB... |
| DxARPBLDateCancelledFxYear | varchar |  |  | SI | Dimension: DxARPBLDateCancelledFxYear<br/>
Source... |
| DxARPBLDatePrinted | date |  |  | SI | Dimension: DxARPBLDatePrinted<br/>
Source: ARPBLD... |
| DxARPBLDatePrintedFxYear | varchar |  |  | SI | Dimension: DxARPBLDatePrintedFxYear<br/>
Source: ... |
| DxARPBLDateStatusChanged | date |  |  | SI | Dimension: DxARPBLDateStatusChanged<br/>
Source: ... |
| DxBatchNumber | bigint |  |  | SI | Dimension: DxBatchNumber<br/>
Source: ARPBLBatchD... |
| DxBillCancelled | bigint |  |  | SI | Dimension: DxBillCancelled
Expression: %cube.IsBi... |
| DxBillPrinted | bigint |  |  | SI | Dimension: DxBillPrinted
Expression: %cube.IsBill... |
| DxBillProgressStatus | bigint |  |  | SI | Dimension: DxBillProgressStatus<br/>
Source: ARPB... |
| DxBillRefund | bigint |  |  | SI | Dimension: DxBillRefund<br/>
Source: ARPBLBillRef... |
| DxBillType | bigint |  |  | SI | Dimension: DxBillType<br/>
Source: ARPBLBillType |
| DxBillingHospital | bigint |  |  | SI | Dimension: DxBillingHospital<br/>
Source: ARPBLHo... |
| DxClaimDenialReason | bigint |  |  | SI | Dimension: DxClaimDenialReason<br/>
Source: ARPBL... |
| DxClaimSettleDays | bigint |  |  | SI | Dimension: DxClaimSettleDays
Expression: ##class(... |
| DxClaimStatus | bigint |  |  | SI | Dimension: DxClaimStatus<br/>
Source: ARPBLBillCl... |
| DxDiscountType | bigint |  |  | SI | Dimension: DxDiscountType<br/>
Source: ARPBLDiscT... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: ARPBLPAADMDR.... |
| DxHasOutstandingAmount | bigint |  |  | SI | Dimension: DxHasOutstandingAmount
Expression: %cu... |
| DxHospitalCancelled | bigint |  |  | SI | Dimension: DxHospitalCancelled<br/>
Source: ARPBL... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ARPBLPAADMDR.... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: ARPBLInsuranceTyp... |
| DxPayorGroup | bigint |  |  | SI | Dimension: DxPayorGroup<br/>
Source: ARPBLInsuran... |
| DxPayorType | bigint |  |  | SI | Dimension: DxPayorType<br/>
Source: ARPBLPayorTyp... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: ARPBLAuxInsTypeDR.... |
| DxReasonForCancel | bigint |  |  | SI | Dimension: DxReasonForCancel<br/>
Source: ARPBLRe... |
| DxReasonForRefund | bigint |  |  | SI | Dimension: DxReasonForRefund<br/>
Source: ARPBLRe... |
| DxReasonForWriteOff | bigint |  |  | SI | Dimension: DxReasonForWriteOff<br/>
Source: ARPBL... |
| DxSundryDebtor | bigint |  |  | SI | Dimension: DxSundryDebtor<br/>
Source: ARPBLSundr... |
| DxTransactionType | bigint |  |  | SI | Dimension: DxTransactionType
Expression: %cube.Ge... |
| DxUserCancelled | bigint |  |  | SI | Dimension: DxUserCancelled<br/>
Source: ARPBLUser... |
| MxBillAmount | double |  |  | SI | Measure: MxBillAmount
Expression: %cube.BillAmoun... |
| MxClaimSettleDays | double |  |  | SI | Measure: MxClaimSettleDays
Expression: ##class(TC... |
| MxDRGCost | double |  |  | SI | Measure: MxDRGCost<br/>
Source: ARPBLTotalDRGCost |
| MxDiscretionaryAmount | double |  |  | SI | Measure: MxDiscretionaryAmount<br/>
Source: ARPBL... |
| MxPaidAmount | double |  |  | SI | Measure: MxPaidAmount
Expression: %cube.PaidAmoun... |
| MxPayorApprovPayment | double |  |  | SI | Measure: MxPayorApprovPayment<br/>
Source: ARPBLT... |
| MxTotalPatientAmount | double |  |  | SI | Measure: MxTotalPatientAmount<br/>
Source: ARPBLT... |
| MxTotalPayorAmount | double |  |  | SI | Measure: MxTotalPayorAmount<br/>
Source: ARPBLTot... |
| MxTotalTax | double |  |  | SI | Measure: MxTotalTax
Expression: %cube.TaxAmount(%... |
| MxWriteOffAmount | double |  |  | SI | Measure: MxWriteOffAmount<br/>
Source: ARPBLWrite... |
| RxIDViaARPBLPAADMDR | bigint |  | FK | SI | Relationship: RxIDViaARPBLPAADMDR<br/>
Source: AR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*