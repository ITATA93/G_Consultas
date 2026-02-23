# TCBI_Cubes_ORAnaesthesia.Fact

**Schema:** TCBI_Cubes_ORAnaesthesia
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1206364338 | varchar |  |  | SI | Dimension: Dx1206364338<br/>
Source: ANAAreaOutDa... |
| Dx1210787216 | varchar |  |  | SI | Dimension: Dx1210787216<br/>
Source: ANAPACUReady... |
| Dx1450743229 | varchar |  |  | SI | Dimension: Dx1450743229<br/>
Source: ANAPACUStart... |
| Dx1579091062 | varchar |  |  | SI | Dimension: Dx1579091062<br/>
Source: ANAAreaInDat... |
| Dx161447415 | varchar |  |  | SI | Dimension: Dx161447415<br/>
Source: ANAAreaOutDat... |
| Dx1698706986 | varchar |  |  | SI | Dimension: Dx1698706986<br/>
Source: ANAAreaOutDa... |
| Dx1746602050 | varchar |  |  | SI | Dimension: Dx1746602050<br/>
Source: ANAFinishDat... |
| Dx1845559608 | varchar |  |  | SI | Dimension: Dx1845559608<br/>
Source: ANAAreaInDat... |
| Dx2086263519 | varchar |  |  | SI | Dimension: Dx2086263519<br/>
Source: ANAPACUStart... |
| Dx2230512145 | varchar |  |  | SI | Dimension: Dx2230512145<br/>
Source: ANAFinishDat... |
| Dx2259095905 | varchar |  |  | SI | Dimension: Dx2259095905<br/>
Source: ANAPACUStart... |
| Dx235111016 | varchar |  |  | SI | Dimension: Dx235111016<br/>
Source: ANAFinishDate |
| Dx2490427409 | varchar |  |  | SI | Dimension: Dx2490427409<br/>
Source: ANAPACUReady... |
| Dx2570331764 | varchar |  |  | SI | Dimension: Dx2570331764<br/>
Source: ANAPACUReady... |
| Dx2764228547 | varchar |  |  | SI | Dimension: Dx2764228547<br/>
Source: ANAPACUReady... |
| Dx3002525221 | varchar |  |  | SI | Dimension: Dx3002525221<br/>
Source: ANAAreaInDat... |
| Dx3654146263 | varchar |  |  | SI | Dimension: Dx3654146263<br/>
Source: ANAPACUStart... |
| Dx3708787581 | varchar |  |  | SI | Dimension: Dx3708787581<br/>
Source: ANAAreaInDat... |
| Dx3849756580 | varchar |  |  | SI | Dimension: Dx3849756580<br/>
Source: ANAAreaOutDa... |
| Dx51374538 | varchar |  |  | SI | Dimension: Dx51374538<br/>
Source: ANAFinishDate |
| Dx528719415 | varchar |  |  | SI | Dimension: Dx528719415<br/>
Source: ANAPACUReadyL... |
| Dx709645112 | varchar |  |  | SI | Dimension: Dx709645112<br/>
Source: ANAPACUReadyL... |
| Dx891566724 | varchar |  |  | SI | Dimension: Dx891566724<br/>
Source: ANAPACUStartD... |
| DxANAAreaInDate | date |  |  | SI | Dimension: DxANAAreaInDate<br/>
Source: ANAAreaIn... |
| DxANAAreaInDateFxMonthYear | varchar |  |  | SI | Dimension: DxANAAreaInDateFxMonthYear<br/>
Source... |
| DxANAAreaInDateFxYear | varchar |  |  | SI | Dimension: DxANAAreaInDateFxYear<br/>
Source: ANA... |
| DxANAAreaOutDate | date |  |  | SI | Dimension: DxANAAreaOutDate<br/>
Source: ANAAreaO... |
| DxANAAreaOutDateFxMonthYear | varchar |  |  | SI | Dimension: DxANAAreaOutDateFxMonthYear<br/>
Sourc... |
| DxANAAreaOutDateFxYear | varchar |  |  | SI | Dimension: DxANAAreaOutDateFxYear<br/>
Source: AN... |
| DxANADate | date |  |  | SI | Dimension: DxANADate<br/>
Source: ANADate |
| DxANADateFxDayMonthYear | varchar |  |  | SI | Dimension: DxANADateFxDayMonthYear<br/>
Source: A... |
| DxANADateFxMonthNumber | varchar |  |  | SI | Dimension: DxANADateFxMonthNumber<br/>
Source: AN... |
| DxANADateFxMonthYear | varchar |  |  | SI | Dimension: DxANADateFxMonthYear<br/>
Source: ANAD... |
| DxANADateFxQuarterNumber | varchar |  |  | SI | Dimension: DxANADateFxQuarterNumber<br/>
Source: ... |
| DxANADateFxQuarterYear | varchar |  |  | SI | Dimension: DxANADateFxQuarterYear<br/>
Source: AN... |
| DxANADateFxYear | varchar |  |  | SI | Dimension: DxANADateFxYear<br/>
Source: ANADate |
| DxANAFinishDate | date |  |  | SI | Dimension: DxANAFinishDate<br/>
Source: ANAFinish... |
| DxANAFinishDateFxMonthYear | varchar |  |  | SI | Dimension: DxANAFinishDateFxMonthYear<br/>
Source... |
| DxANAFinishDateFxYear | varchar |  |  | SI | Dimension: DxANAFinishDateFxYear<br/>
Source: ANA... |
| DxANAPACUReadyLeaveDate | date |  |  | SI | Dimension: DxANAPACUReadyLeaveDate<br/>
Source: A... |
| DxANAPACUStartDate | date |  |  | SI | Dimension: DxANAPACUStartDate<br/>
Source: ANAPAC... |
| DxANAPACUStartDateFxYear | varchar |  |  | SI | Dimension: DxANAPACUStartDateFxYear<br/>
Source: ... |
| DxAnaestheticASA | bigint |  |  | SI | Dimension: DxAnaestheticASA<br/>
Source: ANAASADR... |
| DxAnaestheticFinishTimeRange | bigint |  |  | SI | Dimension: DxAnaestheticFinishTimeRange
Expressio... |
| DxAnaestheticMethod | bigint |  |  | SI | Dimension: DxAnaestheticMethod<br/>
Source: ANAMe... |
| DxAnaestheticOutcome | bigint |  |  | SI | Dimension: DxAnaestheticOutcome<br/>
Source: ANAO... |
| DxAnaestheticStartTimeRange | bigint |  |  | SI | Dimension: DxAnaestheticStartTimeRange
Expression... |
| DxAnaestheticStatus | bigint |  |  | SI | Dimension: DxAnaestheticStatus<br/>
Source: ANASt... |
| DxAnaestheticType | bigint |  |  | SI | Dimension: DxAnaestheticType<br/>
Source: ANAMeth... |
| DxAnaesthetist | bigint |  |  | SI | Dimension: DxAnaesthetist<br/>
Source: ANAAnaesth... |
| DxAreaInTimeRange | bigint |  |  | SI | Dimension: DxAreaInTimeRange
Expression: %source.... |
| DxAreaOutTimeRange | bigint |  |  | SI | Dimension: DxAreaOutTimeRange
Expression: %source... |
| DxComplication | varchar |  |  | SI | Dimension: DxComplication
Expression: %cube.GetAn... |
| DxIVStartToProcedure | bigint |  |  | SI | Dimension: DxIVStartToProcedure
Expression: %cube... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ANAPAADMParRe... |
| DxReadyToLeaveToPACUOutTime | bigint |  |  | SI | Dimension: DxReadyToLeaveToPACUOutTime
Expression... |
| DxRecoveryLeaveTimeRange | bigint |  |  | SI | Dimension: DxRecoveryLeaveTimeRange
Expression: %... |
| DxRecoveryStartTimeRange | bigint |  |  | SI | Dimension: DxRecoveryStartTimeRange
Expression: %... |
| MxTotalAnaestheticTime | double |  |  | SI | Measure: MxTotalAnaestheticTime
Expression: ##cla... |
| MxTotalOperationTime | double |  |  | SI | Measure: MxTotalOperationTime
Expression: ##class... |
| MxTotalProcedureTime | double |  |  | SI | Measure: MxTotalProcedureTime
Expression: %cube.G... |
| MxTotalRecoveryTime | double |  |  | SI | Measure: MxTotalRecoveryTime
Expression: ##class(... |
| MxTotalRecoveryToLeaveTime | double |  |  | SI | Measure: MxTotalRecoveryToLeaveTime
Expression: #... |
| MxTotalTheatreTime | double |  |  | SI | Measure: MxTotalTheatreTime
Expression: ##class(T... |
| RxIDViaANARBOperatingRoomDR | bigint |  | FK | SI | Relationship: RxIDViaANARBOperatingRoomDR<br/>
So... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*