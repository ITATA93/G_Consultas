# TCDS_Cubes_EPVisitTestSetData_Version73.Fact

**Schema:** TCDS_Cubes_EPVisitTestSetData_Version73
**Columnas:** 41
**Actualizado:** 2026-01-30 15:30:27

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1183445310 | varchar |  |  | SI | Dimension: Dx1183445310<br/>
Source: VISTDParRef.... |
| Dx188173670 | varchar |  |  | SI | Dimension: Dx188173670<br/>
Source: VISTDParRef.V... |
| Dx2103831404 | varchar |  |  | SI | Dimension: Dx2103831404<br/>
Source: VISTDParRef.... |
| Dx2968687156 | date |  |  | SI | Dimension: Dx2968687156<br/>
Source: VISTDParRef.... |
| Dx3133930688 | varchar |  |  | SI | Dimension: Dx3133930688<br/>
Source: VISTDParRef.... |
| Dx3238682743 | varchar |  |  | SI | Dimension: Dx3238682743<br/>
Source: VISTDParRef.... |
| Dx3457723995 | date |  |  | SI | Dimension: Dx3457723995<br/>
Source: VISTDParRef.... |
| Dx4021871580 | varchar |  |  | SI | Dimension: Dx4021871580<br/>
Source: VISTDParRef.... |
| Dx4294638144 | date |  |  | SI | Dimension: Dx4294638144<br/>
Source: VISTDParRef.... |
| DxAbnormalFlag | bigint |  |  | SI | Dimension: DxAbnormalFlag<br/>
Source: VISTDAbnor... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup<br/>
Source: VISTDParRef.VI... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: VISTDParRe... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: VISTDParRe... |
| DxDoctor | bigint |  |  | SI | Dimension: DxDoctor<br/>
Source: VISTDParRef.VIST... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital<br/>
Source: VISTDParRef.VI... |
| DxInternalReferral | bigint |  |  | SI | Dimension: DxInternalReferral<br/>
Source: VISTDP... |
| DxPatientLocation | bigint |  |  | SI | Dimension: DxPatientLocation<br/>
Source: VISTDPa... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: VISTDParRef... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: VISTDParRef.VI... |
| DxRecDayOfWeek | bigint |  |  | SI | Dimension: DxRecDayOfWeek
Expression: ##class(TCD... |
| DxRecTimeRange | bigint |  |  | SI | Dimension: DxRecTimeRange
Expression: %source.VIS... |
| DxReceivingDay | varchar |  |  | SI | Dimension: DxReceivingDay<br/>
Source: VISTDParRe... |
| DxReceivingMonth | varchar |  |  | SI | Dimension: DxReceivingMonth<br/>
Source: VISTDPar... |
| DxReceivingYear | varchar |  |  | SI | Dimension: DxReceivingYear<br/>
Source: VISTDParR... |
| DxResultFlags | bigint |  |  | SI | Dimension: DxResultFlags
Expression: %expression.... |
| DxResultRead | bigint |  |  | SI | Dimension: DxResultRead<br/>
Source: VISTDParRef.... |
| DxResultValue | bigint |  |  | SI | Dimension: DxResultValue<br/>
Source: VISTDTestDa... |
| DxSendAwayReferral | bigint |  |  | SI | Dimension: DxSendAwayReferral<br/>
Source: VISTDP... |
| DxTestDepartment | bigint |  |  | SI | Dimension: DxTestDepartment<br/>
Source: VISTDTes... |
| DxTestItemCode | bigint |  |  | SI | Dimension: DxTestItemCode<br/>
Source: VISTDTestC... |
| DxTestItemDesc | bigint |  |  | SI | Dimension: DxTestItemDesc<br/>
Source: VISTDTestC... |
| DxTestSetCode | bigint |  |  | SI | Dimension: DxTestSetCode<br/>
Source: VISTDParRef... |
| DxTestSetDesc | bigint |  |  | SI | Dimension: DxTestSetDesc<br/>
Source: VISTDParRef... |
| DxTestSetPriority | bigint |  |  | SI | Dimension: DxTestSetPriority<br/>
Source: VISTDPa... |
| DxTestUserSite | bigint |  |  | SI | Dimension: DxTestUserSite<br/>
Source: VISTDParRe... |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: VISTDParRef.VI... |
| DxUserSite | bigint |  |  | SI | Dimension: DxUserSite<br/>
Source: VISTDParRef.VI... |
| MxNumberAbnormal | double |  |  | SI | Measure: MxNumberAbnormal
Expression: %cube.GetAb... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*