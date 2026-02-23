# TCBI_Cubes_LBTestSetItem.Fact

**Schema:** TCBI_Cubes_LBTestSetItem
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1326956922 | varchar |  |  | SI | Dimension: Dx1326956922<br/>
Source: LBTSINotPerf... |
| Dx1719071779 | varchar |  |  | SI | Dimension: Dx1719071779<br/>
Source: LBTSINotPerf... |
| Dx1723007294 | varchar |  |  | SI | Dimension: Dx1723007294<br/>
Source: LBTSIEntered... |
| Dx1795236086 | varchar |  |  | SI | Dimension: Dx1795236086<br/>
Source: LBTSIAuthori... |
| Dx2134600777 | varchar |  |  | SI | Dimension: Dx2134600777<br/>
Source: LBTSINotPerf... |
| Dx228147797 | varchar |  |  | SI | Dimension: Dx228147797<br/>
Source: LBTSINotPerfo... |
| Dx2317570511 | bigint |  |  | SI | Dimension: Dx2317570511
Expression: %source.LBTSI... |
| Dx2558510383 | varchar |  |  | SI | Dimension: Dx2558510383<br/>
Source: LBTSIAuthori... |
| Dx2770133921 | bigint |  |  | SI | Dimension: Dx2770133921
Expression: $ztime(%sourc... |
| Dx2956716577 | varchar |  |  | SI | Dimension: Dx2956716577<br/>
Source: LBTSIEntered... |
| Dx305663412 | bigint |  |  | SI | Dimension: Dx305663412<br/>
Source: LBTSIPathogen... |
| Dx3426131250 | bigint |  |  | SI | Dimension: Dx3426131250
Expression: $ztime(%sourc... |
| Dx3469339730 | bigint |  |  | SI | Dimension: Dx3469339730
Expression: $ztime(%sourc... |
| Dx350049579 | varchar |  |  | SI | Dimension: Dx350049579<br/>
Source: LBTSIAuthoris... |
| Dx3663745050 | varchar |  |  | SI | Dimension: Dx3663745050<br/>
Source: LBTSIAuthori... |
| Dx36876336 | varchar |  |  | SI | Dimension: Dx36876336<br/>
Source: LBTSIEnteredDa... |
| Dx3743415091 | bigint |  |  | SI | Dimension: Dx3743415091<br/>
Source: LBTSISpecime... |
| Dx3758630532 | bigint |  |  | SI | Dimension: Dx3758630532
Expression: %source.LBTSI... |
| Dx3782254598 | varchar |  |  | SI | Dimension: Dx3782254598<br/>
Source: LBTSINotPerf... |
| Dx4013058185 | varchar |  |  | SI | Dimension: Dx4013058185<br/>
Source: LBTSIEntered... |
| Dx415295252 | bigint |  |  | SI | Dimension: Dx415295252
Expression: %source.LBTSIN... |
| Dx4191639586 | varchar |  |  | SI | Dimension: Dx4191639586<br/>
Source: LBTSINotPerf... |
| Dx64719578 | varchar |  |  | SI | Dimension: Dx64719578<br/>
Source: LBTSIEnteredDa... |
| Dx914993737 | varchar |  |  | SI | Dimension: Dx914993737<br/>
Source: LBTSIAuthoris... |
| DxAbnormalFlag | bigint |  |  | SI | Dimension: DxAbnormalFlag<br/>
Source: LBTSIResul... |
| DxAuthDayOfWeek | bigint |  |  | SI | Dimension: DxAuthDayOfWeek
Expression: ##class(TC... |
| DxAuthorisingUserName | bigint |  |  | SI | Dimension: DxAuthorisingUserName<br/>
Source: LBT... |
| DxBillable | bigint |  |  | SI | Dimension: DxBillable<br/>
Source: LBTSIBillable |
| DxClinicalReview | bigint |  |  | SI | Dimension: DxClinicalReview
Expression: %expressi... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSIPar... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: LBTSIPar... |
| DxDSSLBTestSetItemID | bigint |  |  | SI | Dimension: DxDSSLBTestSetItemID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSIParRe... |
| DxDeltaCheck | bigint |  |  | SI | Dimension: DxDeltaCheck
Expression: %expression.D... |
| DxEnteredDayOfWeek | bigint |  |  | SI | Dimension: DxEnteredDayOfWeek
Expression: ##class... |
| DxEnteringSecurityGroup | bigint |  |  | SI | Dimension: DxEnteringSecurityGroup<br/>
Source: L... |
| DxEnteringUserName | bigint |  |  | SI | Dimension: DxEnteringUserName<br/>
Source: LBTSIE... |
| DxExtendedValidity | bigint |  |  | SI | Dimension: DxExtendedValidity
Expression: %expres... |
| DxInfectionControlReportable | bigint |  |  | SI | Dimension: DxInfectionControlReportable
Expressio... |
| DxInstrument | bigint |  |  | SI | Dimension: DxInstrument<br/>
Source: LBTSIInstrum... |
| DxInvalidAtReceive | bigint |  |  | SI | Dimension: DxInvalidAtReceive
Expression: %expres... |
| DxLBCOrganismSubType | bigint |  |  | SI | Dimension: DxLBCOrganismSubType<br/>
Source: LBTS... |
| DxLBCOrganismSubTypeGroup | bigint |  |  | SI | Dimension: DxLBCOrganismSubTypeGroup<br/>
Source:... |
| DxLBTSIAnatomicalSiteQualifiers | varchar |  |  | SI | Dimension: DxLBTSIAnatomicalSiteQualifiers
Expres... |
| DxLBTSIAnatomicalSites | varchar |  |  | SI | Dimension: DxLBTSIAnatomicalSites
Expression: %ex... |
| DxLBTSIAuthoriseDate | date |  |  | SI | Dimension: DxLBTSIAuthoriseDate<br/>
Source: LBTS... |
| DxLBTSIAuthoriseDateFxYear | varchar |  |  | SI | Dimension: DxLBTSIAuthoriseDateFxYear<br/>
Source... |
| DxLBTSIContainers | varchar |  |  | SI | Dimension: DxLBTSIContainers
Expression: %express... |
| DxLBTSIEnteredDate | date |  |  | SI | Dimension: DxLBTSIEnteredDate<br/>
Source: LBTSIE... |
| DxLBTSIEnteredDateFxYear | varchar |  |  | SI | Dimension: DxLBTSIEnteredDateFxYear<br/>
Source: ... |
| DxLBTSILesions | varchar |  |  | SI | Dimension: DxLBTSILesions
Expression: %expression... |
| DxLBTSINotPerformedDate | date |  |  | SI | Dimension: DxLBTSINotPerformedDate<br/>
Source: L... |
| DxLBTSIPathogen | bigint |  |  | SI | Dimension: DxLBTSIPathogen<br/>
Source: LBTSIPath... |
| DxLBTSIPathogenDuplicate | bigint |  |  | SI | Dimension: DxLBTSIPathogenDuplicate<br/>
Source: ... |
| DxLBTSIPathogenGrowth | bigint |  |  | SI | Dimension: DxLBTSIPathogenGrowth<br/>
Source: LBT... |
| DxLBTSIPathogenSignificant | bigint |  |  | SI | Dimension: DxLBTSIPathogenSignificant<br/>
Source... |
| DxLBTSIPathogenType | bigint |  |  | SI | Dimension: DxLBTSIPathogenType
Expression: %expre... |
| DxLBTSISpecimenGroups | varchar |  |  | SI | Dimension: DxLBTSISpecimenGroups
Expression: %exp... |
| DxLBTSISpecimens | varchar |  |  | SI | Dimension: DxLBTSISpecimens
Expression: %expressi... |
| DxLBTSIValidityExtensionReason | bigint |  |  | SI | Dimension: DxLBTSIValidityExtensionReason<br/>
So... |
| DxNotPerformed | bigint |  |  | SI | Dimension: DxNotPerformed<br/>
Source: LBTSINotPe... |
| DxNotPerformedDayOfWeek | bigint |  |  | SI | Dimension: DxNotPerformedDayOfWeek
Expression: ##... |
| DxNotPerformedSecurityGroup | bigint |  |  | SI | Dimension: DxNotPerformedSecurityGroup<br/>
Sourc... |
| DxNotPerformedUserName | bigint |  |  | SI | Dimension: DxNotPerformedUserName<br/>
Source: LB... |
| DxPerformedDate | bigint |  |  | SI | Dimension: DxPerformedDate<br/>
Source: LBTSIPerf... |
| DxPerformedTime | bigint |  |  | SI | Dimension: DxPerformedTime
Expression: $ztime(%so... |
| DxRangeFlag | bigint |  |  | SI | Dimension: DxRangeFlag
Expression: %expression.Ra... |
| DxResult | varchar |  |  | SI | Dimension: DxResult
Expression: %expression.GetFo... |
| DxResultType | bigint |  |  | SI | Dimension: DxResultType<br/>
Source: LBTSITestSet... |
| DxSecurityGroup | bigint |  |  | SI | Dimension: DxSecurityGroup<br/>
Source: LBTSIAuth... |
| DxSpecimenValidityExceeded | bigint |  |  | SI | Dimension: DxSpecimenValidityExceeded
Expression:... |
| DxSpecimenValidityExceededSlot | bigint |  |  | SI | Dimension: DxSpecimenValidityExceededSlot
Express... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: LBTSIStatus |
| DxTestItem | bigint |  |  | SI | Dimension: DxTestItem<br/>
Source: LBTSITestSetIt... |
| DxWithinValidityPeriod | bigint |  |  | SI | Dimension: DxWithinValidityPeriod
Expression: %ex... |
| NumberAbnormalMx | double |  |  | SI | Measure: NumberAbnormalMx
Expression: %source.LBT... |
| NumberClinicalReviewMx | double |  |  | SI | Measure: NumberClinicalReviewMx
Expression: %sour... |
| NumberExtendedMx | double |  |  | SI | Measure: NumberExtendedMx
Expression: %expression... |
| NumberInvalidMx | double |  |  | SI | Measure: NumberInvalidMx
Expression: %expression.... |
| NumberValidMx | double |  |  | SI | Measure: NumberValidMx
Expression: %expression.Wi... |
| RxLBTSIParRef | bigint |  |  | SI | Relationship: RxLBTSIParRef<br/>
Source: LBTSIPar... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*