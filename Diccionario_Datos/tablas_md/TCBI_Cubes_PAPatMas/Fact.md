# TCBI_Cubes_PAPatMas.Fact

**Schema:** TCBI_Cubes_PAPatMas
**Columnas:** 77
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**TrakCare BI Cube**. Cubo OLAP para análisis de datos clínicos y operacionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| %dspartition | integer |  |  | SI | This indicates which partition (set of 1M) this fa... |
| %sourceId | bigint |  |  | SI | Reference to original data in source table. |
| Dx1298366053 | varchar |  |  | SI | Dimension: Dx1298366053<br/>
Source: PAPMIRowId.P... |
| Dx1423654878 | varchar |  |  | SI | Dimension: Dx1423654878<br/>
Source: PAPMIRowId.P... |
| Dx1575787577 | date |  |  | SI | Dimension: Dx1575787577<br/>
Source: PAPMIRowId.P... |
| Dx1621928670 | varchar |  |  | SI | Dimension: Dx1621928670<br/>
Source: PAPMIRowId.P... |
| Dx2710215734 | varchar |  |  | SI | Dimension: Dx2710215734<br/>
Source: PAPMIRowId.P... |
| Dx2871807861 | varchar |  |  | SI | Dimension: Dx2871807861<br/>
Source: PAPMIRowId.P... |
| Dx3016719288 | varchar |  |  | SI | Dimension: Dx3016719288<br/>
Source: PAPMIDecease... |
| Dx3019049172 | varchar |  |  | SI | Dimension: Dx3019049172<br/>
Source: PAPMIDecease... |
| Dx3367631356 | varchar |  |  | SI | Dimension: Dx3367631356<br/>
Source: PAPMIDecease... |
| Dx3572449163 | varchar |  |  | SI | Dimension: Dx3572449163<br/>
Source: PAPMIRowId.P... |
| Dx578469394 | varchar |  |  | SI | Dimension: Dx578469394<br/>
Source: PAPMIDeceased... |
| Dx609229743 | varchar |  |  | SI | Dimension: Dx609229743<br/>
Source: PAPMIDeceased... |
| DxAccommodationSetting | bigint |  |  | SI | Dimension: DxAccommodationSetting<br/>
Source: PA... |
| DxAdditionalBloodGroup | varchar |  |  | SI | Dimension: DxAdditionalBloodGroup
Expression: %cu... |
| DxBirthGender | bigint |  |  | SI | Dimension: DxBirthGender<br/>
Source: PAPMIPAPERD... |
| DxBloodGroup | bigint |  |  | SI | Dimension: DxBloodGroup<br/>
Source: PAPMIPAPERDR... |
| DxBloodGroupAntibodies | varchar |  |  | SI | Dimension: DxBloodGroupAntibodies
Expression: %cu... |
| DxBloodGroupStatus | bigint |  |  | SI | Dimension: DxBloodGroupStatus
Expression: %expres... |
| DxCardType | bigint |  |  | SI | Dimension: DxCardType<br/>
Source: PAPMICardTypeD... |
| DxCitizenship | bigint |  |  | SI | Dimension: DxCitizenship<br/>
Source: PAPMIRowId.... |
| DxCity | bigint |  |  | SI | Dimension: DxCity
Expression: %source.PAPMIRowId.... |
| DxCityArea | bigint |  |  | SI | Dimension: DxCityArea<br/>
Source: PAPMIRowId.PAP... |
| DxCommunicationPreference | bigint |  |  | SI | Dimension: DxCommunicationPreference
Expression: ... |
| DxCommunityHealthStatus | bigint |  |  | SI | Dimension: DxCommunityHealthStatus<br/>
Source: P... |
| DxCountry | bigint |  |  | SI | Dimension: DxCountry<br/>
Source: PAPMIRowId.PAPE... |
| DxCountryOfBirth | bigint |  |  | SI | Dimension: DxCountryOfBirth<br/>
Source: PAPMIPAP... |
| DxDeceased | bigint |  |  | SI | Dimension: DxDeceased<br/>
Source: PAPMIDeceased |
| DxEmployeeType | bigint |  |  | SI | Dimension: DxEmployeeType<br/>
Source: PAPMIRowId... |
| DxEmploymentStatus | bigint |  |  | SI | Dimension: DxEmploymentStatus<br/>
Source: PAPMIR... |
| DxEthnicity | varchar |  |  | SI | Dimension: DxEthnicity
Expression: %cube.GetEthni... |
| DxGPClinic | bigint |  |  | SI | Dimension: DxGPClinic<br/>
Source: PAPMIPAPERDR.P... |
| DxGPName | bigint |  |  | SI | Dimension: DxGPName<br/>
Source: PAPMIPAPERDR.PAP... |
| DxGender | bigint |  |  | SI | Dimension: DxGender<br/>
Source: PAPMISexDR.CTSEX... |
| DxGenderIdentity | bigint |  |  | SI | Dimension: DxGenderIdentity<br/>
Source: PAPMIPAP... |
| DxHasAlerts | bigint |  |  | SI | Dimension: DxHasAlerts
Expression: %cube.HasAlert... |
| DxHasAllergies | bigint |  |  | SI | Dimension: DxHasAllergies
Expression: %cube.HasAl... |
| DxHealthCareArea | bigint |  |  | SI | Dimension: DxHealthCareArea<br/>
Source: PAPMIRow... |
| DxHospital | bigint |  |  | SI | Dimension: DxHospital
Expression: %cube.GetRegist... |
| DxIndigenousStatus | bigint |  |  | SI | Dimension: DxIndigenousStatus<br/>
Source: PAPMII... |
| DxInsuranceCategory | bigint |  |  | SI | Dimension: DxInsuranceCategory<br/>
Source: PAPMI... |
| DxInterpreterRequired | bigint |  |  | SI | Dimension: DxInterpreterRequired<br/>
Source: PAP... |
| DxIsRegisteredPatient | bigint |  |  | SI | Dimension: DxIsRegisteredPatient
Expression: %cub... |
| DxLivingArrangement | bigint |  |  | SI | Dimension: DxLivingArrangement<br/>
Source: PAPMI... |
| DxMaritalStatus | bigint |  |  | SI | Dimension: DxMaritalStatus<br/>
Source: PAPMIRowI... |
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
Expression: %cube.PD... |
| DxPatientPayor | bigint |  |  | SI | Dimension: DxPatientPayor<br/>
Source: PAPMIRowId... |
| DxPatientPlan | bigint |  |  | SI | Dimension: DxPatientPlan<br/>
Source: PAPMIRowId.... |
| DxPatientType | bigint |  |  | SI | Dimension: DxPatientType<br/>
Source: PAPMIRowId.... |
| DxPensionType | bigint |  |  | SI | Dimension: DxPensionType<br/>
Source: PAPMIPensio... |
| DxPostalCode | bigint |  |  | SI | Dimension: DxPostalCode<br/>
Source: PAPMIRowId.P... |
| DxPrimaryLanguage | bigint |  |  | SI | Dimension: DxPrimaryLanguage<br/>
Source: PAPMIPr... |
| DxRace | bigint |  |  | SI | Dimension: DxRace<br/>
Source: PAPMIPAPERDR.PAPER... |
| DxReasonForAttention | bigint |  |  | SI | Dimension: DxReasonForAttention
Expression: %cube... |
| DxRegion | bigint |  |  | SI | Dimension: DxRegion<br/>
Source: PAPMIRowId.PAPER... |
| DxRegistrationUser | bigint |  |  | SI | Dimension: DxRegistrationUser<br/>
Source: PAPMIR... |
| DxReligion | bigint |  |  | SI | Dimension: DxReligion<br/>
Source: PAPMIRowId.PAP... |
| DxResidencyStatus | bigint |  |  | SI | Dimension: DxResidencyStatus<br/>
Source: PAPMIRo... |
| DxSocialStatus | bigint |  |  | SI | Dimension: DxSocialStatus<br/>
Source: PAPMIRowId... |
| DxSourceOfIncome | bigint |  |  | SI | Dimension: DxSourceOfIncome<br/>
Source: PAPMIPAP... |
| DxState | bigint |  |  | SI | Dimension: DxState
Expression: %cube.GetState(%so... |
| DxStayingPermanentlyStatus | bigint |  |  | SI | Dimension: DxStayingPermanentlyStatus
Expression:... |
| DxVIPStatus | bigint |  |  | SI | Dimension: DxVIPStatus
Expression: %cube.GetVIPFl... |
| Mx51580404I | integer |  |  | SI | Measure: Mx51580404I
Expression: %cube.GetEpisode... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*