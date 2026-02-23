# TCBI_Cubes_ORAnaestOperation.Fact

**Schema:** TCBI_Cubes_ORAnaestOperation
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1522411911 | varchar |  |  | SI | Dimension: Dx1522411911<br/>
Source: ANAOPParRef.... |
| Dx1544018852 | date |  |  | SI | Dimension: Dx1544018852<br/>
Source: ANAOPParRef.... |
| Dx1575382567 | varchar |  |  | SI | Dimension: Dx1575382567<br/>
Source: ANAOPParRef.... |
| Dx1623647890 | varchar |  |  | SI | Dimension: Dx1623647890<br/>
Source: ANAOPParRef.... |
| Dx1669635594 | varchar |  |  | SI | Dimension: Dx1669635594<br/>
Source: ANAOPOpEndDa... |
| Dx1891979605 | varchar |  |  | SI | Dimension: Dx1891979605<br/>
Source: ANAOPParRef.... |
| Dx1980748892 | varchar |  |  | SI | Dimension: Dx1980748892<br/>
Source: ANAOPOpEndDa... |
| Dx2087478341 | date |  |  | SI | Dimension: Dx2087478341<br/>
Source: ANAOPParRef.... |
| Dx2144411376 | varchar |  |  | SI | Dimension: Dx2144411376<br/>
Source: ANAOPOpStart... |
| Dx218028052 | varchar |  |  | SI | Dimension: Dx218028052<br/>
Source: ANAOPParRef.A... |
| Dx2225697556 | varchar |  |  | SI | Dimension: Dx2225697556<br/>
Source: ANAOPParRef.... |
| Dx2406317145 | varchar |  |  | SI | Dimension: Dx2406317145<br/>
Source: ANAOPOpEndDa... |
| Dx2970586228 | varchar |  |  | SI | Dimension: Dx2970586228<br/>
Source: ANAOPParRef.... |
| Dx3195453479 | varchar |  |  | SI | Dimension: Dx3195453479<br/>
Source: ANAOPOpStart... |
| Dx3244295029 | varchar |  |  | SI | Dimension: Dx3244295029<br/>
Source: ANAOPParRef.... |
| Dx339451090 | varchar |  |  | SI | Dimension: Dx339451090<br/>
Source: ANAOPParRef.A... |
| Dx3452003640 | varchar |  |  | SI | Dimension: Dx3452003640<br/>
Source: ANAOPOpStart... |
| Dx3468918953 | varchar |  |  | SI | Dimension: Dx3468918953<br/>
Source: ANAOPParRef.... |
| Dx3856449673 | varchar |  |  | SI | Dimension: Dx3856449673<br/>
Source: ANAOPOpStart... |
| Dx4174544513 | varchar |  |  | SI | Dimension: Dx4174544513<br/>
Source: ANAOPParRef.... |
| Dx525079060 | varchar |  |  | SI | Dimension: Dx525079060<br/>
Source: ANAOPParRef.A... |
| Dx556304235 | varchar |  |  | SI | Dimension: Dx556304235<br/>
Source: ANAOPOpStartD... |
| Dx583209257 | varchar |  |  | SI | Dimension: Dx583209257<br/>
Source: ANAOPOpEndDat... |
| DxANAOPOpEndDate | date |  |  | SI | Dimension: DxANAOPOpEndDate<br/>
Source: ANAOPOpE... |
| DxANAOPOpEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxANAOPOpEndDateFxMonthYear<br/>
Sourc... |
| DxANAOPOpEndDateFxYear | varchar |  |  | SI | Dimension: DxANAOPOpEndDateFxYear<br/>
Source: AN... |
| DxANAOPOpStartDate | date |  |  | SI | Dimension: DxANAOPOpStartDate<br/>
Source: ANAOPO... |
| DxANAOPOpStartDateFxYear | varchar |  |  | SI | Dimension: DxANAOPOpStartDateFxYear<br/>
Source: ... |
| DxEarlyFinishTimeRang | bigint |  |  | SI | Dimension: DxEarlyFinishTimeRang
Expression: "sou... |
| DxElectiveOrEmergency | bigint |  |  | SI | Dimension: DxElectiveOrEmergency<br/>
Source: ANA... |
| DxEpisodeID | bigint |  |  | SI | Dimension: DxEpisodeID<br/>
Source: ANAOPParRef.A... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: ANAOPResourceD... |
| DxLateStartTimeRange | bigint |  |  | SI | Dimension: DxLateStartTimeRange
Expression: %cube... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: ANAOPResourceD... |
| DxOperation | bigint |  |  | SI | Dimension: DxOperation<br/>
Source: ANAOPTypeDR.O... |
| DxOperationDayOfWeek | bigint |  |  | SI | Dimension: DxOperationDayOfWeek
Expression: $syst... |
| DxOperationEndTimeRange | bigint |  |  | SI | Dimension: DxOperationEndTimeRange
Expression: %s... |
| DxOperationStartTimeRange | bigint |  |  | SI | Dimension: DxOperationStartTimeRange
Expression: ... |
| DxOperationStatus | bigint |  |  | SI | Dimension: DxOperationStatus
Expression: %cube.Ge... |
| DxOperationType | bigint |  |  | SI | Dimension: DxOperationType<br/>
Source: ANAOPOper... |
| DxOverrunTimeRange | bigint |  |  | SI | Dimension: DxOverrunTimeRange
Expression: %cube.G... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ANAOPParRef.A... |
| DxProcedure | bigint |  |  | SI | Dimension: DxProcedure<br/>
Source: ANAOPStatePPP... |
| DxResource | bigint |  |  | SI | Dimension: DxResource<br/>
Source: ANAOPResourceD... |
| DxSurgeon | bigint |  |  | SI | Dimension: DxSurgeon<br/>
Source: ANAOPSurgeonDR.... |
| DxSurgeonSpecialty | bigint |  |  | SI | Dimension: DxSurgeonSpecialty<br/>
Source: ANAOPS... |
| DxTTimeOfOperationTimeRange | bigint |  |  | SI | Dimension: DxTTimeOfOperationTimeRange
Expression... |
| DxTheatreInTimeRange | bigint |  |  | SI | Dimension: DxTheatreInTimeRange
Expression: %sour... |
| DxTheatreOutTimeRange | bigint |  |  | SI | Dimension: DxTheatreOutTimeRange
Expression: %sou... |
| DxTimeInAreaTimeRange | bigint |  |  | SI | Dimension: DxTimeInAreaTimeRange
Expression: ##cl... |
| DxTimeInTheatreTimeRange | bigint |  |  | SI | Dimension: DxTimeInTheatreTimeRange
Expression: #... |
| MxEarlyFinish | double |  |  | SI | Measure: MxEarlyFinish
Expression: %cube.GetEarly... |
| MxLateStart | double |  |  | SI | Measure: MxLateStart
Expression: %cube.GetLateSta... |
| MxOverrun | double |  |  | SI | Measure: MxOverrun
Expression: %cube.GetOverrun(%... |
| MxTotalOperationTime | double |  |  | SI | Measure: MxTotalOperationTime
Expression: ##class... |
| MxTotalProcedureTime | double |  |  | SI | Measure: MxTotalProcedureTime
Expression: ##class... |
| MxTotalTheatreTime | double |  |  | SI | Measure: MxTotalTheatreTime
Expression: ##class(T... |
| MxTotalTimeToTheatre | double |  |  | SI | Measure: MxTotalTimeToTheatre
Expression: ##class... |
| RxIDViaANAOPParRef | bigint |  |  | SI | Relationship: RxIDViaANAOPParRef<br/>
Source: ANA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*