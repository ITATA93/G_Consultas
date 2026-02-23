# TCDS_Cubes_PAAllergy.Fact

**Schema:** TCDS_Cubes_PAAllergy
**Columnas:** 25
**Actualizado:** 2026-01-30 15:31:33

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

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
| DxALGDate | date |  |  | SI | Dimension: DxALGDate<br/>
Source: ALGDate |
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
| DxAllergyDescription | bigint |  |  | SI | Dimension: DxAllergyDescription
Expression: %expr... |
| DxAllergyGroup | bigint |  |  | SI | Dimension: DxAllergyGroup<br/>
Source: ALGAllergy... |
| DxAllergyReaction | bigint |  |  | SI | Dimension: DxAllergyReaction<br/>
Source: ALGCate... |
| DxAllergyReactionCode | bigint |  |  | SI | Dimension: DxAllergyReactionCode
Expression: "sou... |
| DxAllergySeverity | bigint |  |  | SI | Dimension: DxAllergySeverity<br/>
Source: ALGSeve... |
| DxAllergySeverityCode | bigint |  |  | SI | Dimension: DxAllergySeverityCode
Expression: "sou... |
| DxAllergyStatus | bigint |  |  | SI | Dimension: DxAllergyStatus
Expression: %expressio... |
| DxAllergyTag | bigint |  |  | SI | Dimension: DxAllergyTag<br/>
Source: ALGMRCAllTyp... |
| DxAllergyType | bigint |  |  | SI | Dimension: DxAllergyType<br/>
Source: ALGMRCAllTy... |
| DxChangeReason | bigint |  |  | SI | Dimension: DxChangeReason<br/>
Source: ALGReasFor... |
| DxDSSEffectiveDate | varchar |  |  | SI | Dimension: DxDSSEffectiveDate<br/>
Source: ALGDat... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: ALGPAPMIPa... |
| DxErrorReason | bigint |  |  | SI | Dimension: DxErrorReason
Expression: "sourceError... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*