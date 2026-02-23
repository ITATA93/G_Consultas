# TCBI_Cubes_RBAppointment.Fact

**Schema:** TCBI_Cubes_RBAppointment
**Columnas:** 69
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1347406380 | varchar |  |  | SI | Dimension: Dx1347406380<br/>
Source: APPTBookedDa... |
| Dx1401696568 | varchar |  |  | SI | Dimension: Dx1401696568<br/>
Source: APPTFollowUp... |
| Dx1639756368 | varchar |  |  | SI | Dimension: Dx1639756368<br/>
Source: APPTBookedDa... |
| Dx1740341641 | varchar |  |  | SI | Dimension: Dx1740341641<br/>
Source: APPTFollowUp... |
| Dx1948848218 | varchar |  |  | SI | Dimension: Dx1948848218<br/>
Source: APPTASParRef... |
| Dx2312817449 | varchar |  |  | SI | Dimension: Dx2312817449<br/>
Source: APPTFollowUp... |
| Dx2371178499 | varchar |  |  | SI | Dimension: Dx2371178499<br/>
Source: APPTBookedDa... |
| Dx2617453957 | varchar |  |  | SI | Dimension: Dx2617453957<br/>
Source: APPTASParRef... |
| Dx3202911603 | varchar |  |  | SI | Dimension: Dx3202911603<br/>
Source: APPTFollowUp... |
| Dx3211121515 | varchar |  |  | SI | Dimension: Dx3211121515<br/>
Source: APPTFollowUp... |
| Dx3292164250 | varchar |  |  | SI | Dimension: Dx3292164250<br/>
Source: APPTASParRef... |
| Dx3416429272 | varchar |  |  | SI | Dimension: Dx3416429272<br/>
Source: APPTASParRef... |
| Dx3783616395 | varchar |  |  | SI | Dimension: Dx3783616395<br/>
Source: APPTASParRef... |
| Dx4256388250 | varchar |  |  | SI | Dimension: Dx4256388250<br/>
Source: APPTBookedDa... |
| Dx684954313 | varchar |  |  | SI | Dimension: Dx684954313<br/>
Source: APPTASParRef.... |
| Dx939652540 | varchar |  |  | SI | Dimension: Dx939652540<br/>
Source: APPTFollowUpA... |
| DxAPPTBookedDate | date |  |  | SI | Dimension: DxAPPTBookedDate<br/>
Source: APPTBook... |
| DxAPPTBookedDateFxMonthYear | varchar |  |  | SI | Dimension: DxAPPTBookedDateFxMonthYear<br/>
Sourc... |
| DxAPPTBookedDateFxYear | varchar |  |  | SI | Dimension: DxAPPTBookedDateFxYear<br/>
Source: AP... |
| DxAPPTFollowUpApptDate | date |  |  | SI | Dimension: DxAPPTFollowUpApptDate<br/>
Source: AP... |
| DxASDateViaAPPTASParRef | date |  |  | SI | Dimension: DxASDateViaAPPTASParRef<br/>
Source: A... |
| DxAge | bigint |  |  | SI | Dimension: DxAge
Expression: %cube.CalculateAge(%... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup
Expression: %cube.Calculate... |
| DxAppointmentAccountClass | bigint |  |  | SI | Dimension: DxAppointmentAccountClass<br/>
Source:... |
| DxAppointmentDayOfWeek | bigint |  |  | SI | Dimension: DxAppointmentDayOfWeek
Expression: $sy... |
| DxAppointmentInsuranceCategory | bigint |  |  | SI | Dimension: DxAppointmentInsuranceCategory
Express... |
| DxAppointmentMethod | bigint |  |  | SI | Dimension: DxAppointmentMethod<br/>
Source: APPTM... |
| DxAppointmentPayor | bigint |  |  | SI | Dimension: DxAppointmentPayor
Expression: $lg(%ex... |
| DxAppointmentPayorCode | bigint |  |  | SI | Dimension: DxAppointmentPayorCode
Expression: $lg... |
| DxAppointmentPlan | bigint |  |  | SI | Dimension: DxAppointmentPlan
Expression: $lg(%exp... |
| DxAppointmentPlanCode | bigint |  |  | SI | Dimension: DxAppointmentPlanCode
Expression: $lg(... |
| DxAppointmentStatus | bigint |  |  | SI | Dimension: DxAppointmentStatus
Expression: %cube.... |
| DxAppointmentToArriveTime | bigint |  |  | SI | Dimension: DxAppointmentToArriveTime
Expression: ... |
| DxAppointmentToSeenTime | bigint |  |  | SI | Dimension: DxAppointmentToSeenTime
Expression: ##... |
| DxArrivalTimeRange | bigint |  |  | SI | Dimension: DxArrivalTimeRange
Expression: %source... |
| DxArriveToDepartTime | bigint |  |  | SI | Dimension: DxArriveToDepartTime
Expression: ##cla... |
| DxArriveToSeenTime | bigint |  |  | SI | Dimension: DxArriveToSeenTime
Expression: ##class... |
| DxBookedByUser | bigint |  |  | SI | Dimension: DxBookedByUser
Expression: %expression... |
| DxBookingToAppointmentDays | bigint |  |  | SI | Dimension: DxBookingToAppointmentDays
Expression:... |
| DxBookingType | bigint |  |  | SI | Dimension: DxBookingType<br/>
Source: APPTAdmDR.P... |
| DxConsultationCategory | bigint |  |  | SI | Dimension: DxConsultationCategory<br/>
Source: AP... |
| DxFirstAppointmentFlag | bigint |  |  | SI | Dimension: DxFirstAppointmentFlag
Expression: %cu... |
| DxFollowUpDayofWeek | bigint |  |  | SI | Dimension: DxFollowUpDayofWeek
Expression: ##clas... |
| DxFundingCategoryDepartment | bigint |  |  | SI | Dimension: DxFundingCategoryDepartment<br/>
Sourc... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: APPTStat... |
| DxLastStatusChangeHospital | bigint |  |  | SI | Dimension: DxLastStatusChangeHospital<br/>
Source... |
| DxLastStatusChangeUser | bigint |  |  | SI | Dimension: DxLastStatusChangeUser<br/>
Source: AP... |
| DxOutcomeOfAppointment | bigint |  |  | SI | Dimension: DxOutcomeOfAppointment<br/>
Source: AP... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: APPTPAPMIDR.%... |
| DxReasonForCancel | bigint |  |  | SI | Dimension: DxReasonForCancel<br/>
Source: APPTRea... |
| DxReasonForNoShow | bigint |  |  | SI | Dimension: DxReasonForNoShow<br/>
Source: APPTRea... |
| DxReasonForOverbook | bigint |  |  | SI | Dimension: DxReasonForOverbook<br/>
Source: APPTR... |
| DxReasonForTransfer | bigint |  |  | SI | Dimension: DxReasonForTransfer<br/>
Source: APPTR... |
| DxSecondaryCareProvider | bigint |  |  | SI | Dimension: DxSecondaryCareProvider<br/>
Source: A... |
| DxSecondaryCareProviderType | bigint |  |  | SI | Dimension: DxSecondaryCareProviderType<br/>
Sourc... |
| DxSeenByCareProvider | bigint |  |  | SI | Dimension: DxSeenByCareProvider<br/>
Source: APPT... |
| DxSeenToDepartTime | bigint |  |  | SI | Dimension: DxSeenToDepartTime
Expression: ##class... |
| DxService | bigint |  |  | SI | Dimension: DxService<br/>
Source: APPTRBCServDR.S... |
| DxServiceGroup | bigint |  |  | SI | Dimension: DxServiceGroup<br/>
Source: APPTRBCSer... |
| MxDuration | double |  |  | SI | Measure: MxDuration<br/>
Source: APPTDuration |
| MxNumberNewAppointments | double |  |  | SI | Measure: MxNumberNewAppointments
Expression: %exp... |
| MxTotalConsultationTime | double |  |  | SI | Measure: MxTotalConsultationTime
Expression: ##cl... |
| MxTotalPatientJourneyTime | double |  |  | SI | Measure: MxTotalPatientJourneyTime
Expression: ##... |
| MxTotalSeenWaitTime | double |  |  | SI | Measure: MxTotalSeenWaitTime
Expression: ##class(... |
| RxIDViaAPPTASParRef | bigint |  |  | SI | Relationship: RxIDViaAPPTASParRef<br/>
Source: AP... |
| RxIDViaAPPTAdmDR | bigint |  | FK | SI | Relationship: RxIDViaAPPTAdmDR<br/>
Source: APPTA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*