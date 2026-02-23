# websys_DecisionSupport.Action

**Schema:** websys_DecisionSupport
**Columnas:** 61
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ParRef | bigint | PK |  | NO | - |
| ActionType | varchar |  |  | SI | - |
| ActiveDatePart | varchar |  |  | SI | - |
| ActiveDatePartPeriod | double |  |  | SI | - |
| AlertType | varchar |  |  | SI | - |
| AlwaysNotifyCurrentUser | bit |  |  | SI | - |
| BillingOrderItemDR | varchar |  | FK | SI | - |
| ContactRecipient | varchar |  |  | SI | If Action_Type='preferred contact - this will stor... |
| Description | varchar |  |  | SI | - |
| EmailFrom | varchar |  |  | SI | - |
| EmailSubject | varchar |  |  | SI | - |
| EmailTo | varchar |  |  | SI | - |
| ID | varchar |  |  | NO | - |
| InvokeOnceOnly | bit |  |  | SI | - |
| IsDisabled | bit |  |  | SI | - |
| LBCQueueDR | bigint |  | FK | SI | - |
| LBCTestItemDR | bigint |  | FK | SI | - |
| LBCTestSetDR | bigint |  | FK | SI | - |
| LBLinkRequestedTestSet | bit |  |  | SI | - |
| LBReplaceComment | bit |  |  | SI | - |
| LBTSIReportableFlag | bit |  |  | SI | - |
| LabCurrentInitiator | bit |  |  | SI | - |
| LabEpisodeLevel | bit |  |  | SI | - |
| LabTestComment | longvarchar |  |  | SI | - |
| LinkedDateField | varchar |  |  | SI | the linked date to use for calculation of an offse... |
| Message | varchar |  |  | SI | - |
| MessageRTF | longvarchar |  |  | SI | - |
| OverrideMandatory | bit |  |  | SI | - |
| PatientAlertDR | bigint |  | FK | SI | - |
| PatientFlagDR | bigint |  | FK | SI | - |
| PushRecipient | varchar |  |  | SI | If Action_Type='PN - this will store the dimension... |
| QuestionnaireDR | bigint |  | FK | SI | - |
| ReasonNotPerformedDR | bigint |  | FK | SI | - |
| RecipientType | varchar |  |  | SI | - |
| ReportCareProvDR | varchar |  | FK | SI | - |
| ReportClinicDR | bigint |  | FK | SI | - |
| ReportCopies | numeric |  |  | SI | - |
| ReportLocationDR | bigint |  | FK | SI | - |
| ReportReferringDoctorDR | bigint |  | FK | SI | - |
| ReportThirdPartyDR | bigint |  | FK | SI | - |
| SMSMobileNo | varchar |  |  | SI | - |
| SMSRecipient | varchar |  |  | SI | If Action_Type='SMS - this will store the dimensio... |
| SMSTo | varchar |  |  | SI | - |
| SendSMSToPatient | bit |  |  | SI | - |
| TaskARCIMDR | varchar |  | FK | SI | - |
| TaskARCOrdSetsDR | varchar |  | FK | SI | - |
| TaskAssignGroupDR | bigint |  | FK | SI | - |
| TaskItemDR | bigint |  | FK | SI | - |
| TimeOffset | varchar |  |  | SI | - |
| TimeOffsetType | varchar |  |  | SI | - |
| TimeToSend | time |  |  | SI | - |
| TimeUnit | varchar |  |  | SI | - |
| TrakCareGroup | bigint |  |  | SI | - |
| TrakCareRecipients | varchar |  |  | SI | - |
| TriggerOncePer | varchar |  |  | SI | - |
| TriggerOnceTime | double |  |  | SI | - |
| TriggerOnceTimeUnit | varchar |  |  | SI | - |
| UserNotPerformedDR | bigint |  | FK | SI | - |
| WaitListDR | bigint |  | FK | SI | - |
| WorkflowDR | bigint |  | FK | SI | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*