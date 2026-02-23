# TCBI_Cubes_Questionnaire_QTCBR.Fact

**Schema:** TCBI_Cubes_Questionnaire_QTCBR
**Columnas:** 71
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| AdmissionDoctorID | bigint |  |  | SI | Dimension: AdmissionDoctorID<br/>
Source: QUESPAA... |
| DSSEffectiveDate | varchar |  |  | SI | Dimension: DSSEffectiveDate |
| DXEPISODEID | bigint |  |  | SI | Dimension: DXEPISODEID<br/>
Source: QUESPAAdmDR.%... |
| DXPatientID | bigint |  |  | SI | Dimension: DXPatientID<br/>
Source: QUESPAPatMasD... |
| Dx1184484864 | date |  |  | SI | Dimension: Dx1184484864
Expression: %source.QUESC... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: QUESPAPatM... |
| DxQ01 | varchar |  |  | SI | Dimension: DxQ01
Expression: $lg(%expression.Comp... |
| DxQ02 | varchar |  |  | SI | Dimension: DxQ02
Expression: $lg(%expression.Comp... |
| DxQ03 | varchar |  |  | SI | Dimension: DxQ03
Expression: $lg(%expression.Comp... |
| DxQ04 | varchar |  |  | SI | Dimension: DxQ04
Expression: $lg(%expression.Comp... |
| DxQ05 | varchar |  |  | SI | Dimension: DxQ05
Expression: $lg(%expression.Comp... |
| DxQ06 | varchar |  |  | SI | Dimension: DxQ06
Expression: $lg(%expression.Comp... |
| DxQ07 | varchar |  |  | SI | Dimension: DxQ07
Expression: $lg(%expression.Comp... |
| DxQ08 | varchar |  |  | SI | Dimension: DxQ08
Expression: $lg(%expression.Comp... |
| DxQ09 | varchar |  |  | SI | Dimension: DxQ09
Expression: $lg(%expression.Comp... |
| DxQ10 | varchar |  |  | SI | Dimension: DxQ10
Expression: $lg(%expression.Comp... |
| DxQ11 | varchar |  |  | SI | Dimension: DxQ11
Expression: $lg(%expression.Comp... |
| DxQ12 | varchar |  |  | SI | Dimension: DxQ12
Expression: $lg(%expression.Comp... |
| DxQ13 | varchar |  |  | SI | Dimension: DxQ13
Expression: $lg(%expression.Comp... |
| DxQ14 | varchar |  |  | SI | Dimension: DxQ14
Expression: $lg(%expression.Comp... |
| DxQ15 | varchar |  |  | SI | Dimension: DxQ15
Expression: $lg(%expression.Comp... |
| DxQ16 | varchar |  |  | SI | Dimension: DxQ16
Expression: $lg(%expression.Comp... |
| DxQ17 | varchar |  |  | SI | Dimension: DxQ17
Expression: $lg(%expression.Comp... |
| DxQ18 | varchar |  |  | SI | Dimension: DxQ18
Expression: $lg(%expression.Comp... |
| DxQ19 | varchar |  |  | SI | Dimension: DxQ19
Expression: $lg(%expression.Comp... |
| DxQ20 | varchar |  |  | SI | Dimension: DxQ20
Expression: $lg(%expression.Comp... |
| DxQ21 | varchar |  |  | SI | Dimension: DxQ21
Expression: $lg(%expression.Comp... |
| DxQ22 | varchar |  |  | SI | Dimension: DxQ22
Expression: $lg(%expression.Comp... |
| DxQ23 | varchar |  |  | SI | Dimension: DxQ23
Expression: $lg(%expression.Comp... |
| DxQ24 | varchar |  |  | SI | Dimension: DxQ24
Expression: $lg(%expression.Comp... |
| DxQ25 | varchar |  |  | SI | Dimension: DxQ25
Expression: $lg(%expression.Comp... |
| DxQ26 | varchar |  |  | SI | Dimension: DxQ26
Expression: $lg(%expression.Comp... |
| DxQ27 | varchar |  |  | SI | Dimension: DxQ27
Expression: $lg(%expression.Comp... |
| DxQ28 | varchar |  |  | SI | Dimension: DxQ28
Expression: $lg(%expression.Comp... |
| DxQ29 | varchar |  |  | SI | Dimension: DxQ29
Expression: $lg(%expression.Comp... |
| DxQ30 | varchar |  |  | SI | Dimension: DxQ30
Expression: $lg(%expression.Comp... |
| DxQ31 | varchar |  |  | SI | Dimension: DxQ31
Expression: $lg(%expression.Comp... |
| DxQ32 | varchar |  |  | SI | Dimension: DxQ32
Expression: $lg(%expression.Comp... |
| DxQ33 | varchar |  |  | SI | Dimension: DxQ33
Expression: $lg(%expression.Comp... |
| DxQ34 | varchar |  |  | SI | Dimension: DxQ34
Expression: $lg(%expression.Comp... |
| DxQ35 | varchar |  |  | SI | Dimension: DxQ35
Expression: $lg(%expression.Comp... |
| DxQ36 | varchar |  |  | SI | Dimension: DxQ36
Expression: $lg(%expression.Comp... |
| DxQ37 | varchar |  |  | SI | Dimension: DxQ37
Expression: $lg(%expression.Comp... |
| DxQ38 | varchar |  |  | SI | Dimension: DxQ38
Expression: $lg(%expression.Comp... |
| DxQ39 | varchar |  |  | SI | Dimension: DxQ39
Expression: $lg(%expression.Comp... |
| DxQ40 | varchar |  |  | SI | Dimension: DxQ40
Expression: $lg(%expression.Comp... |
| DxQ41 | varchar |  |  | SI | Dimension: DxQ41
Expression: $lg(%expression.Comp... |
| DxQ42 | varchar |  |  | SI | Dimension: DxQ42
Expression: $lg(%expression.Comp... |
| DxQ43 | varchar |  |  | SI | Dimension: DxQ43
Expression: $lg(%expression.Comp... |
| DxQ44 | varchar |  |  | SI | Dimension: DxQ44
Expression: $lg(%expression.Comp... |
| DxQ45 | varchar |  |  | SI | Dimension: DxQ45
Expression: $lg(%expression.Comp... |
| DxQUESCreateDate | date |  |  | SI | Dimension: DxQUESCreateDate<br/>
Source: QUESCrea... |
| DxQUESCreateDateDay | varchar |  |  | SI | Dimension: DxQUESCreateDateDay<br/>
Source: QUESC... |
| DxQUESCreateDateMonth | varchar |  |  | SI | Dimension: DxQUESCreateDateMonth<br/>
Source: QUE... |
| DxQUESCreateDateMonthOfYear | varchar |  |  | SI | Dimension: DxQUESCreateDateMonthOfYear<br/>
Sourc... |
| DxQUESCreateDateQuarter | varchar |  |  | SI | Dimension: DxQUESCreateDateQuarter<br/>
Source: Q... |
| DxQUESCreateDateYear | varchar |  |  | SI | Dimension: DxQUESCreateDateYear<br/>
Source: QUES... |
| DxQUESScore | varchar |  |  | SI | Dimension: DxQUESScore<br/>
Source: QUESScore |
| DxQUESStatusDR | varchar |  | FK | SI | Dimension: DxQUESStatusDR
Expression: %expression... |
| Mx1091174330 | double |  |  | SI | Measure: Mx1091174330
Expression: %cube.GetPatien... |
| Mx1981747727 | double |  |  | SI | Measure: Mx1981747727
Expression: %cube.GetEpisod... |
| Mx2487661433 | double |  |  | SI | Measure: Mx2487661433
Expression: %cube.GetEpisod... |
| Mx282617046 | double |  |  | SI | Measure: Mx282617046
Expression: %cube.GetAssIndi... |
| Mx4245437454 | double |  |  | SI | Measure: Mx4245437454
Expression: %cube.GetPatien... |
| Mx832245153 | double |  |  | SI | Measure: Mx832245153
Expression: %cube.GetAssIndi... |
| ReferralDoctorID | bigint |  |  | SI | Dimension: ReferralDoctorID<br/>
Source: QUESPAAd... |
| RxIDViaQUESPAAdmDR | bigint |  | FK | SI | Relationship: RxIDViaQUESPAAdmDR<br/>
Source: QUE... |
| RxIDViaQUESPAPatMasDR | bigint |  | FK | SI | Relationship: RxIDViaQUESPAPatMasDR<br/>
Source: ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*