# TCBI_Cubes_PAAdm2GroupNumber.Fact

**Schema:** TCBI_Cubes_PAAdm2GroupNumber
**Columnas:** 31
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| DxCareProvider | bigint |  |  | SI | Dimension: DxCareProvider
Expression: %expression... |
| DxDateFromDay | varchar |  |  | SI | Dimension: DxDateFromDay<br/>
Source: GRPDateFrom |
| DxDateFromDayOfWeek | bigint |  |  | SI | Dimension: DxDateFromDayOfWeek
Expression: $syste... |
| DxDateFromMonth | varchar |  |  | SI | Dimension: DxDateFromMonth<br/>
Source: GRPDateFr... |
| DxDateFromMonthOfYear | varchar |  |  | SI | Dimension: DxDateFromMonthOfYear<br/>
Source: GRP... |
| DxDateFromQuarter | varchar |  |  | SI | Dimension: DxDateFromQuarter<br/>
Source: GRPDate... |
| DxDateFromQuarterOfYear | varchar |  |  | SI | Dimension: DxDateFromQuarterOfYear<br/>
Source: G... |
| DxDateFromYear | varchar |  |  | SI | Dimension: DxDateFromYear<br/>
Source: GRPDateFro... |
| DxDateToDay | varchar |  |  | SI | Dimension: DxDateToDay<br/>
Source: GRPDateTo |
| DxDateToDayOfWeek | bigint |  |  | SI | Dimension: DxDateToDayOfWeek
Expression: "sourceD... |
| DxDateToMonth | varchar |  |  | SI | Dimension: DxDateToMonth<br/>
Source: GRPDateTo |
| DxDateToMonthOfYear | varchar |  |  | SI | Dimension: DxDateToMonthOfYear<br/>
Source: GRPDa... |
| DxDateToQuarter | varchar |  |  | SI | Dimension: DxDateToQuarter<br/>
Source: GRPDateTo |
| DxDateToQuarterOfYear | varchar |  |  | SI | Dimension: DxDateToQuarterOfYear<br/>
Source: GRP... |
| DxDateToYear | varchar |  |  | SI | Dimension: DxDateToYear<br/>
Source: GRPDateTo |
| DxDiagnosis | bigint |  |  | SI | Dimension: DxDiagnosis<br/>
Source: GRPDiagnosisD... |
| DxElectronicPrescriptions | bigint |  |  | SI | Dimension: DxElectronicPrescriptions<br/>
Source:... |
| DxGRPDateFrom | date |  |  | SI | Dimension: DxGRPDateFrom<br/>
Source: GRPDateFrom |
| DxGRPDateTo | date |  |  | SI | Dimension: DxGRPDateTo<br/>
Source: GRPDateTo |
| DxPCPrint | bigint |  |  | SI | Dimension: DxPCPrint<br/>
Source: GRPCode1DR.BILL... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: GRPPayorDR.INSTDe... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: GRPPlanDR.AUXITDes... |
| DxPregnancyProgram | bigint |  |  | SI | Dimension: DxPregnancyProgram<br/>
Source: GRPChe... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: GRPPriorityDR.... |
| DxSessionType | bigint |  |  | SI | Dimension: DxSessionType<br/>
Source: GRPSessionT... |
| DxSuggested | bigint |  |  | SI | Dimension: DxSuggested<br/>
Source: GRPCheckBox1 |
| DxTextDiagnosis | bigint |  |  | SI | Dimension: DxTextDiagnosis<br/>
Source: GRPText1 |
| Rx2932718627 | bigint |  |  | SI | Relationship: Rx2932718627<br/>
Source: GRPParRef... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*