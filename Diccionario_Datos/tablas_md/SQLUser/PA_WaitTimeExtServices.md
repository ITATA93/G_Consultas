# SQLUser.PA_WaitTimeExtServices

**Schema:** SQLUser
**Columnas:** 42
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera. Extensión de datos adicionales.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| EXT_RowId | bigint | PK |  | NO | - |
| EXT_ActiveMonitoring | varchar |  |  | SI | Active Monitoring |
| EXT_ActualWaitTime | double |  |  | SI | Actual Wait Time |
| EXT_CancelAPPTDate | date |  |  | SI | Cancel APPT Date |
| EXT_CancelAPPTDate2 | date |  |  | SI | Cancel APPT Date2 |
| EXT_Complete | varchar |  |  | SI | Complete |
| EXT_ContTreatStoppedPathway | varchar |  |  | SI | Contining Treatment for Stopped Pathway |
| EXT_ContactEmail | varchar |  |  | SI | Contact Email |
| EXT_ContactName | varchar |  |  | SI | ContactName |
| EXT_ContactPhone | varchar |  |  | SI | Contact Phone |
| EXT_ContinuationActivePathway | varchar |  |  | SI | Continuation ActivePathway |
| EXT_DNADate | date |  |  | SI | DNADate |
| EXT_DateCreated | date |  |  | SI | DateCreated |
| EXT_DateDecisionRefer | date |  |  | SI | Date of Decisionto Refer |
| EXT_DiagnosticTestOnly | varchar |  |  | SI | Diagnostic TestOnly |
| EXT_EndDate | date |  |  | SI | End Date |
| EXT_ExcludedDays | double |  |  | SI | Excluded days, update the planned stage end date |
| EXT_FreeText | varchar |  |  | SI | FreeText |
| EXT_HoldDays | double |  |  | SI | Hold Days |
| EXT_OpinionOnly | varchar |  |  | SI | Opinion Only |
| EXT_OtherOrganisationCodes | varchar |  |  | SI | Other Organisation Codes |
| EXT_PatientOn18wRTT | varchar |  |  | SI | Patient On 18wRTT |
| EXT_RTTActivityOutcome_DR | bigint |  | FK | SI | Des Ref RTT Activity Outcome |
| EXT_RTTFromOtherBoard | varchar |  |  | SI | RTTFromOtherBoard |
| EXT_RTTPeriodEndDate | date |  |  | SI | RTT Period EndDate |
| EXT_RTTPeriodTargetDate | date |  |  | SI | RTT Period Target Date |
| EXT_RTTStartDate | date |  |  | SI | RTT StartDate |
| EXT_ReasonRTTPeriodEnded | varchar |  |  | SI | Reason RTT Period Ended |
| EXT_ReceiveSpecialty_DR | bigint |  | FK | SI | Des Ref ReceiveSpecialty |
| EXT_ReceivingClinician_DR | varchar |  | FK | SI | Des Ref ReceivingClinician |
| EXT_ReceivingHospital_DR | bigint |  | FK | SI | Des Ref ReceivingHospital |
| EXT_ReferralFrom_DR | bigint |  | FK | SI | Des Ref Health Care Area |
| EXT_StartDate | date |  |  | SI | Start Date |
| EXT_StartNewPathway | varchar |  |  | SI | Start New Pathway |
| EXT_SuspensionComments | varchar |  |  | SI | Suspension Comments |
| EXT_SuspensionDays | double |  |  | SI | Suspension Days |
| EXT_TargetEndDate | date |  |  | SI | Target End Date |
| EXT_TimeCreated | time |  |  | SI | TimeCreated |
| EXT_TransferOfPatientCare | varchar |  |  | SI | Transfer Of PatientCare |
| EXT_UCPNOrganisationCode | varchar |  |  | SI | UCPN OrganisationCode |
| EXT_UserCreated_DR | bigint |  | FK | SI | Des Ref UserCreated |
| EXT_WaitList_DR | bigint |  | FK | SI | Des Ref WaitList |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*