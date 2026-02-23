# web_Msg.LBC_TestItem

**Schema:** web_Msg
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCTI_AdditionalBloodGroupSystem_DR | bigint |  | FK | SI | Additional Blood Group System
This property will ... |
| LBCTI_AllowedCodedResults | varchar |  |  | SI | Allowed Coded Results (for Numeric Type) |
| LBCTI_AntibodyScreenOutcome | varchar |  |  | SI | Antibody Screen Outcome
Marks the test item as an... |
| LBCTI_Code | varchar |  |  | SI | Code
Required by User.LBCTestItem. |
| LBCTI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTI_ConditionalDecimals | integer |  |  | SI | Conditional Decimals Places |
| LBCTI_ConditionalDecimalsOperator | varchar |  |  | SI | Conditional Decimals Places Operator |
| LBCTI_ConditionalDecimalsValue | varchar |  |  | SI | Conditional Decimals Places Value |
| LBCTI_CreatedDate | date |  |  | SI | Created Date |
| LBCTI_CreatedTime | time |  |  | SI | Created Time |
| LBCTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTI_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTI_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTI_Decimals | integer |  |  | SI | Default Decimal Places |
| LBCTI_Desc | varchar |  |  | SI | Description
HTMLTextBox
Uses SQLUPPER Collation ... |
| LBCTI_IncludeInCumulative | varchar |  |  | SI | Include in Cumulative report |
| LBCTI_Owner | varchar |  |  | SI | Owner |
| LBCTI_ResultType_DR | bigint |  | FK | SI | Result Type
Required by User.LBCTestItem. |
| LBCTI_RowID | varchar |  |  | SI | - |
| LBCTI_Units_DR | bigint |  | FK | SI | Units of Measurement |
| LBCTI_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTI_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCTI_UseForAKIAlert | varchar |  |  | SI | Creatinine result used to calculate AKI alerts
Ma... |
| LBCTI_UseLabSiteAccreditation | varchar |  |  | SI | Use Lab Site Accreditation  |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*