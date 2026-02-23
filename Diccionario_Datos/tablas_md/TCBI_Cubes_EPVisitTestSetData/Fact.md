# TCBI_Cubes_EPVisitTestSetData.Fact

**Schema:** TCBI_Cubes_EPVisitTestSetData
**Columnas:** 41
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx2968687156 | date |  |  | SI | Dimension: Dx2968687156<br/>
Source: VISTDParRef.... |
| Dx3457723995 | date |  |  | SI | Dimension: Dx3457723995<br/>
Source: VISTDParRef.... |
| Dx4294638144 | date |  |  | SI | Dimension: Dx4294638144<br/>
Source: VISTDParRef.... |
| DxAbnormalFlag | bigint |  |  | SI | Dimension: DxAbnormalFlag<br/>
Source: VISTDAbnor... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup<br/>
Source: VISTDParRef.VI... |
| DxCollectionDay | varchar |  |  | SI | Dimension: DxCollectionDay<br/>
Source: VISTDParR... |
| DxCollectionMonth | varchar |  |  | SI | Dimension: DxCollectionMonth<br/>
Source: VISTDPa... |
| DxCollectionYear | varchar |  |  | SI | Dimension: DxCollectionYear<br/>
Source: VISTDPar... |
| DxCreationDay | varchar |  |  | SI | Dimension: DxCreationDay<br/>
Source: VISTDParRef... |
| DxCreationMonth | varchar |  |  | SI | Dimension: DxCreationMonth<br/>
Source: VISTDParR... |
| DxCreationYear | varchar |  |  | SI | Dimension: DxCreationYear<br/>
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
Expression: ##class(TCB... |
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
| Rx144486457 | bigint |  |  | SI | Relationship: Rx144486457<br/>
Source: VISTDParRe... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*