# TCBI_Cubes_MRPresentIllness.Fact

**Schema:** TCBI_Cubes_MRPresentIllness
**Columnas:** 28
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1249674668 | varchar |  |  | SI | Dimension: Dx1249674668<br/>
Source: PRESIDateOns... |
| Dx1963815173 | varchar |  |  | SI | Dimension: Dx1963815173<br/>
Source: PRESIDateOns... |
| Dx2543349439 | varchar |  |  | SI | Dimension: Dx2543349439<br/>
Source: PRESIEndDate |
| Dx2581893974 | varchar |  |  | SI | Dimension: Dx2581893974<br/>
Source: PRESIDateOns... |
| Dx338209166 | varchar |  |  | SI | Dimension: Dx338209166<br/>
Source: PRESIDateOnse... |
| Dx455161169 | varchar |  |  | SI | Dimension: Dx455161169<br/>
Source: PRESIEndDate |
| DxBodyPart | bigint |  |  | SI | Dimension: DxBodyPart<br/>
Source: PRESIBodyParts... |
| DxCategory | bigint |  |  | SI | Dimension: DxCategory<br/>
Source: PRESICategoryD... |
| DxDiagnosisCode | bigint |  |  | SI | Dimension: DxDiagnosisCode<br/>
Source: PRESIICDC... |
| DxDiagnosisDescription | bigint |  |  | SI | Dimension: DxDiagnosisDescription
Expression: %so... |
| DxDiagnosisName | bigint |  |  | SI | Dimension: DxDiagnosisName
Expression: %expressio... |
| DxPRESIDateOnset | date |  |  | SI | Dimension: DxPRESIDateOnset<br/>
Source: PRESIDat... |
| DxPRESIDateOnsetFxMonthYear | varchar |  |  | SI | Dimension: DxPRESIDateOnsetFxMonthYear<br/>
Sourc... |
| DxPRESIDateOnsetFxYear | varchar |  |  | SI | Dimension: DxPRESIDateOnsetFxYear<br/>
Source: PR... |
| DxPRESIEndDate | date |  |  | SI | Dimension: DxPRESIEndDate<br/>
Source: PRESIEndDa... |
| DxPRESIEndDateFxMonthNumber | varchar |  |  | SI | Dimension: DxPRESIEndDateFxMonthNumber<br/>
Sourc... |
| DxPRESIEndDateFxMonthYear | varchar |  |  | SI | Dimension: DxPRESIEndDateFxMonthYear<br/>
Source:... |
| DxPRESIEndDateFxQuarterYear | varchar |  |  | SI | Dimension: DxPRESIEndDateFxQuarterYear<br/>
Sourc... |
| DxPRESIEndDateFxYear | varchar |  |  | SI | Dimension: DxPRESIEndDateFxYear<br/>
Source: PRES... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: PRESIParRef.M... |
| DxSnomedTerm | bigint |  |  | SI | Dimension: DxSnomedTerm<br/>
Source: PRESISnomedT... |
| DxStatus | bigint |  |  | SI | Dimension: DxStatus<br/>
Source: PRESIDiagnosStat... |
| DxSubSymptom | bigint |  |  | SI | Dimension: DxSubSymptom<br/>
Source: PRESIBodyPar... |
| DxSymptom | bigint |  |  | SI | Dimension: DxSymptom<br/>
Source: PRESIBodyPartsS... |
| Rx1031195976 | bigint |  |  | SI | Relationship: Rx1031195976<br/>
Source: PRESIParR... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*