# TCBI_Cubes_PAAdm.Fact

**Schema:** TCBI_Cubes_PAAdm
**Columnas:** 243
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1012448990 | bigint |  |  | SI | Dimension: Dx1012448990<br/>
Source: PAADMPAAdm2D... |
| Dx1071941118 | bigint |  |  | SI | Dimension: Dx1071941118<br/>
Source: PAADMBilling... |
| Dx1291922942 | varchar |  |  | SI | Dimension: Dx1291922942<br/>
Source: PAADMDischgD... |
| Dx1498567482 | varchar |  |  | SI | Dimension: Dx1498567482<br/>
Source: PAADMPAAdm2D... |
| Dx1577719573 | bigint |  |  | SI | Dimension: Dx1577719573<br/>
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
| Dx2205717384 | varchar |  |  | SI | Dimension: Dx2205717384<br/>
Source: PAADMTriageD... |
| Dx2334538110 | varchar |  |  | SI | Dimension: Dx2334538110<br/>
Source: PAADMPAAdm2D... |
| Dx2334665789 | bigint |  |  | SI | Dimension: Dx2334665789<br/>
Source: PAADMBilling... |
| Dx2468250854 | bigint |  |  | SI | Dimension: Dx2468250854
Expression: %cube.GetShor... |
| Dx2476561932 | varchar |  |  | SI | Dimension: Dx2476561932<br/>
Source: PAADMAdmDate |
| Dx2573102766 | varchar |  |  | SI | Dimension: Dx2573102766<br/>
Source: PAADMEmergen... |
| Dx274861259 | varchar |  |  | SI | Dimension: Dx274861259<br/>
Source: PAADMRefExpir... |
| Dx2931468779 | varchar |  |  | SI | Dimension: Dx2931468779<br/>
Source: PAADMRefDate |
| Dx307441253 | varchar |  |  | SI | Dimension: Dx307441253<br/>
Source: PAADMEmergenc... |
| Dx3168032988 | varchar |  |  | SI | Dimension: Dx3168032988<br/>
Source: PAADMRefExpi... |
| Dx3262893339 | varchar |  |  | SI | Dimension: Dx3262893339<br/>
Source: PAADMTriageD... |
| Dx3327154939 | varchar |  |  | SI | Dimension: Dx3327154939<br/>
Source: PAADMDischgD... |
| Dx3400896372 | bigint |  |  | SI | Dimension: Dx3400896372<br/>
Source: PAADMPAAdm2D... |
| Dx3448919731 | varchar |  |  | SI | Dimension: Dx3448919731<br/>
Source: PAADMPAAdm2D... |
| Dx3484502405 | varchar |  |  | SI | Dimension: Dx3484502405<br/>
Source: PAADMRefExpi... |
| Dx3624349403 | varchar |  |  | SI | Dimension: Dx3624349403<br/>
Source: PAADMTriageD... |
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
| Dx4135149753 | bigint |  |  | SI | Dimension: Dx4135149753<br/>
Source: PAADMAdmMeth... |
| Dx420386953 | varchar |  |  | SI | Dimension: Dx420386953<br/>
Source: PAADMConvertD... |
| Dx4249666301 | date |  |  | SI | Dimension: Dx4249666301<br/>
Source: PAADMPAAdm2D... |
| Dx4277162500 | varchar |  |  | SI | Dimension: Dx4277162500<br/>
Source: PAADMTriageD... |
| Dx46435520 | varchar |  |  | SI | Dimension: Dx46435520<br/>
Source: PAADMConvertDa... |
| Dx46830843 | varchar |  |  | SI | Dimension: Dx46830843<br/>
Source: PAADMRefExpiry... |
| Dx471731197 | varchar |  |  | SI | Dimension: Dx471731197<br/>
Source: PAADMTriageDa... |
| Dx491952580 | varchar |  |  | SI | Dimension: Dx491952580<br/>
Source: PAADMPAAdm2DR... |
| Dx555905842 | varchar |  |  | SI | Dimension: Dx555905842<br/>
Source: PAADMPAAdm2DR... |
| Dx55633779 | varchar |  |  | SI | Dimension: Dx55633779<br/>
Source: PAADMConvertDa... |
| Dx563069918 | varchar |  |  | SI | Dimension: Dx563069918<br/>
Source: PAADMPAAdm2DR... |
| Dx587286637 | varchar |  |  | SI | Dimension: Dx587286637<br/>
Source: PAADMPAAdm2DR... |
| Dx597808487 | varchar |  |  | SI | Dimension: Dx597808487<br/>
Source: PAADMAdmDate |
| Dx602911046 | bigint |  |  | SI | Dimension: Dx602911046<br/>
Source: PAADMSourceOf... |
| Dx749450210 | varchar |  |  | SI | Dimension: Dx749450210<br/>
Source: PAADMPAAdm2DR... |
| Dx781332296 | varchar |  |  | SI | Dimension: Dx781332296<br/>
Source: PAADMTriageDa... |
| Dx8124707 | varchar |  |  | SI | Dimension: Dx8124707<br/>
Source: PAADMDischgDate |
| DxActivityWhenInjured | bigint |  |  | SI | Dimension: DxActivityWhenInjured<br/>
Source: PAA... |
| DxAcuityWaitTime | bigint |  |  | SI | Dimension: DxAcuityWaitTime<br/>
Source: PAADMPri... |
| DxAdmissionCategory | bigint |  |  | SI | Dimension: DxAdmissionCategory<br/>
Source: PAADM... |
| DxAdmissionMethod | bigint |  |  | SI | Dimension: DxAdmissionMethod<br/>
Source: PAADMAd... |
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
Expression: %cube.Ha... |
| DxAge | bigint |  |  | SI | Dimension: DxAge
Expression: %cube.CalculateAge(%... |
| DxAgeGroup | bigint |  |  | SI | Dimension: DxAgeGroup
Expression: %cube.Calculate... |
| DxAgeInDays | bigint |  |  | SI | Dimension: DxAgeInDays
Expression: %cube.Calculat... |
| DxAgeInMonths | bigint |  |  | SI | Dimension: DxAgeInMonths
Expression: %cube.Calcul... |
| DxAgeInWeeks | bigint |  |  | SI | Dimension: DxAgeInWeeks
Expression: %cube.Calcula... |
| DxArrivalMode | bigint |  |  | SI | Dimension: DxArrivalMode<br/>
Source: PAADMMainMR... |
| DxArrivalTimeRange | bigint |  |  | SI | Dimension: DxArrivalTimeRange
Expression: "source... |
| DxArrivalToAdmissionTimeRange | bigint |  |  | SI | Dimension: DxArrivalToAdmissionTimeRange
Expressi... |
| DxArrivalToHandoverTimeRange | bigint |  |  | SI | Dimension: DxArrivalToHandoverTimeRange
Expressio... |
| DxAutopsyType | bigint |  |  | SI | Dimension: DxAutopsyType<br/>
Source: PAADMMainMR... |
| DxBed | bigint |  |  | SI | Dimension: DxBed<br/>
Source: PAADMCurrentBedDR.B... |
| DxBedType | bigint |  |  | SI | Dimension: DxBedType<br/>
Source: PAADMCurrentBed... |
| DxCancelReason | bigint |  |  | SI | Dimension: DxCancelReason<br/>
Source: PAADMCance... |
| DxCaseManager | bigint |  |  | SI | Dimension: DxCaseManager<br/>
Source: PAADMCaseMa... |
| DxCauseOfInjury | bigint |  |  | SI | Dimension: DxCauseOfInjury<br/>
Source: PAADMCaus... |
| DxCommunityUnit | bigint |  |  | SI | Dimension: DxCommunityUnit<br/>
Source: PAADMDepC... |
| DxContractType | bigint |  |  | SI | Dimension: DxContractType<br/>
Source: PAADMContr... |
| DxConversionTimeRange | bigint |  |  | SI | Dimension: DxConversionTimeRange
Expression: "sou... |
| DxCreatedByUser | bigint |  |  | SI | Dimension: DxCreatedByUser<br/>
Source: PAADMCrea... |
| DxCurrentResource | bigint |  |  | SI | Dimension: DxCurrentResource<br/>
Source: PAADMCu... |
| DxCurrentTemporaryLocation | bigint |  |  | SI | Dimension: DxCurrentTemporaryLocation<br/>
Source... |
| DxDaySurgery | bigint |  |  | SI | Dimension: DxDaySurgery<br/>
Source: PAADMDaySurg... |
| DxDaysAfterDischarge | bigint |  |  | SI | Dimension: DxDaysAfterDischarge
Expression: $lg(%... |
| DxDaysAfterDischargeRange | bigint |  |  | SI | Dimension: DxDaysAfterDischargeRange
Expression: ... |
| DxDecisionToAdmitToDischargeTimeRange | bigint |  |  | SI | Dimension: DxDecisionToAdmitToDischargeTimeRange
... |
| DxDecisionToAdmitToInpatientTimeRange | bigint |  |  | SI | Dimension: DxDecisionToAdmitToInpatientTimeRange
... |
| DxDepartment | bigint |  |  | SI | Dimension: DxDepartment<br/>
Source: PAADMDepCode... |
| DxDepartmentCode | bigint |  |  | SI | Dimension: DxDepartmentCode<br/>
Source: PAADMDep... |
| DxDepartureStatus | bigint |  |  | SI | Dimension: DxDepartureStatus<br/>
Source: PAADMMa... |
| DxDiagnosisRelatedGroup | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroup<br/>
Source: P... |
| DxDiagnosisRelatedGroupCategory | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupCategory<br/>
S... |
| DxDiagnosisRelatedGroupCode | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupCode<br/>
Sourc... |
| DxDiagnosisRelatedGroupType | bigint |  |  | SI | Dimension: DxDiagnosisRelatedGroupType<br/>
Sourc... |
| DxDidNotAttendReason | bigint |  |  | SI | Dimension: DxDidNotAttendReason<br/>
Source: PAAD... |
| DxDischargeCareType | bigint |  |  | SI | Dimension: DxDischargeCareType<br/>
Source: PAADM... |
| DxDischargeCondition | bigint |  |  | SI | Dimension: DxDischargeCondition<br/>
Source: PAAD... |
| DxDischargeConditionStatus | bigint |  |  | SI | Dimension: DxDischargeConditionStatus<br/>
Source... |
| DxDischargeDayOfWeek | bigint |  |  | SI | Dimension: DxDischargeDayOfWeek
Expression: $syst... |
| DxDischargeDestination | bigint |  |  | SI | Dimension: DxDischargeDestination<br/>
Source: PA... |
| DxDischargeReferral | varchar |  |  | SI | Dimension: DxDischargeReferral
Expression: %cube.... |
| DxDischargeTime | bigint |  |  | SI | Dimension: DxDischargeTime
Expression: "sourceDis... |
| DxDischargeTimeRange | bigint |  |  | SI | Dimension: DxDischargeTimeRange
Expression: %sour... |
| DxDischargeTransport | bigint |  |  | SI | Dimension: DxDischargeTransport<br/>
Source: PAAD... |
| DxDischargeType | bigint |  |  | SI | Dimension: DxDischargeType<br/>
Source: PAADMMain... |
| DxDischargeWard | bigint |  |  | SI | Dimension: DxDischargeWard
Expression: $LG(%expre... |
| DxDischargeWardCode | bigint |  |  | SI | Dimension: DxDischargeWardCode
Expression: $LG(%e... |
| DxDischargingCareProvider | bigint |  |  | SI | Dimension: DxDischargingCareProvider<br/>
Source:... |
| DxEDLengthOfStay | bigint |  |  | SI | Dimension: DxEDLengthOfStay
Expression: %expressi... |
| DxEDWaitTime | bigint |  |  | SI | Dimension: DxEDWaitTime
Expression: %expression.G... |
| DxEmergencyTimeRange | bigint |  |  | SI | Dimension: DxEmergencyTimeRange
Expression: %sour... |
| DxEmergencyToAdmitTimeRange | bigint |  |  | SI | Dimension: DxEmergencyToAdmitTimeRange
Expression... |
| DxEpisodeAccountClass | bigint |  |  | SI | Dimension: DxEpisodeAccountClass<br/>
Source: PAA... |
| DxEpisodeDayOfWeek | bigint |  |  | SI | Dimension: DxEpisodeDayOfWeek
Expression: $system... |
| DxEpisodeInsuranceCategory | bigint |  |  | SI | Dimension: DxEpisodeInsuranceCategory
Expression:... |
| DxEpisodePayor | bigint |  |  | SI | Dimension: DxEpisodePayor
Expression: %cube.GetEp... |
| DxEpisodePayorCode | bigint |  |  | SI | Dimension: DxEpisodePayorCode
Expression: %cube.G... |
| DxEpisodePlan | bigint |  |  | SI | Dimension: DxEpisodePlan
Expression: %cube.GetEpi... |
| DxEpisodePlanCode | bigint |  |  | SI | Dimension: DxEpisodePlanCode
Expression: %cube.Ge... |
| DxEpisodeSubType | bigint |  |  | SI | Dimension: DxEpisodeSubType<br/>
Source: PAADMEpi... |
| DxEpisodeSubTypeCode | bigint |  |  | SI | Dimension: DxEpisodeSubTypeCode<br/>
Source: PAAD... |
| DxEpisodeSubTypeNationalCode | bigint |  |  | SI | Dimension: DxEpisodeSubTypeNationalCode
Expressio... |
| DxEpisodeTime | bigint |  |  | SI | Dimension: DxEpisodeTime
Expression: "sourceEpiso... |
| DxEpisodeTimeRange | bigint |  |  | SI | Dimension: DxEpisodeTimeRange
Expression: %source... |
| DxEpisodeType | bigint |  |  | SI | Dimension: DxEpisodeType
Expression: %cube.GetAdm... |
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
| DxFallsRisk | bigint |  |  | SI | Dimension: DxFallsRisk
Expression: %expression.Ha... |
| DxFirstVisit | bigint |  |  | SI | Dimension: DxFirstVisit
Expression: %cube.IsFirst... |
| DxFundingArrangement | bigint |  |  | SI | Dimension: DxFundingArrangement<br/>
Source: PAAD... |
| DxFundingCategory | bigint |  |  | SI | Dimension: DxFundingCategory<br/>
Source: PAADMPA... |
| DxFundingDepartment | bigint |  |  | SI | Dimension: DxFundingDepartment<br/>
Source: PAADM... |
| DxHandOverNurse | bigint |  |  | SI | Dimension: DxHandOverNurse<br/>
Source: PAADMPAAd... |
| DxHasClinicalNotes | bigint |  |  | SI | Dimension: DxHasClinicalNotes
Expression: %cube.H... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital
Expression: $LG(%expression... |
| DxHospitalCode | bigint |  |  | SI | Dimension: DxHospitalCode
Expression: $LG(%expres... |
| DxHumanIntent | bigint |  |  | SI | Dimension: DxHumanIntent<br/>
Source: PAADMHumanI... |
| DxInpatientUnit | bigint |  |  | SI | Dimension: DxInpatientUnit<br/>
Source: PAADMDepC... |
| DxIntentionToReadmit | bigint |  |  | SI | Dimension: DxIntentionToReadmit<br/>
Source: PAAD... |
| DxInternalStatus | bigint |  |  | SI | Dimension: DxInternalStatus<br/>
Source: PAADMVis... |
| DxInternalType | bigint |  |  | SI | Dimension: DxInternalType<br/>
Source: PAADMType |
| DxLastEWSAgeRange | bigint |  |  | SI | Dimension: DxLastEWSAgeRange
Expression: $lg(%exp... |
| DxLastEWSLocation | bigint |  |  | SI | Dimension: DxLastEWSLocation
Expression: $lg(%exp... |
| DxLastEWSTotal | bigint |  |  | SI | Dimension: DxLastEWSTotal
Expression: $lg(%expres... |
| DxLastEWSTrend | bigint |  |  | SI | Dimension: DxLastEWSTrend
Expression: $lg(%expres... |
| DxLengthOfStayDays | bigint |  |  | SI | Dimension: DxLengthOfStayDays
Expression: %cube.G... |
| DxLengthOfStayRangeDays | bigint |  |  | SI | Dimension: DxLengthOfStayRangeDays
Expression: %c... |
| DxLengthofStayOvernight | bigint |  |  | SI | Dimension: DxLengthofStayOvernight
Expression: %c... |
| DxLengthofStayRangeHours | bigint |  |  | SI | Dimension: DxLengthofStayRangeHours
Expression: #... |
| DxLikelyToAdmit | bigint |  |  | SI | Dimension: DxLikelyToAdmit<br/>
Source: PAADMLike... |
| DxLocType | bigint |  |  | SI | Dimension: DxLocType<br/>
Source: PAADMDepCodeDR.... |
| DxLocation | bigint |  |  | SI | Dimension: DxLocation<br/>
Source: PAADMDepCodeDR... |
| DxLocationCode | bigint |  |  | SI | Dimension: DxLocationCode<br/>
Source: PAADMDepCo... |
| DxMedicalDischargeDoctor | bigint |  |  | SI | Dimension: DxMedicalDischargeDoctor<br/>
Source: ... |
| DxMentalHealthUnit | bigint |  |  | SI | Dimension: DxMentalHealthUnit<br/>
Source: PAADMD... |
| DxOutpatientUnit | bigint |  |  | SI | Dimension: DxOutpatientUnit<br/>
Source: PAADMDep... |
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
| DxPAADMConvertDateFxYear | varchar |  |  | SI | Dimension: DxPAADMConvertDateFxYear<br/>
Source: ... |
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
| DxPAADMTriageDate | date |  |  | SI | Dimension: DxPAADMTriageDate<br/>
Source: PAADMTr... |
| DxPAADMTriageDateFxYear | varchar |  |  | SI | Dimension: DxPAADMTriageDateFxYear<br/>
Source: P... |
| DxPatientID | bigint |  |  | SI | Dimension: DxPatientID<br/>
Source: PAADMPAPMIDR.... |
| DxPlaceOfInjury | bigint |  |  | SI | Dimension: DxPlaceOfInjury<br/>
Source: PAADMPlac... |
| DxProgram | bigint |  |  | SI | Dimension: DxProgram<br/>
Source: PAADMPAAdm2DR.P... |
| DxProgramFunding | bigint |  |  | SI | Dimension: DxProgramFunding<br/>
Source: PAADMMai... |
| DxQualificationStatus | bigint |  |  | SI | Dimension: DxQualificationStatus<br/>
Source: PAA... |
| DxReasonForDelayDischarge | bigint |  |  | SI | Dimension: DxReasonForDelayDischarge<br/>
Source:... |
| DxReceiptMethod | bigint |  |  | SI | Dimension: DxReceiptMethod<br/>
Source: PAADMMeth... |
| DxReceiptMethodCode | bigint |  |  | SI | Dimension: DxReceiptMethodCode<br/>
Source: PAADM... |
| DxReferralOrganisation | bigint |  |  | SI | Dimension: DxReferralOrganisation<br/>
Source: PA... |
| DxReferralPriority | bigint |  |  | SI | Dimension: DxReferralPriority<br/>
Source: PAADMR... |
| DxReferralReason | bigint |  |  | SI | Dimension: DxReferralReason<br/>
Source: PAADMPAA... |
| DxReferralStatus | bigint |  |  | SI | Dimension: DxReferralStatus<br/>
Source: PAADMRef... |
| DxReferralStatusReason | bigint |  |  | SI | Dimension: DxReferralStatusReason<br/>
Source: PA... |
| DxReferralType | bigint |  |  | SI | Dimension: DxReferralType<br/>
Source: PAADMRefer... |
| DxReferredBy | bigint |  |  | SI | Dimension: DxReferredBy<br/>
Source: PAADMRefClin... |
| DxReferredTo | bigint |  |  | SI | Dimension: DxReferredTo<br/>
Source: PAADMMainMRA... |
| DxReferringCareProvider | bigint |  |  | SI | Dimension: DxReferringCareProvider<br/>
Source: P... |
| DxResponsibleUnit | bigint |  |  | SI | Dimension: DxResponsibleUnit<br/>
Source: PAADMDe... |
| DxRoom | bigint |  |  | SI | Dimension: DxRoom<br/>
Source: PAADMCurrentRoomDR... |
| DxRoomType | bigint |  |  | SI | Dimension: DxRoomType<br/>
Source: PAADMCurrentRo... |
| DxSeenByDoctor | bigint |  |  | SI | Dimension: DxSeenByDoctor
Expression: $lg(%expres... |
| DxSeenTimeRangeMinutes | bigint |  |  | SI | Dimension: DxSeenTimeRangeMinutes
Expression: ##c... |
| DxSeenToDischargeTimeRange | bigint |  |  | SI | Dimension: DxSeenToDischargeTimeRange
Expression:... |
| DxSepsis | bigint |  |  | SI | Dimension: DxSepsis
Expression: %expression.HasAn... |
| DxSourceOfAddition | bigint |  |  | SI | Dimension: DxSourceOfAddition<br/>
Source: PAADMW... |
| DxSourceOfAttendance | bigint |  |  | SI | Dimension: DxSourceOfAttendance<br/>
Source: PAAD... |
| DxSummaryCompleted | bigint |  |  | SI | Dimension: DxSummaryCompleted
Expression: %cube.S... |
| DxSummaryNotRequired | bigint |  |  | SI | Dimension: DxSummaryNotRequired
Expression: %cube... |
| DxSummaryRequired | bigint |  |  | SI | Dimension: DxSummaryRequired
Expression: %cube.Su... |
| DxTotalLOSForEMLoc | bigint |  |  | SI | Dimension: DxTotalLOSForEMLoc
Expression: %expres... |
| DxTransferDestination | bigint |  |  | SI | Dimension: DxTransferDestination<br/>
Source: PAA... |
| DxTransferLocation | bigint |  |  | SI | Dimension: DxTransferLocation
Expression: $lg(%ex... |
| DxTransferReason | bigint |  |  | SI | Dimension: DxTransferReason<br/>
Source: PAADMMai... |
| DxTransferWard | bigint |  |  | SI | Dimension: DxTransferWard
Expression: $lg(%expres... |
| DxTriageCategory | bigint |  |  | SI | Dimension: DxTriageCategory<br/>
Source: PAADMPri... |
| DxTriageNurse | bigint |  |  | SI | Dimension: DxTriageNurse<br/>
Source: PAADMTriage... |
| DxTriageSymptomsProblems | varchar |  |  | SI | Dimension: DxTriageSymptomsProblems
Expression: %... |
| DxTriageTime | bigint |  |  | SI | Dimension: DxTriageTime
Expression: (%source.PAAD... |
| DxTriageToAdmitTimeRange | bigint |  |  | SI | Dimension: DxTriageToAdmitTimeRange
Expression: #... |
| DxTrust | bigint |  |  | SI | Dimension: DxTrust
Expression: $LG(%expression.Ge... |
| DxTrustCode | bigint |  |  | SI | Dimension: DxTrustCode
Expression: $LG(%expressio... |
| DxViewableByEpisodeCareProvider | bigint |  |  | SI | Dimension: DxViewableByEpisodeCareProvider<br/>
S... |
| DxViewableByEpisodeLocation | bigint |  |  | SI | Dimension: DxViewableByEpisodeLocation<br/>
Sourc... |
| DxVisitStatus | bigint |  |  | SI | Dimension: DxVisitStatus
Expression: %cube.GetAdm... |
| DxWEISScore | bigint |  |  | SI | Dimension: DxWEISScore<br/>
Source: PAADMMainMRAD... |
| DxWard | bigint |  |  | SI | Dimension: DxWard<br/>
Source: PAADMCurrentWardDR... |
| DxWardCode | bigint |  |  | SI | Dimension: DxWardCode<br/>
Source: PAADMCurrentWa... |
| MxEDLengthOfStay | double |  |  | SI | Measure: MxEDLengthOfStay
Expression: %cube.GetED... |
| MxEDWaitTime | double |  |  | SI | Measure: MxEDWaitTime
Expression: %cube.GetEDWait... |
| MxExceedWaitTime | double |  |  | SI | Measure: MxExceedWaitTime
Expression: ##class(TCB... |
| MxNumberDeceased | double |  |  | SI | Measure: MxNumberDeceased
Expression: %expression... |
| MxNumberDischarges | double |  |  | SI | Measure: MxNumberDischarges
Expression: %expressi... |
| MxOvernightStays | double |  |  | SI | Measure: MxOvernightStays
Expression: %cube.GetNi... |
| MxTotalLOS | double |  |  | SI | Measure: MxTotalLOS
Expression: %cube.GetLengthOf... |
| MxTotalLOSHours | double |  |  | SI | Measure: MxTotalLOSHours
Expression: ##class(TCBI... |
| RxIDViaPAADMPAPMIDR | bigint |  | FK | SI | Relationship: RxIDViaPAADMPAPMIDR<br/>
Source: PA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*