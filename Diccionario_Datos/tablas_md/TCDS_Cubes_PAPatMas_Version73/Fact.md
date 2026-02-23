# TCDS_Cubes_PAPatMas_Version73.Fact

**Schema:** TCDS_Cubes_PAPatMas_Version73
**Columnas:** 85
**Actualizado:** 2026-01-30 15:31:37

## Utilidad

**TrakCare Data Store**. Almacén de datos para reportería y análisis.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1575787577 | date |  |  | SI | Dimension: Dx1575787577<br/>
Source: PAPMIRowId.P... |
| Dx1621928670 | varchar |  |  | SI | Dimension: Dx1621928670<br/>
Source: PAPMIRowId.P... |
| Dx3016719288 | varchar |  |  | SI | Dimension: Dx3016719288<br/>
Source: PAPMIDecease... |
| Dx3019049172 | varchar |  |  | SI | Dimension: Dx3019049172<br/>
Source: PAPMIDecease... |
| Dx3367631356 | varchar |  |  | SI | Dimension: Dx3367631356<br/>
Source: PAPMIDecease... |
| Dx578469394 | varchar |  |  | SI | Dimension: Dx578469394<br/>
Source: PAPMIDeceased... |
| Dx609229743 | varchar |  |  | SI | Dimension: Dx609229743<br/>
Source: PAPMIDeceased... |
| DxAccommodationSetting | bigint |  |  | SI | Dimension: DxAccommodationSetting
Expression: "so... |
| DxAdditionalBloodGroup | varchar |  |  | SI | Dimension: DxAdditionalBloodGroup
Expression: %ex... |
| DxBlackList | bigint |  |  | SI | Dimension: DxBlackList<br/>
Source: PAPMIBlackLis... |
| DxBloodGroup | bigint |  |  | SI | Dimension: DxBloodGroup<br/>
Source: PAPMIPAPERDR... |
| DxBloodGroupAntibodies | varchar |  |  | SI | Dimension: DxBloodGroupAntibodies
Expression: %ex... |
| DxBloodGroupStatus | bigint |  |  | SI | Dimension: DxBloodGroupStatus
Expression: %expres... |
| DxCardType | bigint |  |  | SI | Dimension: DxCardType<br/>
Source: PAPMICardTypeD... |
| DxCheckEPV | bigint |  |  | SI | Dimension: DxCheckEPV<br/>
Source: PAPMICheckEPV |
| DxCheckFund | bigint |  |  | SI | Dimension: DxCheckFund<br/>
Source: PAPMICheckFun... |
| DxCheckMedicare | bigint |  |  | SI | Dimension: DxCheckMedicare<br/>
Source: PAPMIChec... |
| DxCitizenship | bigint |  |  | SI | Dimension: DxCitizenship
Expression: "sourceCitiz... |
| DxCity | bigint |  |  | SI | Dimension: DxCity<br/>
Source: PAPMIRowId.PAPERCi... |
| DxCityArea | bigint |  |  | SI | Dimension: DxCityArea
Expression: "sourceCityArea... |
| DxCommunityHealthStatus | bigint |  |  | SI | Dimension: DxCommunityHealthStatus
Expression: "s... |
| DxCountry | bigint |  |  | SI | Dimension: DxCountry
Expression: "sourceCountry" |
| DxCountryOfBirth | bigint |  |  | SI | Dimension: DxCountryOfBirth<br/>
Source: PAPMIPAP... |
| DxDSSPatientID | bigint |  |  | SI | Dimension: DxDSSPatientID<br/>
Source: %ID |
| DxDVACardType | bigint |  |  | SI | Dimension: DxDVACardType<br/>
Source: PAPMICardTy... |
| DxDVAnumber | bigint |  |  | SI | Dimension: DxDVAnumber<br/>
Source: PAPMIDVAnumbe... |
| DxDeceased | bigint |  |  | SI | Dimension: DxDeceased<br/>
Source: PAPMIDeceased |
| DxEmployeeType | bigint |  |  | SI | Dimension: DxEmployeeType
Expression: "sourceEmpl... |
| DxEmploymentStatus | bigint |  |  | SI | Dimension: DxEmploymentStatus
Expression: "source... |
| DxEthnicity | varchar |  |  | SI | Dimension: DxEthnicity
Expression: %cube.GetEthni... |
| DxGPClinic | bigint |  |  | SI | Dimension: DxGPClinic<br/>
Source: PAPMIPAPERDR.P... |
| DxGPName | bigint |  |  | SI | Dimension: DxGPName<br/>
Source: PAPMIPAPERDR.PAP... |
| DxGender | bigint |  |  | SI | Dimension: DxGender<br/>
Source: PAPMISexDR.CTSEX... |
| DxHasAlerts | bigint |  |  | SI | Dimension: DxHasAlerts
Expression: "sourceHasAler... |
| DxHasAllergies | bigint |  |  | SI | Dimension: DxHasAllergies
Expression: "sourceHasA... |
| DxHealthCareArea | bigint |  |  | SI | Dimension: DxHealthCareArea<br/>
Source: PAPMIRow... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital
Expression: %cube.GetRegist... |
| DxIndigenousStatus | bigint |  |  | SI | Dimension: DxIndigenousStatus<br/>
Source: PAPMII... |
| DxInterpreterRequired | bigint |  |  | SI | Dimension: DxInterpreterRequired<br/>
Source: PAP... |
| DxIsRegisteredPatient | bigint |  |  | SI | Dimension: DxIsRegisteredPatient
Expression: "sou... |
| DxLivingArrangement | bigint |  |  | SI | Dimension: DxLivingArrangement
Expression: "sourc... |
| DxMHRConsent | bigint |  |  | SI | Dimension: DxMHRConsent<br/>
Source: PAPMIPAPERDR... |
| DxMaritalStatus | bigint |  |  | SI | Dimension: DxMaritalStatus<br/>
Source: PAPMIRowI... |
| DxMedicare | bigint |  |  | SI | Dimension: DxMedicare<br/>
Source: PAPMIMedicare |
| DxMedicareSuffix | bigint |  |  | SI | Dimension: DxMedicareSuffix<br/>
Source: PAPMIMed... |
| DxOccupation | bigint |  |  | SI | Dimension: DxOccupation<br/>
Source: PAPMIRowId.P... |
| DxOverseasVisitorStatus | bigint |  |  | SI | Dimension: DxOverseasVisitorStatus<br/>
Source: P... |
| DxPAPMIDOB | date |  |  | SI | Dimension: DxPAPMIDOB<br/>
Source: PAPMIDOB |
| DxPAPMIDOBFxDayMonthYear | varchar |  |  | SI | Dimension: DxPAPMIDOBFxDayMonthYear<br/>
Source: ... |
| DxPAPMIDOBFxMonthNumber | varchar |  |  | SI | Dimension: DxPAPMIDOBFxMonthNumber<br/>
Source: P... |
| DxPAPMIDOBFxMonthYear | varchar |  |  | SI | Dimension: DxPAPMIDOBFxMonthYear<br/>
Source: PAP... |
| DxPAPMIDOBFxQuarterNumber | varchar |  |  | SI | Dimension: DxPAPMIDOBFxQuarterNumber<br/>
Source:... |
| DxPAPMIDOBFxQuarterYear | varchar |  |  | SI | Dimension: DxPAPMIDOBFxQuarterYear<br/>
Source: P... |
| DxPAPMIDOBFxYear | varchar |  |  | SI | Dimension: DxPAPMIDOBFxYear<br/>
Source: PAPMIDOB |
| DxPAPMIDeceasedDate | date |  |  | SI | Dimension: DxPAPMIDeceasedDate<br/>
Source: PAPMI... |
| DxPAPMIDeceasedDateFxYear | varchar |  |  | SI | Dimension: DxPAPMIDeceasedDateFxYear<br/>
Source:... |
| DxPDSSerialNumber | bigint |  |  | SI | Dimension: DxPDSSerialNumber
Expression: "sourceP... |
| DxPassportNumber | bigint |  |  | SI | Dimension: DxPassportNumber<br/>
Source: PAPMIPAP... |
| DxPassportPlaceOfIssue | bigint |  |  | SI | Dimension: DxPassportPlaceOfIssue<br/>
Source: PA... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: PAPMIRowId.... |
| DxPensionType | bigint |  |  | SI | Dimension: DxPensionType<br/>
Source: PAPMIPensio... |
| DxPostalCode | bigint |  |  | SI | Dimension: DxPostalCode<br/>
Source: PAPMIRowId.P... |
| DxPostcode | bigint |  |  | SI | Dimension: DxPostcode<br/>
Source: PAPMIPAPERDR.P... |
| DxPreferredContactMethod | bigint |  |  | SI | Dimension: DxPreferredContactMethod<br/>
Source: ... |
| DxPrimaryLanguage | bigint |  |  | SI | Dimension: DxPrimaryLanguage<br/>
Source: PAPMIPr... |
| DxRace | bigint |  |  | SI | Dimension: DxRace<br/>
Source: PAPMIPAPERDR.PAPER... |
| DxReasonForAttention | bigint |  |  | SI | Dimension: DxReasonForAttention
Expression: "sour... |
| DxRegion | bigint |  |  | SI | Dimension: DxRegion
Expression: "sourceRegion" |
| DxRegistrationDay | varchar |  |  | SI | Dimension: DxRegistrationDay<br/>
Source: PAPMIRo... |
| DxRegistrationMonth | varchar |  |  | SI | Dimension: DxRegistrationMonth<br/>
Source: PAPMI... |
| DxRegistrationQuarter | varchar |  |  | SI | Dimension: DxRegistrationQuarter<br/>
Source: PAP... |
| DxRegistrationUser | bigint |  |  | SI | Dimension: DxRegistrationUser
Expression: "source... |
| DxRegistrationYear | varchar |  |  | SI | Dimension: DxRegistrationYear<br/>
Source: PAPMIR... |
| DxReligion | bigint |  |  | SI | Dimension: DxReligion<br/>
Source: PAPMIRowId.PAP... |
| DxResidencyStatus | bigint |  |  | SI | Dimension: DxResidencyStatus
Expression: "sourceR... |
| DxSocialStatus | bigint |  |  | SI | Dimension: DxSocialStatus<br/>
Source: PAPMIRowId... |
| DxSourceOfIncome | bigint |  |  | SI | Dimension: DxSourceOfIncome
Expression: "sourceSo... |
| DxState | bigint |  |  | SI | Dimension: DxState<br/>
Source: PAPMIRowId.PAPERC... |
| DxStayingPermanentlyStatus | bigint |  |  | SI | Dimension: DxStayingPermanentlyStatus
Expression:... |
| DxVIPStatus | bigint |  |  | SI | Dimension: DxVIPStatus
Expression: %expression.VI... |
| PatientPayor | bigint |  |  | SI | Dimension: PatientPayor<br/>
Source: PAPMIPAPERDR... |
| PatientPlan | bigint |  |  | SI | Dimension: PatientPlan<br/>
Source: PAPMIRowId.PA... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*