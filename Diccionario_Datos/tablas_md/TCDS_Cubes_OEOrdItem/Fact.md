# TCDS_Cubes_OEOrdItem.Fact

**Schema:** TCDS_Cubes_OEOrdItem
**Columnas:** 85
**Actualizado:** 2026-01-30 15:31:16

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1364899999 | varchar |  |  | SI | Dimension: Dx1364899999<br/>
Source: OEORIDateExe... |
| Dx2244958179 | varchar |  |  | SI | Dimension: Dx2244958179<br/>
Source: OEORISttDat |
| Dx2308600660 | varchar |  |  | SI | Dimension: Dx2308600660<br/>
Source: OEORIDateExe... |
| Dx3628078376 | varchar |  |  | SI | Dimension: Dx3628078376<br/>
Source: OEORIDateExe... |
| Dx545904463 | varchar |  |  | SI | Dimension: Dx545904463<br/>
Source: OEORIDateExec... |
| Dx883554171 | varchar |  |  | SI | Dimension: Dx883554171<br/>
Source: OEORIDateExec... |
| DxAbnormal | bigint |  |  | SI | Dimension: DxAbnormal<br/>
Source: OEORIAbnormal |
| DxAdminRoute | bigint |  |  | SI | Dimension: DxAdminRoute<br/>
Source: OEORIAdminRo... |
| DxAuthorisingDoctorCode | bigint |  |  | SI | Dimension: DxAuthorisingDoctorCode<br/>
Source: O... |
| DxAuthorisingDoctorDR | bigint |  | FK | SI | Dimension: DxAuthorisingDoctorDR<br/>
Source: OEO... |
| DxAuthorisinggDoctorID | bigint |  |  | SI | Dimension: DxAuthorisinggDoctorID<br/>
Source: OE... |
| DxClassificationScheme | varchar |  |  | SI | Dimension: DxClassificationScheme
Expression: %ex... |
| DxClinicallySignificant | bigint |  |  | SI | Dimension: DxClinicallySignificant
Expression: %e... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: OEORIOEORD... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: OEORIOEORD... |
| DxDispenseType | bigint |  |  | SI | Dimension: DxDispenseType<br/>
Source: OEORIOEOrd... |
| DxDurationDays | bigint |  |  | SI | Dimension: DxDurationDays
Expression: %expression... |
| DxExecuteDayOfWeek | bigint |  |  | SI | Dimension: DxExecuteDayOfWeek
Expression: ##class... |
| DxExecuteTimeRange | bigint |  |  | SI | Dimension: DxExecuteTimeRange
Expression: %source... |
| DxExecutingCareProvider | bigint |  |  | SI | Dimension: DxExecutingCareProvider<br/>
Source: O... |
| DxExecutingCareProviderType | bigint |  |  | SI | Dimension: DxExecutingCareProviderType<br/>
Sourc... |
| DxFormulary | bigint |  |  | SI | Dimension: DxFormulary
Expression: %expression.Fo... |
| DxFrequency | bigint |  |  | SI | Dimension: DxFrequency<br/>
Source: OEORIPHFreqDR... |
| DxFrequencyFactor | bigint |  |  | SI | Dimension: DxFrequencyFactor<br/>
Source: OEORIPH... |
| DxGeneric | bigint |  |  | SI | Dimension: DxGeneric
Expression: %expression.Gene... |
| DxIsCollected | bigint |  |  | SI | Dimension: DxIsCollected
Expression: %expression.... |
| DxIsPRN | bigint |  |  | SI | Dimension: DxIsPRN<br/>
Source: OEORIOEOrdItem2DR... |
| DxIsRead | bigint |  |  | SI | Dimension: DxIsRead
Expression: %expression.IsRea... |
| DxNationalCode | bigint |  |  | SI | Dimension: DxNationalCode
Expression: "sourceNati... |
| DxNationalCodeDescription | bigint |  |  | SI | Dimension: DxNationalCodeDescription
Expression: ... |
| DxOEORIDateExecuted | date |  |  | SI | Dimension: DxOEORIDateExecuted<br/>
Source: OEORI... |
| DxOEORIDateExecutedFxYear | varchar |  |  | SI | Dimension: DxOEORIDateExecutedFxYear<br/>
Source:... |
| DxOEORISttDat | date |  |  | SI | Dimension: DxOEORISttDat<br/>
Source: OEORISttDat |
| DxOEORISttDatFxDayMonthYear | varchar |  |  | SI | Dimension: DxOEORISttDatFxDayMonthYear<br/>
Sourc... |
| DxOEORISttDatFxMonthNumber | varchar |  |  | SI | Dimension: DxOEORISttDatFxMonthNumber<br/>
Source... |
| DxOEORISttDatFxMonthYear | varchar |  |  | SI | Dimension: DxOEORISttDatFxMonthYear<br/>
Source: ... |
| DxOEORISttDatFxQuarterYear | varchar |  |  | SI | Dimension: DxOEORISttDatFxQuarterYear<br/>
Source... |
| DxOEORISttDatFxYear | varchar |  |  | SI | Dimension: DxOEORISttDatFxYear<br/>
Source: OEORI... |
| DxOrderAction | bigint |  |  | SI | Dimension: DxOrderAction<br/>
Source: OEORIAction... |
| DxOrderBillingGroup | bigint |  |  | SI | Dimension: DxOrderBillingGroup<br/>
Source: OEORI... |
| DxOrderBillingSubGroup | bigint |  |  | SI | Dimension: DxOrderBillingSubGroup<br/>
Source: OE... |
| DxOrderCategory | bigint |  |  | SI | Dimension: DxOrderCategory<br/>
Source: OEORIItmM... |
| DxOrderCode | bigint |  |  | SI | Dimension: DxOrderCode<br/>
Source: OEORIItmMastD... |
| DxOrderDayOfWeek | bigint |  |  | SI | Dimension: DxOrderDayOfWeek
Expression: ##class(T... |
| DxOrderDescription | bigint |  |  | SI | Dimension: DxOrderDescription<br/>
Source: OEORII... |
| DxOrderName | bigint |  |  | SI | Dimension: DxOrderName
Expression: %expression.Or... |
| DxOrderPriority | bigint |  |  | SI | Dimension: DxOrderPriority<br/>
Source: OEORIPrio... |
| DxOrderStartTimeRange | bigint |  |  | SI | Dimension: DxOrderStartTimeRange
Expression: %sou... |
| DxOrderStatus | bigint |  |  | SI | Dimension: DxOrderStatus
Expression: %expression.... |
| DxOrderSubCategory | bigint |  |  | SI | Dimension: DxOrderSubCategory<br/>
Source: OEORII... |
| DxOrderSubCategoryCode | bigint |  |  | SI | Dimension: DxOrderSubCategoryCode
Expression: "so... |
| DxOrderType | bigint |  |  | SI | Dimension: DxOrderType
Expression: %expression.Or... |
| DxOrderingCareProvider | bigint |  |  | SI | Dimension: DxOrderingCareProvider<br/>
Source: OE... |
| DxOrderingCareProviderType | bigint |  |  | SI | Dimension: DxOrderingCareProviderType<br/>
Source... |
| DxOrderingDepartment | bigint |  |  | SI | Dimension: DxOrderingDepartment<br/>
Source: OEOR... |
| DxOrderingDepartmentGroup | bigint |  |  | SI | Dimension: DxOrderingDepartmentGroup
Expression: ... |
| DxOrderingDoctorID | bigint |  |  | SI | Dimension: DxOrderingDoctorID<br/>
Source: OEORID... |
| DxOrderingHospital | bigint |  |  | SI | Dimension: DxOrderingHospital<br/>
Source: OEORIO... |
| DxOrderingLocation | bigint |  |  | SI | Dimension: DxOrderingLocation
Expression: "source... |
| DxOrderingLocationCode | bigint |  |  | SI | Dimension: DxOrderingLocationCode
Expression: "so... |
| DxOrderingTrust | bigint |  |  | SI | Dimension: DxOrderingTrust
Expression: "sourceOrd... |
| DxOrderingTrustCode | bigint |  |  | SI | Dimension: DxOrderingTrustCode
Expression: "sourc... |
| DxPRNIndication | bigint |  |  | SI | Dimension: DxPRNIndication<br/>
Source: OEORIPRNI... |
| DxPharmacyCategory | bigint |  |  | SI | Dimension: DxPharmacyCategory
Expression: %expres... |
| DxPharmacySubCategory | bigint |  |  | SI | Dimension: DxPharmacySubCategory
Expression: %exp... |
| DxPhoneOrder | bigint |  |  | SI | Dimension: DxPhoneOrder
Expression: %expression.I... |
| DxPhoneOrderSignedOff | bigint |  |  | SI | Dimension: DxPhoneOrderSignedOff
Expression: %exp... |
| DxPregnancyCheck | bigint |  |  | SI | Dimension: DxPregnancyCheck<br/>
Source: OEORIPre... |
| DxPregnant | bigint |  |  | SI | Dimension: DxPregnant<br/>
Source: OEORIPregnant |
| DxRadiologyStatus | bigint |  |  | SI | Dimension: DxRadiologyStatus
Expression: %express... |
| DxReasonForRefund | bigint |  |  | SI | Dimension: DxReasonForRefund
Expression: "sourceR... |
| DxReceivingInpatientUnit | bigint |  |  | SI | Dimension: DxReceivingInpatientUnit
Expression: "... |
| DxReceivingLocation | bigint |  |  | SI | Dimension: DxReceivingLocation<br/>
Source: OEORI... |
| DxReceivingLocationCode | bigint |  |  | SI | Dimension: DxReceivingLocationCode
Expression: "s... |
| DxReceivingLocationHospital | bigint |  |  | SI | Dimension: DxReceivingLocationHospital<br/>
Sourc... |
| DxReceivingOutpatientUnit | bigint |  |  | SI | Dimension: DxReceivingOutpatientUnit
Expression: ... |
| DxReceivingTrust | bigint |  |  | SI | Dimension: DxReceivingTrust
Expression: "sourceRe... |
| DxReceivingTrustCode | bigint |  |  | SI | Dimension: DxReceivingTrustCode
Expression: "sour... |
| DxReferralClinic | bigint |  |  | SI | Dimension: DxReferralClinic<br/>
Source: OEORIRef... |
| DxReferralDoctor | bigint |  |  | SI | Dimension: DxReferralDoctor<br/>
Source: OEORIRef... |
| DxStartToExecutedTime | bigint |  |  | SI | Dimension: DxStartToExecutedTime
Expression: "sou... |
| MxOrderSet | double |  |  | SI | Measure: MxOrderSet
Expression: $S(%source.OEORIO... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*