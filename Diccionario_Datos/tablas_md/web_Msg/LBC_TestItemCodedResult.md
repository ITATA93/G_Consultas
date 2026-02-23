# web_Msg.LBC_TestItemCodedResult

**Schema:** web_Msg
**Columnas:** 21
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTICR_ClinicalReviewFlag | varchar |  |  | SI | Flag to indicate clinical review |
| LBCTICR_Code | varchar |  |  | SI | Code 
Exception for collation to allow + and - si... |
| LBCTICR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTICR_DateFrom | date |  |  | SI | Effective date for the record
Required by User.LB... |
| LBCTICR_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTICR_DefaultSnomedTerms | varchar |  |  | SI | List of default snomed codes (will be copied to th... |
| LBCTICR_Desc | varchar |  |  | SI | Description
Exception for collation to allow + an... |
| LBCTICR_ExcludeFromElectronicIssue | varchar |  |  | SI |  Exclude From Electronic Issue |
| LBCTICR_ImplicitValue | varchar |  |  | SI | Implicit value
Only available for antibody screen |
| LBCTICR_InfectionReport | varchar |  |  | SI | Infection Report |
| LBCTICR_InfectionReportTime | time |  |  | SI | Infection Report Time |
| LBCTICR_NotPerformed | varchar |  |  | SI | Not Performed Flag |
| LBCTICR_ParRef | bigint |  |  | SI | The Test Item the Standard Code can be selected fo... |
| LBCTICR_RangeFlag | varchar |  |  | SI | Flag to indicate if range is normal, abnormal or b... |
| LBCTICR_RowID | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*