# TCBI_Cubes_LBEpisodeAction.Fact

**Schema:** TCBI_Cubes_LBEpisodeAction
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1674593156 | bigint |  |  | SI | Dimension: Dx1674593156
Expression: $ztime(%sourc... |
| Dx1737934927 | bigint |  |  | SI | Dimension: Dx1737934927
Expression: $ztime(%sourc... |
| Dx2818742922 | bigint |  |  | SI | Dimension: Dx2818742922
Expression: %source.LBEPA... |
| Dx3749868770 | varchar |  |  | SI | Dimension: Dx3749868770<br/>
Source: LBEPACloseDa... |
| Dx3809054553 | bigint |  |  | SI | Dimension: Dx3809054553
Expression: %source.LBEPA... |
| Dx4010581001 | varchar |  |  | SI | Dimension: Dx4010581001<br/>
Source: LBEPAOpenDat... |
| Dx486859848 | varchar |  |  | SI | Dimension: Dx486859848<br/>
Source: LBEPAOpenDate |
| Dx65371738 | varchar |  |  | SI | Dimension: Dx65371738<br/>
Source: LBEPAOpenDate |
| Dx720130384 | varchar |  |  | SI | Dimension: Dx720130384<br/>
Source: LBEPACloseDat... |
| Dx724156039 | varchar |  |  | SI | Dimension: Dx724156039<br/>
Source: LBEPACloseDat... |
| Dx862688945 | varchar |  |  | SI | Dimension: Dx862688945<br/>
Source: LBEPACloseDat... |
| Dx947048036 | varchar |  |  | SI | Dimension: Dx947048036<br/>
Source: LBEPAOpenDate |
| DxAction | bigint |  |  | SI | Dimension: DxAction<br/>
Source: LBEPAEpisodeActi... |
| DxCloseDayOfWeek | bigint |  |  | SI | Dimension: DxCloseDayOfWeek
Expression: ##class(T... |
| DxClosingSecurityGroup | bigint |  |  | SI | Dimension: DxClosingSecurityGroup<br/>
Source: LB... |
| DxClosingUserName | bigint |  |  | SI | Dimension: DxClosingUserName<br/>
Source: LBEPACl... |
| DxInterimRegistration | bigint |  |  | SI | Dimension: DxInterimRegistration<br/>
Source: LBE... |
| DxLBEPACloseDate | date |  |  | SI | Dimension: DxLBEPACloseDate<br/>
Source: LBEPAClo... |
| DxLBEPACloseDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBEPACloseDateFxMonthYear<br/>
Sourc... |
| DxLBEPACloseDateFxYear | varchar |  |  | SI | Dimension: DxLBEPACloseDateFxYear<br/>
Source: LB... |
| DxLBEPAOpenDate | date |  |  | SI | Dimension: DxLBEPAOpenDate<br/>
Source: LBEPAOpen... |
| DxLBEPAOpenDateFxMonthYear | varchar |  |  | SI | Dimension: DxLBEPAOpenDateFxMonthYear<br/>
Source... |
| DxLBEPAOpenDateFxYear | varchar |  |  | SI | Dimension: DxLBEPAOpenDateFxYear<br/>
Source: LBE... |
| DxOpenDayOfWeek | bigint |  |  | SI | Dimension: DxOpenDayOfWeek
Expression: ##class(TC... |
| DxOpeningSecurityGroup | bigint |  |  | SI | Dimension: DxOpeningSecurityGroup<br/>
Source: LB... |
| DxOpeningUserName | bigint |  |  | SI | Dimension: DxOpeningUserName<br/>
Source: LBEPAOp... |
| DxSuppressBilling | bigint |  |  | SI | Dimension: DxSuppressBilling<br/>
Source: LBEPAEp... |
| DxSuppressReports | bigint |  |  | SI | Dimension: DxSuppressReports<br/>
Source: LBEPAEp... |
| MxInterimRegistration | double |  |  | SI | Measure: MxInterimRegistration
Expression: %sourc... |
| MxSuppressBilling | double |  |  | SI | Measure: MxSuppressBilling
Expression: %source.LB... |
| MxSuppressReports | double |  |  | SI | Measure: MxSuppressReports
Expression: %source.LB... |
| RxLBEPAParRef | bigint |  |  | SI | Relationship: RxLBEPAParRef<br/>
Source: LBEPAPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*