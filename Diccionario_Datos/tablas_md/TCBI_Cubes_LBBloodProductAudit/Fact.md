# TCBI_Cubes_LBBloodProductAudit.Fact

**Schema:** TCBI_Cubes_LBBloodProductAudit
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1087675393 | bigint |  |  | SI | Dimension: Dx1087675393<br/>
Source: LBBPAUBloodG... |
| Dx1100822687 | varchar |  |  | SI | Dimension: Dx1100822687<br/>
Source: LBBPAUExpiry... |
| Dx124367862 | varchar |  |  | SI | Dimension: Dx124367862<br/>
Source: LBBPAUDonatio... |
| Dx1319604791 | varchar |  |  | SI | Dimension: Dx1319604791<br/>
Source: LBBPAUExpiry... |
| Dx1350364601 | bigint |  |  | SI | Dimension: Dx1350364601<br/>
Source: LBBPAUTransf... |
| Dx1404117547 | bigint |  |  | SI | Dimension: Dx1404117547<br/>
Source: LBBPAUSource... |
| Dx1705892190 | varchar |  |  | SI | Dimension: Dx1705892190<br/>
Source: LBBPAUOrdere... |
| Dx1723070588 | bigint |  |  | SI | Dimension: Dx1723070588<br/>
Source: LBBPAUBloodP... |
| Dx2131115013 | bigint |  |  | SI | Dimension: Dx2131115013<br/>
Source: LBBPAUDispos... |
| Dx233642260 | bigint |  |  | SI | Dimension: Dx233642260<br/>
Source: LBBPAUStorage... |
| Dx2347556888 | varchar |  |  | SI | Dimension: Dx2347556888<br/>
Source: LBBPAUDispat... |
| Dx2841837510 | bigint |  |  | SI | Dimension: Dx2841837510<br/>
Source: LBBPAUHighTi... |
| Dx2847969970 | varchar |  |  | SI | Dimension: Dx2847969970<br/>
Source: LBBPAUDonati... |
| Dx2962803913 | varchar |  |  | SI | Dimension: Dx2962803913<br/>
Source: LBBPAUOrdere... |
| Dx2979288597 | bigint |  |  | SI | Dimension: Dx2979288597<br/>
Source: LBBPAUUnitSt... |
| Dx3419455977 | varchar |  |  | SI | Dimension: Dx3419455977<br/>
Source: LBBPAUDispat... |
| Dx346839907 | varchar |  |  | SI | Dimension: Dx346839907<br/>
Source: LBBPAUOrdered... |
| Dx3476211070 | bigint |  |  | SI | Dimension: Dx3476211070<br/>
Source: LBBPAUEntryM... |
| Dx3488380276 | varchar |  |  | SI | Dimension: Dx3488380276<br/>
Source: LBBPAUFateDa... |
| Dx3935081222 | varchar |  |  | SI | Dimension: Dx3935081222<br/>
Source: LBBPAUEntryD... |
| Dx3985298857 | varchar |  |  | SI | Dimension: Dx3985298857<br/>
Source: LBBPAUDispat... |
| Dx4057161773 | bigint |  |  | SI | Dimension: Dx4057161773<br/>
Source: LBBPAUTransp... |
| Dx4185053428 | bigint |  |  | SI | Dimension: Dx4185053428<br/>
Source: LBBPAUUnitFa... |
| Dx68800394 | varchar |  |  | SI | Dimension: Dx68800394<br/>
Source: LBBPAUEntryDat... |
| Dx80102301 | varchar |  |  | SI | Dimension: Dx80102301<br/>
Source: LBBPAUExpiryDa... |
| Dx820932330 | varchar |  |  | SI | Dimension: Dx820932330<br/>
Source: LBBPAUDonatio... |
| Dx865077536 | varchar |  |  | SI | Dimension: Dx865077536<br/>
Source: LBBPAUFateDat... |
| Dx86806429 | varchar |  |  | SI | Dimension: Dx86806429<br/>
Source: LBBPAUEntryDat... |
| Dx980035617 | bigint |  |  | SI | Dimension: Dx980035617<br/>
Source: LBBPAUManufac... |
| DxAntigenReactions | varchar |  |  | SI | Dimension: DxAntigenReactions
Expression: %expres... |
| DxAntigens | varchar |  |  | SI | Dimension: DxAntigens
Expression: %expression.Get... |
| DxCTUOMDescViaLBBPAUUOMDR | bigint |  | FK | SI | Dimension: DxCTUOMDescViaLBBPAUUOMDR<br/>
Source:... |
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
| DxLBBPAUAction | bigint |  |  | SI | Dimension: DxLBBPAUAction<br/>
Source: LBBPAUActi... |
| DxLBBPAUBatchIndex | bigint |  |  | SI | Dimension: DxLBBPAUBatchIndex<br/>
Source: LBBPAU... |
| DxLBBPAUCMVStatus | bigint |  |  | SI | Dimension: DxLBBPAUCMVStatus<br/>
Source: LBBPAUC... |
| DxLBBPAUCompatibility | bigint |  |  | SI | Dimension: DxLBBPAUCompatibility<br/>
Source: LBB... |
| DxLBBPAUDispatchDate | date |  |  | SI | Dimension: DxLBBPAUDispatchDate<br/>
Source: LBBP... |
| DxLBBPAUDispatchDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUDispatchDateFxYear<br/>
Source... |
| DxLBBPAUDonationDate | date |  |  | SI | Dimension: DxLBBPAUDonationDate<br/>
Source: LBBP... |
| DxLBBPAUDonationDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUDonationDateFxYear<br/>
Source... |
| DxLBBPAUEntryDate | date |  |  | SI | Dimension: DxLBBPAUEntryDate<br/>
Source: LBBPAUE... |
| DxLBBPAUEntryDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUEntryDateFxYear<br/>
Source: L... |
| DxLBBPAUExpiryDate | date |  |  | SI | Dimension: DxLBBPAUExpiryDate<br/>
Source: LBBPAU... |
| DxLBBPAUExpiryDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUExpiryDateFxYear<br/>
Source: ... |
| DxLBBPAUFateDate | date |  |  | SI | Dimension: DxLBBPAUFateDate<br/>
Source: LBBPAUFa... |
| DxLBBPAUFateDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBBPAUFateDateFxMonthYear<br/>
Sourc... |
| DxLBBPAUFateDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUFateDateFxYear<br/>
Source: LB... |
| DxLBBPAUHLAFlag | bigint |  |  | SI | Dimension: DxLBBPAUHLAFlag<br/>
Source: LBBPAUHLA... |
| DxLBBPAUHbSStatus | bigint |  |  | SI | Dimension: DxLBBPAUHbSStatus<br/>
Source: LBBPAUH... |
| DxLBBPAUHepatitisE | bigint |  |  | SI | Dimension: DxLBBPAUHepatitisE<br/>
Source: LBBPAU... |
| DxLBBPAUIrradiated | bigint |  |  | SI | Dimension: DxLBBPAUIrradiated<br/>
Source: LBBPAU... |
| DxLBBPAUOrderedDate | date |  |  | SI | Dimension: DxLBBPAUOrderedDate<br/>
Source: LBBPA... |
| DxLBBPAUOrderedDateFxYear | varchar |  |  | SI | Dimension: DxLBBPAUOrderedDateFxYear<br/>
Source:... |
| DxLBBPAUSuitability | bigint |  |  | SI | Dimension: DxLBBPAUSuitability<br/>
Source: LBBPA... |
| DxLBBPAUType | bigint |  |  | SI | Dimension: DxLBBPAUType<br/>
Source: LBBPAUType |
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
Expression: %source.LBBPAU... |
| MxNumberIssued | double |  |  | SI | Measure: MxNumberIssued
Expression: %source.LBBPA... |
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
Expression: %source.LBBPAUU... |
| RxIDViaLBBPAUTestSetDR | bigint |  | FK | SI | Relationship: RxIDViaLBBPAUTestSetDR<br/>
Source:... |
| RxLBBPAUParRef | bigint |  |  | SI | Relationship: RxLBBPAUParRef<br/>
Source: LBBPAUP... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*