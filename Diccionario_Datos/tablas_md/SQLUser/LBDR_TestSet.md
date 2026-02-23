# SQLUser.LBDR_TestSet

**Schema:** SQLUser
**Columnas:** 74
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio DR**. Referencias de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBDRTS_ParRef | varchar | PK |  | NO | Parent Reference LBDRSection DR |
| LBDRTSRNP_ReportableMessage | varchar |  |  | SI | Report message
If the TestSetRevision could not b... |
| LBDRTS_AccreditationLegend | varchar |  |  | SI | Accreditation Legend |
| LBDRTS_BloodProduct_DR | bigint |  | FK | SI | Blood Product Table
The table for Blood Product C... |
| LBDRTS_CTestSet_DR | bigint |  | FK | SI | The TestSet (Code table) |
| LBDRTS_Comments_DR | bigint |  | FK | SI | TestSetRevision Comments to be printed.
HMLRichTe... |
| LBDRTS_CustomLayout | varchar |  |  | SI | Custom Report Layout
This property indicates that... |
| LBDRTS_DFT_DR | bigint |  | FK | SI | Dynamic Function Test (DFT) Table |
| LBDRTS_DepartmentCode | varchar |  |  | SI | Department Code (for readability)
For the TestSet... |
| LBDRTS_EnteredDate | varchar |  |  | SI | Date when Test Set Status was set to Entered |
| LBDRTS_EnteredTime | varchar |  |  | SI | Time when Test Set Status was set to Entered |
| LBDRTS_EnteredUser | varchar |  |  | SI | User who Entered the Test Set |
| LBDRTS_EnteredUser_DR | bigint |  | FK | SI | Entered User Reference |
| LBDRTS_HCumulative_DR | bigint |  | FK | SI | Details for the Horizontal TestSet Cumulative (if ... |
| LBDRTS_InterpretationText_DR | bigint |  | FK | SI | Interpretation to be printed. HTML document (OTHER... |
| LBDRTS_Label | varchar |  |  | SI | The label text to print on the report for the Test... |
| LBDRTS_Legend_DR | bigint |  | FK | SI | Legend Table
Tha table containing a Legend (if an... |
| LBDRTS_LinkEpisode | bigint |  |  | SI | For a linked (slave) TestSet, this record contains... |
| LBDRTS_LinkTestSet | varchar |  |  | SI | Linking Test Set (Master)
The LBDRTestSet Id to t... |
| LBDRTS_LinkTestSets | varchar |  |  | SI | Linking Test Sets (Slaves)
A list of LBDRTestSet ... |
| LBDRTS_MultiDisplayOrder | double |  |  | SI | Multi Display Order |
| LBDRTS_Pathogens_DR | bigint |  | FK | SI | Pathogen Table
The table listing the antibiotics ... |
| LBDRTS_PerformedAtRefLab | varchar |  |  | SI | Performed at (Reference Laboratory) Desc |
| LBDRTS_PerformedAtRefLabIndicator | varchar |  |  | SI | Indicator for Performed At Ref Lab |
| LBDRTS_PrintSeparatePage | varchar |  |  | SI | Print New Page
Start a new page in the Doctors Re... |
| LBDRTS_PrintSequence | double |  |  | NO | Print Sequence
Sort key 1
The Testset or WorkGro... |
| LBDRTS_Priority | varchar |  |  | SI | Test Set Priority Description |
| LBDRTS_ReasonNotPerformed_DR | bigint |  | FK | SI | If test could not be performed this dr links a cod... |
| LBDRTS_ReceivedDate | varchar |  |  | SI | Date when Test Set Status was set to Received |
| LBDRTS_ReceivedTime | varchar |  |  | SI | Time when Test Set Status was set to Received |
| LBDRTS_ReceivedUser | varchar |  |  | SI | User who Received the Test Set |
| LBDRTS_ReceivedUser_DR | bigint |  | FK | SI | Received User Reference |
| LBDRTS_ReportGroupCode | varchar |  |  | SI | ReportGroup Code (for readability)
For the TestSe... |
| LBDRTS_ReportRequest_DR | bigint |  | FK | SI | The ReportRequest for this TestSet
Some TestSetRe... |
| LBDRTS_RevisionCode | varchar |  |  | SI | Revision Code
TestSetCode#RevisionNumber |
| LBDRTS_RowID | varchar |  |  | NO | - |
| LBDRTS_SNOMED_DR | bigint |  | FK | SI | SNOMED Table
The table listing the SNOMED terms a... |
| LBDRTS_SpecimenDescriptions | varchar |  |  | SI | SpecimenDescriptions
List of the Full Specimen De... |
| LBDRTS_Specimens | varchar |  |  | SI | Specimens
String containing Specimens involved in... |
| LBDRTS_StatusDate | varchar |  |  | SI | Status Date
The date (external format) when the t... |
| LBDRTS_StatusDateTime | varchar |  |  | SI | Status Date and Time
The date and time (external ... |
| LBDRTS_StatusResult | varchar |  |  | SI | The ResultStatus of the Testset when it was added ... |
| LBDRTS_StatusSentence | varchar |  |  | SI | Status Sentence
The complete sentence explaining ... |
| LBDRTS_StatusText | varchar |  |  | SI | Status Text
The text to include in the TestSet He... |
| LBDRTS_StatusTime | varchar |  |  | SI | Status Time
The time (external format) when the t... |
| LBDRTS_StatusUser | varchar |  |  | SI | Status User
The user (Name) who approved the test... |
| LBDRTS_StatusUser_DR | bigint |  | FK | SI | Status User Reference |
| LBDRTS_SuppressMethod | varchar |  |  | SI | Suppress Test Method in Result Block |
| LBDRTS_TestMethods | varchar |  |  | SI | Test Methods |
| LBDRTS_TestSetCode | varchar |  |  | SI | TestSet Code
Sort key 3
The (code-table) code fo... |
| LBDRTS_TestSetDesc | varchar |  |  | SI | TestSet Desc (LBCTSRDesc)
HTMLTextBox
For a Work... |
| LBDRTS_TestSetFooterClass | varchar |  |  | SI | TestSet Footer Zen Report
The Zen Report which cr... |
| LBDRTS_TestSetFooterExtraText | varchar |  |  | SI | TestSet Footer Extra Text
Extra Text to add to th... |
| LBDRTS_TestSetHeaderClass | varchar |  |  | SI | TestSet Header Zen Report
The Zen Report which cr... |
| LBDRTS_TestSetHeaderExtraText | varchar |  |  | SI | TestSet Header Extra Text
Extra Text to add to th... |
| LBDRTS_TestSetSeq | integer |  |  | NO | TestSet Sequence
Sort key 4
The sequence (occurr... |
| LBDRTS_TestSet_DR | bigint |  | FK | SI | The TestSet (Transactional) |
| LBDRTS_VCumulative_DR | bigint |  | FK | SI | Details for the Vertical TestSet Cumulative (if an... |
| LBDRTS_ValidatedDate | varchar |  |  | SI | Date when Test Set passed first Verification queue |
| LBDRTS_ValidatedTime | varchar |  |  | SI | Time when Test Set passed first Verification queue |
| LBDRTS_ValidatedUser | varchar |  |  | SI | User who Validated the Test Set |
| LBDRTS_ValidatedUser_DR | bigint |  | FK | SI | Validated User Reference |
| LBDRTS_WGCumulative_DR | bigint |  | FK | SI | Details for the WorkGroup Cumulative (if any) |
| LBDRTS_WGFooter | varchar |  |  | SI | The Footer (if any) to appear after the Data and C... |
| LBDRTS_WGHeader | varchar |  |  | SI | The Header (if any) to appear after the Column Hea... |
| LBDRTS_WorkGroupCode | varchar |  |  | SI | WorkGroup Code (for readability)
For the TestSetR... |
| LBDRTS_WorkGroupCodeSort | varchar |  |  | SI | WorkGroup Code or Slave Number
Sort key 2
The co... |
| LBDRTS_WorkGroupFirst_DR | varchar |  | FK | SI | WorkGroup First DR
The record containing full det... |
| LBDRTS_WorkGroup_DR | bigint |  | FK | SI | WorkGroup DR
The WorkGroup (if any) under which t... |
| Q80Q1 | - |  |  | SI | Área |
| Q80Q2 | - |  |  | SI | Resultado |
| Q80Q3 | - |  |  | SI | Observaciones |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*