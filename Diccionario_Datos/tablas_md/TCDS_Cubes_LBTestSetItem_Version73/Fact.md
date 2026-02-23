# TCDS_Cubes_LBTestSetItem_Version73.Fact

**Schema:** TCDS_Cubes_LBTestSetItem_Version73
**Columnas:** 29
**Actualizado:** 2026-01-30 15:31:00

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx305663412 | bigint |  |  | SI | Dimension: Dx305663412<br/>
Source: LBTSIPathogen... |
| DxAbnormalFlag | bigint |  |  | SI | Dimension: DxAbnormalFlag
Expression: %expression... |
| DxClinicalReview | bigint |  |  | SI | Dimension: DxClinicalReview
Expression: %expressi... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSIPar... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBTSIPar... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBTSIPar... |
| DxDSSLBTestSetItemID | bigint |  |  | SI | Dimension: DxDSSLBTestSetItemID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSIParRe... |
| DxDeltaCheck | bigint |  |  | SI | Dimension: DxDeltaCheck
Expression: %expression.D... |
| DxInfectionControlReportable | bigint |  |  | SI | Dimension: DxInfectionControlReportable
Expressio... |
| DxInstrument | bigint |  |  | SI | Dimension: DxInstrument<br/>
Source: LBTSIInstrum... |
| DxInstrumentPerformedDate | bigint |  |  | SI | Dimension: DxInstrumentPerformedDate<br/>
Source:... |
| DxInstrumentPerformedTime | bigint |  |  | SI | Dimension: DxInstrumentPerformedTime
Expression: ... |
| DxLBTSIPathogen | bigint |  |  | SI | Dimension: DxLBTSIPathogen<br/>
Source: LBTSIPath... |
| DxLBTSIPathogenDuplicate | bigint |  |  | SI | Dimension: DxLBTSIPathogenDuplicate
Expression: %... |
| DxLBTSIPathogenGrowth | bigint |  |  | SI | Dimension: DxLBTSIPathogenGrowth<br/>
Source: LBT... |
| DxLBTSIPathogenSignificant | bigint |  |  | SI | Dimension: DxLBTSIPathogenSignificant
Expression:... |
| DxLBTSIPathogenSubTypeDR | bigint |  | FK | SI | Dimension: DxLBTSIPathogenSubTypeDR<br/>
Source: ... |
| DxLBTSIPathogenType | bigint |  |  | SI | Dimension: DxLBTSIPathogenType
Expression: %expre... |
| DxRangeFlag | bigint |  |  | SI | Dimension: DxRangeFlag
Expression: %expression.Ra... |
| DxResult | varchar |  |  | SI | Dimension: DxResult
Expression: %expression.GetFo... |
| DxResultType | bigint |  |  | SI | Dimension: DxResultType<br/>
Source: LBTSITestSet... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: LBTSIStatus |
| DxTestItem | bigint |  |  | SI | Dimension: DxTestItem<br/>
Source: LBTSITestSetIt... |
| DxTestSet | bigint |  |  | SI | Dimension: DxTestSet<br/>
Source: LBTSIParRef.LBT... |
| NumberAbnormalMx | double |  |  | SI | Measure: NumberAbnormalMx
Expression: %source.LBT... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*