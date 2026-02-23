# web_Msg.PA_PathwayItem

**Schema:** web_Msg
**Columnas:** 102
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Datos de Paciente**. Información demográfica y administrativa. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| Included | bit |  |  | SI | Indicates that the item is in or will be added to ... |
| MsgITM2DurationType | varchar |  |  | SI | Duration Type for Order Item Default from NCP goal... |
| MsgITM2DurationUnit | varchar |  |  | SI | Duration Unit for Order Item Default from NCP goal... |
| MsgITM2DurationValue | varchar |  |  | SI | Duration Value for Order Item Default from NCP goa... |
| MsgITM2FreeTextFreqUnit | varchar |  |  | SI | Free Text Frequency Unit for Order Item Default fr... |
| MsgITM2FreeTextFreqValue | varchar |  |  | SI | Free Text Frequency for Order Item Default from NC... |
| MsgITM2PRNFlag | varchar |  |  | SI | PRN Flag for Order Item Default from NCP goal or a... |
| MsgOEORIEndDate | date |  |  | SI | Duration End Date used with Until Clause |
| MsgOEORIEndTime | time |  |  | SI | Duration End Time used with Until Clause |
| MsgOEORIQty | varchar |  |  | SI | Frequency Quantity for Order Item Default from NCP... |
| MsgParRef | varchar |  |  | SI | Parent Reference to web.Msg.PAPathway, not User.PA... |
| MsgParentItem_DR | varchar |  | FK | SI | Parent item to web.Msg.PAPathwayItem, not User.PAP... |
| MsgPrefParams_DR | bigint |  | FK | SI | Order Item Default from NCP goal or activity |
| MsgRMFrequency | bigint |  |  | SI | Frequency for Order Item Default from NCP goal or ... |
| NRC_Problem_DR | bigint |  | FK | SI | NRCProblem DR -- Not held in User.PAPathway |
| PATHI_Antecedent_DR | varchar |  | FK | SI | Antecedent |
| PATHI_AutoOrder | varchar |  |  | SI | Order Automatically |
| PATHI_CarePlanStatus | varchar |  |  | SI | Care Plan Status -- for Care Plan module |
| PATHI_ChangeReason | varchar |  |  | SI | Reason for Change |
| PATHI_ChangedBy_DR | bigint |  | FK | SI | Changed By |
| PATHI_ChangedDate | date |  |  | SI | Changed Date |
| PATHI_Childsub | double |  |  | SI | Childsub |
| PATHI_Consent | bigint |  |  | SI | Patient Consent |
| PATHI_ConsentDate | date |  |  | SI | Patient Consent Received Date |
| PATHI_ConsentGiven | bit |  |  | SI | Patient Consent Received |
| PATHI_ConsentTime | time |  |  | SI | Patient Consent Received Time |
| PATHI_CopyCycleOrders | varchar |  |  | SI | [DEPRECATED]Cycle changes are now marked for carry... |
| PATHI_CreatedByWizard | bit |  |  | SI | Whether the pathway item was created by the NCP Wi... |
| PATHI_CreatedBy_DR | bigint |  | FK | SI | Created By |
| PATHI_CreatedDate | date |  |  | SI | Created Date |
| PATHI_CycleDur | double |  |  | SI | Cycle Period |
| PATHI_CycleDurType | varchar |  |  | SI | Cycle Period Type |
| PATHI_CycleFlag | bit |  |  | SI | Cycle Flag |
| PATHI_CycleReps | double |  |  | SI | Cycle Repetitions |
| PATHI_DeletedBy_DR | bigint |  | FK | SI | Deleted By |
| PATHI_DeletedDate | date |  |  | SI | Deleted Date |
| PATHI_Desc | varchar |  |  | SI | Description |
| PATHI_DescComputed | bit |  |  | SI | Item Description Computed
1 - the item descriptio... |
| PATHI_DirectlyExecute | varchar |  |  | SI | Directly Execute |
| PATHI_DoNotConsolidate | bit |  |  | SI | Do not consolidate |
| PATHI_EndedBy_DR | bigint |  | FK | SI | Ended By |
| PATHI_EndedDate | date |  |  | SI | Ended Date |
| PATHI_EndedFromWizard | bit |  |  | SI | Ended from the NCP Wizard (Plan in progress) |
| PATHI_EndedTime | time |  |  | SI | Ended Time |
| PATHI_Episode_DR | bigint |  | FK | SI | Episode |
| PATHI_HasAdditionalOrderItems | bit |  |  | SI | Flag to mark whether the underlying order item, or... |
| PATHI_HasDiscontinuedOrders | bit |  |  | SI | Has Discontinued Orders |
| PATHI_HistVac | bit |  |  | SI | Flag indicating if a Historical Vaccination exists |
| PATHI_IsAdhoc | bit |  |  | SI | Flags an adhoc item added to a Pathway |
| PATHI_ItmMast_DR | varchar |  | FK | SI | Order Item |
| PATHI_LinkedOrderItem_DR | varchar |  | FK | SI | Order Item that has been manually linked to the Pa... |
| PATHI_ListType | varchar |  |  | SI | Type of List |
| PATHI_LongDescription | varchar |  |  | SI | Long description -- for items containing descripti... |
| PATHI_NCPType | varchar |  |  | SI | NCP Item Type -- for Care Plan Module |
| PATHI_NRInterventionActivity_DR | varchar |  | FK | SI | Nursing Intervention Activity DR |
| PATHI_NRIntervention_DR | bigint |  | FK | SI | Nursing Intervention DR |
| PATHI_NROutcome_DR | bigint |  | FK | SI | Nursing Outcome DR |
| PATHI_Note | varchar |  |  | SI | Recommendation Note |
| PATHI_NursingGoal_DR | bigint |  | FK | SI | Nursing Goal DR -- for Care Plan module |
| PATHI_NursingProblem_DR | varchar |  | FK | SI | Nursing Problem DR -- for Care Plan module |
| PATHI_Operation_DR | bigint |  | FK | SI | Procedure |
| PATHI_OrdSets_DR | varchar |  | FK | SI | Order Set |
| PATHI_OrderedDate | date |  |  | SI | Ordered Date |
| PATHI_Outcome_DR | bigint |  | FK | SI | Item Outcome |
| PATHI_ParRef | varchar |  |  | SI | Parent Reference
Required by User.PAPathwayItem. |
| PATHI_ParentItem_DR | varchar |  | FK | SI | Parent Item |
| PATHI_PlanStartComputed | bit |  |  | SI | Planned Start Date Computed
1 - the planned start... |
| PATHI_PlannedEndDate | date |  |  | SI | Planned End Date |
| PATHI_PlannedStartDate | date |  |  | SI | Planned Start Date |
| PATHI_PrefParams_DR | bigint |  | FK | SI | Default Parameters |
| PATHI_ProblemGroup_DR | bigint |  | FK | SI | NRC Problem Group DR -- for Care Plan module |
| PATHI_Problem_DR | varchar |  | FK | SI | Patient Problem DR |
| PATHI_ProtocolItem_DR | varchar |  | FK | SI | Protocol Item |
| PATHI_Protocol_DR | bigint |  | FK | SI | Protocol |
| PATHI_Questionnaire_DR | bigint |  | FK | SI | Questionnaire |
| PATHI_Questionnaire_ID | varchar |  |  | SI | Questionnaire ID
Note that it should be stored as... |
| PATHI_RowId | varchar |  |  | SI | - |
| PATHI_SequenceNumber | numeric |  |  | SI | Sequence Number |
| PATHI_StartedBy_DR | bigint |  | FK | SI | Started By |
| PATHI_StartedDate | date |  |  | SI | Started Date |
| PATHI_StartedTime | time |  |  | SI | Started Time |
| PATHI_StatePPP_DR | bigint |  | FK | SI | State PPP |
| PATHI_Status | varchar |  |  | SI | Status |
| PATHI_Task_DR | bigint |  | FK | SI | Task |
| PATHI_TimeNotAfter | double |  |  | SI | Time Constraint Not After: Offset Time between pre... |
| PATHI_TimeNotAfterType | varchar |  |  | SI | Time Constraint Not After Duration Type |
| PATHI_TimeNotBefore | double |  |  | SI | Time Constraint Not Before: Offset Time between pr... |
| PATHI_TimeNotBeforeType | varchar |  |  | SI | Time Constraint Not Before Duration Type |
| PATHI_TimeStart | varchar |  |  | SI | Time Constraint Starting Point |
| PATHI_UpdateDate | date |  |  | SI | UpdateDate |
| PATHI_UpdateTime | time |  |  | SI | UpdateTime |
| PATHI_UpdateUserHospital_DR | bigint |  | FK | SI | Des Ref UpdateUserHospital |
| PATHI_UpdateUser_DR | bigint |  | FK | SI | Des Ref UpdateUser |
| PATHI_UseProtTypeOrdWorkflow | varchar |  |  | SI | Use Ordering workflow defined for the Protocol Typ... |
| PATHI_VacDose_DR | bigint |  | FK | SI | Vaccination Dose DR |
| PATHI_WaitingList_DR | bigint |  | FK | SI | Waiting List DR |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*