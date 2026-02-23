# websys.Report

> Report Interface Definition

**Schema:** websys
**Columnas:** 58
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Report Interface Definition

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Code | varchar |  |  | SI | Code which uniquely identifies a report |
| ConsentQuestionnaire | bigint |  |  | SI | Consent Questionnaire to be associated when printi... |
| DSN | varchar |  |  | SI | - |
| Description | varchar |  |  | SI | Brief Description of the report |
| DoNotSaveHistory | bit |  |  | SI | - |
| DocSigningAllow | bit |  |  | SI | When previewed, the report allows user to add sign... |
| DocSigningUID | varchar |  |  | SI | Stores delimited 9 pieces of P1-P9 which determine... |
| Expression | varchar |  |  | SI | Pre-processing expression |
| Hospital | bigint |  |  | SI | - |
| IsQuestionnaireTemplate | bit |  |  | SI |  indicates this is the report that prints z ZEN re... |
| JReportCatalog | varchar |  |  | SI | Jreport Catalog |
| JReportEncoding | varchar |  |  | SI | JReport Encoding code used to generate report |
| LongDescription | varchar |  |  | SI | - |
| NoOfCopies | integer |  |  | SI | Number of copies to be printed by default |
| OutputFormat | varchar |  |  | SI | Output format for the Report |
| Owner | varchar |  |  | SI | Owner - Standard type "EditionOwnerType" |
| P1 | varchar |  |  | SI | - |
| P1Name | varchar |  |  | SI | - |
| P2 | varchar |  |  | SI | - |
| P2Name | varchar |  |  | SI | - |
| P3 | varchar |  |  | SI | - |
| P3Name | varchar |  |  | SI | - |
| P4 | varchar |  |  | SI | - |
| P4Name | varchar |  |  | SI | - |
| P5 | varchar |  |  | SI | - |
| P5Name | varchar |  |  | SI | - |
| P6 | varchar |  |  | SI | - |
| P6Name | varchar |  |  | SI | - |
| P7 | varchar |  |  | SI | - |
| P7Name | varchar |  |  | SI | - |
| P8 | varchar |  |  | SI | - |
| P8Name | varchar |  |  | SI | - |
| P9 | varchar |  |  | SI | - |
| P9Name | varchar |  |  | SI | - |
| ParameterComponent | bigint |  |  | SI | Component for page to capture report parameter.
U... |
| ParameterUrl | varchar |  |  | SI | Url for page to capture report parameter. |
| PreventUnsignedEntryTR | bit |  |  | SI | Do not show unsigned entry for the text result |
| PrintDescriptionExpression | varchar |  |  | SI | Expression to calculate Print description in websy... |
| PrintPriority | varchar |  |  | SI | - |
| Printer | bigint |  |  | SI | - |
| ReportClass | varchar |  |  | SI | - |
| ReportDisabled | bit |  |  | SI | ab 28.03.06 45135 |
| ReportGroup | bigint |  |  | SI | - |
| ReportIsAuditLetter | bit |  |  | SI | - |
| ReportUrl | varchar |  |  | SI | - |
| RunLinkedReport | varchar |  |  | SI | When checked, run Linked JReport when generating r... |
| SaveToDatabase | bit |  |  | SI | - |
| SaveToFile | bit |  |  | SI | - |
| SaveToFilePathExpression | varchar |  |  | SI | - |
| Type | varchar |  |  | SI | - |
| UpdateDate | date |  |  | SI | - |
| UpdateTime | time |  |  | SI | - |
| UpdateUser | bigint |  |  | SI | - |
| ZenDirectPrint | bit |  |  | SI | - |
| ZenSplitMerge | bit |  |  | SI | When checked, Zen report will be split for pdf gen... |
| ZenSplitMergeElement | varchar |  |  | SI | Element that determines where the report will be s... |
| ZenSplitMergeElementCount | integer |  |  | SI | Number of instances of the element that occur in e... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*