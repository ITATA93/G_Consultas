# TCBI_Cubes_RBEventTimes.Fact

**Schema:** TCBI_Cubes_RBEventTimes
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxBookingStatus | bigint |  |  | SI | Dimension: DxBookingStatus<br/>
Source: TIMEParRe... |
| DxCareProvider | varchar |  |  | SI | Dimension: DxCareProvider
Expression: %cube.GetCa... |
| DxContactMethod | bigint |  |  | SI | Dimension: DxContactMethod<br/>
Source: TIMEParRe... |
| DxEventAdministrator | bigint |  |  | SI | Dimension: DxEventAdministrator<br/>
Source: TIME... |
| DxEventDateDay | varchar |  |  | SI | Dimension: DxEventDateDay<br/>
Source: TIMEDate |
| DxEventDateMonth | varchar |  |  | SI | Dimension: DxEventDateMonth<br/>
Source: TIMEDate |
| DxEventDateMonthOfYear | varchar |  |  | SI | Dimension: DxEventDateMonthOfYear<br/>
Source: TI... |
| DxEventDateQuarter | varchar |  |  | SI | Dimension: DxEventDateQuarter<br/>
Source: TIMEDa... |
| DxEventDateQuarterOfYear | varchar |  |  | SI | Dimension: DxEventDateQuarterOfYear<br/>
Source: ... |
| DxEventDateYear | varchar |  |  | SI | Dimension: DxEventDateYear<br/>
Source: TIMEDate |
| DxEventDayOfWeek | bigint |  |  | SI | Dimension: DxEventDayOfWeek
Expression: $system.S... |
| DxEventName | bigint |  |  | SI | Dimension: DxEventName<br/>
Source: TIMEParRef.EV... |
| DxEventNumber | bigint |  |  | SI | Dimension: DxEventNumber<br/>
Source: TIMEParRef.... |
| DxEventResource | bigint |  |  | SI | Dimension: DxEventResource<br/>
Source: TIMEParRe... |
| DxEventStartTimeRange | bigint |  |  | SI | Dimension: DxEventStartTimeRange
Expression: %sou... |
| DxEventType | bigint |  |  | SI | Dimension: DxEventType<br/>
Source: TIMEParRef.EV... |
| DxFacilitator | varchar |  |  | SI | Dimension: DxFacilitator
Expression: %cube.GetFac... |
| DxOrganisationalClient | bigint |  |  | SI | Dimension: DxOrganisationalClient<br/>
Source: TI... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: TIMEParRef.EVInsT... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: TIMEParRef.EVAuxIn... |
| DxPopulationGroup | bigint |  |  | SI | Dimension: DxPopulationGroup<br/>
Source: TIMEPar... |
| DxProgramPriority | bigint |  |  | SI | Dimension: DxProgramPriority<br/>
Source: TIMEPar... |
| DxProgramType | bigint |  |  | SI | Dimension: DxProgramType<br/>
Source: TIMEParRef.... |
| DxService | bigint |  |  | SI | Dimension: DxService<br/>
Source: TIMEItemCatDR.A... |
| DxSessionStatus | bigint |  |  | SI | Dimension: DxSessionStatus<br/>
Source: TIMEStatu... |
| DxTIMEDate | date |  |  | SI | Dimension: DxTIMEDate<br/>
Source: TIMEDate |
| DxTeam | bigint |  |  | SI | Dimension: DxTeam<br/>
Source: TIMEParRef.EVLocat... |
| MxAttendeeFemaleNo | double |  |  | SI | Measure: MxAttendeeFemaleNo
Expression: %source.T... |
| MxAttendeeMaleNo | double |  |  | SI | Measure: MxAttendeeMaleNo
Expression: %source.TIM... |
| MxCharge | double |  |  | SI | Measure: MxCharge
Expression: %source.TIMECharge |
| MxDirectTime | double |  |  | SI | Measure: MxDirectTime
Expression: %source.TIMEPar... |
| MxIndirectTime | double |  |  | SI | Measure: MxIndirectTime
Expression: %source.TIMEP... |
| MxInterpreterTime | double |  |  | SI | Measure: MxInterpreterTime
Expression: %source.TI... |
| MxNoOfAttendees | double |  |  | SI | Measure: MxNoOfAttendees
Expression: %source.TIME... |
| MxTravelTime | double |  |  | SI | Measure: MxTravelTime
Expression: %source.TIMETra... |
| Rx69056849 | bigint |  |  | SI | Relationship: Rx69056849
Expression: %cube.GetApp... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*