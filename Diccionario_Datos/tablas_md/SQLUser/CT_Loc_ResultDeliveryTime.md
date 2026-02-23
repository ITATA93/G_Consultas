# SQLUser.CT_Loc_ResultDeliveryTime

**Schema:** SQLUser
**Columnas:** 90
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Catálogo de Ubicaciones**. Servicios, salas, unidades del hospital.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| RDT_ParRef | bigint | PK |  | NO | CT_Loc Parent Reference |
| Q01 | - |  |  | SI | Booking bloods and MSU done |
| Q02 | - |  |  | SI | Spina Bifida screening due |
| Q03 | - |  |  | SI | Spina Bifida screening done |
| Q04 | - |  |  | SI | Down's syndrome screening due |
| Q05 | - |  |  | SI | Down's syndrome screening done |
| Q06 | - |  |  | SI | Edward's syndrome screening due |
| Q07 | - |  |  | SI | Edward's syndrome screening done |
| Q08 | - |  |  | SI | Chlamydia screening required |
| Q08ObsDR | - |  |  | SI | Chlamydia screening required DR |
| Q09 | - |  |  | SI | Chlamydia screening done |
| Q10 | - |  |  | SI | Repeat blood group and Antibody check required |
| Q10ObsDR | - |  |  | SI | Repeat blood group and Antibody check required DR |
| Q11 | - |  |  | SI | Repeat blood group and Antibody check due |
| Q12 | - |  |  | SI | Repeat blood group and Antibody check done |
| Q13 | - |  |  | SI | Repeat FBC required |
| Q13ObsDR | - |  |  | SI | Repeat FBC required DR |
| Q14 | - |  |  | SI | Repeat FBC due |
| Q15 | - |  |  | SI | Repeat FBC done |
| Q16 | - |  |  | SI | Repeat random blood glucose required |
| Q16ObsDR | - |  |  | SI | Repeat random blood glucose required DR |
| Q17 | - |  |  | SI | Repeat random blood glucose due |
| Q18 | - |  |  | SI | Repeat random blood glucose done |
| Q19 | - |  |  | SI | Haemoglobinopathy screening required |
| Q19ObsDR | - |  |  | SI | Haemoglobinopathy screening required DR |
| Q20 | - |  |  | SI | Prophylactic Anti D required and discussed |
| Q20ObsDR | - |  |  | SI | Prophylactic Anti D required and discussed DR |
| Q21 | - |  |  | SI | Prophylactic Anti D given |
| Q22 | - |  |  | SI | Prophylactic Anti D given - gestation |
| Q23 | - |  |  | SI | Prophylactic Anti D batch number |
| Q24 | - |  |  | SI | Anti D dose |
| Q25 | - |  |  | SI | Which tests were declined and for what reason |
| Q26 | - |  |  | SI | Test results - action |
| Q27 | - |  |  | SI | Midwife countersigning |
| Q28 | - |  |  | SI | Haemoglobinopathy screening done |
| Q29 | - |  |  | SI | Booking bloods and MSU due |
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
| RDT_Childsub | double |  |  | NO | Childsub |
| RDT_ClosingTime | time |  |  | SI | Closing Time |
| RDT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| RDT_CreatedDate | date |  |  | SI | Created Date |
| RDT_CreatedTime | time |  |  | SI | Created Time |
| RDT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| RDT_DOW_DR | double |  | FK | SI | Des Ref DOW |
| RDT_DateFrom | date |  |  | SI | Date From |
| RDT_DateTo | date |  |  | SI | Date To |
| RDT_OpeningTime | time |  |  | SI | Opening Time |
| RDT_RowId | varchar |  |  | NO | - |
| RDT_UpdatedDate | date |  |  | SI | Updated Date |
| RDT_UpdatedTime | time |  |  | SI | Updated Time |
| RDT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*