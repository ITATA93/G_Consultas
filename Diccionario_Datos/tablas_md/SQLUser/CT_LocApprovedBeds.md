# SQLUser.CT_LocApprovedBeds

**Schema:** SQLUser
**Columnas:** 81
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| APB_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| APB_Childsub | double |  |  | NO | Childsub |
| APB_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| APB_CreatedDate | date |  |  | SI | Created Date |
| APB_CreatedTime | time |  |  | SI | Created Time |
| APB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| APB_DateFrom | date |  |  | SI | DateFrom |
| APB_DateTo | date |  |  | SI | DateTo |
| APB_NumberOfBeds | double |  |  | SI | Number Of Beds |
| APB_RowId | varchar |  |  | NO | - |
| APB_SurgeCapacity | double |  |  | SI | Surge Capacity |
| APB_UpdatedDate | date |  |  | SI | Updated Date |
| APB_UpdatedTime | time |  |  | SI | Updated Time |
| APB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Anaesthetic type |
| Q04 | - |  |  | SI | Consent for |
| Q05 | - |  |  | SI | Complications of general anaesthetic / sedation  d... |
| Q06 | - |  |  | SI | Additional anaesthetic / sedation discussion notes |
| Q07 | - |  |  | SI | Complications of regional anaesthesia discussed |
| Q08 | - |  |  | SI | Additional regional anaesthesia discussion notes |
| Q09 | - |  |  | SI | Supplementary techniques |
| Q10 | - |  |  | SI | Complications of supplementary techniques discusse... |
| Q11 | - |  |  | SI | Exclusions |
| Q12 | - |  |  | SI | Exclusions details |
| Q13 | - |  |  | SI | Patient signature |
| Q13UDt | - |  |  | SI | Patient signature Last Updated Date |
| Q13UTm | - |  |  | SI | Patient signature Last Updated Time |
| Q14 | - |  |  | SI | Guardian name (if applicable) |
| Q15 | - |  |  | SI | Guardian signature (if applicable) |
| Q15UDt | - |  |  | SI | Guardian signature (if applicable) Last Updated Da... |
| Q15UTm | - |  |  | SI | Guardian signature (if applicable) Last Updated Ti... |
| Q16 | - |  |  | SI | Interpreter name (if applicable) |
| Q17 | - |  |  | SI | Interpreter signature (if applicable) |
| Q17UDt | - |  |  | SI | Interpreter signature (if applicable) Last Updated... |
| Q17UTm | - |  |  | SI | Interpreter signature (if applicable) Last Updated... |
| Q18 | - |  |  | SI | Anaesthetist name |
| Q19 | - |  |  | SI | Anaesthetist signature |
| Q19UDt | - |  |  | SI | Anaesthetist signature Last Updated Date |
| Q19UTm | - |  |  | SI | Anaesthetist signature Last Updated Time |
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