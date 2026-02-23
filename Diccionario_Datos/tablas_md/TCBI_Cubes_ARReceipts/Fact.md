# TCBI_Cubes_ARReceipts.Fact

**Schema:** TCBI_Cubes_ARReceipts
**Columnas:** 43
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1814293404 | varchar |  |  | SI | Dimension: Dx1814293404<br/>
Source: ARRCPRefundD... |
| Dx2319575808 | varchar |  |  | SI | Dimension: Dx2319575808<br/>
Source: ARRCPRefundD... |
| Dx2457220542 | varchar |  |  | SI | Dimension: Dx2457220542<br/>
Source: ARRCPRefundD... |
| Dx3319436555 | varchar |  |  | SI | Dimension: Dx3319436555<br/>
Source: ARRCPAddDate |
| Dx346716038 | varchar |  |  | SI | Dimension: Dx346716038<br/>
Source: ARRCPRefundDa... |
| Dx3618042194 | varchar |  |  | SI | Dimension: Dx3618042194<br/>
Source: ARRCPAddDate |
| Dx4165178837 | varchar |  |  | SI | Dimension: Dx4165178837<br/>
Source: ARRCPRefundD... |
| DxARRCPAddDate | date |  |  | SI | Dimension: DxARRCPAddDate<br/>
Source: ARRCPAddDa... |
| DxARRCPAddDateFxMonthNumber | varchar |  |  | SI | Dimension: DxARRCPAddDateFxMonthNumber<br/>
Sourc... |
| DxARRCPAddDateFxMonthYear | varchar |  |  | SI | Dimension: DxARRCPAddDateFxMonthYear<br/>
Source:... |
| DxARRCPAddDateFxQuarterYear | varchar |  |  | SI | Dimension: DxARRCPAddDateFxQuarterYear<br/>
Sourc... |
| DxARRCPAddDateFxYear | varchar |  |  | SI | Dimension: DxARRCPAddDateFxYear<br/>
Source: ARRC... |
| DxARRCPDate | date |  |  | SI | Dimension: DxARRCPDate<br/>
Source: ARRCPDate |
| DxARRCPDateFxDayMonthYear | varchar |  |  | SI | Dimension: DxARRCPDateFxDayMonthYear<br/>
Source:... |
| DxARRCPDateFxMonthNumber | varchar |  |  | SI | Dimension: DxARRCPDateFxMonthNumber<br/>
Source: ... |
| DxARRCPDateFxMonthYear | varchar |  |  | SI | Dimension: DxARRCPDateFxMonthYear<br/>
Source: AR... |
| DxARRCPDateFxQuarterNumber | varchar |  |  | SI | Dimension: DxARRCPDateFxQuarterNumber<br/>
Source... |
| DxARRCPDateFxQuarterYear | varchar |  |  | SI | Dimension: DxARRCPDateFxQuarterYear<br/>
Source: ... |
| DxARRCPDateFxYear | varchar |  |  | SI | Dimension: DxARRCPDateFxYear<br/>
Source: ARRCPDa... |
| DxARRCPRefundDate | date |  |  | SI | Dimension: DxARRCPRefundDate<br/>
Source: ARRCPRe... |
| DxARRCPRefundDateFxYear | varchar |  |  | SI | Dimension: DxARRCPRefundDateFxYear<br/>
Source: A... |
| DxAccountingPeriod | bigint |  |  | SI | Dimension: DxAccountingPeriod<br/>
Source: ARRCPA... |
| DxAccountingPeriodStatus | bigint |  |  | SI | Dimension: DxAccountingPeriodStatus<br/>
Source: ... |
| DxAddLocation | bigint |  |  | SI | Dimension: DxAddLocation
Expression: "sourceAddLo... |
| DxCashierLocation | bigint |  |  | SI | Dimension: DxCashierLocation<br/>
Source: ARRCPLo... |
| DxDiscountType | bigint |  |  | SI | Dimension: DxDiscountType<br/>
Source: ARRCPDisco... |
| DxItemDescription | bigint |  |  | SI | Dimension: DxItemDescription<br/>
Source: ARRCARC... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ARRCPPAPMIDR.... |
| DxPaymentMode | bigint |  |  | SI | Dimension: DxPaymentMode<br/>
Source: ARRCPPayMod... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: ARRCPInsTypeDR.IN... |
| DxPayorGroup | bigint |  |  | SI | Dimension: DxPayorGroup<br/>
Source: ARRCPInsType... |
| DxReasonForCancel | bigint |  |  | SI | Dimension: DxReasonForCancel<br/>
Source: ARRCPCa... |
| DxReasonForRefund | bigint |  |  | SI | Dimension: DxReasonForRefund<br/>
Source: ARRCPRe... |
| DxReceiptStatus | bigint |  |  | SI | Dimension: DxReceiptStatus<br/>
Source: ARRCPStat... |
| DxRefundLocationAdded | bigint |  |  | SI | Dimension: DxRefundLocationAdded<br/>
Source: ARR... |
| DxUserAdded | bigint |  |  | SI | Dimension: DxUserAdded<br/>
Source: ARRCPAddUserI... |
| DxUserCancelled | bigint |  |  | SI | Dimension: DxUserCancelled<br/>
Source: ARRCPCanc... |
| DxUserRefunded | bigint |  |  | SI | Dimension: DxUserRefunded<br/>
Source: ARRCPRefun... |
| MxPaidAmount | double |  |  | SI | Measure: MxPaidAmount<br/>
Source: ARRCPPayAmount |
| RxIDViaARRCPPAPMIDR | bigint |  | FK | SI | Relationship: RxIDViaARRCPPAPMIDR<br/>
Source: AR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*