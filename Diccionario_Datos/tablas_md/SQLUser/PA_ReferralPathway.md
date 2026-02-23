# SQLUser.PA_ReferralPathway

**Schema:** SQLUser
**Columnas:** 44
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RFPW_RowId | bigint | PK |  | NO | - |
| RFPW_ActualWaitTime | double |  |  | SI | ActualWaitTime |
| RFPW_AlertState_DR | bigint |  | FK | SI | AlarmStateDR |
| RFPW_BreachAllowed | varchar |  |  | SI | Breach Allowed |
| RFPW_CancerConfirm | varchar |  |  | SI | Cancer Confirm |
| RFPW_CancerConfirmDate | date |  |  | SI | Cancer Confirm Date |
| RFPW_CancerConfirmTime | time |  |  | SI | TimeMarkedAsCancer |
| RFPW_CancerReferral | varchar |  |  | SI | Cancer Referral indicates if the pathway is a canc... |
| RFPW_CancerTreatAgreeDate | date |  |  | SI | Cancer Treatment Agreement Date |
| RFPW_CancerTreatAgreeTime | time |  |  | SI | Cancer Treatment Agreement Time |
| RFPW_Comments | varchar |  |  | SI | Comments |
| RFPW_Desc | varchar |  |  | SI | Description |
| RFPW_Diagnos_DR | varchar |  | FK | SI | RFPWDiagnosisDR |
| RFPW_Duration | double |  |  | SI | Duration |
| RFPW_EndDate | date |  |  | SI | EndDate |
| RFPW_EndTime | time |  |  | SI | EndTime |
| RFPW_ExcludedDays | double |  |  | SI | Excluded Days |
| RFPW_GES | varchar |  |  | SI | GES |
| RFPW_LatestStgPlanEndDate | date |  |  | SI | Latest planned end date (STG_PlanendEndDate) of th... |
| RFPW_NonCancerConfirm | varchar |  |  | SI | Non Cancer Confirm |
| RFPW_NonCancerConfirmDate | date |  |  | SI | Non Cancer Confirm Date |
| RFPW_NonCancerConfirmTime | date |  |  | SI | Non Cancer Confirm Time |
| RFPW_OPOutcome_DR | bigint |  | FK | SI | Des Ref PACWLTriageOutcome |
| RFPW_OriginalEndDate | date |  |  | SI | Original End Date |
| RFPW_PathwayOwner_DR | bigint |  | FK | SI | Des Ref SSUser |
| RFPW_PathwayReviewedBy_DR | bigint |  | FK | SI | Pathway Reviewed By |
| RFPW_PathwayReviewedDate | date |  |  | SI | Pathway Reviewed Date |
| RFPW_Patient_DR | bigint |  | FK | SI | Des Ref PAPMI |
| RFPW_PlannedEndDate | date |  |  | SI | Planned End Date |
| RFPW_ProjectedBreachDays | double |  |  | SI | Early/Late Days  |
| RFPW_ProjectedWaitTime | double |  |  | SI | Remaining Wait Time |
| RFPW_Qualifier_DR | bigint |  | FK | SI | Source of Referral Qualifier |
| RFPW_ReasonBreach | varchar |  |  | SI | Reason for Breach  |
| RFPW_RefTreatPathComplReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| RFPW_RefTreatPathRTTStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| RFPW_RefTreatPathReasonBreach_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathReasonBreach |
| RFPW_StartDate | date |  |  | SI | StartDate |
| RFPW_StartTime | time |  |  | SI | StartTime |
| RFPW_TargetEndDate | date |  |  | SI | Target End Date |
| RFPW_Template_DR | bigint |  | FK | SI | Referral Template |
| RFPW_TreatPathReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| RFPW_UCPN | varchar |  |  | SI | UCPN |
| RFPW_VettingOutcome_DR | bigint |  | FK | SI | Des Ref PACWLTriageOutcome |
| RFPW_WLEntriesRemoved | varchar |  |  | SI | WLEntriesRemoved |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*