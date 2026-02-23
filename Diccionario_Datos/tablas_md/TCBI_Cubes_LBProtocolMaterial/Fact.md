# TCBI_Cubes_LBProtocolMaterial.Fact

**Schema:** TCBI_Cubes_LBProtocolMaterial
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx123637676 | varchar |  |  | SI | Dimension: Dx123637676<br/>
Source: LBPTMAddOnDat... |
| Dx1302422105 | varchar |  |  | SI | Dimension: Dx1302422105<br/>
Source: LBPTMAddOnDa... |
| Dx1336404044 | varchar |  |  | SI | Dimension: Dx1336404044<br/>
Source: LBPTMComplet... |
| Dx1438370303 | bigint |  |  | SI | Dimension: Dx1438370303
Expression: %source.LBPTM... |
| Dx2199400147 | bigint |  |  | SI | Dimension: Dx2199400147
Expression: $ztime(%sourc... |
| Dx2219045358 | varchar |  |  | SI | Dimension: Dx2219045358<br/>
Source: LBPTMAddOnDa... |
| Dx2705883146 | varchar |  |  | SI | Dimension: Dx2705883146<br/>
Source: LBPTMAddOnDa... |
| Dx3011282876 | varchar |  |  | SI | Dimension: Dx3011282876<br/>
Source: LBPTMComplet... |
| Dx3138765001 | bigint |  |  | SI | Dimension: Dx3138765001
Expression: %source.LBPTM... |
| Dx3474086473 | varchar |  |  | SI | Dimension: Dx3474086473<br/>
Source: LBPTMComplet... |
| Dx4097269807 | varchar |  |  | SI | Dimension: Dx4097269807<br/>
Source: LBPTMComplet... |
| Dx417235580 | varchar |  |  | SI | Dimension: Dx417235580<br/>
Source: LBPTMComplete... |
| Dx964890330 | bigint |  |  | SI | Dimension: Dx964890330
Expression: $ztime(%source... |
| DxAddOnDayOfWeek | bigint |  |  | SI | Dimension: DxAddOnDayOfWeek
Expression: ##class(T... |
| DxBillable | bigint |  |  | SI | Dimension: DxBillable<br/>
Source: LBPTMBillable |
| DxCompletedDayOfWeek | bigint |  |  | SI | Dimension: DxCompletedDayOfWeek
Expression: ##cla... |
| DxCompletedSecurityGroup | bigint |  |  | SI | Dimension: DxCompletedSecurityGroup<br/>
Source: ... |
| DxCompletedUserName | bigint |  |  | SI | Dimension: DxCompletedUserName<br/>
Source: LBPTM... |
| DxConverted | bigint |  |  | SI | Dimension: DxConverted
Expression: %expression.Ma... |
| DxConvertedContainerDesc | bigint |  |  | SI | Dimension: DxConvertedContainerDesc
Expression: %... |
| DxConvertedSpecimenDesc | bigint |  |  | SI | Dimension: DxConvertedSpecimenDesc
Expression: %e... |
| DxLBPTMAddOnDate | date |  |  | SI | Dimension: DxLBPTMAddOnDate<br/>
Source: LBPTMAdd... |
| DxLBPTMAddOnDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBPTMAddOnDateFxMonthYear<br/>
Sourc... |
| DxLBPTMAddOnDateFxYear | varchar |  |  | SI | Dimension: DxLBPTMAddOnDateFxYear<br/>
Source: LB... |
| DxLBPTMCompletedDate | date |  |  | SI | Dimension: DxLBPTMCompletedDate<br/>
Source: LBPT... |
| DxLBPTMCompletedDateFxYear | varchar |  |  | SI | Dimension: DxLBPTMCompletedDateFxYear<br/>
Source... |
| DxMaterial | bigint |  |  | SI | Dimension: DxMaterial<br/>
Source: LBPTMMaterialD... |
| DxMaterialStatus | bigint |  |  | SI | Dimension: DxMaterialStatus
Expression: %expressi... |
| DxMaterialType | bigint |  |  | SI | Dimension: DxMaterialType
Expression: %expression... |
| DxPlanned | bigint |  |  | SI | Dimension: DxPlanned
Expression: %expression.Mate... |
| DxRequestedSecurityGroup | bigint |  |  | SI | Dimension: DxRequestedSecurityGroup<br/>
Source: ... |
| DxRequestedUserName | bigint |  |  | SI | Dimension: DxRequestedUserName<br/>
Source: LBPTM... |
| MxNumberCancelled | double |  |  | SI | Measure: MxNumberCancelled
Expression: %source.LB... |
| MxNumberComplete | double |  |  | SI | Measure: MxNumberComplete
Expression: %source.LBP... |
| MxNumberConverted | double |  |  | SI | Measure: MxNumberConverted
Expression: %expressio... |
| MxNumberInProgress | double |  |  | SI | Measure: MxNumberInProgress
Expression: %source.L... |
| MxNumberPlanned | double |  |  | SI | Measure: MxNumberPlanned
Expression: %source.LBPT... |
| MxNumberRequested | double |  |  | SI | Measure: MxNumberRequested
Expression: %source.LB... |
| RxLBPTMParRef | bigint |  |  | SI | Relationship: RxLBPTMParRef<br/>
Source: LBPTMPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*