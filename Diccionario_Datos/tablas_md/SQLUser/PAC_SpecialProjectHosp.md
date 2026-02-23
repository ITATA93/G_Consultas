# SQLUser.PAC_SpecialProjectHosp

**Schema:** SQLUser
**Columnas:** 75
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| HOS_ParRef | bigint | PK |  | NO | PAC_SpecialProject Parent Reference |
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
| Q03 | - |  |  | SI | For each of the questions, select the highest scor... |
| Q04 | - |  |  | SI | Electrocardiogram (ECG) (12-lead / ambulatory) |
| Q05 | - |  |  | SI | Does not qualify for this scoring system |
| Q06 | - |  |  | SI | Clinical history |
| Q07 | - |  |  | SI | Family history |
| Q08 | - |  |  | SI | Genetic test result: probable pathogenic mutation ... |
| Q09 | - |  |  | SI | Score |
| Q10 | - |  |  | SI | Classification |
| Q11 | - |  |  | SI | ≥ 3.5 |
| Q12 | - |  |  | SI | Probable / Definite Brugada Syndrome |
| Q13 | - |  |  | SI | 2 – 3 |
| Q14 | - |  |  | SI | Possible Brugada Syndrome |
| Q15 | - |  |  | SI | 0.5 - 1.5 |
| Q16 | - |  |  | SI | Non diagnostic |
| Q17 | - |  |  | SI | 0 |
| Q18 | - |  |  | SI | Does not qualify for this scoring system |
| Q19 | - |  |  | SI | ≥ 3.5: Probable / Definite Brugada Syndrome |
| Q20 | - |  |  | SI | 2 – 3: Possible Brugada Syndrome |
| Q21 | - |  |  | SI | 0.5 - 1.5: Non diagnostic |
| Q22 | - |  |  | SI | 0: Does not qualify for this scoring system |
| Q23 | - |  |  | SI | The Shanghai Brugada Scoring System is from the 20... |
| Q24 | - |  |  | SI | electrocardiographic recordings, genetic results, ... |
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