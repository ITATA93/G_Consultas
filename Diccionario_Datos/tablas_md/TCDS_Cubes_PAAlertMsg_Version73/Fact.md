# TCDS_Cubes_PAAlertMsg_Version73.Fact

**Schema:** TCDS_Cubes_PAAlertMsg_Version73
**Columnas:** 40
**Actualizado:** 2026-01-30 15:31:32

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1742667116 | varchar |  |  | SI | Dimension: Dx1742667116<br/>
Source: ALMCreateDat... |
| Dx1929850753 | varchar |  |  | SI | Dimension: Dx1929850753<br/>
Source: ALMReviewDat... |
| Dx2335645503 | varchar |  |  | SI | Dimension: Dx2335645503<br/>
Source: ALMCreateDat... |
| Dx2571149850 | varchar |  |  | SI | Dimension: Dx2571149850<br/>
Source: ALMReviewDat... |
| Dx2599966431 | varchar |  |  | SI | Dimension: Dx2599966431<br/>
Source: ALMOnsetDate |
| Dx2683227602 | varchar |  |  | SI | Dimension: Dx2683227602<br/>
Source: ALMReviewDat... |
| Dx2787506372 | varchar |  |  | SI | Dimension: Dx2787506372<br/>
Source: ALMClosedDat... |
| Dx3310818236 | varchar |  |  | SI | Dimension: Dx3310818236<br/>
Source: ALMClosedDat... |
| Dx3704037491 | varchar |  |  | SI | Dimension: Dx3704037491<br/>
Source: ALMClosedDat... |
| Dx4042075499 | varchar |  |  | SI | Dimension: Dx4042075499<br/>
Source: ALMOnsetDate |
| Dx4277921001 | varchar |  |  | SI | Dimension: Dx4277921001<br/>
Source: ALMReviewDat... |
| Dx441288858 | varchar |  |  | SI | Dimension: Dx441288858<br/>
Source: ALMCreateDate |
| Dx542417918 | varchar |  |  | SI | Dimension: Dx542417918<br/>
Source: ALMCreateDate |
| Dx700379631 | varchar |  |  | SI | Dimension: Dx700379631<br/>
Source: ALMClosedDate |
| DxALMClosedDate | date |  |  | SI | Dimension: DxALMClosedDate<br/>
Source: ALMClosed... |
| DxALMClosedDateFxMonthYear | varchar |  |  | SI | Dimension: DxALMClosedDateFxMonthYear<br/>
Source... |
| DxALMClosedDateFxYear | varchar |  |  | SI | Dimension: DxALMClosedDateFxYear<br/>
Source: ALM... |
| DxALMCreateDate | date |  |  | SI | Dimension: DxALMCreateDate<br/>
Source: ALMCreate... |
| DxALMCreateDateFxMonthYear | varchar |  |  | SI | Dimension: DxALMCreateDateFxMonthYear<br/>
Source... |
| DxALMCreateDateFxYear | varchar |  |  | SI | Dimension: DxALMCreateDateFxYear<br/>
Source: ALM... |
| DxALMOnsetDate | date |  |  | SI | Dimension: DxALMOnsetDate<br/>
Source: ALMOnsetDa... |
| DxALMOnsetDateFxMonthNumber | varchar |  |  | SI | Dimension: DxALMOnsetDateFxMonthNumber<br/>
Sourc... |
| DxALMOnsetDateFxMonthYear | varchar |  |  | SI | Dimension: DxALMOnsetDateFxMonthYear<br/>
Source:... |
| DxALMOnsetDateFxQuarterYear | varchar |  |  | SI | Dimension: DxALMOnsetDateFxQuarterYear<br/>
Sourc... |
| DxALMOnsetDateFxYear | varchar |  |  | SI | Dimension: DxALMOnsetDateFxYear<br/>
Source: ALMO... |
| DxALMReviewDate | date |  |  | SI | Dimension: DxALMReviewDate<br/>
Source: ALMReview... |
| DxALMReviewDateFxMonthYear | varchar |  |  | SI | Dimension: DxALMReviewDateFxMonthYear<br/>
Source... |
| DxALMReviewDateFxYear | varchar |  |  | SI | Dimension: DxALMReviewDateFxYear<br/>
Source: ALM... |
| DxAlertCategory | bigint |  |  | SI | Dimension: DxAlertCategory<br/>
Source: ALMAlertC... |
| DxAlertDescription | bigint |  |  | SI | Dimension: DxAlertDescription<br/>
Source: ALMAle... |
| DxAlertStatus | bigint |  |  | SI | Dimension: DxAlertStatus
Expression: %expression.... |
| DxClosedFlag | bigint |  |  | SI | Dimension: DxClosedFlag<br/>
Source: ALMClosedFla... |
| DxCreateHospital | bigint |  |  | SI | Dimension: DxCreateHospital<br/>
Source: ALMCreat... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: ALMPAPMIPa... |
| DxErrorReason | bigint |  |  | SI | Dimension: DxErrorReason
Expression: "sourceError... |
| DxExpiryReason | bigint |  |  | SI | Dimension: DxExpiryReason
Expression: "sourceExpi... |
| DxSourceOfAlert | bigint |  |  | SI | Dimension: DxSourceOfAlert
Expression: "sourceSou... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*