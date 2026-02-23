# SQLUser.PAC_ImmedCareRequired

**Schema:** SQLUser
**Columnas:** 79
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| IMCAR_RowId | bigint | PK |  | NO | - |
| ChildQ14DR | - |  |  | SI | Child Reference: Healthcare figures involved |
| IMCAR_Code | varchar |  |  | NO | Code |
| IMCAR_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| IMCAR_CreatedDate | date |  |  | SI | Created Date |
| IMCAR_CreatedTime | time |  |  | SI | Created Time |
| IMCAR_CreatedUser_DR | bigint |  | FK | SI | Created User |
| IMCAR_DateFrom | date |  |  | SI | Date From |
| IMCAR_DateTo | date |  |  | SI | Date To |
| IMCAR_Desc | varchar |  |  | NO | Description |
| IMCAR_Owner | varchar |  |  | SI | Owner |
| IMCAR_UpdatedDate | date |  |  | SI | Updated Date |
| IMCAR_UpdatedTime | time |  |  | SI | Updated Time |
| IMCAR_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Date |
| Q02 | - |  |  | SI | Time |
| Q03 | - |  |  | SI | Timing |
| Q04 | - |  |  | SI | Timing, notes |
| Q05 | - |  |  | SI | Assessment |
| Q06 | - |  |  | SI | Rehabilitation anamnesis |
| Q07 | - |  |  | SI | Pathology determining hospitalization |
| Q08 | - |  |  | SI | Comorbidity |
| Q09 | - |  |  | SI | Aids |
| Q10 | - |  |  | SI | Discharge assessment |
| Q11 | - |  |  | SI | Discharge plan |
| Q12 | - |  |  | SI | Rehabilitation plan |
| Q13 | - |  |  | SI | Rehabilitation plan |
| Q15 | - |  |  | SI | Goals definition |
| Q16 | - |  |  | SI | Nursing care involved? |
| Q18 | - |  |  | SI | Physiotherapist care involved? |
| Q20 | - |  |  | SI | Logopedist care involved? |
| Q22 | - |  |  | SI | Occupational therapist care involved? |
| Q24 | - |  |  | SI | Psychotherapist psychologist care involved? |
| Q26 | - |  |  | SI | Neuro-psychomotricity therapist care involved? |
| Q28 | - |  |  | SI | Psychiatric rehabilitation therapist care involved... |
| Q30 | - |  |  | SI | Social assistant care involved? |
| Q32 | - |  |  | SI | Orthoptist care involved? |
| Q34 | - |  |  | SI | Dietitian care involved? |
| Q36 | - |  |  | SI | Outcome predictions |
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