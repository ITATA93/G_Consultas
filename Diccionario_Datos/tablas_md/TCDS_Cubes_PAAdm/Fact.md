# TCDS_Cubes_PAAdm.Fact

**Schema:** TCDS_Cubes_PAAdm
**Columnas:** 224
**Actualizado:** 2026-01-30 15:31:26

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1291922942 | varchar |  |  | SI | Dimension: Dx1291922942<br/>
Source: PAADMDischgD... |
| Dx1498567482 | varchar |  |  | SI | Dimension: Dx1498567482<br/>
Source: PAADMPAAdm2D... |
| Dx1741675309 | varchar |  |  | SI | Dimension: Dx1741675309<br/>
Source: PAADMPAAdm2D... |
| Dx1791064300 | varchar |  |  | SI | Dimension: Dx1791064300<br/>
Source: PAADMDischgD... |
| Dx179170796 | varchar |  |  | SI | Dimension: Dx179170796<br/>
Source: PAADMPAAdm2DR... |
| Dx1906299811 | varchar |  |  | SI | Dimension: Dx1906299811<br/>
Source: PAADMEmergen... |
| Dx197633050 | varchar |  |  | SI | Dimension: Dx197633050<br/>
Source: PAADMEmergenc... |
| Dx2334538110 | varchar |  |  | SI | Dimension: Dx2334538110<br/>
Source: PAADMPAAdm2D... |
| Dx2363598713 | bigint |  |  | SI | Dimension: Dx2363598713
Expression: "sourceAdmiss... |
| Dx2476561932 | varchar |  |  | SI | Dimension: Dx2476561932<br/>
Source: PAADMAdmDate |
| Dx2573102766 | varchar |  |  | SI | Dimension: Dx2573102766<br/>
Source: PAADMEmergen... |
| Dx2710781108 | bigint |  |  | SI | Dimension: Dx2710781108
Expression: ##class(TCDS.... |
| Dx274861259 | varchar |  |  | SI | Dimension: Dx274861259<br/>
Source: PAADMRefExpir... |
| Dx2931468779 | varchar |  |  | SI | Dimension: Dx2931468779<br/>
Source: PAADMRefDate |
| Dx307441253 | varchar |  |  | SI | Dimension: Dx307441253<br/>
Source: PAADMEmergenc... |
| Dx3168032988 | varchar |  |  | SI | Dimension: Dx3168032988<br/>
Source: PAADMRefExpi... |
| Dx3327154939 | varchar |  |  | SI | Dimension: Dx3327154939<br/>
Source: PAADMDischgD... |
| Dx3448919731 | varchar |  |  | SI | Dimension: Dx3448919731<br/>
Source: PAADMPAAdm2D... |
| Dx3484502405 | varchar |  |  | SI | Dimension: Dx3484502405<br/>
Source: PAADMRefExpi... |
| Dx3675129118 | varchar |  |  | SI | Dimension: Dx3675129118<br/>
Source: PAADMConvert... |
| Dx3704349954 | varchar |  |  | SI | Dimension: Dx3704349954<br/>
Source: PAADMRefDate |
| Dx3872968391 | varchar |  |  | SI | Dimension: Dx3872968391<br/>
Source: PAADMEstimDi... |
| Dx3878569545 | varchar |  |  | SI | Dimension: Dx3878569545<br/>
Source: PAADMEmergen... |
| Dx3899526568 | varchar |  |  | SI | Dimension: Dx3899526568<br/>
Source: PAADMEstimDi... |
| Dx3923640476 | varchar |  |  | SI | Dimension: Dx3923640476<br/>
Source: PAADMPAAdm2D... |
| Dx3968998256 | varchar |  |  | SI | Dimension: Dx3968998256<br/>
Source: PAADMDischgD... |
| Dx3995301544 | varchar |  |  | SI | Dimension: Dx3995301544<br/>
Source: PAADMRefExpi... |
| Dx4055595927 | varchar |  |  | SI | Dimension: Dx4055595927<br/>
Source: PAADMPAAdm2D... |
| Dx4090228772 | date |  |  | SI | Dimension: Dx4090228772<br/>
Source: PAADMPAAdm2D... |
| Dx4125588186 | varchar |  |  | SI | Dimension: Dx4125588186<br/>
Source: PAADMConvert... |
| Dx4249666301 | date |  |  | SI | Dimension: Dx4249666301<br/>
Source: PAADMPAAdm2D... |
| Dx46830843 | varchar |  |  | SI | Dimension: Dx46830843<br/>
Source: PAADMRefExpiry... |
| Dx491952580 | varchar |  |  | SI | Dimension: Dx491952580<br/>
Source: PAADMPAAdm2DR... |
| Dx555905842 | varchar |  |  | SI | Dimension: Dx555905842<br/>
Source: PAADMPAAdm2DR... |
| Dx563069918 | varchar |  |  | SI | Dimension: Dx563069918<br/>
Source: PAADMPAAdm2DR... |
| Dx587286637 | varchar |  |  | SI | Dimension: Dx587286637<br/>
Source: PAADMPAAdm2DR... |
| Dx597808487 | varchar |  |  | SI | Dimension: Dx597808487<br/>
Source: PAADMAdmDate |
| Dx749450210 | varchar |  |  | SI | Dimension: Dx749450210<br/>
Source: PAADMPAAdm2DR... |
| Dx8124707 | varchar |  |  | SI | Dimension: Dx8124707<br/>
Source: PAADMDischgDate |
| DxActivityWhenInjured | bigint |  |  | SI | Dimension: DxActivityWhenInjured<br/>
Source: PAA... |
| DxAcuityWaitTime | bigint |  |  | SI | Dimension: DxAcuityWaitTime<br/>
Source: PAADMPri... |
| DxAdmissionCategory | bigint |  |  | SI | Dimension: DxAdmissionCategory<br/>
Source: PAADM... |
| DxAdmissionDoctorID | bigint |  |  | SI | Dimension: DxAdmissionDoctorID<br/>
Source: PAADM... |
| DxAdmissionMethod | bigint |  |  | SI | Dimension: DxAdmissionMethod
Expression: "sourceA... |
| DxAdmissionPoint | bigint |  |  | SI | Dimension: DxAdmissionPoint<br/>
Source: PAADMPAA... |
| DxAdmissionSource | bigint |  |  | SI | Dimension: DxAdmissionSource<br/>
Source: PAADMAd... |
| DxAdmissionType | bigint |  |  | SI | Dimension: DxAdmissionType<br/>
Source: PAADMInPa... |
| DxAdmitReason | bigint |  |  | SI | Dimension: DxAdmitReason<br/>
Source: PAADMAdmRea... |
| DxAdmittingCareProvider | bigint |  |  | SI | Dimension: DxAdmittingCareProvider<br/>
Source: P... |
| DxAdmittingCareProviderGroup | bigint |  |  | SI | Dimension: DxAdmittingCareProviderGroup<br/>
Sour... |
| DxAdmittingRights | bigint |  |  | SI | Dimension: DxAdmittingRights
Expression: "sourceA... |
| DxAge | bigint |  |  | SI | Dimension: DxAge
Expression: %cube.CalculateAge(%... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup
Expression: %cube.Calculate... |
| DxAmbulanceRampedTime | bigint |  |  | SI | Dimension: DxAmbulanceRampedTime
Expression: %exp... |
| DxAmbulanceWaitingTime1 | bigint |  |  | SI | Dimension: DxAmbulanceWaitingTime1
Expression: %e... |
| DxAmbulanceWaitingTime2 | bigint |  |  | SI | Dimension: DxAmbulanceWaitingTime2
Expression: %e... |
| DxAppointmentMethod | bigint |  |  | SI | Dimension: DxAppointmentMethod<br/>
Source: PAADM... |
| DxAppointmentTransport | bigint |  |  | SI | Dimension: DxAppointmentTransport<br/>
Source: PA... |
| DxArrivalMode | bigint |  |  | SI | Dimension: DxArrivalMode<br/>
Source: PAADMMainMR... |
| DxArrivalTimeRange | bigint |  |  | SI | Dimension: DxArrivalTimeRange
Expression: %source... |
| DxArrivalToAdmissionTimeRange | bigint |  |  | SI | Dimension: DxArrivalToAdmissionTimeRange
Expressi... |
| DxArrivalToHandoverTimeRange | bigint |  |  | SI | Dimension: DxArrivalToHandoverTimeRange
Expressio... |
| DxBarthelScore | bigint |  |  | SI | Dimension: DxBarthelScore<br/>
Source: PAADMBarth... |
| DxBed | bigint |  |  | SI | Dimension: DxBed<br/>
Source: PAADMCurrentBedDR.B... |
| DxBedType | bigint |  |  | SI | Dimension: DxBedType<br/>
Source: PAADMCurrentBed... |
| DxBillingMethod | bigint |  |  | SI | Dimension: DxBillingMethod<br/>
Source: PAADMBill... |
| DxBookLocReady | bigint |  |  | SI | Dimension: DxBookLocReady<br/>
Source: PAADMBookL... |
| DxCancelReason | bigint |  |  | SI | Dimension: DxCancelReason<br/>
Source: PAADMCance... |
| DxCareType | bigint |  |  | SI | Dimension: DxCareType<br/>
Source: PAADMMainMRADM... |
| DxCaseManager | bigint |  |  | SI | Dimension: DxCaseManager
Expression: "sourceCaseM... |
| DxCauseOfInjury | bigint |  |  | SI | Dimension: DxCauseOfInjury<br/>
Source: PAADMCaus... |
| DxCommunityUnit | bigint |  |  | SI | Dimension: DxCommunityUnit
Expression: "sourceCom... |
| DxConfidential | bigint |  |  | SI | Dimension: DxConfidential<br/>
Source: PAADMConfi... |
| DxContractType | bigint |  |  | SI | Dimension: DxContractType
Expression: "sourceCont... |
| DxConversionTimeRange | bigint |  |  | SI | Dimension: DxConversionTimeRange
Expression: %sou... |
| DxCreatedByUser | bigint |  |  | SI | Dimension: DxCreatedByUser
Expression: "sourceCre... |
| DxCurrentResource | bigint |  |  | SI | Dimension: DxCurrentResource
Expression: "sourceC... |
| DxCurrentTemporaryLocation | bigint |  |  | SI | Dimension: DxCurrentTemporaryLocation<br/>
Source... |
| DxDSSEpisodeID | bigint |  |  | SI | Dimension: DxDSSEpisodeID<br/>
Source: %ID |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: PAADMPAPMI... |
| DxDaySurgery | bigint |  |  | SI | Dimension: DxDaySurgery<br/>
Source: PAADMDaySurg... |
| DxDecisionToAdmitToDischargeTimeRange | bigint |  |  | SI | Dimension: DxDecisionToAdmitToDischargeTimeRange
... |
| DxDecisionToAdmitToInpatientTimeRange | bigint |  |  | SI | Dimension: DxDecisionToAdmitToInpatientTimeRange
... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment
Expression: "sourceDepart... |
| DxDepartmentCode | bigint |  |  | SI | Dimension: DxDepartmentCode
Expression: "sourceDe... |
| DxDepartureStatus | bigint |  |  | SI | Dimension: DxDepartureStatus<br/>
Source: PAADMMa... |
| DxDiagnosis | bigint |  |  | SI | Dimension: DxDiagnosis
Expression: %cube.GetMainD... |
| DxDiagnosisRelatedGroup | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroup<br/>
Source: P... |
| DxDiagnosisRelatedGroupCategory | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupCategory<br/>
S... |
| DxDiagnosisRelatedGroupCode | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupCode<br/>
Sourc... |
| DxDiagnosisRelatedGroupType | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupType<br/>
Sourc... |
| DxDidNotAttendReason | bigint |  |  | SI | Dimension: DxDidNotAttendReason
Expression: "sour... |
| DxDischargeCareType | bigint |  |  | SI | Dimension: DxDischargeCareType<br/>
Source: PAADM... |
| DxDischargeCondition | bigint |  |  | SI | Dimension: DxDischargeCondition<br/>
Source: PAAD... |
| DxDischargeConditionStatus | bigint |  |  | SI | Dimension: DxDischargeConditionStatus<br/>
Source... |
| DxDischargeDayOfWeek | bigint |  |  | SI | Dimension: DxDischargeDayOfWeek
Expression: ##cla... |
| DxDischargeDestination | bigint |  |  | SI | Dimension: DxDischargeDestination<br/>
Source: PA... |
| DxDischargeTime | bigint |  |  | SI | Dimension: DxDischargeTime
Expression: %expressio... |
| DxDischargeTimeRange | bigint |  |  | SI | Dimension: DxDischargeTimeRange
Expression: %expr... |
| DxDischargeTransport | bigint |  |  | SI | Dimension: DxDischargeTransport<br/>
Source: PAAD... |
| DxDischargeType | bigint |  |  | SI | Dimension: DxDischargeType<br/>
Source: PAADMMain... |
| DxDischargeWard | bigint |  |  | SI | Dimension: DxDischargeWard
Expression: "sourceDis... |
| DxDischargeWardCode | bigint |  |  | SI | Dimension: DxDischargeWardCode
Expression: "sourc... |
| DxDischargingCareProvider | bigint |  |  | SI | Dimension: DxDischargingCareProvider<br/>
Source:... |
| DxEmergencyTimeRange | bigint |  |  | SI | Dimension: DxEmergencyTimeRange
Expression: %sour... |
| DxEmergencyToAdmitTimeRange | bigint |  |  | SI | Dimension: DxEmergencyToAdmitTimeRange
Expression... |
| DxEpisodeAccountClass | bigint |  |  | SI | Dimension: DxEpisodeAccountClass
Expression: "sou... |
| DxEpisodeCheckCompleted | bigint |  |  | SI | Dimension: DxEpisodeCheckCompleted
Expression: %e... |
| DxEpisodeDayOfWeek | bigint |  |  | SI | Dimension: DxEpisodeDayOfWeek
Expression: %expres... |
| DxEpisodeInsuranceCategory | bigint |  |  | SI | Dimension: DxEpisodeInsuranceCategory
Expression:... |
| DxEpisodePayor | bigint |  |  | SI | Dimension: DxEpisodePayor
Expression: %expression... |
| DxEpisodePayorCode | bigint |  |  | SI | Dimension: DxEpisodePayorCode
Expression: "source... |
| DxEpisodePlan | bigint |  |  | SI | Dimension: DxEpisodePlan
Expression: %expression.... |
| DxEpisodePlanCode | bigint |  |  | SI | Dimension: DxEpisodePlanCode
Expression: "sourceE... |
| DxEpisodeSubType | bigint |  |  | SI | Dimension: DxEpisodeSubType<br/>
Source: PAADMEpi... |
| DxEpisodeSubTypeCode | bigint |  |  | SI | Dimension: DxEpisodeSubTypeCode
Expression: "sour... |
| DxEpisodeSubTypeNationalCode | bigint |  |  | SI | Dimension: DxEpisodeSubTypeNationalCode
Expressio... |
| DxEpisodeTime | bigint |  |  | SI | Dimension: DxEpisodeTime
Expression: %expression.... |
| DxEpisodeTimeRange | bigint |  |  | SI | Dimension: DxEpisodeTimeRange
Expression: %source... |
| DxEpisodeType | bigint |  |  | SI | Dimension: DxEpisodeType
Expression: %expression.... |
| DxEscourtSource | bigint |  |  | SI | Dimension: DxEscourtSource<br/>
Source: PAADMMain... |
| DxEstimatedDischargeDay | varchar |  |  | SI | Dimension: DxEstimatedDischargeDay<br/>
Source: P... |
| DxEstimatedDischargeMonth | varchar |  |  | SI | Dimension: DxEstimatedDischargeMonth<br/>
Source:... |
| DxEstimatedDischargeQuarter | varchar |  |  | SI | Dimension: DxEstimatedDischargeQuarter<br/>
Sourc... |
| DxEstimatedDischargeYear | varchar |  |  | SI | Dimension: DxEstimatedDischargeYear<br/>
Source: ... |
| DxFamilyDoctorID | bigint |  |  | SI | Dimension: DxFamilyDoctorID<br/>
Source: PAADMPAP... |
| DxFirstVisit | bigint |  |  | SI | Dimension: DxFirstVisit
Expression: %cube.IsFirst... |
| DxFrequentAdmissions | bigint |  |  | SI | Dimension: DxFrequentAdmissions<br/>
Source: PAAD... |
| DxFundingArrangement | bigint |  |  | SI | Dimension: DxFundingArrangement
Expression: "sour... |
| DxFundingCategory | bigint |  |  | SI | Dimension: DxFundingCategory
Expression: "sourceF... |
| DxFundingDepartment | bigint |  |  | SI | Dimension: DxFundingDepartment
Expression: "sourc... |
| DxHandOverNurse | bigint |  |  | SI | Dimension: DxHandOverNurse
Expression: "sourceHan... |
| DxHasClinicalNotes | bigint |  |  | SI | Dimension: DxHasClinicalNotes
Expression: "source... |
| DxHasProblemEntered | bigint |  |  | SI | Dimension: DxHasProblemEntered
Expression: "sourc... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital
Expression: %expression.Get... |
| DxHospitalCode | bigint |  |  | SI | Dimension: DxHospitalCode
Expression: $LG(%expres... |
| DxHumanIntent | bigint |  |  | SI | Dimension: DxHumanIntent<br/>
Source: PAADMHumanI... |
| DxICUBedRequired | bigint |  |  | SI | Dimension: DxICUBedRequired<br/>
Source: PAADMPAA... |
| DxInfectionType | bigint |  |  | SI | Dimension: DxInfectionType<br/>
Source: PAADMInfe... |
| DxInpatientUnit | bigint |  |  | SI | Dimension: DxInpatientUnit
Expression: "sourceInp... |
| DxIntentionToReadmit | bigint |  |  | SI | Dimension: DxIntentionToReadmit<br/>
Source: PAAD... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: PAADMVis... |
| DxInternalType | bigint |  |  | SI | Dimension: DxInternalType<br/>
Source: PAADMType |
| DxIsolate | bigint |  |  | SI | Dimension: DxIsolate<br/>
Source: PAADMIsolate |
| DxLengthOfStayDays | bigint |  |  | SI | Dimension: DxLengthOfStayDays
Expression: %expres... |
| DxLengthOfStayRangeDays | bigint |  |  | SI | Dimension: DxLengthOfStayRangeDays
Expression: %e... |
| DxLengthofStayOvernight | bigint |  |  | SI | Dimension: DxLengthofStayOvernight
Expression: "s... |
| DxLengthofStayRangeHours | bigint |  |  | SI | Dimension: DxLengthofStayRangeHours
Expression: %... |
| DxLikelyToAdmit | bigint |  |  | SI | Dimension: DxLikelyToAdmit<br/>
Source: PAADMLike... |
| DxLocType | bigint |  |  | SI | Dimension: DxLocType<br/>
Source: PAADMDepCodeDR.... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: PAADMDepCodeDR... |
| DxLocationCode | bigint |  |  | SI | Dimension: DxLocationCode
Expression: "sourceLoca... |
| DxMedicalDischargeDoctor | bigint |  |  | SI | Dimension: DxMedicalDischargeDoctor<br/>
Source: ... |
| DxMentalHealthUnit | bigint |  |  | SI | Dimension: DxMentalHealthUnit
Expression: "source... |
| DxOutpatientUnit | bigint |  |  | SI | Dimension: DxOutpatientUnit
Expression: "sourceOu... |
| DxPAADMAdmDate | date |  |  | SI | Dimension: DxPAADMAdmDate<br/>
Source: PAADMAdmDa... |
| DxPAADMAdmDateFxMonthNumber | varchar |  |  | SI | Dimension: DxPAADMAdmDateFxMonthNumber<br/>
Sourc... |
| DxPAADMAdmDateFxMonthYear | varchar |  |  | SI | Dimension: DxPAADMAdmDateFxMonthYear<br/>
Source:... |
| DxPAADMAdmDateFxQuarterYear | varchar |  |  | SI | Dimension: DxPAADMAdmDateFxQuarterYear<br/>
Sourc... |
| DxPAADMAdmDateFxYear | varchar |  |  | SI | Dimension: DxPAADMAdmDateFxYear<br/>
Source: PAAD... |
| DxPAADMConvertDate | date |  |  | SI | Dimension: DxPAADMConvertDate<br/>
Source: PAADMC... |
| DxPAADMDischgDate | date |  |  | SI | Dimension: DxPAADMDischgDate<br/>
Source: PAADMDi... |
| DxPAADMDischgDateFxYear | varchar |  |  | SI | Dimension: DxPAADMDischgDateFxYear<br/>
Source: P... |
| DxPAADMEmergencyDate | date |  |  | SI | Dimension: DxPAADMEmergencyDate<br/>
Source: PAAD... |
| DxPAADMEmergencyDateFxYear | varchar |  |  | SI | Dimension: DxPAADMEmergencyDateFxYear<br/>
Source... |
| DxPAADMEstimDischargeDate | date |  |  | SI | Dimension: DxPAADMEstimDischargeDate<br/>
Source:... |
| DxPAADMRefDate | date |  |  | SI | Dimension: DxPAADMRefDate<br/>
Source: PAADMRefDa... |
| DxPAADMRefDateFxMonthNumber | varchar |  |  | SI | Dimension: DxPAADMRefDateFxMonthNumber<br/>
Sourc... |
| DxPAADMRefDateFxMonthYear | varchar |  |  | SI | Dimension: DxPAADMRefDateFxMonthYear<br/>
Source:... |
| DxPAADMRefDateFxQuarterYear | varchar |  |  | SI | Dimension: DxPAADMRefDateFxQuarterYear<br/>
Sourc... |
| DxPAADMRefDateFxYear | varchar |  |  | SI | Dimension: DxPAADMRefDateFxYear<br/>
Source: PAAD... |
| DxPAADMRefExpiryDate | date |  |  | SI | Dimension: DxPAADMRefExpiryDate<br/>
Source: PAAD... |
| DxPAADMRefExpiryDateFxYear | varchar |  |  | SI | Dimension: DxPAADMRefExpiryDateFxYear<br/>
Source... |
| DxPallCare | bigint |  |  | SI | Dimension: DxPallCare<br/>
Source: PAADMPalliativ... |
| DxPatientJourneyTimeRange | bigint |  |  | SI | Dimension: DxPatientJourneyTimeRange
Expression: ... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: PAADMPAAdm2... |
| DxPlaceOfInjury | bigint |  |  | SI | Dimension: DxPlaceOfInjury<br/>
Source: PAADMPlac... |
| DxProgram | bigint |  |  | SI | Dimension: DxProgram
Expression: "sourceProgram" |
| DxProgramFunding | bigint |  |  | SI | Dimension: DxProgramFunding
Expression: "sourcePr... |
| DxQualificationStatus | bigint |  |  | SI | Dimension: DxQualificationStatus<br/>
Source: PAA... |
| DxReasonForDelayDischarge | bigint |  |  | SI | Dimension: DxReasonForDelayDischarge<br/>
Source:... |
| DxReferralDoctorID | bigint |  |  | SI | Dimension: DxReferralDoctorID<br/>
Source: PAADMI... |
| DxReferralMethod | bigint |  |  | SI | Dimension: DxReferralMethod<br/>
Source: PAADMMet... |
| DxReferralReason | bigint |  |  | SI | Dimension: DxReferralReason<br/>
Source: PAADMPAA... |
| DxReferredBy | bigint |  |  | SI | Dimension: DxReferredBy<br/>
Source: PAADMRefClin... |
| DxResponsibleUnit | bigint |  |  | SI | Dimension: DxResponsibleUnit
Expression: "sourceR... |
| DxRoom | bigint |  |  | SI | Dimension: DxRoom<br/>
Source: PAADMCurrentRoomDR... |
| DxRoomType | bigint |  |  | SI | Dimension: DxRoomType<br/>
Source: PAADMCurrentRo... |
| DxSeenByDoctor | bigint |  |  | SI | Dimension: DxSeenByDoctor
Expression: %expression... |
| DxSeenTimeRangeMinutes | bigint |  |  | SI | Dimension: DxSeenTimeRangeMinutes
Expression: %ex... |
| DxSeenToDischargeTimeRange | bigint |  |  | SI | Dimension: DxSeenToDischargeTimeRange
Expression:... |
| DxShortStayIntent | bigint |  |  | SI | Dimension: DxShortStayIntent
Expression: %express... |
| DxShortStayReason | bigint |  |  | SI | Dimension: DxShortStayReason<br/>
Source: PAADMPA... |
| DxSourceOfAttendance | bigint |  |  | SI | Dimension: DxSourceOfAttendance<br/>
Source: PAAD... |
| DxSummaryCompleted | bigint |  |  | SI | Dimension: DxSummaryCompleted
Expression: "Summar... |
| DxSummaryNotRequired | bigint |  |  | SI | Dimension: DxSummaryNotRequired
Expression: "sour... |
| DxSummaryRequired | bigint |  |  | SI | Dimension: DxSummaryRequired
Expression: "sourceS... |
| DxSuspectedCancerType | bigint |  |  | SI | Dimension: DxSuspectedCancerType<br/>
Source: PAA... |
| DxTransferDestination | bigint |  |  | SI | Dimension: DxTransferDestination<br/>
Source: PAA... |
| DxTransferLocation | bigint |  |  | SI | Dimension: DxTransferLocation
Expression: "source... |
| DxTransferReason | bigint |  |  | SI | Dimension: DxTransferReason<br/>
Source: PAADMMai... |
| DxTransferWard | bigint |  |  | SI | Dimension: DxTransferWard
Expression: "sourceTran... |
| DxTransportRequired | bigint |  |  | SI | Dimension: DxTransportRequired<br/>
Source: PAADM... |
| DxTreatmentStream | bigint |  |  | SI | Dimension: DxTreatmentStream<br/>
Source: PAADMPA... |
| DxTriageCategory | bigint |  |  | SI | Dimension: DxTriageCategory<br/>
Source: PAADMPri... |
| DxTriageNurse | bigint |  |  | SI | Dimension: DxTriageNurse<br/>
Source: PAADMTriage... |
| DxTriageSymptomsProblems | varchar |  |  | SI | Dimension: DxTriageSymptomsProblems
Expression: %... |
| DxTriageToAdmitTimeRange | bigint |  |  | SI | Dimension: DxTriageToAdmitTimeRange
Expression: %... |
| DxTrust | bigint |  |  | SI | Dimension: DxTrust
Expression: $LG(%expression.Ge... |
| DxTrustCode | bigint |  |  | SI | Dimension: DxTrustCode
Expression: $LG(%expressio... |
| DxViewableByEpisodeCareProvider | bigint |  |  | SI | Dimension: DxViewableByEpisodeCareProvider
Expres... |
| DxViewableByEpisodeLocation | bigint |  |  | SI | Dimension: DxViewableByEpisodeLocation
Expression... |
| DxVisitStatus | bigint |  |  | SI | Dimension: DxVisitStatus
Expression: %expression.... |
| DxWEISScore | bigint |  |  | SI | Dimension: DxWEISScore
Expression: "WEISScore" |
| DxWard | bigint |  |  | SI | Dimension: DxWard<br/>
Source: PAADMCurrentWardDR... |
| DxWardCode | bigint |  |  | SI | Dimension: DxWardCode
Expression: "sourceWardCode... |
| MxDeceasedDays | double |  |  | SI | Measure: MxDeceasedDays
Expression: %cube.GetDece... |
| MxExceedWaitTime | double |  |  | SI | Measure: MxExceedWaitTime
Expression: %cube.SeenW... |
| MxNumberDeceased | double |  |  | SI | Measure: MxNumberDeceased
Expression: %expression... |
| MxNumberDischarges | double |  |  | SI | Measure: MxNumberDischarges
Expression: %expressi... |
| MxTotalLOS | double |  |  | SI | Measure: MxTotalLOS
Expression: %expression.GetDa... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*