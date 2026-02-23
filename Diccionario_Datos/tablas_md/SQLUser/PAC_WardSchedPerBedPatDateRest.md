# SQLUser.PAC_WardSchedPerBedPatDateRest

**Schema:** SQLUser
**Columnas:** 67
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BDR_ParRef | varchar | PK |  | NO | PAC_WardSchedPerBedPat Parent Reference |
| BDR_Childsub | double |  |  | NO | Childsub |
| BDR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BDR_CreatedDate | date |  |  | SI | Created Date |
| BDR_CreatedTime | time |  |  | SI | Created Time |
| BDR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| BDR_Date | date |  |  | SI | Date |
| BDR_DateExclusive | varchar |  |  | SI | DateExclusive          |
| BDR_RowId | varchar |  |  | NO | - |
| BDR_UpdatedDate | date |  |  | SI | Updated Date |
| BDR_UpdatedTime | time |  |  | SI | Updated Time |
| BDR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Spinal Team Doctor	 |
| Q02 | - |  |  | SI | Care provider type	 |
| Q03 | - |  |  | SI | Cervical fracture details	 |
| Q04 | - |  |  | SI | Thoracic fracture details	 |
| Q05 | - |  |  | SI | Lumbar fracture details	 |
| Q06 | - |  |  | SI | Fracture Level	 |
| Q07 | - |  |  | SI | Cord injury	 |
| Q08 | - |  |  | SI | Neurological Status	 |
| Q09 | - |  |  | SI | Is an Aspen collar required?	 |
| Q10 | - |  |  | SI | Is a log roll required?	 |
| Q11 | - |  |  | SI | Can the patient side lie?	 |
| Q12 | - |  |  | SI | Can the patient sit up?	 |
| Q13 | - |  |  | SI | What angle can the patient's head be raised to (de... |
| Q14 | - |  |  | SI | Can prophylactic fragmin be given?	 |
| Q15 | - |  |  | SI | Notes	 |
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