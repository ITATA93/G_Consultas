# SQLUser.PA_RefPathwayEv

**Schema:** SQLUser
**Columnas:** 35
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EV_ParRef | bigint | PK |  | NO | PA_ReferralPathway Parent Reference |
| EV_BreachAllowed | varchar |  |  | SI | Breach Allowed |
| EV_CancerConfirm | varchar |  |  | SI | Cancer Confirm |
| EV_CancerConfirmDate | date |  |  | SI | DateMarkedAsCancer |
| EV_CancerConfirmTime | time |  |  | SI | TimeMarkedAsCancer |
| EV_CancerNonConfirm | varchar |  |  | SI | Cancer Confirm |
| EV_CancerNonConfirmDate | date |  |  | SI | Cancer Non Confirm Date  |
| EV_CancerNonConfirmTime | time |  |  | SI | Cancer Non Confirm Time  |
| EV_CancerReferral | varchar |  |  | SI | CancerReferral |
| EV_CancerTreatAgreeDate | date |  |  | SI | DateMarkedAsCancer |
| EV_CancerTreatAgreeTime | time |  |  | SI | TimeMarkedAsCancer |
| EV_Childsub | double |  |  | NO | Childsub |
| EV_Comments | varchar |  |  | SI | Comments |
| EV_Desc | varchar |  |  | SI | Description |
| EV_Duration | double |  |  | SI | Duration |
| EV_EndDate | date |  |  | SI | EndDate |
| EV_EndTime | time |  |  | SI | EndTime |
| EV_EventAction | varchar |  |  | SI | EventAction |
| EV_EventDate | date |  |  | SI | EventDate |
| EV_EventTime | time |  |  | SI | EventTime |
| EV_EventUser_DR | bigint |  | FK | SI | Des Ref SSUser |
| EV_PathwayOwner_DR | bigint |  | FK | SI | Des Ref SSUser |
| EV_PathwayReviewedBy_DR | bigint |  | FK | SI | Pathway Reviewed By |
| EV_PathwayReviewedDate | date |  |  | SI | Pathway Reviewed Date |
| EV_Qualifier_DR | bigint |  | FK | SI | Source of Referral Qualifier |
| EV_ReasonBreach | varchar |  |  | SI | Reason for Breach  |
| EV_RefTreatPathComplReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| EV_RefTreatPathRTTStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| EV_RefTreatPathReasonBreach_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathReasonBreach |
| EV_RowId | varchar |  |  | NO | - |
| EV_StartDate | date |  |  | SI | StartDate |
| EV_StartTime | time |  |  | SI | StartTime |
| EV_Template_DR | bigint |  | FK | SI | Referral Template |
| EV_TreatPathReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| EV_UCPN | varchar |  |  | SI | UCPN |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*