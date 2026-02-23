# SQLUser.MRC_ClinPathwEpDays

**Schema:** SQLUser
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DAYS_ParRef | varchar | PK |  | NO | MRC_ClinPathwaysEpisodes Parent Reference |
| DAYS_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| DAYS_Childsub | double |  |  | NO | Childsub |
| DAYS_CreatedDate | date |  |  | SI | Created Date |
| DAYS_CreatedTime | time |  |  | SI | Created Time |
| DAYS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DAYS_Day | double |  |  | SI | Day |
| DAYS_DayNumber | double |  |  | SI | Day Number |
| DAYS_Desc | varchar |  |  | SI | Description |
| DAYS_IPEpisodeRequired | varchar |  |  | SI | IPEpisodeRequired |
| DAYS_Notes | varchar |  |  | SI | Notes |
| DAYS_RBResource_DR | bigint |  | FK | SI | Des Ref RBResource |
| DAYS_RefTemplStage_DR | varchar |  | FK | SI | Des Ref PACRefTemplateStage |
| DAYS_RowId | varchar |  |  | NO | - |
| DAYS_Service_DR | bigint |  | FK | SI | Des Ref Service |
| DAYS_UpdatedDate | date |  |  | SI | Updated Date |
| DAYS_UpdatedTime | time |  |  | SI | Updated Time |
| DAYS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q1 | - |  |  | SI | Madre o padre obeso |
| Q2 | - |  |  | SI | Lactancia materna exclusiva menor a 4 meses |
| Q3 | - |  |  | SI | RN PEG o macrosómico (peso> o = a 4Kg.) |
| Q4 | - |  |  | SI | Antecedente de diabetes gestacional en ese embaraz... |
| Q5 | - |  |  | SI | Diabetes tipo 2 en padres o abuelos |
| QR | - |  |  | SI | Resultado Score Riesgo de Obesidad |
| QRObsDR | - |  |  | SI | Resultado Score Riesgo de Obesidad   DR |
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