# TCBI_Cubes_LBBloodProduct.Fact

**Schema:** TCBI_Cubes_LBBloodProduct
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx112784956 | varchar |  |  | SI | Dimension: Dx112784956<br/>
Source: LBBPEntryDate |
| Dx1173682056 | varchar |  |  | SI | Dimension: Dx1173682056<br/>
Source: LBBPDonation... |
| Dx1282864087 | bigint |  |  | SI | Dimension: Dx1282864087<br/>
Source: LBBPTransfer... |
| Dx1388024668 | varchar |  |  | SI | Dimension: Dx1388024668<br/>
Source: LBBPEntryDat... |
| Dx1678185953 | varchar |  |  | SI | Dimension: Dx1678185953<br/>
Source: LBBPFateDate |
| Dx1742243106 | varchar |  |  | SI | Dimension: Dx1742243106<br/>
Source: LBBPDispatch... |
| Dx1848533156 | bigint |  |  | SI | Dimension: Dx1848533156<br/>
Source: LBBPDisposal... |
| Dx2298824734 | bigint |  |  | SI | Dimension: Dx2298824734<br/>
Source: LBBPEntryMod... |
| Dx2455411812 | bigint |  |  | SI | Dimension: Dx2455411812<br/>
Source: LBBPBloodGro... |
| Dx2833869651 | varchar |  |  | SI | Dimension: Dx2833869651<br/>
Source: LBBPOrderedD... |
| Dx2913557925 | varchar |  |  | SI | Dimension: Dx2913557925<br/>
Source: LBBPExpiryDa... |
| Dx3114333243 | bigint |  |  | SI | Dimension: Dx3114333243<br/>
Source: LBBPHighTitr... |
| Dx3257314890 | varchar |  |  | SI | Dimension: Dx3257314890<br/>
Source: LBBPExpiryDa... |
| Dx3263996484 | bigint |  |  | SI | Dimension: Dx3263996484<br/>
Source: LBBPManufact... |
| Dx335460301 | bigint |  |  | SI | Dimension: Dx335460301<br/>
Source: LBBPBloodProd... |
| Dx3528242868 | varchar |  |  | SI | Dimension: Dx3528242868<br/>
Source: LBBPOrderedD... |
| Dx3675441684 | varchar |  |  | SI | Dimension: Dx3675441684<br/>
Source: LBBPDispatch... |
| Dx4094459567 | bigint |  |  | SI | Dimension: Dx4094459567<br/>
Source: LBBPUnitFate... |
| Dx4126896691 | varchar |  |  | SI | Dimension: Dx4126896691<br/>
Source: LBBPDispatch... |
| Dx4215124203 | bigint |  |  | SI | Dimension: Dx4215124203<br/>
Source: LBBPTranspor... |
| Dx521671788 | varchar |  |  | SI | Dimension: Dx521671788<br/>
Source: LBBPDonationD... |
| Dx539780375 | varchar |  |  | SI | Dimension: Dx539780375<br/>
Source: LBBPDonationD... |
| Dx670905949 | bigint |  |  | SI | Dimension: Dx670905949<br/>
Source: LBBPUnitStatu... |
| Dx842712479 | varchar |  |  | SI | Dimension: Dx842712479<br/>
Source: LBBPOrderedDa... |
| DxAPCVMNameViaLBBPSourceDR | bigint |  | FK | SI | Dimension: DxAPCVMNameViaLBBPSourceDR<br/>
Source... |
| DxAntigenReactions | varchar |  |  | SI | Dimension: DxAntigenReactions
Expression: %expres... |
| DxAntigens | varchar |  |  | SI | Dimension: DxAntigens
Expression: %expression.Get... |
| DxCTUOMDescViaLBBPUOMDR | bigint |  | FK | SI | Dimension: DxCTUOMDescViaLBBPUOMDR<br/>
Source: L... |
| DxDispatchDayOfWeek | bigint |  |  | SI | Dimension: DxDispatchDayOfWeek
Expression: ##clas... |
| DxDispatchTime | bigint |  |  | SI | Dimension: DxDispatchTime
Expression: $ztime(%sou... |
| DxDispatchTimeRange | bigint |  |  | SI | Dimension: DxDispatchTimeRange
Expression: %sourc... |
| DxDonationDayOfWeek | bigint |  |  | SI | Dimension: DxDonationDayOfWeek
Expression: ##clas... |
| DxDonationTime | bigint |  |  | SI | Dimension: DxDonationTime
Expression: $ztime(%sou... |
| DxDonationTimeRange | bigint |  |  | SI | Dimension: DxDonationTimeRange
Expression: %sourc... |
| DxEntryDayOfWeek | bigint |  |  | SI | Dimension: DxEntryDayOfWeek
Expression: ##class(T... |
| DxEntryTime | bigint |  |  | SI | Dimension: DxEntryTime
Expression: $ztime(%source... |
| DxEntryTimeRange | bigint |  |  | SI | Dimension: DxEntryTimeRange
Expression: %source.L... |
| DxExpiryDayOfWeek | bigint |  |  | SI | Dimension: DxExpiryDayOfWeek
Expression: ##class(... |
| DxExpiryTime | bigint |  |  | SI | Dimension: DxExpiryTime
Expression: $ztime(%sourc... |
| DxExpiryTimeRange | bigint |  |  | SI | Dimension: DxExpiryTimeRange
Expression: %source.... |
| DxFateDayOfWeek | bigint |  |  | SI | Dimension: DxFateDayOfWeek
Expression: ##class(TC... |
| DxFateTime | bigint |  |  | SI | Dimension: DxFateTime
Expression: $ztime(%source.... |
| DxFateTimeRange | bigint |  |  | SI | Dimension: DxFateTimeRange
Expression: %source.LB... |
| DxLBBPBatchNumber | bigint |  |  | SI | Dimension: DxLBBPBatchNumber<br/>
Source: LBBPBat... |
| DxLBBPCMVStatus | bigint |  |  | SI | Dimension: DxLBBPCMVStatus<br/>
Source: LBBPCMVSt... |
| DxLBBPDispatchDate | date |  |  | SI | Dimension: DxLBBPDispatchDate<br/>
Source: LBBPDi... |
| DxLBBPDispatchDateFxYear | varchar |  |  | SI | Dimension: DxLBBPDispatchDateFxYear<br/>
Source: ... |
| DxLBBPDonationDate | date |  |  | SI | Dimension: DxLBBPDonationDate<br/>
Source: LBBPDo... |
| DxLBBPDonationDateFxYear | varchar |  |  | SI | Dimension: DxLBBPDonationDateFxYear<br/>
Source: ... |
| DxLBBPEntryDate | date |  |  | SI | Dimension: DxLBBPEntryDate<br/>
Source: LBBPEntry... |
| DxLBBPEntryDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBBPEntryDateFxMonthYear<br/>
Source... |
| DxLBBPEntryDateFxYear | varchar |  |  | SI | Dimension: DxLBBPEntryDateFxYear<br/>
Source: LBB... |
| DxLBBPExpiryDate | date |  |  | SI | Dimension: DxLBBPExpiryDate<br/>
Source: LBBPExpi... |
| DxLBBPExpiryDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBBPExpiryDateFxMonthYear<br/>
Sourc... |
| DxLBBPExpiryDateFxYear | varchar |  |  | SI | Dimension: DxLBBPExpiryDateFxYear<br/>
Source: LB... |
| DxLBBPFateDate | date |  |  | SI | Dimension: DxLBBPFateDate<br/>
Source: LBBPFateDa... |
| DxLBBPFateDateFxMonthNumber | varchar |  |  | SI | Dimension: DxLBBPFateDateFxMonthNumber<br/>
Sourc... |
| DxLBBPFateDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBBPFateDateFxMonthYear<br/>
Source:... |
| DxLBBPFateDateFxYear | varchar |  |  | SI | Dimension: DxLBBPFateDateFxYear<br/>
Source: LBBP... |
| DxLBBPHLAFlag | bigint |  |  | SI | Dimension: DxLBBPHLAFlag<br/>
Source: LBBPHLAFlag |
| DxLBBPHbSStatus | bigint |  |  | SI | Dimension: DxLBBPHbSStatus<br/>
Source: LBBPHbSSt... |
| DxLBBPHepatitisE | bigint |  |  | SI | Dimension: DxLBBPHepatitisE<br/>
Source: LBBPHepa... |
| DxLBBPIrradiated | bigint |  |  | SI | Dimension: DxLBBPIrradiated<br/>
Source: LBBPIrra... |
| DxLBBPOrderedDate | date |  |  | SI | Dimension: DxLBBPOrderedDate<br/>
Source: LBBPOrd... |
| DxLBBPOrderedDateFxYear | varchar |  |  | SI | Dimension: DxLBBPOrderedDateFxYear<br/>
Source: L... |
| DxLBCSTDescViaLBBPStorageDR | bigint |  | FK | SI | Dimension: DxLBCSTDescViaLBBPStorageDR<br/>
Sourc... |
| DxOrderedDayOfWeek | bigint |  |  | SI | Dimension: DxOrderedDayOfWeek
Expression: ##class... |
| DxOrderedTime | bigint |  |  | SI | Dimension: DxOrderedTime
Expression: $ztime(%sour... |
| DxOrderedTimeRange | bigint |  |  | SI | Dimension: DxOrderedTimeRange
Expression: %source... |
| MxNumberAdministered | double |  |  | SI | Measure: MxNumberAdministered
Expression: %source... |
| MxNumberAvailable | double |  |  | SI | Measure: MxNumberAvailable
Expression: %source.LB... |
| MxNumberDirected | double |  |  | SI | Measure: MxNumberDirected
Expression: %source.LBB... |
| MxNumberDisposed | double |  |  | SI | Measure: MxNumberDisposed
Expression: %source.LBB... |
| MxNumberFated | double |  |  | SI | Measure: MxNumberFated
Expression: %source.LBBPUn... |
| MxNumberIssued | double |  |  | SI | Measure: MxNumberIssued
Expression: %source.LBBPU... |
| MxNumberNotAcknowledged | double |  |  | SI | Measure: MxNumberNotAcknowledged
Expression: %sou... |
| MxNumberQuarantine | double |  |  | SI | Measure: MxNumberQuarantine
Expression: %source.L... |
| MxNumberReserved | double |  |  | SI | Measure: MxNumberReserved
Expression: %source.LBB... |
| MxNumberTesting | double |  |  | SI | Measure: MxNumberTesting
Expression: %source.LBBP... |
| MxNumberTransferred | double |  |  | SI | Measure: MxNumberTransferred
Expression: %source.... |
| MxNumberTransfused | double |  |  | SI | Measure: MxNumberTransfused
Expression: %source.L... |
| MxNumberUsed | double |  |  | SI | Measure: MxNumberUsed
Expression: %source.LBBPUni... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*