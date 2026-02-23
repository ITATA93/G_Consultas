# Tools_Upload.TU_TaskDefinition

**Schema:** Tools_Upload
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| TUTD_CSTClass | varchar |  |  | SI | If Custom Region Class is derived from Tools.Uploa... |
| TUTD_CSTExport | varchar |  |  | SI | - |
| TUTD_CSTImport | varchar |  |  | SI | - |
| TUTD_CSTLoadFile | varchar |  |  | SI | - |
| TUTD_CSTPostCleanup | varchar |  |  | SI | - |
| TUTD_CSTPreCleanup | varchar |  |  | SI | - |
| TUTD_CSTSimulate | varchar |  |  | SI | - |
| TUTD_CSTSingle | varchar |  |  | SI | - |
| TUTD_CSTValidate | varchar |  |  | SI | Regional / Custom Method Calls |
| TUTD_CSTValidateFile | varchar |  |  | SI | - |
| TUTD_CSVDelimiter | varchar |  |  | SI | For CSV Import the Delimiter 
STDType: "CSVDelimi... |
| TUTD_CSVonServer | varchar |  |  | SI | FileName on Server for CSV Export (delimiter as co... |
| TUTD_CaptionRowNumber | integer |  |  | SI | Caption Row Number (default and min 1)  |
| TUTD_Code | varchar |  |  | NO | - |
| TUTD_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| TUTD_CreateDate | date |  |  | SI | - |
| TUTD_CreateTime | time |  |  | SI | - |
| TUTD_Description | varchar |  |  | NO | - |
| TUTD_FirstDataRowNumber | integer |  |  | SI | First Data Row Number (default and min 2)  |
| TUTD_FreezeDate | date |  |  | SI | used to compare if a new freeze is required  |
| TUTD_FreezeForCode | varchar |  |  | SI | Reference to the original Task (just Code)  |
| TUTD_FreezeTime | time |  |  | SI | used to compare if a new freeze is required  |
| TUTD_FreezeVersion | integer |  |  | SI | To keep freezed copies this flag indicates a "used... |
| TUTD_FromDate | date |  |  | SI | - |
| TUTD_Owner | varchar |  |  | SI | Owner |
| TUTD_PreSelClass | varchar |  |  | SI | Class to derive the SQL Table  |
| TUTD_PreSelColumns | varchar |  |  | SI | Select columns List  |
| TUTD_PreSelName | varchar |  |  | SI | SQL like task properties
Named pre-select |
| TUTD_SupportedActions | varchar |  |  | SI | Supported Actions |
| TUTD_ToDate | date |  |  | SI | - |
| TUTD_UpdDate | date |  |  | SI | - |
| TUTD_UpdTime | time |  |  | SI | - |
| TUTD_UploadType | varchar |  |  | NO | STDType: "UploadTypes"  |
| TUTD_WorkbookFilter | varchar |  |  | SI | For Excel Import a startswith string to Filter for... |
| TUTD_WorkbookGlobal | varchar |  |  | SI | For Excel Import a KEY for Global can be defined, ... |
| TUTD_XDataValidation | varchar |  |  | SI | For Excel / CSV Import Validation a XData can be d... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*