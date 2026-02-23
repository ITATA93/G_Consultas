# TCDS_Cubes_MRDiagnos_Version73.Fact

**Schema:** TCDS_Cubes_MRDiagnos_Version73
**Columnas:** 43
**Actualizado:** 2026-01-30 15:31:08

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1886916646 | date |  |  | SI | Dimension: Dx1886916646
Expression: %source.MRDIA... |
| Dx2119229136 | varchar |  |  | SI | Dimension: Dx2119229136<br/>
Source: MRDIADateDia... |
| Dx269761494 | varchar |  |  | SI | Dimension: Dx269761494<br/>
Source: MRDIADateDiag... |
| Dx3471246055 | varchar |  |  | SI | Dimension: Dx3471246055<br/>
Source: MRDIADateDia... |
| Dx3695229796 | varchar |  |  | SI | Dimension: Dx3695229796<br/>
Source: MRDIADateDia... |
| DxBillingGroup | bigint |  |  | SI | Dimension: DxBillingGroup
Expression: "sourceBill... |
| DxBillingSubGroup1 | bigint |  |  | SI | Dimension: DxBillingSubGroup1
Expression: "source... |
| DxBillingSubGroup2 | bigint |  |  | SI | Dimension: DxBillingSubGroup2
Expression: "source... |
| DxDSSEffectiveDate | varchar |  |  | SI | Dimension: DxDSSEffectiveDate |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: MRDIAMRADM... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: MRDIAMRADM... |
| DxDeletionReason | bigint |  |  | SI | Dimension: DxDeletionReason<br/>
Source: MRDIADel... |
| DxDiagnosingCareProvider | bigint |  |  | SI | Dimension: DxDiagnosingCareProvider<br/>
Source: ... |
| DxDiagnosisCode | bigint |  |  | SI | Dimension: DxDiagnosisCode<br/>
Source: MRDIAICDC... |
| DxDiagnosisDescription | bigint |  |  | SI | Dimension: DxDiagnosisDescription<br/>
Source: MR... |
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
| DxIdentifiedTime | bigint |  |  | SI | Dimension: DxIdentifiedTime<br/>
Source: MRDIATim... |
| DxIsActive | bigint |  |  | SI | Dimension: DxIsActive<br/>
Source: MRDIAActive |
| DxIsApproximate | bigint |  |  | SI | Dimension: DxIsApproximate<br/>
Source: MRDIAAppr... |
| DxLymphaticInvasion | bigint |  |  | SI | Dimension: DxLymphaticInvasion
Expression: "sourc... |
| DxLymphaticNode | bigint |  |  | SI | Dimension: DxLymphaticNode
Expression: "sourceLym... |
| DxMRDIADate | date |  |  | SI | Dimension: DxMRDIADate<br/>
Source: MRDIADate |
| DxMRDIADateDiagnosisIdentif | date |  |  | SI | Dimension: DxMRDIADateDiagnosisIdentif<br/>
Sourc... |
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
| DxMalignantGrade | bigint |  |  | SI | Dimension: DxMalignantGrade
Expression: "sourceMa... |
| DxPrimaryDiagnosisGroup | bigint |  |  | SI | Dimension: DxPrimaryDiagnosisGroup
Expression: "s... |
| DxPrimaryTumourSite | bigint |  |  | SI | Dimension: DxPrimaryTumourSite
Expression: "sourc... |
| DxSecondaryDiagnosisGroup | bigint |  |  | SI | Dimension: DxSecondaryDiagnosisGroup
Expression: ... |
| DxStage | bigint |  |  | SI | Dimension: DxStage<br/>
Source: MRDIAStagesDR.STG... |
| DxStageClassification | bigint |  |  | SI | Dimension: DxStageClassification<br/>
Source: MRD... |
| DxTumour | bigint |  |  | SI | Dimension: DxTumour<br/>
Source: MRDIATumourDR.TU... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*