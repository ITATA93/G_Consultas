# TCBI_Cubes_MRDiagnosis.Fact

**Schema:** TCBI_Cubes_MRDiagnosis
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx124482657 | varchar |  |  | SI | Dimension: Dx124482657<br/>
Source: MRDIAOnsetDat... |
| Dx2981641454 | varchar |  |  | SI | Dimension: Dx2981641454<br/>
Source: MRDIAOnsetDa... |
| Dx4012735010 | varchar |  |  | SI | Dimension: Dx4012735010<br/>
Source: MRDIAOnsetDa... |
| Dx63215729 | varchar |  |  | SI | Dimension: Dx63215729<br/>
Source: MRDIAOnsetDate |
| DxBillingSubGroup1 | bigint |  |  | SI | Dimension: DxBillingSubGroup1<br/>
Source: MRDIAI... |
| DxBillingSubGroup2 | bigint |  |  | SI | Dimension: DxBillingSubGroup2<br/>
Source: MRDIAI... |
| DxDiagnosingCareProvider | bigint |  |  | SI | Dimension: DxDiagnosingCareProvider<br/>
Source: ... |
| DxDiagnosisCode | bigint |  |  | SI | Dimension: DxDiagnosisCode<br/>
Source: MRDIAICDC... |
| DxDiagnosisDescription | bigint |  |  | SI | Dimension: DxDiagnosisDescription
Expression: %so... |
| DxDiagnosisName | bigint |  |  | SI | Dimension: DxDiagnosisName
Expression: %expressio... |
| DxDiagnosisSeverity | bigint |  |  | SI | Dimension: DxDiagnosisSeverity<br/>
Source: MRDIA... |
| DxDiagnosisStatus | bigint |  |  | SI | Dimension: DxDiagnosisStatus<br/>
Source: MRDIADi... |
| DxDiagnosisSymptom | bigint |  |  | SI | Dimension: DxDiagnosisSymptom<br/>
Source: MRDIAS... |
| DxDiagnosisType | varchar |  |  | SI | Dimension: DxDiagnosisType
Expression: %expressio... |
| DxLymphaticInvasion | bigint |  |  | SI | Dimension: DxLymphaticInvasion<br/>
Source: MRDIA... |
| DxLymphaticNode | bigint |  |  | SI | Dimension: DxLymphaticNode<br/>
Source: MRDIALymp... |
| DxMRDIADate | date |  |  | SI | Dimension: DxMRDIADate<br/>
Source: MRDIADate |
| DxMRDIADateFxDayMonthYear | varchar |  |  | SI | Dimension: DxMRDIADateFxDayMonthYear<br/>
Source:... |
| DxMRDIADateFxMonthNumber | varchar |  |  | SI | Dimension: DxMRDIADateFxMonthNumber<br/>
Source: ... |
| DxMRDIADateFxMonthYear | varchar |  |  | SI | Dimension: DxMRDIADateFxMonthYear<br/>
Source: MR... |
| DxMRDIADateFxQuarterNumber | varchar |  |  | SI | Dimension: DxMRDIADateFxQuarterNumber<br/>
Source... |
| DxMRDIADateFxQuarterYear | varchar |  |  | SI | Dimension: DxMRDIADateFxQuarterYear<br/>
Source: ... |
| DxMRDIADateFxYear | varchar |  |  | SI | Dimension: DxMRDIADateFxYear<br/>
Source: MRDIADa... |
| DxMRDIAOnsetDate | date |  |  | SI | Dimension: DxMRDIAOnsetDate<br/>
Source: MRDIAOns... |
| DxMRDIAOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxMRDIAOnsetDateFxMonthYear<br/>
Sourc... |
| DxMRDIAOnsetDateFxYear | varchar |  |  | SI | Dimension: DxMRDIAOnsetDateFxYear<br/>
Source: MR... |
| DxMalignantGrade | bigint |  |  | SI | Dimension: DxMalignantGrade<br/>
Source: MRDIAMal... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: MRDIAMRADMPar... |
| DxPrimaryDiagnosisGroup | bigint |  |  | SI | Dimension: DxPrimaryDiagnosisGroup<br/>
Source: M... |
| DxPrimaryTumourSite | bigint |  |  | SI | Dimension: DxPrimaryTumourSite<br/>
Source: MRDIA... |
| DxSecondaryDiagnosisGroup | bigint |  |  | SI | Dimension: DxSecondaryDiagnosisGroup<br/>
Source:... |
| DxStage | bigint |  |  | SI | Dimension: DxStage<br/>
Source: MRDIAStagesDR.STG... |
| DxStageClassification | bigint |  |  | SI | Dimension: DxStageClassification<br/>
Source: MRD... |
| DxTumour | bigint |  |  | SI | Dimension: DxTumour<br/>
Source: MRDIATumourDR.TU... |
| Rx966579485 | bigint |  |  | SI | Relationship: Rx966579485<br/>
Source: MRDIAMRADM... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*