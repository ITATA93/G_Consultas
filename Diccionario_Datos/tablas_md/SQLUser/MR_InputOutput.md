# SQLUser.MR_InputOutput

**Schema:** SQLUser
**Columnas:** 70
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INPOUT_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| INPOUT_Aspiration | double |  |  | SI | Aspiration |
| INPOUT_Blood | double |  |  | SI | Blood |
| INPOUT_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| INPOUT_Childsub | double |  |  | NO | Childsub |
| INPOUT_Date | date |  |  | SI | Date |
| INPOUT_Drainage | double |  |  | SI | Drainage |
| INPOUT_EndDate | date |  |  | SI | End Date |
| INPOUT_EndTime | time |  |  | SI | End Time |
| INPOUT_IOBalance | double |  |  | SI | I/O Balance |
| INPOUT_IVIntake | double |  |  | SI | IV Intake |
| INPOUT_OralIntake | double |  |  | SI | Oral Intake |
| INPOUT_OrderStat_DR | bigint |  | FK | SI | Admin. Order State Des Ref to OECOrdSt |
| INPOUT_RowId | varchar |  |  | NO | - |
| INPOUT_Shift | varchar |  |  | SI | Shift |
| INPOUT_Stool | double |  |  | SI | Stool |
| INPOUT_Time | time |  |  | SI | Time |
| INPOUT_TotalIntake | double |  |  | SI | Total Intake |
| INPOUT_TotalOutput | double |  |  | SI | Total Output |
| INPOUT_UpdateDate | date |  |  | SI | UpdateDate |
| INPOUT_UpdateTime | time |  |  | SI | UpdateTime |
| INPOUT_UpdateUser_DR | bigint |  | FK | SI | DEs REf User |
| INPOUT_UrineOutput | double |  |  | SI | Urine Output |
| INPOUT_Vomit | double |  |  | SI | Vomit |
| Q01 | - |  |  | SI | Age |
| Q02 | - |  |  | SI | Disability |
| Q03 | - |  |  | SI | Prior Living Status |
| Q04 | - |  |  | SI | Self-Reported Walking Limitation |
| Q05 | - |  |  | SI | Risk Assessment Score |
| Q06 | - |  |  | SI | Early Screening For Discharge allows care provider... |
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