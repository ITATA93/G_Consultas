# SQLUser.RBC_OutcomeOfAppoint

**Schema:** SQLUser
**Columnas:** 51
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de RB**. Parámetros de módulos RB.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OUTC_RowId | bigint | PK |  | NO | - |
| OUTC_AssociatedAction | varchar |  |  | SI | Associated Action |
| OUTC_AttendanceClass | varchar |  |  | SI | Attendance Class |
| OUTC_CancerTreatAgree | varchar |  |  | SI | Cancer Treatment Agreed |
| OUTC_Code | varchar |  |  | NO | Code |
| OUTC_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| OUTC_ConfirmCancer | varchar |  |  | SI | Confirimed Cancer |
| OUTC_CreatePathway | varchar |  |  | SI | Create New Pathway |
| OUTC_CreateTask | varchar |  |  | SI | Create Task |
| OUTC_CreateWL | varchar |  |  | SI | Create WL |
| OUTC_CreatedDate | date |  |  | SI | Created Date |
| OUTC_CreatedTime | time |  |  | SI | Created Time |
| OUTC_CreatedUser_DR | bigint |  | FK | SI | Created User |
| OUTC_DateFrom | date |  |  | SI | Date From |
| OUTC_DateTo | date |  |  | SI | Date To |
| OUTC_DefWaitListLocation_DR | bigint |  | FK | SI | Default waiting list location for newly created wa... |
| OUTC_DefWaitListPrior_DR | bigint |  | FK | SI | Default waiting list priority for newly created wa... |
| OUTC_DefWaitListType_DR | bigint |  | FK | SI | Default waiting list type for newly created waitin... |
| OUTC_Desc | varchar |  |  | NO | Description |
| OUTC_DischargeFlag | varchar |  |  | SI | Discharge Flag |
| OUTC_LaunchOE | varchar |  |  | SI | Launch OEOrder.Custom |
| OUTC_LaunchQuestionnaire | varchar |  |  | SI | Launch Questionnaire |
| OUTC_LaunchWL | varchar |  |  | SI | Launch PAWaitingList.Edit |
| OUTC_LetterTemplate_DR | bigint |  | FK | SI | Des Ref Letter Template |
| OUTC_LetterType_DR | bigint |  | FK | SI | Des Ref Letter Type |
| OUTC_Module_DR | bigint |  | FK | SI | Des Ref Module |
| OUTC_NationalCode | varchar |  |  | SI | National Code |
| OUTC_NonCancer | varchar |  |  | SI | Non Cancer |
| OUTC_OutcomeType | varchar |  |  | SI | Outcome Type |
| OUTC_Owner | varchar |  |  | SI | Owner |
| OUTC_QuesErrorReason_DR | bigint |  | FK | SI | Questionnaire Error Reason |
| OUTC_Questionnaire_DR | bigint |  | FK | SI | Des Ref SSUserDefWindow |
| OUTC_RTTOutcome | varchar |  |  | SI | RTT Outcome |
| OUTC_RefTreatPathRTTStatus_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathRTTStatus |
| OUTC_RemoveAppWL | varchar |  |  | SI | RemoveAppWL |
| OUTC_RemoveWL | varchar |  |  | SI | Remove WL |
| OUTC_SinglePatientOnly | varchar |  |  | SI | Single Patient Outcome only |
| OUTC_StageStart_DR | bigint |  | FK | SI | Des Ref PACRefTemplateStageType |
| OUTC_StageStop_DR | bigint |  | FK | SI | Des Ref PACRefTemplateStageType |
| OUTC_StopPath | varchar |  |  | SI | StopPath |
| OUTC_StopStage | varchar |  |  | SI | Stop Stage |
| OUTC_Task_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| OUTC_TreatPathReason_DR | bigint |  | FK | SI | Des Ref PACRefTreatPathCompleteReason |
| OUTC_UDF | varchar |  |  | SI | UDF |
| OUTC_UpdatedDate | date |  |  | SI | Updated Date |
| OUTC_UpdatedTime | time |  |  | SI | Updated Time |
| OUTC_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| OUTC_WLNotAvail_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| OUTC_WLReinstateReason_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| OUTC_WLRemoveReason_DR | bigint |  | FK | SI | Des Ref PACWLReasonNotAvail |
| OUTC_WLStatus_DR | bigint |  | FK | SI | Des Ref WLStatus |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*