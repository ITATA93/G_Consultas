# TCBI_Cubes_PADischargeSummaryReferral.Fact

**Schema:** TCBI_Cubes_PADischargeSummaryReferral
**Columnas:** 24
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1538818175 | varchar |  |  | SI | Dimension: Dx1538818175<br/>
Source: REFERStartDa... |
| Dx2156517135 | varchar |  |  | SI | Dimension: Dx2156517135<br/>
Source: REFERStartDa... |
| Dx3129265240 | bigint |  |  | SI | Dimension: Dx3129265240<br/>
Source: REFERPrescri... |
| Dx3594465525 | varchar |  |  | SI | Dimension: Dx3594465525<br/>
Source: REFERStartDa... |
| Dx987157158 | varchar |  |  | SI | Dimension: Dx987157158<br/>
Source: REFERStartDat... |
| DxARCIMDescViaREFERARCIMDR | bigint |  | FK | SI | Dimension: DxARCIMDescViaREFERARCIMDR<br/>
Source... |
| DxDiagnosticProblem | bigint |  |  | SI | Dimension: DxDiagnosticProblem<br/>
Source: REFER... |
| DxDuration | bigint |  |  | SI | Dimension: DxDuration<br/>
Source: REFERDurationD... |
| DxFrequency | bigint |  |  | SI | Dimension: DxFrequency<br/>
Source: REFERFreqDR.P... |
| DxPayor | bigint |  |  | SI | Dimension: DxPayor<br/>
Source: REFERPayorDR.INST... |
| DxPlan | bigint |  |  | SI | Dimension: DxPlan<br/>
Source: REFERPlanDR.AUXITD... |
| DxPriority | bigint |  |  | SI | Dimension: DxPriority<br/>
Source: REFERPriorityD... |
| DxREFERStartDate | date |  |  | SI | Dimension: DxREFERStartDate<br/>
Source: REFERSta... |
| DxREFERStartDateFxMonthYear | varchar |  |  | SI | Dimension: DxREFERStartDateFxMonthYear<br/>
Sourc... |
| DxREFERStartDateFxYear | varchar |  |  | SI | Dimension: DxREFERStartDateFxYear<br/>
Source: RE... |
| DxReferralCategory | bigint |  |  | SI | Dimension: DxReferralCategory<br/>
Source: REFERR... |
| DxReferralMethod | bigint |  |  | SI | Dimension: DxReferralMethod<br/>
Source: REFERRef... |
| DxReferralPriority | bigint |  |  | SI | Dimension: DxReferralPriority<br/>
Source: REFERR... |
| DxReferralStatus | bigint |  |  | SI | Dimension: DxReferralStatus<br/>
Source: REFERRef... |
| DxReferralType | bigint |  |  | SI | Dimension: DxReferralType<br/>
Source: REFERRefer... |
| Rx109889049 | bigint |  |  | SI | Relationship: Rx109889049
Expression: %cube.GetGr... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*