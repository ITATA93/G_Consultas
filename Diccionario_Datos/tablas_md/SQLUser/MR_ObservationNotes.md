# SQLUser.MR_ObservationNotes

**Schema:** SQLUser
**Columnas:** 101
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Observaciones**. Datos de observación clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBSN_ParRef | bigint | PK |  | NO | MR_Adm Parent Reference |
| OBSN_Childsub | double |  |  | NO | Childsub |
| OBSN_CreatedDate | date |  |  | SI | CreatedDate |
| OBSN_CreatedHospital_DR | bigint |  | FK | SI | Des Ref CreatedHospital |
| OBSN_CreatedObsGroup_DR | bigint |  | FK | SI | Des Ref LastUpdateObsGroup |
| OBSN_CreatedTime | time |  |  | SI | CreatedTime |
| OBSN_CreatedUser_DR | bigint |  | FK | SI | Des Ref CreatedUser |
| OBSN_Date | date |  |  | SI | Date |
| OBSN_Entry_DR | varchar |  | FK | SI | Des Ref Observ Entry |
| OBSN_LastUpdateDate | date |  |  | SI | LastUpdateDate |
| OBSN_LastUpdateHospital_DR | bigint |  | FK | SI | Des Ref LastUpdateHospital |
| OBSN_LastUpdateObsGroup_DR | bigint |  | FK | SI | Des Ref LastUpdateObsGroup |
| OBSN_LastUpdateTime | time |  |  | SI | LastUpdateTime |
| OBSN_LastUpdateUser_DR | bigint |  | FK | SI | Des Ref LastUpdateUser |
| OBSN_Notes | varchar |  |  | SI | Notes |
| OBSN_RowId | varchar |  |  | NO | - |
| OBSN_Time | time |  |  | SI | Time |
| Q01 | - |  |  | SI | Lives at home |
| Q01N | - |  |  | SI | Note |
| Q01ObsDR | - |  |  | SI | Lives at home DR |
| Q03 | - |  |  | SI | Activation care |
| Q03N | - |  |  | SI | Note |
| Q03ObsDR | - |  |  | SI | Activation care DR |
| Q05 | - |  |  | SI | Intensive short observation |
| Q05N | - |  |  | SI | Note |
| Q05ObsDR | - |  |  | SI | Intensive short observation DR |
| Q07 | - |  |  | SI | Emergency room |
| Q07N | - |  |  | SI | Note |
| Q07ObsDR | - |  |  | SI | Emergency room DR |
| Q09 | - |  |  | SI | Another hospital |
| Q09N | - |  |  | SI | Note |
| Q09ObsDR | - |  |  | SI | Another hospital DR |
| Q11 | - |  |  | SI | Other department |
| Q11N | - |  |  | SI | Note |
| Q11ObsDR | - |  |  | SI | Other department DR |
| Q13 | - |  |  | SI | Nursing home |
| Q13N | - |  |  | SI | Note |
| Q13ObsDR | - |  |  | SI | Nursing home DR |
| Q15 | - |  |  | SI | Via contact |
| Q15ObsDR | - |  |  | SI | Via contact DR |
| Q16N | - |  |  | SI | Note |
| Q17 | - |  |  | SI | Via airway |
| Q17N | - |  |  | SI | Note |
| Q17ObsDR | - |  |  | SI | Via airway DR |
| Q19 | - |  |  | SI | Via blood-borne |
| Q19N | - |  |  | SI | Note |
| Q19ObsDR | - |  |  | SI | Via blood-borne DR |
| Q21 | - |  |  | SI | Via droplets |
| Q21N | - |  |  | SI | Note |
| Q21ObsDR | - |  |  | SI | Via droplets DR |
| Q23 | - |  |  | SI | Other |
| Q23TxtOnly | - |  |  | SI | Other Plain Text Only |
| Q25 | - |  |  | SI | Management of home care |
| Q25N | - |  |  | SI | Note |
| Q25ObsDR | - |  |  | SI | Management of home care DR |
| Q27 | - |  |  | SI | Management of their own health |
| Q27N | - |  |  | SI | Note |
| Q27ObsDR | - |  |  | SI | Management of their own health DR |
| Q29 | - |  |  | SI | Hygienic conditions |
| Q29N | - |  |  | SI | Note |
| Q29ObsDR | - |  |  | SI | Hygienic conditions DR |
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