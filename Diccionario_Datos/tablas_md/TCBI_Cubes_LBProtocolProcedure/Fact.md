# TCBI_Cubes_LBProtocolProcedure.Fact

**Schema:** TCBI_Cubes_LBProtocolProcedure
**Columnas:** 47
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1001131559 | varchar |  |  | SI | Dimension: Dx1001131559<br/>
Source: LBPTPAddOnDa... |
| Dx1406802718 | varchar |  |  | SI | Dimension: Dx1406802718<br/>
Source: LBPTPComplet... |
| Dx1444897206 | bigint |  |  | SI | Dimension: Dx1444897206
Expression: $ztime(%sourc... |
| Dx1728867828 | varchar |  |  | SI | Dimension: Dx1728867828<br/>
Source: LBPTPComplet... |
| Dx2347077543 | varchar |  |  | SI | Dimension: Dx2347077543<br/>
Source: LBPTPComplet... |
| Dx237394081 | bigint |  |  | SI | Dimension: Dx237394081
Expression: %source.LBPTPC... |
| Dx2572609936 | varchar |  |  | SI | Dimension: Dx2572609936<br/>
Source: LBPTPComplet... |
| Dx3238414613 | varchar |  |  | SI | Dimension: Dx3238414613<br/>
Source: LBPTPAddOnDa... |
| Dx3611683956 | varchar |  |  | SI | Dimension: Dx3611683956<br/>
Source: LBPTPAddOnDa... |
| Dx3732957720 | varchar |  |  | SI | Dimension: Dx3732957720<br/>
Source: LBPTPComplet... |
| Dx3758122913 | bigint |  |  | SI | Dimension: Dx3758122913
Expression: %source.LBPTP... |
| Dx762634624 | varchar |  |  | SI | Dimension: Dx762634624<br/>
Source: LBPTPAddOnDat... |
| Dx925670260 | bigint |  |  | SI | Dimension: Dx925670260
Expression: $ztime(%source... |
| DxAddOnDayOfWeek | bigint |  |  | SI | Dimension: DxAddOnDayOfWeek
Expression: ##class(T... |
| DxAuthorisedBy | bigint |  |  | SI | Dimension: DxAuthorisedBy<br/>
Source: LBPTPCompl... |
| DxBillable | bigint |  |  | SI | Dimension: DxBillable<br/>
Source: LBPTPBillable |
| DxCompletedDayOfWeek | bigint |  |  | SI | Dimension: DxCompletedDayOfWeek
Expression: ##cla... |
| DxCompletedSecurityGroup | bigint |  |  | SI | Dimension: DxCompletedSecurityGroup<br/>
Source: ... |
| DxCompletedUserName | bigint |  |  | SI | Dimension: DxCompletedUserName<br/>
Source: LBPTP... |
| DxIndirectCost | bigint |  |  | SI | Dimension: DxIndirectCost<br/>
Source: LBPTPProce... |
| DxLBPTPAddOnDate | date |  |  | SI | Dimension: DxLBPTPAddOnDate<br/>
Source: LBPTPAdd... |
| DxLBPTPAddOnDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBPTPAddOnDateFxMonthYear<br/>
Sourc... |
| DxLBPTPAddOnDateFxYear | varchar |  |  | SI | Dimension: DxLBPTPAddOnDateFxYear<br/>
Source: LB... |
| DxLBPTPCompletedDate | date |  |  | SI | Dimension: DxLBPTPCompletedDate<br/>
Source: LBPT... |
| DxLBPTPCompletedDateFxYear | varchar |  |  | SI | Dimension: DxLBPTPCompletedDateFxYear<br/>
Source... |
| DxPlanned | bigint |  |  | SI | Dimension: DxPlanned
Expression: %expression.Proc... |
| DxProcedure | bigint |  |  | SI | Dimension: DxProcedure<br/>
Source: LBPTPProcedur... |
| DxProcedureStatus | bigint |  |  | SI | Dimension: DxProcedureStatus
Expression: %express... |
| DxProcedureType | bigint |  |  | SI | Dimension: DxProcedureType
Expression: %expressio... |
| DxProcedureWorkArea | varchar |  |  | SI | Dimension: DxProcedureWorkArea
Expression: %expre... |
| DxProcedureWorkAreaLabSite | varchar |  |  | SI | Dimension: DxProcedureWorkAreaLabSite
Expression:... |
| DxRequestedSecurityGroup | bigint |  |  | SI | Dimension: DxRequestedSecurityGroup<br/>
Source: ... |
| DxRequestedUserName | bigint |  |  | SI | Dimension: DxRequestedUserName<br/>
Source: LBPTP... |
| DxTurnaroundTime | bigint |  |  | SI | Dimension: DxTurnaroundTime<br/>
Source: LBPTPTur... |
| DxTurnaroundTimeFail | bigint |  |  | SI | Dimension: DxTurnaroundTimeFail
Expression: %expr... |
| DxTurnaroundTimeFlag | bigint |  |  | SI | Dimension: DxTurnaroundTimeFlag
Expression: %expr... |
| DxTurnaroundTimeSlot | bigint |  |  | SI | Dimension: DxTurnaroundTimeSlot
Expression: %expr... |
| DxWorkLoadFactor | bigint |  |  | SI | Dimension: DxWorkLoadFactor<br/>
Source: LBPTPPro... |
| MxNumberCancelled | double |  |  | SI | Measure: MxNumberCancelled
Expression: %source.LB... |
| MxNumberComplete | double |  |  | SI | Measure: MxNumberComplete
Expression: %source.LBP... |
| MxNumberInProgress | double |  |  | SI | Measure: MxNumberInProgress
Expression: %source.L... |
| MxNumberPlanned | double |  |  | SI | Measure: MxNumberPlanned
Expression: %source.LBPT... |
| MxNumberRequested | double |  |  | SI | Measure: MxNumberRequested
Expression: %source.LB... |
| RxLBPTPParRef | bigint |  |  | SI | Relationship: RxLBPTPParRef<br/>
Source: LBPTPPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*