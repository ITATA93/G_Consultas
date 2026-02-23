# Region_CLXX_Misc_Referral.SpecialtyRequest

**Schema:** Region_CLXX_Misc_Referral
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencias/Derivaciones**. Gestión de derivaciones entre centros.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| ApprovalDate | date |  |  | SI | - |
| ApprovalTime | date |  |  | SI | - |
| ApprovedBy_EMail | varchar |  |  | SI | - |
| ApprovedBy_Names | varchar |  |  | SI | - |
| ApprovedBy_NationalId | varchar |  |  | SI | - |
| ApprovedBy_PhoneNumber | varchar |  |  | SI | - |
| ApprovedBy_PhoneNumber2 | varchar |  |  | SI | - |
| ApprovedBy_PhoneNumber3 | varchar |  |  | SI | - |
| ApprovedBy_PhoneNumber4 | varchar |  |  | SI | - |
| ApprovedBy_Surname1 | varchar |  |  | SI | - |
| ApprovedBy_Surname2 | varchar |  |  | SI | - |
| DestinationFacilityCode | varchar |  |  | SI | Esta propiedad, cuando presente, se ocupará en lug... |
| DiagnosisCode | varchar |  |  | SI | - |
| DiagnosisCodingSystem | varchar |  |  | SI | - |
| DiagnosisControlLevel | integer |  |  | SI | - |
| DiagnosisRemarks | varchar |  |  | SI | - |
| EpisodeComplexityLevelCode | varchar |  |  | SI | - |
| EpisodePriorityCode | varchar |  |  | SI | - |
| GeneralData | varchar |  |  | SI | - |
| HealthProblemCode | varchar |  |  | SI | - |
| OriginatingFacilityCode | varchar |  |  | SI | - |
| OriginatingReferralCode | varchar |  |  | SI | - |
| OriginatingRegionCode | varchar |  |  | SI | - |
| OriginatingSpecialtyCode | varchar |  |  | SI | - |
| OriginatingSystemCode | varchar |  |  | SI | - |
| Patient_Address_Address | varchar |  |  | SI | - |
| Patient_Address_CityCode | varchar |  |  | SI | - |
| Patient_Address_ProvinceCode | varchar |  |  | SI | - |
| Patient_Address_RegionCode | varchar |  |  | SI | - |
| Patient_CountryOfBirthCode | varchar |  |  | SI | - |
| Patient_DateOfBirth | date |  |  | SI | - |
| Patient_EMail | varchar |  |  | SI | - |
| Patient_EthnicGroupCode | varchar |  |  | SI | - |
| Patient_HealthCareProviderCode | varchar |  |  | SI | - |
| Patient_IsNewBorn | bit |  |  | SI | - |
| Patient_MRN | varchar |  |  | SI | - |
| Patient_MaritalStatusCode | varchar |  |  | SI | - |
| Patient_Names | varchar |  |  | SI | - |
| Patient_NationalId | varchar |  |  | SI | - |
| Patient_PRAIS | bit |  |  | SI | - |
| Patient_ParentNationalId | varchar |  |  | SI | - |
| Patient_PassportNumber | varchar |  |  | SI | - |
| Patient_PhoneNumber | varchar |  |  | SI | - |
| Patient_PhoneNumber2 | varchar |  |  | SI | - |
| Patient_PhoneNumber3 | varchar |  |  | SI | - |
| Patient_PhoneNumber4 | varchar |  |  | SI | - |
| Patient_ReligionCode | varchar |  |  | SI | - |
| Patient_SexCode | varchar |  |  | SI | - |
| Patient_Surname1 | varchar |  |  | SI | - |
| Patient_Surname2 | varchar |  |  | SI | - |
| Patient_TimeOfBirth | time |  |  | SI | - |
| ReferralDate | date |  |  | SI | - |
| ReferralReasonCode | varchar |  |  | SI | - |
| ReferralTime | time |  |  | SI | - |
| Remarks | varchar |  |  | SI | - |
| RequestingCareProvider_EMail | varchar |  |  | SI | - |
| RequestingCareProvider_Names | varchar |  |  | SI | - |
| RequestingCareProvider_NationalId | varchar |  |  | SI | - |
| RequestingCareProvider_PhoneNumber | varchar |  |  | SI | - |
| RequestingCareProvider_PhoneNumber2 | varchar |  |  | SI | - |
| RequestingCareProvider_PhoneNumber3 | varchar |  |  | SI | - |
| RequestingCareProvider_PhoneNumber4 | varchar |  |  | SI | - |
| RequestingCareProvider_Surname1 | varchar |  |  | SI | - |
| RequestingCareProvider_Surname2 | varchar |  |  | SI | - |
| SpecialtyCode | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*