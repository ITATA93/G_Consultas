# SQLUser.LB_ReportRequest

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBRR_RowID | bigint | PK |  | NO | - |
| LBRR_AuthorisedBy_DR | bigint |  | FK | SI | User who (last) authorised the result |
| LBRR_CareProv_DR | varchar |  | FK | SI | CareProvider DR (eg Doctor) to receive the report |
| LBRR_Clinic_DR | bigint |  | FK | SI | Clinic DR for Referring Doctor DR to receive the r... |
| LBRR_Copies | numeric |  |  | SI | No of Copies, default 1 |
| LBRR_Courier_DR | bigint |  | FK | SI | The Courier to use |
| LBRR_DestinationType | varchar |  |  | SI | This is the type of destination to which the repor... |
| LBRR_Episode_DR | bigint |  | FK | SI | The LabEpisode for the Request |
| LBRR_LBCCCode | varchar |  |  | SI | A copy of the Courier Code (see index LBCCCode) |
| LBRR_LBCCDesc | varchar |  |  | SI | A copy of the Courier Desc (see index LBCCDesc) |
| LBRR_LastDate | date |  |  | SI | Date Processed
The date when this request was las... |
| LBRR_LastTime | time |  |  | SI | Time Processed
The time when this request was las... |
| LBRR_Location_DR | bigint |  | FK | SI | Location DR to receive the report |
| LBRR_QuickPrint | varchar |  |  | NO | QuickPrint Flag
If set the request (all TestSets ... |
| LBRR_RecipientID | varchar |  |  | SI | The Recipient (ID of User.CTCareProv, User.CTLoc, ... |
| LBRR_RecipientType | varchar |  |  | SI | The type of Recipient for the Requested report |
| LBRR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor DR to receive the report |
| LBRR_ReprintBatchId | varchar |  |  | SI | Reprint BatchId
The batchid to be reprinted (not ... |
| LBRR_ReprintCareProviders | varchar |  |  | SI | Reprint CareProviders
A list of CareProvider reci... |
| LBRR_ReprintLocations | varchar |  |  | SI | Reprint Locations
A list of Location recipient Id... |
| LBRR_ReprintReferringDoctors | varchar |  |  | SI | Reprint ReferringDoctors
A list of the pairs of r... |
| LBRR_ReprintThirdParties | varchar |  |  | SI | Reprint ThirdParties
A list of ThirdParty recipie... |
| LBRR_TestSetCode | varchar |  |  | SI | The Code of the TestSet User.LBCTestSetRevision, f... |
| LBRR_TestSet_DR | bigint |  | FK | SI | The TestSet whose Authorisation caused the Request |
| LBRR_ThirdParty_DR | bigint |  | FK | SI | ThirdParty DR to receive the report |
| LBRR_WithheldReason | varchar |  |  | SI | Withheld Reason
When a request cannot be processe... |
| Q01 | - |  |  | SI | Factores de Riesgo Asociados Pre-Existentes |
| Q02 | - |  |  | SI | Factores de Riesgo Asociados Pre-Existentes (Sólo ... |
| Q03 | - |  |  | SI | Situaciones Asociadas a la Hospitalización |
| Q04 | - |  |  | SI | Comorbilidad que Incrementa el Riesgo |
| Q05 | - |  |  | SI | Se Realizan Medidas Según Riesgo Evaluado |
| Q06 | - |  |  | SI | Tipo de Tromboprofilaxis No Realizada |
| Q07 | - |  |  | SI | Razón de No Realización (M) |
| Q08 | - |  |  | SI | Otra Razón de No Realización (M) |
| Q09 | - |  |  | SI | Razón de No Realización (F) |
| Q10 | - |  |  | SI | Otra Razón de No Realización (F) |
| Q11 | - |  |  | SI | Riesgo Bajo |
| Q12 | - |  |  | SI | Riesgo Moderado |
| Q13 | - |  |  | SI | Riesgo Alto |
| Q14 | - |  |  | SI | Clasificación de Riesgo |
| Q14ObsDR | - |  |  | SI | Clasificación de Riesgo DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*