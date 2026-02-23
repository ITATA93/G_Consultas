# SQLUser.PA_RefPathwayStage

**Schema:** SQLUser
**Columnas:** 39
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| STG_ParRef | bigint | PK |  | NO | PA_ReferralPathway Parent Reference |
| STG_ActualWaitTime | double |  |  | SI | Actual Wait Time |
| STG_AlertState_DR | bigint |  | FK | SI | Alert State DR |
| STG_ApptCancelledDate | date |  |  | SI | ApptCancelledDate |
| STG_Childsub | double |  |  | NO | Childsub |
| STG_Comments | varchar |  |  | SI | Comments |
| STG_DateOwner | date |  |  | SI | DateOwner |
| STG_Desc | varchar |  |  | SI | Description |
| STG_Duration | double |  |  | SI | Duration |
| STG_EndDate | date |  |  | SI | EndDate |
| STG_EndTime | time |  |  | SI | EndTime |
| STG_Episode_DR | bigint |  | FK | SI | Episode DR |
| STG_ExcludedDays | double |  |  | SI | Excluded Days  |
| STG_ManualExcludedDays | double |  |  | SI | Stage Manual Excluded Days (only available if stag... |
| STG_OriginalEndDate | date |  |  | SI | Original End Date (corresbonding to STG_SequenceNu... |
| STG_PathwayManualExcludedDays | double |  |  | SI | Pathway Manual Excluded Days (only available if st... |
| STG_PlannedEndDate | date |  |  | SI | Planned End Date |
| STG_PlannedStartDate | date |  |  | SI | Planned Start Date |
| STG_ProjectedBreachDays | double |  |  | SI | Early/Late Days  |
| STG_ProjectedOrderEndDate | date |  |  | SI | ProjectedOrderEndDate |
| STG_ProjectedStartDate | date |  |  | SI | Projected Start Date |
| STG_ProjectedWaitTime | double |  |  | SI | Remaining Wait Time |
| STG_ReasonBreach | varchar |  |  | SI | Reason for Breach  |
| STG_RefTreatPathComplReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| STG_RefTreatPathReasonBreach_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathReasonBreach |
| STG_RowId | varchar |  |  | NO | - |
| STG_SequenceNumber | date |  |  | SI | SequenceNumber |
| STG_ShiftOfPlannedStartDate | double |  |  | SI | Shift Of Planned Start Date (Extension/Reduction o... |
| STG_StageOwner_DR | bigint |  | FK | SI | Des Ref SSUser |
| STG_StageStatus_DR | bigint |  | FK | SI | Current Stage Status |
| STG_StageTemplate_DR | bigint |  | FK | SI | Des Ref PACRefStageTemplate |
| STG_StartDate | date |  |  | SI | StartDate |
| STG_StartTime | time |  |  | SI | StartTime |
| STG_TargetEndDate | date |  |  | SI | Target End Date |
| STG_TimeOwner | time |  |  | SI | TimeOwner |
| STG_TotalCalendarDays | double |  |  | SI | Total Days  |
| STG_Type_DR | bigint |  | FK | SI | Des Ref Type |
| STG_WaitTimeExtServices_DR | bigint |  | FK | SI | Wait time external services DR |
| STG_WaitTimeForStageEnd | double |  |  | SI | Wait Time from appointment arrival/order result to... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*