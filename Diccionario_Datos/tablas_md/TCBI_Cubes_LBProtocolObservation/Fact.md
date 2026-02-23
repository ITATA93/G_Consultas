# TCBI_Cubes_LBProtocolObservation.Fact

**Schema:** TCBI_Cubes_LBProtocolObservation
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1289638883 | varchar |  |  | SI | Dimension: Dx1289638883<br/>
Source: LBPTOAddOnDa... |
| Dx1421204016 | bigint |  |  | SI | Dimension: Dx1421204016
Expression: %source.LBPTO... |
| Dx1568161249 | varchar |  |  | SI | Dimension: Dx1568161249<br/>
Source: LBPTOAddOnDa... |
| Dx1880459769 | bigint |  |  | SI | Dimension: Dx1880459769
Expression: %source.LBPTO... |
| Dx2177187964 | bigint |  |  | SI | Dimension: Dx2177187964
Expression: $ztime(%sourc... |
| Dx2309511684 | varchar |  |  | SI | Dimension: Dx2309511684<br/>
Source: LBPTOComplet... |
| Dx2537073137 | varchar |  |  | SI | Dimension: Dx2537073137<br/>
Source: LBPTOAddOnDa... |
| Dx2688004528 | varchar |  |  | SI | Dimension: Dx2688004528<br/>
Source: LBPTOAddOnDa... |
| Dx3158441237 | bigint |  |  | SI | Dimension: Dx3158441237<br/>
Source: LBPTOObserva... |
| Dx3318134014 | varchar |  |  | SI | Dimension: Dx3318134014<br/>
Source: LBPTOComplet... |
| Dx3430522995 | varchar |  |  | SI | Dimension: Dx3430522995<br/>
Source: LBPTOComplet... |
| Dx588947937 | varchar |  |  | SI | Dimension: Dx588947937<br/>
Source: LBPTOComplete... |
| Dx690968237 | varchar |  |  | SI | Dimension: Dx690968237<br/>
Source: LBPTOComplete... |
| Dx777883146 | bigint |  |  | SI | Dimension: Dx777883146
Expression: $ztime(%source... |
| Dx785333956 | bigint |  |  | SI | Dimension: Dx785333956
Expression: %expression.Ob... |
| DxAddOnDayOfWeek | bigint |  |  | SI | Dimension: DxAddOnDayOfWeek
Expression: ##class(T... |
| DxCompletedDayOfWeek | bigint |  |  | SI | Dimension: DxCompletedDayOfWeek
Expression: ##cla... |
| DxCompletedSecurityGroup | bigint |  |  | SI | Dimension: DxCompletedSecurityGroup<br/>
Source: ... |
| DxCompletedUserName | bigint |  |  | SI | Dimension: DxCompletedUserName<br/>
Source: LBPTO... |
| DxEnteredSecurityGroup | bigint |  |  | SI | Dimension: DxEnteredSecurityGroup<br/>
Source: LB... |
| DxEnteredUserName | bigint |  |  | SI | Dimension: DxEnteredUserName<br/>
Source: LBPTOAd... |
| DxLBPTOAddOnDate | date |  |  | SI | Dimension: DxLBPTOAddOnDate<br/>
Source: LBPTOAdd... |
| DxLBPTOAddOnDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBPTOAddOnDateFxMonthYear<br/>
Sourc... |
| DxLBPTOAddOnDateFxYear | varchar |  |  | SI | Dimension: DxLBPTOAddOnDateFxYear<br/>
Source: LB... |
| DxLBPTOCompletedDate | date |  |  | SI | Dimension: DxLBPTOCompletedDate<br/>
Source: LBPT... |
| DxLBPTOCompletedDateFxYear | varchar |  |  | SI | Dimension: DxLBPTOCompletedDateFxYear<br/>
Source... |
| DxPlanned | bigint |  |  | SI | Dimension: DxPlanned
Expression: %expression.Obse... |
| MxNumberComplete | double |  |  | SI | Measure: MxNumberComplete
Expression: %source.LBP... |
| MxNumberPlanned | double |  |  | SI | Measure: MxNumberPlanned
Expression: %source.LBPT... |
| RxLBPTOParRef | bigint |  |  | SI | Relationship: RxLBPTOParRef<br/>
Source: LBPTOPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*