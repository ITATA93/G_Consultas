# TCDS_Cubes_LBTestSet.Fact

**Schema:** TCDS_Cubes_LBTestSet
**Columnas:** 47
**Actualizado:** 2026-01-30 15:30:55

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1256134610 | varchar |  |  | SI | Dimension: Dx1256134610<br/>
Source: LBTSAuthoris... |
| Dx2308660708 | varchar |  |  | SI | Dimension: Dx2308660708<br/>
Source: LBTSReceived... |
| Dx2587128100 | varchar |  |  | SI | Dimension: Dx2587128100<br/>
Source: LBTSCollecte... |
| Dx2790979782 | bigint |  |  | SI | Dimension: Dx2790979782
Expression: %expression.G... |
| Dx3016082642 | varchar |  |  | SI | Dimension: Dx3016082642<br/>
Source: LBTSAuthoris... |
| Dx3289994581 | varchar |  |  | SI | Dimension: Dx3289994581<br/>
Source: LBTSAuthoris... |
| Dx3892608821 | varchar |  |  | SI | Dimension: Dx3892608821<br/>
Source: LBTSReceived... |
| Dx4245293132 | bigint |  |  | SI | Dimension: Dx4245293132
Expression: %source.LBTSA... |
| Dx623491154 | bigint |  |  | SI | Dimension: Dx623491154
Expression: $ztime(%source... |
| Dx759468767 | varchar |  |  | SI | Dimension: Dx759468767<br/>
Source: LBTSCollected... |
| DxAuthDayOfWeek | bigint |  |  | SI | Dimension: DxAuthDayOfWeek
Expression: ##class(TC... |
| DxCTLOCDescViaLBTSLabSiteDR | bigint |  | FK | SI | Dimension: DxCTLOCDescViaLBTSLabSiteDR<br/>
Sourc... |
| DxClinicalReview | bigint |  |  | SI | Dimension: DxClinicalReview
Expression: %expressi... |
| DxDSSLBEpisodeID | bigint |  |  | SI | Dimension: DxDSSLBEpisodeID<br/>
Source: LBTSEpis... |
| DxDSSLBSubjectID | bigint |  |  | SI | Dimension: DxDSSLBSubjectID<br/>
Source: LBTSEpis... |
| DxDSSLBTestSetID | bigint |  |  | SI | Dimension: DxDSSLBTestSetID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: LBTSEpisod... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: LBTSTestSetD... |
| DxLBTSAnatomicalSiteQualifiers | varchar |  |  | SI | Dimension: DxLBTSAnatomicalSiteQualifiers
Express... |
| DxLBTSAnatomicalSites | varchar |  |  | SI | Dimension: DxLBTSAnatomicalSites
Expression: %exp... |
| DxLBTSAuthoriseDate | date |  |  | SI | Dimension: DxLBTSAuthoriseDate<br/>
Source: LBTSA... |
| DxLBTSAuthoriseDateFxYear | varchar |  |  | SI | Dimension: DxLBTSAuthoriseDateFxYear<br/>
Source:... |
| DxLBTSCollectedDate | date |  |  | SI | Dimension: DxLBTSCollectedDate<br/>
Source: LBTSC... |
| DxLBTSCollectedDateFxYear | varchar |  |  | SI | Dimension: DxLBTSCollectedDateFxYear<br/>
Source:... |
| DxLBTSIContainers | varchar |  |  | SI | Dimension: DxLBTSIContainers
Expression: %express... |
| DxLBTSISpecimenGroups | varchar |  |  | SI | Dimension: DxLBTSISpecimenGroups
Expression: %exp... |
| DxLBTSLesions | varchar |  |  | SI | Dimension: DxLBTSLesions
Expression: %expression.... |
| DxLBTSPathogensIdentified | varchar |  |  | SI | Dimension: DxLBTSPathogensIdentified
Expression: ... |
| DxLBTSReceivedDate | date |  |  | SI | Dimension: DxLBTSReceivedDate<br/>
Source: LBTSRe... |
| DxLBTSReceivedDateFxYear | varchar |  |  | SI | Dimension: DxLBTSReceivedDateFxYear<br/>
Source: ... |
| DxLBTSSignificantResult | bigint |  |  | SI | Dimension: DxLBTSSignificantResult
Expression: %e... |
| DxLBTSSpecimens | varchar |  |  | SI | Dimension: DxLBTSSpecimens
Expression: %expressio... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: LBTSPriorityDR... |
| DxReasonNotPerfomed | bigint |  |  | SI | Dimension: DxReasonNotPerfomed<br/>
Source: LBTSR... |
| DxReferralLab | bigint |  |  | SI | Dimension: DxReferralLab<br/>
Source: LBTSReferra... |
| DxStatusResult | bigint |  |  | SI | Dimension: DxStatusResult
Expression: %expression... |
| DxTestSet | bigint |  |  | SI | Dimension: DxTestSet<br/>
Source: LBTSTestSetDR.L... |
| DxTurnaroundTime | bigint |  |  | SI | Dimension: DxTurnaroundTime<br/>
Source: LBTSTurn... |
| DxTurnaroundTimeFail | bigint |  |  | SI | Dimension: DxTurnaroundTimeFail
Expression: %expr... |
| DxTurnaroundTimeFlag | bigint |  |  | SI | Dimension: DxTurnaroundTimeFlag
Expression: %expr... |
| DxTurnaroundTimeSlot | bigint |  |  | SI | Dimension: DxTurnaroundTimeSlot<br/>
Source: LBTS... |
| DxUserName | bigint |  |  | SI | Dimension: DxUserName<br/>
Source: LBTSAuthorised... |
| MxNumberIT | double |  |  | SI | Measure: MxNumberIT
Expression: %source.LBTSTurna... |
| MxNumberTTFail | double |  |  | SI | Measure: MxNumberTTFail
Expression: (%source.LBTS... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*