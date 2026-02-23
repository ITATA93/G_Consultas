# TCBI_Cubes_OEOrdItem.Fact

**Schema:** TCBI_Cubes_OEOrdItem
**Columnas:** 100
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1071910542 | varchar |  |  | SI | Dimension: Dx1071910542 |
| Dx1364899999 | varchar |  |  | SI | Dimension: Dx1364899999<br/>
Source: OEORIDateExe... |
| Dx1434985399 | varchar |  |  | SI | Dimension: Dx1434985399<br/>
Source: OEORIARPBLIt... |
| Dx144490795 | varchar |  |  | SI | Dimension: Dx144490795<br/>
Source: OEORIARPBLIte... |
| Dx1599580982 | varchar |  |  | SI | Dimension: Dx1599580982 |
| Dx1994240894 | date |  |  | SI | Dimension: Dx1994240894<br/>
Source: OEORIARPBLIt... |
| Dx2040040218 | varchar |  |  | SI | Dimension: Dx2040040218<br/>
Source: OEORIARPBLIt... |
| Dx2244958179 | varchar |  |  | SI | Dimension: Dx2244958179<br/>
Source: OEORISttDat |
| Dx2250374594 | varchar |  |  | SI | Dimension: Dx2250374594 |
| Dx2308600660 | varchar |  |  | SI | Dimension: Dx2308600660<br/>
Source: OEORIDateExe... |
| Dx2367914818 | varchar |  |  | SI | Dimension: Dx2367914818 |
| Dx2408431888 | varchar |  |  | SI | Dimension: Dx2408431888 |
| Dx249269792 | varchar |  |  | SI | Dimension: Dx249269792 |
| Dx2571627996 | date |  |  | SI | Dimension: Dx2571627996
Expression: %cube.GetAppr... |
| Dx2626089973 | varchar |  |  | SI | Dimension: Dx2626089973 |
| Dx2800103966 | varchar |  |  | SI | Dimension: Dx2800103966 |
| Dx3110191588 | varchar |  |  | SI | Dimension: Dx3110191588<br/>
Source: OEORIARPBLIt... |
| Dx3540905181 | varchar |  |  | SI | Dimension: Dx3540905181 |
| Dx3628078376 | varchar |  |  | SI | Dimension: Dx3628078376<br/>
Source: OEORIDateExe... |
| Dx3660373000 | varchar |  |  | SI | Dimension: Dx3660373000 |
| Dx3794955379 | varchar |  |  | SI | Dimension: Dx3794955379 |
| Dx3851994559 | date |  |  | SI | Dimension: Dx3851994559
Expression: %cube.GetAppr... |
| Dx434788811 | varchar |  |  | SI | Dimension: Dx434788811<br/>
Source: OEORIARPBLIte... |
| Dx52136756 | varchar |  |  | SI | Dimension: Dx52136756 |
| Dx545904463 | varchar |  |  | SI | Dimension: Dx545904463<br/>
Source: OEORIDateExec... |
| Dx828898940 | varchar |  |  | SI | Dimension: Dx828898940<br/>
Source: OEORIARPBLIte... |
| Dx883554171 | varchar |  |  | SI | Dimension: Dx883554171<br/>
Source: OEORIDateExec... |
| DxApprovalBatchStatus | bigint |  |  | SI | Dimension: DxApprovalBatchStatus
Expression: %cub... |
| DxApprovalRejectionReason | bigint |  |  | SI | Dimension: DxApprovalRejectionReason
Expression: ... |
| DxApprovalRequestType | bigint |  |  | SI | Dimension: DxApprovalRequestType
Expression: %cub... |
| DxApprovalSource | bigint |  |  | SI | Dimension: DxApprovalSource
Expression: %cube.Get... |
| DxExecuteDayOfWeek | bigint |  |  | SI | Dimension: DxExecuteDayOfWeek
Expression: $system... |
| DxExecuteTimeRange | bigint |  |  | SI | Dimension: DxExecuteTimeRange
Expression: %source... |
| DxExecutingCareProvider | bigint |  |  | SI | Dimension: DxExecutingCareProvider<br/>
Source: O... |
| DxExecutingCareProviderType | bigint |  |  | SI | Dimension: DxExecutingCareProviderType<br/>
Sourc... |
| DxInternalRadiologyStatus | bigint |  |  | SI | Dimension: DxInternalRadiologyStatus<br/>
Source:... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: OEORIIte... |
| DxInternalType | bigint |  |  | SI | Dimension: DxInternalType<br/>
Source: OEORIItmMa... |
| DxIsCollected | bigint |  |  | SI | Dimension: DxIsCollected
Expression: %cube.IsColl... |
| DxIsRead | bigint |  |  | SI | Dimension: DxIsRead
Expression: %cube.IsRead(%sou... |
| DxMealType | bigint |  |  | SI | Dimension: DxMealType<br/>
Source: OEORIMealTypeD... |
| DxNationalCode | bigint |  |  | SI | Dimension: DxNationalCode
Expression: $lg(%expres... |
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
Expression: $system.S... |
| DxOrderDescription | bigint |  |  | SI | Dimension: DxOrderDescription
Expression: %source... |
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
| DxOrderSubCategoryCode | bigint |  |  | SI | Dimension: DxOrderSubCategoryCode<br/>
Source: OE... |
| DxOrderType | bigint |  |  | SI | Dimension: DxOrderType
Expression: %expression.Or... |
| DxOrderingCareProvider | bigint |  |  | SI | Dimension: DxOrderingCareProvider<br/>
Source: OE... |
| DxOrderingCareProviderType | bigint |  |  | SI | Dimension: DxOrderingCareProviderType<br/>
Source... |
| DxOrderingDepartmentGroup | bigint |  |  | SI | Dimension: DxOrderingDepartmentGroup<br/>
Source:... |
| DxOrderingHospital | bigint |  |  | SI | Dimension: DxOrderingHospital<br/>
Source: OEORIO... |
| DxOrderingHospitalCode | bigint |  |  | SI | Dimension: DxOrderingHospitalCode<br/>
Source: OE... |
| DxOrderingLocation | bigint |  |  | SI | Dimension: DxOrderingLocation<br/>
Source: OEORIO... |
| DxOrderingLocationCode | bigint |  |  | SI | Dimension: DxOrderingLocationCode<br/>
Source: OE... |
| DxOrderingTrust | bigint |  |  | SI | Dimension: DxOrderingTrust
Expression: %expressio... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: OEORIOEORDPar... |
| DxRadiologyStatus | bigint |  |  | SI | Dimension: DxRadiologyStatus
Expression: %express... |
| DxReasonForRefund | bigint |  |  | SI | Dimension: DxReasonForRefund<br/>
Source: OEORIRe... |
| DxReceivingInpatientUnit | bigint |  |  | SI | Dimension: DxReceivingInpatientUnit
Expression: %... |
| DxReceivingLocation | bigint |  |  | SI | Dimension: DxReceivingLocation<br/>
Source: OEORI... |
| DxReceivingLocationCode | bigint |  |  | SI | Dimension: DxReceivingLocationCode<br/>
Source: O... |
| DxReceivingLocationHospital | bigint |  |  | SI | Dimension: DxReceivingLocationHospital<br/>
Sourc... |
| DxReceivingLocationHospitalCode | bigint |  |  | SI | Dimension: DxReceivingLocationHospitalCode<br/>
S... |
| DxReceivingOutpatientUnit | bigint |  |  | SI | Dimension: DxReceivingOutpatientUnit
Expression: ... |
| DxReceivingTrust | bigint |  |  | SI | Dimension: DxReceivingTrust
Expression: %expressi... |
| DxReferralClinic | bigint |  |  | SI | Dimension: DxReferralClinic<br/>
Source: OEORIRef... |
| DxReferralDoctor | bigint |  |  | SI | Dimension: DxReferralDoctor<br/>
Source: OEORIRef... |
| DxRequestStatus | bigint |  |  | SI | Dimension: DxRequestStatus
Expression: %cube.GetA... |
| DxStartToExecutedTime | bigint |  |  | SI | Dimension: DxStartToExecutedTime
Expression: ##cl... |
| DxePrescOverrideReason | bigint |  |  | SI | Dimension: DxePrescOverrideReason<br/>
Source: OE... |
| DxePrescStatus | bigint |  |  | SI | Dimension: DxePrescStatus<br/>
Source: OEORIOEOrd... |
| MxItemCost | double |  |  | SI | Measure: MxItemCost
Expression: %cube.GetItmCost(... |
| MxItemRevenue | double |  |  | SI | Measure: MxItemRevenue
Expression: %cube.GetItmPr... |
| MxOrderSet | double |  |  | SI | Measure: MxOrderSet
Expression: $S(%source.OEORIO... |
| MxWaitingTimeTotal | double |  |  | SI | Measure: MxWaitingTimeTotal
Expression: ##class(T... |
| Rx1753220819 | bigint |  |  | SI | Relationship: Rx1753220819<br/>
Source: OEORIOEOr... |
| Rx3747508390 | bigint |  |  | SI | Relationship: Rx3747508390
Expression: %cube.GetP... |
| Rx59125920 | bigint |  |  | SI | Relationship: Rx59125920
Expression: %cube.GetGro... |
| Rx818000209 | bigint |  |  | SI | Relationship: Rx818000209<br/>
Source: OEORIOEORD... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*