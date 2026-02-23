# TCDS_Cubes_RBAppointment.Fact

**Schema:** TCDS_Cubes_RBAppointment
**Columnas:** 82
**Actualizado:** 2026-01-30 15:31:58

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | varchar |  |  | SI | Reference to original data in source table. |
| Dx1449093771 | varchar |  |  | SI | Dimension: Dx1449093771<br/>
Source: APPTDepartur... |
| Dx1456811492 | varchar |  |  | SI | Dimension: Dx1456811492<br/>
Source: APPTDepartur... |
| Dx1556085375 | varchar |  |  | SI | Dimension: Dx1556085375<br/>
Source: APPTDepartur... |
| Dx1948848218 | varchar |  |  | SI | Dimension: Dx1948848218<br/>
Source: APPTASParRef... |
| Dx2160787049 | varchar |  |  | SI | Dimension: Dx2160787049<br/>
Source: APPTArrivalD... |
| Dx2561636775 | varchar |  |  | SI | Dimension: Dx2561636775<br/>
Source: APPTArrivalD... |
| Dx2617453957 | varchar |  |  | SI | Dimension: Dx2617453957<br/>
Source: APPTASParRef... |
| Dx3292164250 | varchar |  |  | SI | Dimension: Dx3292164250<br/>
Source: APPTASParRef... |
| Dx3416429272 | varchar |  |  | SI | Dimension: Dx3416429272<br/>
Source: APPTASParRef... |
| Dx3444066568 | varchar |  |  | SI | Dimension: Dx3444066568<br/>
Source: APPTArrivalD... |
| Dx3783616395 | varchar |  |  | SI | Dimension: Dx3783616395<br/>
Source: APPTASParRef... |
| Dx684954313 | varchar |  |  | SI | Dimension: Dx684954313<br/>
Source: APPTASParRef.... |
| DxAPPTArrivalDate | date |  |  | SI | Dimension: DxAPPTArrivalDate<br/>
Source: APPTArr... |
| DxAPPTArrivalDateFxYear | varchar |  |  | SI | Dimension: DxAPPTArrivalDateFxYear<br/>
Source: A... |
| DxAPPTDepartureDate | date |  |  | SI | Dimension: DxAPPTDepartureDate<br/>
Source: APPTD... |
| DxAPPTDepartureDateFxYear | varchar |  |  | SI | Dimension: DxAPPTDepartureDateFxYear<br/>
Source:... |
| DxAPPTFollowUpApptDate | bigint |  |  | SI | Dimension: DxAPPTFollowUpApptDate<br/>
Source: AP... |
| DxASDateViaAPPTASParRef | date |  |  | SI | Dimension: DxASDateViaAPPTASParRef<br/>
Source: A... |
| DxAge | bigint |  |  | SI | Dimension: DxAge
Expression: %cube.CalculateAge(%... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup
Expression: %cube.Calculate... |
| DxAppointmentAccountClass | bigint |  |  | SI | Dimension: DxAppointmentAccountClass
Expression: ... |
| DxAppointmentDayOfWeek | bigint |  |  | SI | Dimension: DxAppointmentDayOfWeek
Expression: %ex... |
| DxAppointmentHospital | bigint |  |  | SI | Dimension: DxAppointmentHospital<br/>
Source: APP... |
| DxAppointmentInsuranceCategory | bigint |  |  | SI | Dimension: DxAppointmentInsuranceCategory
Express... |
| DxAppointmentLocation | bigint |  |  | SI | Dimension: DxAppointmentLocation<br/>
Source: APP... |
| DxAppointmentMethod | bigint |  |  | SI | Dimension: DxAppointmentMethod<br/>
Source: APPTM... |
| DxAppointmentPayor | bigint |  |  | SI | Dimension: DxAppointmentPayor
Expression: "source... |
| DxAppointmentPayorCode | bigint |  |  | SI | Dimension: DxAppointmentPayorCode
Expression: "so... |
| DxAppointmentPlan | bigint |  |  | SI | Dimension: DxAppointmentPlan
Expression: "sourceA... |
| DxAppointmentPlanCode | bigint |  |  | SI | Dimension: DxAppointmentPlanCode
Expression: "sou... |
| DxAppointmentStartTime | bigint |  |  | SI | Dimension: DxAppointmentStartTime<br/>
Source: AP... |
| DxAppointmentStatus | bigint |  |  | SI | Dimension: DxAppointmentStatus
Expression: %expre... |
| DxAppointmentToArriveTime | bigint |  |  | SI | Dimension: DxAppointmentToArriveTime
Expression: ... |
| DxAppointmentToSeenTime | bigint |  |  | SI | Dimension: DxAppointmentToSeenTime
Expression: ##... |
| DxAppointmentType | bigint |  |  | SI | Dimension: DxAppointmentType<br/>
Source: APPTATD... |
| DxArrivalTime | bigint |  |  | SI | Dimension: DxArrivalTime<br/>
Source: APPTArrival... |
| DxArrivalTimeRange | bigint |  |  | SI | Dimension: DxArrivalTimeRange
Expression: %source... |
| DxArriveToDepartTime | bigint |  |  | SI | Dimension: DxArriveToDepartTime
Expression: ##cla... |
| DxArriveToSeenTime | bigint |  |  | SI | Dimension: DxArriveToSeenTime
Expression: ##class... |
| DxBookedByUser | bigint |  |  | SI | Dimension: DxBookedByUser
Expression: "sourceBook... |
| DxBookingToAppointmentDays | bigint |  |  | SI | Dimension: DxBookingToAppointmentDays
Expression:... |
| DxBookingType | bigint |  |  | SI | Dimension: DxBookingType<br/>
Source: APPTAdmDR.P... |
| DxClinicName | bigint |  |  | SI | Dimension: DxClinicName<br/>
Source: APPTASParRef... |
| DxClinicPhone | bigint |  |  | SI | Dimension: DxClinicPhone<br/>
Source: APPTASParRe... |
| DxConfirmedDate | bigint |  |  | SI | Dimension: DxConfirmedDate<br/>
Source: APPTConfi... |
| DxContactDeliveryMode | bigint |  |  | SI | Dimension: DxContactDeliveryMode<br/>
Source: APP... |
| DxContactSessionType | bigint |  |  | SI | Dimension: DxContactSessionType<br/>
Source: APPT... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: APPTPAPMID... |
| DxDepartedTime | bigint |  |  | SI | Dimension: DxDepartedTime<br/>
Source: APPTDepart... |
| DxFirstAppointmentFlag | bigint |  |  | SI | Dimension: DxFirstAppointmentFlag
Expression: "so... |
| DxFundingCategoryDepartment | bigint |  |  | SI | Dimension: DxFundingCategoryDepartment
Expression... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: APPTStat... |
| DxInterpreterRequired | bigint |  |  | SI | Dimension: DxInterpreterRequired<br/>
Source: APP... |
| DxLastStatusChangeHospital | bigint |  |  | SI | Dimension: DxLastStatusChangeHospital
Expression:... |
| DxLastStatusChangeUser | bigint |  |  | SI | Dimension: DxLastStatusChangeUser
Expression: "so... |
| DxOutcomeOfAppointment | bigint |  |  | SI | Dimension: DxOutcomeOfAppointment<br/>
Source: AP... |
| DxPrimaryCareProvider | bigint |  |  | SI | Dimension: DxPrimaryCareProvider
Expression: "sou... |
| DxPrimaryCareProviderType | bigint |  |  | SI | Dimension: DxPrimaryCareProviderType
Expression: ... |
| DxReasonForCancel | bigint |  |  | SI | Dimension: DxReasonForCancel<br/>
Source: APPTRea... |
| DxReasonForNoShow | bigint |  |  | SI | Dimension: DxReasonForNoShow<br/>
Source: APPTRea... |
| DxReasonForOverbook | bigint |  |  | SI | Dimension: DxReasonForOverbook<br/>
Source: APPTR... |
| DxReasonForTransfer | bigint |  |  | SI | Dimension: DxReasonForTransfer<br/>
Source: APPTR... |
| DxResource | bigint |  |  | SI | Dimension: DxResource<br/>
Source: APPTASParRef.A... |
| DxRoom | bigint |  |  | SI | Dimension: DxRoom<br/>
Source: APPTASParRef.ASRBE... |
| DxRoomPhone | bigint |  |  | SI | Dimension: DxRoomPhone<br/>
Source: APPTASParRef.... |
| DxSecondaryCareProvider | bigint |  |  | SI | Dimension: DxSecondaryCareProvider<br/>
Source: A... |
| DxSecondaryCareProviderType | bigint |  |  | SI | Dimension: DxSecondaryCareProviderType
Expression... |
| DxSeenByCareProvider | bigint |  |  | SI | Dimension: DxSeenByCareProvider<br/>
Source: APPT... |
| DxSeenToDepartTime | bigint |  |  | SI | Dimension: DxSeenToDepartTime
Expression: ##class... |
| DxService | bigint |  |  | SI | Dimension: DxService<br/>
Source: APPTRBCServDR.S... |
| DxServiceGroup | bigint |  |  | SI | Dimension: DxServiceGroup<br/>
Source: APPTRBCSer... |
| DxSourceOfAttendance | bigint |  |  | SI | Dimension: DxSourceOfAttendance<br/>
Source: APPT... |
| DxTransportRequired | bigint |  |  | SI | Dimension: DxTransportRequired<br/>
Source: APPTT... |
| DxTransportType | bigint |  |  | SI | Dimension: DxTransportType<br/>
Source: APPTTrans... |
| DxWaitListStatus | bigint |  |  | SI | Dimension: DxWaitListStatus<br/>
Source: APPTWait... |
| DxWaitListType | bigint |  |  | SI | Dimension: DxWaitListType<br/>
Source: APPTWaitLi... |
| MxTotalConsultationTime | double |  |  | SI | Measure: MxTotalConsultationTime
Expression: ##cl... |
| MxTotalPatientJourneyTime | double |  |  | SI | Measure: MxTotalPatientJourneyTime
Expression: ##... |
| MxTotalSeenWaitTime | double |  |  | SI | Measure: MxTotalSeenWaitTime
Expression: ##class(... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*