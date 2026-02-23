# SQLUser.MH_Detention

**Schema:** SQLUser
**Columnas:** 94
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| MHD_RowId | bigint | PK |  | NO | - |
| MHD_AdjustSuspensionDays | double |  |  | SI | AdjustSuspensionDays |
| MHD_AuthDate | date |  |  | SI | AuthDate |
| MHD_AuthorisedAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| MHD_AuthorisedDetAgent_DR | varchar |  | FK | SI | Des Ref MHDetAgent |
| MHD_CommunityBased | varchar |  |  | SI | CommunityBased  |
| MHD_CreateDate | date |  |  | SI | CreateDate |
| MHD_CreateTime | time |  |  | SI | CreateTime |
| MHD_Deleted | varchar |  |  | SI | Deleted |
| MHD_DetentionType_DR | bigint |  | FK | SI | Des Ref MHCDetentionType |
| MHD_DurationNum | double |  |  | SI | DurationNum |
| MHD_DurationUnits | varchar |  |  | SI | DurationUnits |
| MHD_EndDate | date |  |  | SI | EndDate |
| MHD_EndTime | time |  |  | SI | EndTime |
| MHD_EndedAgent_DR | bigint |  | FK | SI | Des Ref MHCAgent |
| MHD_EndedDate | date |  |  | SI | EndedDate |
| MHD_EndedDetAgent_DR | varchar |  | FK | SI | Des Ref MHDetAgent |
| MHD_EndedReason | varchar |  |  | SI | EndedReason |
| MHD_EndedTime | time |  |  | SI | EndedTime |
| MHD_Historical | varchar |  |  | SI | Historical |
| MHD_Hospital_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MHD_LinkedDetention_DR | bigint |  | FK | SI | Des Ref MHDetention |
| MHD_Outcome_DR | bigint |  | FK | SI | Des Ref MHCDetentionOutcome |
| MHD_PatientConsent | varchar |  |  | SI | PatientConsent |
| MHD_PatientConsentDate | date |  |  | SI | PatientConsentDate |
| MHD_Patient_DR | bigint |  | FK | SI | Des Ref PAPMI |
| MHD_ReminderTask_DR | bigint |  | FK | SI | ReminderTask |
| MHD_SecondOpinion | varchar |  |  | SI | SecondOpinion |
| MHD_SecondOpinionDate | date |  |  | SI | SecondOpinionDate |
| MHD_SecondOpinionDocExt | varchar |  |  | SI | SecondOpinionDocExt |
| MHD_SecondOpinionDoc_DR | varchar |  | FK | SI | Des Ref CTCareProv |
| MHD_SecondOpinionRefDoc_DR | bigint |  | FK | SI | Des Ref PACRefDoctor |
| MHD_StartDate | date |  |  | SI | StartDate |
| MHD_StartTime | time |  |  | SI | StartTime |
| MHD_TransferFrom | varchar |  |  | SI | TransferFrom |
| MHD_TransferFromDate | date |  |  | SI | TransferFromDate |
| MHD_TransferFromHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MHD_TransferFromType_DR | bigint |  | FK | SI | Des Ref MHCTransferType |
| MHD_TransferTo | varchar |  |  | SI | TransferTo |
| MHD_TransferToDate | date |  |  | SI | TransferToDate |
| MHD_TransferToHosp_DR | bigint |  | FK | SI | Des Ref CTHospital |
| MHD_TransferToType_DR | bigint |  | FK | SI | Des Ref MHCTransferType |
| QAgeMax | - |  |  | SI | Edad Maxima |
| QAgeMin | - |  |  | SI | Edad Minima |
| QCholesterolMax | - |  |  | SI | Colesterol Maximo |
| QCholesterolMin | - |  |  | SI | Colesterol Minimo |
| QDBPMax | - |  |  | SI | Presion Arterial Diastolica Maxima |
| QDBPMin | - |  |  | SI | Presion Arterial Diastolica Minima |
| QDiabetic | - |  |  | SI | Diabetico |
| QRiskP | - |  |  | SI | % de Riesgo |
| QSBPMax | - |  |  | SI | Presion Arterial Sistolica Maxima |
| QSBPMin | - |  |  | SI | Presion Arterial Sistolica Minima |
| QSex | - |  |  | SI | Sexo |
| QSmoker | - |  |  | SI | Fumador |
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