# TC_hmf_IHE.DocumentType

**Schema:** TC_hmf_IHE
**Columnas:** 33
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| IHEDOCTYP_BaseTable | varchar |  |  | SI | HMF SDA Transform Base Table |
| IHEDOCTYP_ClassCode | varchar |  |  | SI | HS XSLT Class Code |
| IHEDOCTYP_Code | varchar |  |  | SI | Code |
| IHEDOCTYP_ConfidentialityCode | varchar |  |  | SI | HS XSLT Confidentiality Code |
| IHEDOCTYP_ContentTypeCode | varchar |  |  | SI | HS XSLT Content Type Code |
| IHEDOCTYP_CreateClass | varchar |  |  | SI | HMF SDA Transform Class |
| IHEDOCTYP_DateFrom | date |  |  | SI | Date From |
| IHEDOCTYP_DateTo | date |  |  | SI | Date To |
| IHEDOCTYP_Desc | varchar |  |  | SI | Description |
| IHEDOCTYP_FormatCode | varchar |  |  | SI | HS XSLT Format Code |
| IHEDOCTYP_HSTransformXSLT | varchar |  |  | SI | HS XSLT Transformation |
| IHEDOCTYP_HealthcareFacilityTypeCode | varchar |  |  | SI | HS XSLT Healthcare Facility Type Code |
| IHEDOCTYP_IncAlertFlag | bit |  |  | SI | Include Alert Flag |
| IHEDOCTYP_IncAllergyFlag | bit |  |  | SI | Include Allergy Flag |
| IHEDOCTYP_IncApptFlag | bit |  |  | SI | Include Appointments Flag |
| IHEDOCTYP_IncDiagnosFlag | bit |  |  | SI | Include Diagnosis Flag |
| IHEDOCTYP_IncEncReasonFlag | bit |  |  | SI | Include Reason For Encounter Flag |
| IHEDOCTYP_IncEpisodeFlag | bit |  |  | SI | Include Episode Flag |
| IHEDOCTYP_IncMedFlag | bit |  |  | SI | Include Medications Flag |
| IHEDOCTYP_IncObsFlag | bit |  |  | SI | Include Observations Flag |
| IHEDOCTYP_IncOrderFlag | bit |  |  | SI | Include Orders Flag |
| IHEDOCTYP_IncProblemFlag | bit |  |  | SI | Include Problems Flag |
| IHEDOCTYP_IncProcFlag | bit |  |  | SI | Include Procedures Flag |
| IHEDOCTYP_IncSocHisFlag | bit |  |  | SI | Include Social History Flag |
| IHEDOCTYP_IncVacFlag | bit |  |  | SI | Include Vaccinations Flag |
| IHEDOCTYP_LanguageCode | varchar |  |  | SI | HS XSLT Language Code |
| IHEDOCTYP_MimeType | varchar |  |  | SI | HS XSLT Mime Type |
| IHEDOCTYP_Owner | varchar |  |  | SI | Owner - Standard Type Item EditionOwnerType |
| IHEDOCTYP_PracticeSettingCode | varchar |  |  | SI | HS XSLT Practice Setting Code |
| IHEDOCTYP_Profile | varchar |  |  | SI | IHE Profile |
| IHEDOCTYP_TypeCodeTypeCode | varchar |  |  | SI | HS XSLT Type Code |
| IHEDOCTYP_UseCSFlags | bit |  |  | SI | Use CS Report Flags |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*