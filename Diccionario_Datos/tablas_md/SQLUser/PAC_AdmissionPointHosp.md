# SQLUser.PAC_AdmissionPointHosp

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOS_ParRef | bigint | PK |  | NO | PAC_AdmissionPoint Parent Reference |
| HOS_Childsub | double |  |  | NO | Childsub |
| HOS_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| HOS_CreatedDate | date |  |  | SI | Created Date |
| HOS_CreatedTime | time |  |  | SI | Created Time |
| HOS_CreatedUser_DR | bigint |  | FK | SI | Created User |
| HOS_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| HOS_RowId | varchar |  |  | NO | - |
| HOS_UpdatedDate | date |  |  | SI | Updated Date |
| HOS_UpdatedTime | time |  |  | SI | Updated Time |
| HOS_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Interpreter present |
| Q04 | - |  |  | SI | Interpreter name |
| Q05 | - |  |  | SI | Carer present |
| Q06 | - |  |  | SI | Names of those present |
| Q07 | - |  |  | SI | Home haemodialysis room / unit orientation |
| Q08 | - |  |  | SI | Orientation notes |
| Q09 | - |  |  | SI | Verbal / written information on home haemodialysis... |
| Q10 | - |  |  | SI | Notes on information provided |
| Q11 | - |  |  | SI | Expectations and commitment explained |
| Q12 | - |  |  | SI | Expectations / commitment notes |
| Q13 | - |  |  | SI | Patient responsibilities explained |
| Q14 | - |  |  | SI | Patient responsibilities notes |
| Q15 | - |  |  | SI | Carer responsibilities explained |
| Q16 | - |  |  | SI | Carer responsibilities notes |
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