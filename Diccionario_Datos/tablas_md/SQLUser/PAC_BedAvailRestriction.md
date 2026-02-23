# SQLUser.PAC_BedAvailRestriction

**Schema:** SQLUser
**Columnas:** 62
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AVR_ParRef | varchar | PK |  | NO | PAC_Bed Parent Reference |
| AVR_Childsub | double |  |  | NO | Childsub |
| AVR_CreatedDate | date |  |  | SI | Created Date |
| AVR_CreatedTime | time |  |  | SI | Created Time |
| AVR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AVR_DateFrom | date |  |  | SI | Date From |
| AVR_DateTo | date |  |  | SI | Date To |
| AVR_Friday | varchar |  |  | SI | Friday |
| AVR_Monday | varchar |  |  | SI | Monday |
| AVR_ReasonNotAvail_DR | bigint |  | FK | SI | Des Ref ReasonNotAvail |
| AVR_RowId | varchar |  |  | NO | - |
| AVR_Saturday | varchar |  |  | SI | Saturday |
| AVR_Sunday | varchar |  |  | SI | Sunday |
| AVR_Thursday | varchar |  |  | SI | Thursday |
| AVR_TimeFrom | time |  |  | SI | Time From |
| AVR_TimeTo | time |  |  | SI | Time To |
| AVR_Tuesday | varchar |  |  | SI | Tuesday |
| AVR_UpdatedDate | date |  |  | SI | Updated Date |
| AVR_UpdatedTime | time |  |  | SI | Updated Time |
| AVR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AVR_Wednesday | varchar |  |  | SI | Wednesday |
| Q02 | - |  |  | SI | Urinary Catheter Insertion Date |
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