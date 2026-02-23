# SQLUser.PAC_PathwayHosp

**Schema:** SQLUser
**Columnas:** 60
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PACPH_ParRef | bigint | PK |  | NO | Parent Reference |
| PACPH_Childsub | double |  |  | NO | Childsub |
| PACPH_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| PACPH_CreatedDate | date |  |  | SI | Created Date |
| PACPH_CreatedTime | time |  |  | SI | Created Time |
| PACPH_CreatedUser_DR | bigint |  | FK | SI | Created User |
| PACPH_Hosp_DR | bigint |  | FK | SI | Hospital |
| PACPH_RowId | varchar |  |  | NO | - |
| PACPH_UpdatedDate | date |  |  | SI | Updated Date |
| PACPH_UpdatedTime | time |  |  | SI | Updated Time |
| PACPH_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Size of nidus |
| Q02 | - |  |  | SI | Eloquence of adjacent brain |
| Q03 | - |  |  | SI | Venous drainage |
| Q04 | - |  |  | SI | The Spetzler Martin Grading Scale estimates the ri... |
| Q05 | - |  |  | SI | It allocates points for various features of intrac... |
| Q06 | - |  |  | SI | A Grade 1 AVM would be considered as small, superf... |
| Q07 | - |  |  | SI | Score 1-2: Spetzler-Ponce class A, Microsurgical r... |
| Q08 | - |  |  | SI | Score 3: Spetzler-Ponce class B, Multimodality tre... |
| Q09 | - |  |  | SI | Score 4-5: Spetzler-Ponce class C, No treatment wi... |
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