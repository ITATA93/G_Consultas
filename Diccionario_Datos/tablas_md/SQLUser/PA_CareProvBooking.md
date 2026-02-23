# SQLUser.PA_CareProvBooking

**Schema:** SQLUser
**Columnas:** 59
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CPB_RowId | bigint | PK |  | NO | - |
| CPB_CTPCP_DR | varchar |  | FK | SI | Des Ref CTPCP |
| CPB_EndDate | date |  |  | SI | EndDate |
| CPB_EndTime | time |  |  | SI | EndTime |
| CPB_ORAnOperAdditStaff_DR | varchar |  | FK | SI | Des Ref ORAnOperAdditionalStaff |
| CPB_ORAnaestAdditStaff_DR | varchar |  | FK | SI | Des Ref ORAnaestAdditionalStaff |
| CPB_RBOPRoomAnaesthetist_DR | bigint |  | FK | SI | Des Ref RBOperatingRoom |
| CPB_RBOPRoomSurgeon_DR | bigint |  | FK | SI | Des Ref RBOperatingRoom |
| CPB_RBOperRoomAdditStaff_DR | varchar |  | FK | SI | Des Ref RBOperRoomAdditionalStaff |
| CPB_StartDate | date |  |  | SI | StartDate |
| CPB_StartTime | time |  |  | SI | StartTime |
| Q01 | - |  |  | SI | Date of test |
| Q02 | - |  |  | SI | Time of test |
| Q03 | - |  |  | SI | Test performed |
| Q04 | - |  |  | SI | Exercise |
| Q05 | - |  |  | SI | Muscle group tested |
| Q06 | - |  |  | SI | Repetitions completed in 30 seconds |
| Q07 | - |  |  | SI | Repetitions completed in 1 minute |
| Q08 | - |  |  | SI | Comments |
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