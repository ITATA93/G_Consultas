# TCBI_Cubes_OEOrdTextResult.Fact

**Schema:** TCBI_Cubes_OEOrdTextResult
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1389085188 | date |  |  | SI | Dimension: Dx1389085188
Expression: $li(%expressi... |
| Dx2125698802 | date |  |  | SI | Dimension: Dx2125698802<br/>
Source: TRESOETRDR.T... |
| Dx3666794841 | date |  |  | SI | Dimension: Dx3666794841<br/>
Source: TRESOETRDR.T... |
| Dx637546403 | date |  |  | SI | Dimension: Dx637546403<br/>
Source: TRESOETRDR.TR... |
| DxAbnormalResult | bigint |  |  | SI | Dimension: DxAbnormalResult<br/>
Source: TRESOETR... |
| DxEnteredByCareProvider | bigint |  |  | SI | Dimension: DxEnteredByCareProvider<br/>
Source: T... |
| DxExecutedToVerifiedTime | bigint |  |  | SI | Dimension: DxExecutedToVerifiedTime
Expression: #... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: TRESParRef.OE... |
| DxReadDateDay | varchar |  |  | SI | Dimension: DxReadDateDay<br/>
Source: TRESOETRDR.... |
| DxReadDateMonth | varchar |  |  | SI | Dimension: DxReadDateMonth<br/>
Source: TRESOETRD... |
| DxReadDateMonthOfYear | varchar |  |  | SI | Dimension: DxReadDateMonthOfYear<br/>
Source: TRE... |
| DxReadDateQuarter | varchar |  |  | SI | Dimension: DxReadDateQuarter<br/>
Source: TRESOET... |
| DxReadDateQuarterOfYear | varchar |  |  | SI | Dimension: DxReadDateQuarterOfYear<br/>
Source: T... |
| DxReadDateYear | varchar |  |  | SI | Dimension: DxReadDateYear<br/>
Source: TRESOETRDR... |
| DxReasonSupplementaryResult | bigint |  |  | SI | Dimension: DxReasonSupplementaryResult<br/>
Sourc... |
| DxReportedByCareProvider | bigint |  |  | SI | Dimension: DxReportedByCareProvider<br/>
Source: ... |
| DxResultAction | bigint |  |  | SI | Dimension: DxResultAction<br/>
Source: TRESOETRDR... |
| DxResultCollectedDay | varchar |  |  | SI | Dimension: DxResultCollectedDay |
| DxResultCollectedMonth | varchar |  |  | SI | Dimension: DxResultCollectedMonth |
| DxResultCollectedMonthOfYear | varchar |  |  | SI | Dimension: DxResultCollectedMonthOfYear |
| DxResultCollectedQuarter | varchar |  |  | SI | Dimension: DxResultCollectedQuarter |
| DxResultCollectedQuarterOfYear | varchar |  |  | SI | Dimension: DxResultCollectedQuarterOfYear |
| DxResultCollectedTimeRange | bigint |  |  | SI | Dimension: DxResultCollectedTimeRange
Expression:... |
| DxResultCollectedYear | varchar |  |  | SI | Dimension: DxResultCollectedYear |
| DxResultCreatedDay | varchar |  |  | SI | Dimension: DxResultCreatedDay<br/>
Source: TRESOE... |
| DxResultCreatedMonth | varchar |  |  | SI | Dimension: DxResultCreatedMonth<br/>
Source: TRES... |
| DxResultCreatedMonthOfYear | varchar |  |  | SI | Dimension: DxResultCreatedMonthOfYear<br/>
Source... |
| DxResultCreatedQuarter | varchar |  |  | SI | Dimension: DxResultCreatedQuarter<br/>
Source: TR... |
| DxResultCreatedQuarterOfYear | varchar |  |  | SI | Dimension: DxResultCreatedQuarterOfYear<br/>
Sour... |
| DxResultCreatedTimeRange | bigint |  |  | SI | Dimension: DxResultCreatedTimeRange
Expression: %... |
| DxResultCreatedYear | varchar |  |  | SI | Dimension: DxResultCreatedYear<br/>
Source: TRESO... |
| DxResultStatus | bigint |  |  | SI | Dimension: DxResultStatus<br/>
Source: TRESOETRDR... |
| DxResultTranscribedDay | varchar |  |  | SI | Dimension: DxResultTranscribedDay<br/>
Source: TR... |
| DxResultTranscribedMonth | varchar |  |  | SI | Dimension: DxResultTranscribedMonth<br/>
Source: ... |
| DxResultTranscribedMonthOfYear | varchar |  |  | SI | Dimension: DxResultTranscribedMonthOfYear<br/>
So... |
| DxResultTranscribedQuarter | varchar |  |  | SI | Dimension: DxResultTranscribedQuarter<br/>
Source... |
| DxResultTranscribedQuarterOfYear | varchar |  |  | SI | Dimension: DxResultTranscribedQuarterOfYear<br/>
... |
| DxResultTranscribedTimeRange | bigint |  |  | SI | Dimension: DxResultTranscribedTimeRange<br/>
Sour... |
| DxResultTranscribedYear | varchar |  |  | SI | Dimension: DxResultTranscribedYear<br/>
Source: T... |
| DxResultType | bigint |  |  | SI | Dimension: DxResultType<br/>
Source: TRESOETRDR.T... |
| DxResultVerifiedDay | varchar |  |  | SI | Dimension: DxResultVerifiedDay<br/>
Source: TRESO... |
| DxResultVerifiedMonth | varchar |  |  | SI | Dimension: DxResultVerifiedMonth<br/>
Source: TRE... |
| DxResultVerifiedMonthOfYear | varchar |  |  | SI | Dimension: DxResultVerifiedMonthOfYear<br/>
Sourc... |
| DxResultVerifiedQuarter | varchar |  |  | SI | Dimension: DxResultVerifiedQuarter<br/>
Source: T... |
| DxResultVerifiedQuarterOfYear | varchar |  |  | SI | Dimension: DxResultVerifiedQuarterOfYear<br/>
Sou... |
| DxResultVerifiedTimeRange | bigint |  |  | SI | Dimension: DxResultVerifiedTimeRange<br/>
Source:... |
| DxResultVerifiedYear | varchar |  |  | SI | Dimension: DxResultVerifiedYear<br/>
Source: TRES... |
| DxTRDateReadViaTRESOETRDR | date |  | FK | SI | Dimension: DxTRDateReadViaTRESOETRDR<br/>
Source:... |
| DxTRDateUnreadViaTRESOETRDR | date |  | FK | SI | Dimension: DxTRDateUnreadViaTRESOETRDR<br/>
Sourc... |
| DxTranscribeUser | bigint |  |  | SI | Dimension: DxTranscribeUser<br/>
Source: TRESOETR... |
| DxTranscribed | bigint |  |  | SI | Dimension: DxTranscribed<br/>
Source: TRESOETRDR.... |
| DxUnreadDateDay | varchar |  |  | SI | Dimension: DxUnreadDateDay<br/>
Source: TRESOETRD... |
| DxUnreadDateMonth | varchar |  |  | SI | Dimension: DxUnreadDateMonth<br/>
Source: TRESOET... |
| DxUnreadDateMonthOfYear | varchar |  |  | SI | Dimension: DxUnreadDateMonthOfYear<br/>
Source: T... |
| DxUnreadDateQuarter | varchar |  |  | SI | Dimension: DxUnreadDateQuarter<br/>
Source: TRESO... |
| DxUnreadDateQuarterOfYear | varchar |  |  | SI | Dimension: DxUnreadDateQuarterOfYear<br/>
Source:... |
| DxUnreadDateYear | varchar |  |  | SI | Dimension: DxUnreadDateYear<br/>
Source: TRESOETR... |
| DxUpdateUser | bigint |  |  | SI | Dimension: DxUpdateUser<br/>
Source: TRESOETRDR.T... |
| DxUrgentResult | bigint |  |  | SI | Dimension: DxUrgentResult<br/>
Source: TRESOETRDR... |
| DxVerifiedByCareProvider | bigint |  |  | SI | Dimension: DxVerifiedByCareProvider<br/>
Source: ... |
| DxVerifiedToCollectedTime | bigint |  |  | SI | Dimension: DxVerifiedToCollectedTime
Expression: ... |
| DxVerifiedToReadTime | bigint |  |  | SI | Dimension: DxVerifiedToReadTime
Expression: ##cla... |
| DxVerifiedUser | bigint |  |  | SI | Dimension: DxVerifiedUser<br/>
Source: TRESOETRDR... |
| MxExecutedToVerified | double |  |  | SI | Measure: MxExecutedToVerified
Expression: ##class... |
| MxIsCollected | double |  |  | SI | Measure: MxIsCollected
Expression: $lg(%expressio... |
| MxOrderedToCorrected | double |  |  | SI | Measure: MxOrderedToCorrected
Expression: ##class... |
| MxOrderedToCreated | double |  |  | SI | Measure: MxOrderedToCreated
Expression: ##class(T... |
| MxOrderedToImage | double |  |  | SI | Measure: MxOrderedToImage
Expression: ##class(TCB... |
| MxOrderedToRead | double |  |  | SI | Measure: MxOrderedToRead
Expression: ##class(TCBI... |
| MxOrderedToVerified | double |  |  | SI | Measure: MxOrderedToVerified
Expression: ##class(... |
| MxVerifiedToCollected | double |  |  | SI | Measure: MxVerifiedToCollected
Expression: ##clas... |
| MxVerifiedToRead | double |  |  | SI | Measure: MxVerifiedToRead
Expression: ##class(TCB... |
| RxIDViaTRESParRef | bigint |  |  | SI | Relationship: RxIDViaTRESParRef<br/>
Source: TRES... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*