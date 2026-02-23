# SQLUser.PA_Drugs

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DRG_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| DRG_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| DRG_Childsub | double |  |  | NO | Childsub |
| DRG_DSReportFlag | varchar |  |  | SI | DSReportFlag |
| DRG_Date | date |  |  | SI | Date |
| DRG_Desc | varchar |  |  | SI | Description |
| DRG_DrugMast_DR | bigint |  | FK | SI | Des Ref to DrugMast |
| DRG_DuratDays | double |  |  | SI | Duration in Days |
| DRG_DuratMonth | double |  |  | SI | Duration in Month |
| DRG_DuratYear | double |  |  | SI | Duration in Year |
| DRG_EndDate | date |  |  | SI | EndDate |
| DRG_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| DRG_InActive | varchar |  |  | SI | InActive |
| DRG_OnsetDate | date |  |  | SI | Onset Date |
| DRG_RowId | varchar |  |  | NO | - |
| DRG_Time | time |  |  | SI | Time |
| DRG_UpdateDate | date |  |  | SI | UpdateDate |
| DRG_UpdateHospital_DR | bigint |  | FK | SI | Des Ref UpdateHospital |
| DRG_UpdateTime | time |  |  | SI | UpdateTime |
| DRG_UpdateUser_DR | bigint |  | FK | SI | Des Ref User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Elevated mood |
| Q04 | - |  |  | SI | Increased motor activity - energy |
| Q05 | - |  |  | SI | Sexual interest |
| Q06 | - |  |  | SI | Sleep |
| Q07 | - |  |  | SI | Irritability |
| Q08 | - |  |  | SI | Speech (rate and amount) |
| Q09 | - |  |  | SI | Language - thought disorder |
| Q10 | - |  |  | SI | Content |
| Q11 | - |  |  | SI | Disruptive - aggressive behavior |
| Q12 | - |  |  | SI | Appearance |
| Q13 | - |  |  | SI | Insight |
| Q14 | - |  |  | SI | • The scale is generally done by a clinician or ot... |
| Q15 | - |  |  | SI | • The purpose of each item is to rate the severity... |
| Q16 | - |  |  | SI | • The keys provided are guides. One can ignore the... |
| Q17 | - |  |  | SI | Scoring between the points given (whole or half po... |
| Q18 | - |  |  | SI | This is particularly useful when severity of a par... |
| Q19 | - |  |  | SI | Score |
| Q20 | - |  |  | SI | Classification |
| Q21 | - |  |  | SI | 0 - 60 |
| Q22 | - |  |  | SI | Higher score indicates worse manic symptoms |
| Q23 | - |  |  | SI | 0 - 60: Higher score indicates worse manic symptom... |
| Q24 | - |  |  | SI | The Young Mania Rating Scale (YMRS) is one of the ... |
| Q25 | - |  |  | SI | The scale has 11 items and is based on the patient... |
| Q26 | - |  |  | SI | Sometimes a clinical study entry requirement of YM... |
| Q27 | - |  |  | SI | • There are four items that are graded on a 0 to 8... |
| Q28 | - |  |  | SI | These four items are given twice the weight of the... |
| Q29 | - |  |  | SI | • There are well described anchor points for each ... |
| Q30 | - |  |  | SI | They depend on the patients’ clinical features suc... |
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