# lab.CT_TestCode

**Schema:** lab
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTTC_RowId | varchar | PK |  | NO | - |
| CTTC_ALPHAUPDesc | varchar |  |  | SI | ALPHAUP Desc |
| CTTC_ALPHAUPNationalNameLong | varchar |  |  | SI | ALPHAUP NationalNumberLong |
| CTTC_ALPHAUPNationalNameShort | varchar |  |  | SI | ALPHAUP NationalNumberShort |
| CTTC_ALPHAUPNationalNumber | varchar |  |  | SI | ALPHAUP NationalNumber |
| CTTC_ALPHAUPSynonym | varchar |  |  | SI | ALPHAUP Synonym |
| CTTC_ActiveFlag | varchar |  |  | SI | Active Flag |
| CTTC_Activity_DR | varchar |  | FK | SI | Activity DR |
| CTTC_Code | varchar |  |  | NO | Code |
| CTTC_ComboBox | varchar |  |  | SI | Combo Box |
| CTTC_DeltaCheckForSC | varchar |  |  | SI | Delta check for Standard comments |
| CTTC_DeltaHoursFrom | double |  |  | SI | Delta Hours from |
| CTTC_DeltaHoursTo | double |  |  | SI | Delta Hours to |
| CTTC_Department_DR | varchar |  | FK | SI | Department |
| CTTC_Desc | varchar |  |  | SI | Data Item Name |
| CTTC_DisallowedDeltaCheck | varchar |  |  | SI | Disallowed Delta Check |
| CTTC_DownsAffectedMean | double |  |  | SI | Downs Affected Mean |
| CTTC_DownsAffectedSD | double |  |  | SI | Downs Affected SD |
| CTTC_DownsUnAffectedMean | double |  |  | SI | Downs UnAffected Mean |
| CTTC_DownsUnAffectedSD | double |  |  | SI | Downs UnAffected SD |
| CTTC_Group | varchar |  |  | SI | Test Item Group |
| CTTC_Hidden | varchar |  |  | SI | Hidden result |
| CTTC_LengthTimePrevResult | varchar |  |  | SI | Length of Time to Notify of Previous Result |
| CTTC_NationalNameLong | varchar |  |  | SI | National Name Long |
| CTTC_NationalNameShort | varchar |  |  | SI | National Name Short |
| CTTC_NationalNumber | varchar |  |  | SI | National Number |
| CTTC_ResultCopy | varchar |  |  | SI | Result Copy |
| CTTC_ResultFormat | varchar |  |  | SI | Result Format |
| CTTC_ResultLength | double |  |  | SI | Result Length |
| CTTC_SMSEnabled | varchar |  |  | SI | SMS Enabled |
| CTTC_SOPFile | varchar |  |  | SI | SOP File |
| CTTC_SOPShort | varchar |  |  | SI | SOP Short |
| CTTC_ShowInCummulative | varchar |  |  | SI | Show In Cummulative |
| CTTC_SignificantFigures | double |  |  | SI | Significant Figures |
| CTTC_Synonym | varchar |  |  | SI | Synonym |
| CTTC_TestMethod_DR | varchar |  | FK | SI | Test Method |
| CTTC_TotalCounter | varchar |  |  | SI | Total Counter |
| CTTC_Units | varchar |  |  | SI | Units |
| CTTC_Welcan | varchar |  |  | SI | Welcan Units |
| CTTC_xxx1 | varchar |  |  | SI | Delta OutPatient Value Absolute |
| CTTC_xxx10 | varchar |  |  | SI | Delta OutPatient Value Rate |
| CTTC_xxx12 | varchar |  |  | SI | Delta Value Percentage Rate |
| CTTC_xxx13 | varchar |  |  | SI | Delta Value Percentage Rate Asc |
| CTTC_xxx14 | varchar |  |  | SI | Delta Value Percentage Rate Dsc |
| CTTC_xxx2 | varchar |  |  | SI | Delta OutPatient Value Absolute Asc |
| CTTC_xxx23 | varchar |  |  | SI | Delta InPatient Value Percentage |
| CTTC_xxx24 | varchar |  |  | SI | Delta InPatient Value Percentage Asc |
| CTTC_xxx25 | varchar |  |  | SI | Delta InPatient Value Percentage Dsc |
| CTTC_xxx26 | varchar |  |  | SI | Delta InPatient Value Percentage Rate |
| CTTC_xxx27 | varchar |  |  | SI | Delta InPatient Value Percentage Rate Asc |
| CTTC_xxx28 | varchar |  |  | SI | Delta InPatient Value Percentage Rate Dsc |
| CTTC_xxx3 | varchar |  |  | SI | Delta OutPatient Value Absolute Dsc |
| CTTC_xxx30 | varchar |  |  | SI | Delta InPatient Value Rate Asc |
| CTTC_xxx31 | varchar |  |  | SI | Delta InPatient Value Rate Dsc |
| CTTC_xxx4 | varchar |  |  | SI | Delta OutPatient Value Percentage |
| CTTC_xxx5 | varchar |  |  | SI | Delta OutPatient Value Percentage Asc |
| CTTC_xxx6 | varchar |  |  | SI | Delta OutPatient Value Percentage Dsc |
| CTTC_xxx7 | varchar |  |  | SI | Delta OutPatient Value Percentage Rate |
| CTTC_xxx8 | varchar |  |  | SI | Delta OutPatient Value Percentage Rate Asc |
| CTTC_xxx9 | varchar |  |  | SI | Delta OutPatient Value Percentage Rate Dsc |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*