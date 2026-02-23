# SQLUser.PAC_ADLCareTypeSub

**Schema:** SQLUser
**Columnas:** 66
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SUB_ParRef | bigint | PK |  | NO | PAC_ADLCareType Parent Reference |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | 2. The acceptability and performance of the 15 ite... |
| Q11 | - |  |  | SI | Geriatric Depression Scale, Four-Item Version (GDS... |
| Q2 | - |  |  | SI | Time |
| Q3 | - |  |  | SI | Are you basically satisfied with your life? |
| Q4 | - |  |  | SI | Do you feel that your life is empty? |
| Q5 | - |  |  | SI | Are you afraid that something bad is going to happ... |
| Q6 | - |  |  | SI | Do you feel happy most of the time? |
| Q7 | - |  |  | SI | Provenance |
| Q8 | - |  |  | SI | Reference |
| Q9 | - |  |  | SI | 1. D'Ath P, Katona P, Mullan E, Evans S, Katona C.... |
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
| SUB_ADLSubType_DR | bigint |  | FK | SI | Des Ref ADLSubType |
| SUB_Childsub | double |  |  | NO | Childsub |
| SUB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| SUB_CreatedDate | date |  |  | SI | Created Date |
| SUB_CreatedTime | time |  |  | SI | Created Time |
| SUB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SUB_DateFrom | date |  |  | SI | Date From |
| SUB_DateTo | date |  |  | SI | Date To |
| SUB_Max | varchar |  |  | SI | Max |
| SUB_Min | varchar |  |  | SI | Min |
| SUB_RowId | varchar |  |  | NO | - |
| SUB_UpdatedDate | date |  |  | SI | Updated Date |
| SUB_UpdatedTime | time |  |  | SI | Updated Time |
| SUB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*