# TCBI_Cubes_OEOrdExec.Fact

**Schema:** TCBI_Cubes_OEOrdExec
**Columnas:** 36
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1259621401 | varchar |  |  | SI | Dimension: Dx1259621401<br/>
Source: OEOREDateExe... |
| Dx1295179377 | varchar |  |  | SI | Dimension: Dx1295179377<br/>
Source: OEOREExStDat... |
| Dx2564087346 | varchar |  |  | SI | Dimension: Dx2564087346<br/>
Source: OEOREExStDat... |
| Dx2715499554 | varchar |  |  | SI | Dimension: Dx2715499554<br/>
Source: OEOREExStDat... |
| Dx2818420298 | varchar |  |  | SI | Dimension: Dx2818420298<br/>
Source: OEOREDateExe... |
| Dx2985740968 | varchar |  |  | SI | Dimension: Dx2985740968<br/>
Source: OEOREExStDat... |
| Dx4070114640 | varchar |  |  | SI | Dimension: Dx4070114640<br/>
Source: OEOREDateExe... |
| Dx737266643 | varchar |  |  | SI | Dimension: Dx737266643<br/>
Source: OEOREDateExec... |
| Dx848417205 | varchar |  |  | SI | Dimension: Dx848417205<br/>
Source: OEOREDateExec... |
| DxAdministeringProvider | bigint |  |  | SI | Dimension: DxAdministeringProvider<br/>
Source: O... |
| DxAdministrationStatus | bigint |  |  | SI | Dimension: DxAdministrationStatus<br/>
Source: OE... |
| DxAlertReason | bigint |  |  | SI | Dimension: DxAlertReason<br/>
Source: OEOREAlertR... |
| DxMedicationOutcome | bigint |  |  | SI | Dimension: DxMedicationOutcome<br/>
Source: OEORE... |
| DxOEOREDateExecuted | date |  |  | SI | Dimension: DxOEOREDateExecuted<br/>
Source: OEORE... |
| DxOEOREDateExecutedFxYear | varchar |  |  | SI | Dimension: DxOEOREDateExecutedFxYear<br/>
Source:... |
| DxOEOREExStDate | date |  |  | SI | Dimension: DxOEOREExStDate<br/>
Source: OEOREExSt... |
| DxOEOREExStDateFxMonthYear | varchar |  |  | SI | Dimension: DxOEOREExStDateFxMonthYear<br/>
Source... |
| DxOEOREExStDateFxYear | varchar |  |  | SI | Dimension: DxOEOREExStDateFxYear<br/>
Source: OEO... |
| DxOrderCode | bigint |  |  | SI | Dimension: DxOrderCode<br/>
Source: OEOREOEORIPar... |
| DxOrderDescription | bigint |  |  | SI | Dimension: DxOrderDescription
Expression: %source... |
| DxOrderingHospital | bigint |  |  | SI | Dimension: DxOrderingHospital<br/>
Source: OEOREO... |
| DxOrderingHospitalCode | bigint |  |  | SI | Dimension: DxOrderingHospitalCode<br/>
Source: OE... |
| DxOrderingLocation | bigint |  |  | SI | Dimension: DxOrderingLocation<br/>
Source: OEOREO... |
| DxOrderingLocationCode | bigint |  |  | SI | Dimension: DxOrderingLocationCode<br/>
Source: OE... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: OEOREOEORIPar... |
| DxScheduledDayOfWeek | bigint |  |  | SI | Dimension: DxScheduledDayOfWeek
Expression: ##cla... |
| DxScheduledDrugClass | bigint |  |  | SI | Dimension: DxScheduledDrugClass<br/>
Source: OEOR... |
| DxStartDayOfWeek | bigint |  |  | SI | Dimension: DxStartDayOfWeek
Expression: ##class(T... |
| DxStartToExecutedTime | bigint |  |  | SI | Dimension: DxStartToExecutedTime
Expression: ##cl... |
| DxVarianceReason | bigint |  |  | SI | Dimension: DxVarianceReason<br/>
Source: OEOREVar... |
| MxQuantityAdministered | double |  |  | SI | Measure: MxQuantityAdministered
Expression: %sour... |
| MxQuantityAdministeredBaseUOM | double |  |  | SI | Measure: MxQuantityAdministeredBaseUOM
Expression... |
| RxIDViaOEOREOEORIParRef | bigint |  |  | SI | Relationship: RxIDViaOEOREOEORIParRef<br/>
Source... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*