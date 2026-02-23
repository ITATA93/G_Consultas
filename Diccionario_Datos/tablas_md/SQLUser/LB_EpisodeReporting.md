# SQLUser.LB_EpisodeReporting

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBEPR_ParRef | bigint | PK |  | NO | - |
| LBEPR_Association | varchar |  |  | SI | Association
This is an internal value used to den... |
| LBEPR_CareProv_DR | varchar |  | FK | SI | Care Provider
CareProvider DR (eg Doctor) to rece... |
| LBEPR_Clinic_DR | bigint |  | FK | SI | Clinic
The Clinic where the Referring Doctor DR t... |
| LBEPR_ConfidentialFax | varchar |  |  | SI | Confidential Fax Number |
| LBEPR_Copies | numeric |  |  | SI | Deprecated
No of Copies
0 = do not produce repor... |
| LBEPR_Fax | varchar |  |  | SI | Fax Number |
| LBEPR_Location_DR | bigint |  | FK | SI | Location
Location DR to receive the report |
| LBEPR_QuickPrint | varchar |  |  | SI | QuickPrint Flag
If set the request (all TestSets ... |
| LBEPR_RecipientID | varchar |  |  | SI | Recipient ID
CareProvider, Location, ReferringDoc... |
| LBEPR_RecipientType | varchar |  |  | NO | Recipient Type
The type of recipient for this rec... |
| LBEPR_ReferringDoctor_DR | bigint |  | FK | SI | Referring Doctor
Referring Doctor DR to receive t... |
| LBEPR_ReportEnabled | varchar |  |  | SI | Report Enabled
Report is Enabled |
| LBEPR_RowID | varchar |  |  | NO | - |
| LBEPR_ThirdParty_DR | bigint |  | FK | SI | Third Party
ThirdParty DR to receive the report |
| Q01 | - |  |  | SI | Origen |
| Q01ObsDR | - |  |  | SI | Origen DR |
| Q02 | - |  |  | SI | Destino |
| Q02ObsDR | - |  |  | SI | Destino DR |
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
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*