# web_Msg.LB_SecurityFunctionRule

**Schema:** web_Msg
**Columnas:** 37
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBSFR_AdditionalBloodGroupOverride | bit |  |  | SI | - |
| LBSFR_AllowChangeBilling | bit |  |  | SI | - |
| LBSFR_AllowCrossmatchOnProvGrp | bit |  |  | SI | - |
| LBSFR_AllowEditBloodProductDetails | bit |  |  | SI | - |
| LBSFR_AllowEmergencyIssue | bit |  |  | SI | - |
| LBSFR_AllowInstantReprint | bit |  |  | SI | - |
| LBSFR_AllowIssueExpiringBP | bit |  |  | SI | - |
| LBSFR_AllowIssueOnPosABScreen | bit |  |  | SI | - |
| LBSFR_AllowManualBloodGroupEntry | bit |  |  | SI | - |
| LBSFR_AllowMarkNotPerformed | bit |  |  | SI | - |
| LBSFR_AllowModifySpecimenSuitabilityPeriod | bit |  |  | SI | - |
| LBSFR_AllowPrintNonAuthorisedLabels | bit |  |  | SI | - |
| LBSFR_AuthoriseTestSetWorkGroups | varchar |  |  | SI | - |
| LBSFR_Department_DR | bigint |  | FK | SI | - |
| LBSFR_ForceBGVerification | bit |  |  | SI | - |
| LBSFR_LabSite_DR | bigint |  | FK | SI | - |
| LBSFR_PatientBloodGroupOverride | bit |  |  | SI | - |
| LBSFR_QCPromoteEvalToCurrent | bit |  |  | SI | - |
| LBSFR_QCUpdateBatchCloseDate | bit |  |  | SI | - |
| LBSFR_QCValuesOverride | bit |  |  | SI | - |
| LBSFR_RemoveFromExternalInterfaceQueue | bit |  |  | SI | - |
| LBSFR_RemoveFromHoldQueue | bit |  |  | SI | - |
| LBSFR_RemoveFromOutbreakQueue | bit |  |  | SI | - |
| LBSFR_RemoveFromSpecialInterestQueue | bit |  |  | SI | - |
| LBSFR_ReportPreview | bit |  |  | SI | - |
| LBSFR_Sequence | numeric |  |  | SI | - |
| LBSFR_TestSetAuthorise | bit |  |  | SI | - |
| LBSFR_TestSetAuthoriseExpiredValidity | bit |  |  | SI | - |
| LBSFR_TestSetDeAuthorise | bit |  |  | SI | - |
| LBSFR_TestSetValidate | bit |  |  | SI | - |
| LBSFR_TestSetValidateExpiredValidity | bit |  |  | SI | - |
| LBSFR_ValidateTestSetWorkGroups | varchar |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*