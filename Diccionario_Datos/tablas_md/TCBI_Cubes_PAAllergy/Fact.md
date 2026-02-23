# TCBI_Cubes_PAAllergy.Fact

**Schema:** TCBI_Cubes_PAAllergy
**Columnas:** 25
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx4225490394 | varchar |  |  | SI | Dimension: Dx4225490394<br/>
Source: ALGOnsetDate |
| Dx647357237 | varchar |  |  | SI | Dimension: Dx647357237<br/>
Source: ALGOnsetDate |
| DxALGOnsetDate | date |  |  | SI | Dimension: DxALGOnsetDate<br/>
Source: ALGOnsetDa... |
| DxALGOnsetDateFxMonthNumber | varchar |  |  | SI | Dimension: DxALGOnsetDateFxMonthNumber<br/>
Sourc... |
| DxALGOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxALGOnsetDateFxMonthYear<br/>
Source:... |
| DxALGOnsetDateFxQuarterYear | varchar |  |  | SI | Dimension: DxALGOnsetDateFxQuarterYear<br/>
Sourc... |
| DxALGOnsetDateFxYear | varchar |  |  | SI | Dimension: DxALGOnsetDateFxYear<br/>
Source: ALGO... |
| DxAllergyCategoryDescription | bigint |  |  | SI | Dimension: DxAllergyCategoryDescription<br/>
Sour... |
| DxAllergyCertainty | bigint |  |  | SI | Dimension: DxAllergyCertainty
Expression: "source... |
| DxAllergyCertaintyCode | bigint |  |  | SI | Dimension: DxAllergyCertaintyCode
Expression: "so... |
| DxAllergyDescription | bigint |  |  | SI | Dimension: DxAllergyDescription
Expression: %cube... |
| DxAllergyGroup | bigint |  |  | SI | Dimension: DxAllergyGroup<br/>
Source: ALGAllergy... |
| DxAllergyReaction | bigint |  |  | SI | Dimension: DxAllergyReaction<br/>
Source: ALGCate... |
| DxAllergySeverity | bigint |  |  | SI | Dimension: DxAllergySeverity<br/>
Source: ALGSeve... |
| DxAllergyStatus | bigint |  |  | SI | Dimension: DxAllergyStatus
Expression: %cube.GetA... |
| DxAllergyTag | bigint |  |  | SI | Dimension: DxAllergyTag<br/>
Source: ALGMRCAllTyp... |
| DxAllergyType | bigint |  |  | SI | Dimension: DxAllergyType<br/>
Source: ALGMRCAllTy... |
| DxChangeReason | bigint |  |  | SI | Dimension: DxChangeReason<br/>
Source: ALGReasFor... |
| DxDiagnosingCareProvider | bigint |  |  | SI | Dimension: DxDiagnosingCareProvider
Expression: "... |
| DxErrorReason | bigint |  |  | SI | Dimension: DxErrorReason<br/>
Source: ALGErrorRea... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: ALGPAPMIParRe... |
| RxIDViaALGPAPMIParRef | bigint |  |  | SI | Relationship: RxIDViaALGPAPMIParRef<br/>
Source: ... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*