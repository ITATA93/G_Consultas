# SQLUser.CT_Disposit

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de configuración**. Tabla de referencia del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTDSP_RowID | bigint | PK |  | NO | - |
| CTDSP_CareAvailability | varchar |  |  | SI | Care Availability |
| CTDSP_CareTyp | varchar |  |  | SI | Care Type |
| CTDSP_Code | varchar |  |  | NO | Disposition Code |
| CTDSP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTDSP_CreatedDate | date |  |  | SI | Created Date |
| CTDSP_CreatedTime | time |  |  | SI | Created Time |
| CTDSP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| CTDSP_DateFrom | date |  |  | SI | Date From |
| CTDSP_DateTo | date |  |  | SI | Date To |
| CTDSP_Default | varchar |  |  | SI | Default |
| CTDSP_Desc | varchar |  |  | NO | Disposition Description |
| CTDSP_GrouperCode | varchar |  |  | SI | Grouper Code |
| CTDSP_IntentReAdmit | varchar |  |  | SI | Intention to ReAdmit |
| CTDSP_NationalCode | varchar |  |  | SI | National Code |
| CTDSP_Owner | varchar |  |  | SI | Owner |
| CTDSP_ReasonForCritCareTransfer | varchar |  |  | SI | Reason for Critical Care Transfer |
| CTDSP_SeparationReferral | varchar |  |  | SI | Separation Referral |
| CTDSP_StatDischarge | varchar |  |  | SI | Statistical Discharge |
| CTDSP_TransferSource | varchar |  |  | SI | Transfer Source |
| CTDSP_UpdatedDate | date |  |  | SI | Updated Date |
| CTDSP_UpdatedTime | time |  |  | SI | Updated Time |
| CTDSP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| QAcuityID | - |  |  | SI | Acuity Row ID |
| QProblemID | - |  |  | SI | Problem RowID |
| QSymptomID | - |  |  | SI | Triage Symptom Row ID |
| QTriageNurseID | - |  |  | SI | Triage Nurse Row ID |
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