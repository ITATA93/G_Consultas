# epr.TaskList

**Schema:** epr
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**EPR - Registro Electrónico de Pacientes**. Módulo de ficha clínica electrónica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AdminStatus | varchar |  |  | SI | - |
| AssignedDate | date |  |  | SI | - |
| AssignedHospDR | bigint |  | FK | SI | - |
| AssignedTime | time |  |  | SI | - |
| AssignedToDetails | varchar |  |  | SI | - |
| AssignedUserDR | bigint |  | FK | SI | - |
| BeginDate | date |  |  | SI | - |
| BeginTime | time |  |  | SI | - |
| BreachDR | varchar |  | FK | SI | - |
| Color | varchar |  |  | SI | - |
| Comments | varchar |  |  | SI | - |
| DetentionDR | bigint |  | FK | SI | - |
| DurationDR | bigint |  | FK | SI | - |
| EscalateAfter | varchar |  |  | SI | - |
| EscalateTimeUnit | varchar |  |  | SI | - |
| ExecNotes | varchar |  |  | SI | - |
| ExecutedBy | varchar |  |  | SI | - |
| ExecutionDate | date |  |  | SI | - |
| ExecutionTime | time |  |  | SI | - |
| ExecutionUser | bigint |  |  | SI | - |
| ExternalMessageID | varchar |  |  | SI | - |
| ForwardCareProvDR | varchar |  | FK | SI | - |
| ForwardUserDR | bigint |  | FK | SI | - |
| FreeText1 | varchar |  |  | SI | - |
| FrequencyDR | bigint |  | FK | SI | - |
| LastUpdateDate | date |  |  | SI | - |
| LastUpdateTime | time |  |  | SI | - |
| LastUpdateUserDR | bigint |  | FK | SI | - |
| MHCTaskTypeDR | bigint |  | FK | SI | - |
| NationalPPPDR | bigint |  | FK | SI | - |
| OrderItems | varchar |  |  | SI | - |
| PAAdmDR | bigint |  | FK | SI | - |
| PAPMIDR | bigint |  | FK | SI | - |
| PAPathwayItemDR | varchar |  | FK | SI | Link to Pathway Item this task is based on |
| PAWaitingListDR | bigint |  | FK | SI | - |
| PAWaitingListTriageOutcome | bit |  |  | SI | - |
| PAletterDR | bigint |  | FK | SI | - |
| PatLeaveDR | varchar |  | FK | SI | - |
| PathwayStageDR | varchar |  | FK | SI | - |
| PatientBillDR | bigint |  | FK | SI | - |
| PatientDetails | varchar |  |  | SI | - |
| PayorAppReqDR | bigint |  | FK | SI | - |
| PayorBillDR | bigint |  | FK | SI | - |
| PayorDR | bigint |  | FK | SI | - |
| PrevTaskDR | bigint |  | FK | SI | - |
| PriorityDR | bigint |  | FK | SI | - |
| ProcessingGroup | varchar |  |  | SI | Checkbox for Processing Group |
| QuestionnaireDR | bigint |  | FK | SI | - |
| RBAppointmentDR | varchar |  | FK | SI | - |
| ReasonNotComplete | bigint |  |  | SI | - |
| Reminder | varchar |  |  | SI | - |
| ReminderTimeUnit | varchar |  |  | SI | - |
| RequestOrderItems | varchar |  |  | SI | - |
| RequestOrderSets | varchar |  |  | SI | - |
| ScheduledDate | date |  |  | SI | - |
| ScheduledTime | time |  |  | SI | - |
| SuspensionDR | varchar |  | FK | SI | - |
| TaskDescription | varchar |  |  | SI | - |
| TaskDispositionDR | bigint |  | FK | SI | - |
| TaskItemDR | bigint |  | FK | SI | - |
| TaskPlanDR | bigint |  | FK | SI | - |
| UserDR | bigint |  | FK | SI | Assigned By User |
| UserGroupDR | bigint |  | FK | SI | - |
| WaitingListType | bigint |  |  | SI | - |
| WardDetails | varchar |  |  | SI | - |
| WorkGroupDR | varchar |  | FK | SI | - |
| Workflow | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*