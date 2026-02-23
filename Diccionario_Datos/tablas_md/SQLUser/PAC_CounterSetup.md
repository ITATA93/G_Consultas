# SQLUser.PAC_CounterSetup

**Schema:** SQLUser
**Columnas:** 68
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SET_RowId | bigint | PK |  | NO | - |
| Q01 | - |  |  | SI | Partner's name |
| Q02 | - |  |  | SI | Procedure indication |
| Q03 | - |  |  | SI | Hormone result |
| Q04 | - |  |  | SI | Anesthetist |
| Q05 | - |  |  | SI | Testicular volume (ml) |
| Q05A | - |  |  | SI | Mapping result |
| Q06 | - |  |  | SI | Complication |
| Q07 | - |  |  | SI | Outcome |
| Q08 | - |  |  | SI | Number of sperm retrieved |
| Q09 | - |  |  | SI | Number of fertilized ovum |
| Q10 | - |  |  | SI | Number of embryos transferred |
| Q11 | - |  |  | SI | Pregnancy |
| Q12 | - |  |  | SI | Delivery |
| Q14 | - |  |  | SI | Date |
| Q15 | - |  |  | SI | Time |
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
| SET_CounterType_DR | bigint |  | FK | SI | Des Ref Counter Type |
| SET_CreatedDate | date |  |  | SI | Created Date |
| SET_CreatedTime | time |  |  | SI | Created Time |
| SET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| SET_DateFrom | date |  |  | SI | DateFrom |
| SET_DateTo | date |  |  | SI | DateTo |
| SET_EpisSubType_DR | bigint |  | FK | SI | Des Ref EpisSubType |
| SET_EpisodeType | varchar |  |  | NO | Episode Type |
| SET_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| SET_UpdatedDate | date |  |  | SI | Updated Date |
| SET_UpdatedTime | time |  |  | SI | Updated Time |
| SET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*