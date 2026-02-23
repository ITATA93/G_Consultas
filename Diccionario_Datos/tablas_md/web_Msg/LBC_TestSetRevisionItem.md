# web_Msg.LBC_TestSetRevisionItem

**Schema:** web_Msg
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTSRI_Billable | varchar |  |  | SI | Billable |
| LBCTSRI_BloodGroupStatus | varchar |  |  | SI | Resulting blood group status
Only applicable for ... |
| LBCTSRI_Bold | varchar |  |  | SI | Bold on Doctor Report |
| LBCTSRI_CalcAllRefResultsRequired | varchar |  |  | SI | Flag to indicate if calculation is only executed i... |
| LBCTSRI_CalcAlways | varchar |  |  | SI | Flag to indicate if calculation is always executed... |
| LBCTSRI_CalcFormula | varchar |  |  | SI | Test Set Item is Reportable
Default 'Y'
Calculat... |
| LBCTSRI_CalcIncludeNumCodes | varchar |  |  | SI | Flag to indicate if numeric codes should be consid... |
| LBCTSRI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTSRI_CodedResultSeparator | varchar |  |  | SI | Multi Coded Result Separator |
| LBCTSRI_Column | integer |  |  | SI | The number of the column the Test Item is displaye... |
| LBCTSRI_IgnoreSigIfDeltaCheckPass | varchar |  |  | SI | Ignore Significant Result if Delta Check Passes |
| LBCTSRI_Italic | varchar |  |  | SI | Italics on Doctor Report |
| LBCTSRI_ManualInstrumentSchedule | varchar |  |  | SI | Manual Instrument Schedule
Do not schedule this t... |
| LBCTSRI_Materials | varchar |  |  | SI | Perform on material
If set this test set item wil... |
| LBCTSRI_ParRef | bigint |  |  | SI | Parent TestSet DR
Required by User.LBCTestSetRevi... |
| LBCTSRI_PlotByDefault | varchar |  |  | SI | Plot on graph by default
Flag to indicate if the ... |
| LBCTSRI_PlotByDefaultForDocRpt | varchar |  |  | SI | Plot on graph by default For Doctor Report
Flag t... |
| LBCTSRI_PrintSequence | double |  |  | SI | Report Sequence
Sequence of the TestItem within t... |
| LBCTSRI_ReportPosition | varchar |  |  | SI | Report Position |
| LBCTSRI_Reportable | varchar |  |  | SI | - |
| LBCTSRI_Required | varchar |  |  | SI | Required: 'Yes' if the TestItem must be present in... |
| LBCTSRI_RowID | varchar |  |  | SI | - |
| LBCTSRI_Sequence | double |  |  | SI | Sequence
Sequence of the TestItem within the Test... |
| LBCTSRI_ShareResult | varchar |  |  | SI | Share Result
Share Result with all test set items... |
| LBCTSRI_SignificantResultEval | varchar |  |  | SI | Significant Result Evaluation  |
| LBCTSRI_TestItem_DR | bigint |  | FK | SI | TestItem
Required by User.LBCTestSetRevisionItem. |
| LBCTSRI_TextResultTemplate_DR | bigint |  | FK | SI | The text result template used if the test item is ... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*