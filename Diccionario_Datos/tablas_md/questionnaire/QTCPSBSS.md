# questionnaire.QTCPSBSS

> Proposed Shanghai Brugada Scoring System

**Schema:** questionnaire
**Columnas:** 65
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Proposed Shanghai Brugada Scoring System

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | date |  |  | SI | Date |
| Q02 | time |  |  | SI | Time |
| Q03 | varchar |  |  | SI | For each of the questions, select the highest scor... |
| Q04 | varchar |  |  | SI | Electrocardiogram (ECG) (12-lead / ambulatory) |
| Q05 | varchar |  |  | SI | Does not qualify for this scoring system |
| Q06 | varchar |  |  | SI | Clinical history |
| Q07 | varchar |  |  | SI | Family history |
| Q08 | varchar |  |  | SI | Genetic test result: probable pathogenic mutation ... |
| Q09 | varchar |  |  | SI | Score |
| Q10 | varchar |  |  | SI | Classification |
| Q11 | varchar |  |  | SI | ≥ 3.5 |
| Q12 | varchar |  |  | SI | Probable / Definite Brugada Syndrome |
| Q13 | varchar |  |  | SI | 2 – 3 |
| Q14 | varchar |  |  | SI | Possible Brugada Syndrome |
| Q15 | varchar |  |  | SI | 0.5 - 1.5 |
| Q16 | varchar |  |  | SI | Non diagnostic |
| Q17 | varchar |  |  | SI | 0 |
| Q18 | varchar |  |  | SI | Does not qualify for this scoring system |
| Q19 | varchar |  |  | SI | ≥ 3.5: Probable / Definite Brugada Syndrome |
| Q20 | varchar |  |  | SI | 2 – 3: Possible Brugada Syndrome |
| Q21 | varchar |  |  | SI | 0.5 - 1.5: Non diagnostic |
| Q22 | varchar |  |  | SI | 0: Does not qualify for this scoring system |
| Q23 | varchar |  |  | SI | The Shanghai Brugada Scoring System is from the 20... |
| Q24 | varchar |  |  | SI | electrocardiographic recordings, genetic results, ... |
| QUESAnaDR | varchar |  | FK | SI | Anaesthesia |
| QUESAnaOperationDR | varchar |  | FK | SI | Operation |
| QUESConsultDR | varchar |  | FK | SI | Consult |
| QUESCopiedComments | varchar |  |  | SI | Copied Comments |
| QUESCopiedDate | date |  |  | SI | Copied Date |
| QUESCopiedEpDR | bigint |  | FK | SI | Copied Episode |
| QUESCopiedSourceDR | bigint |  | FK | SI | Copied Source DR |
| QUESCopiedTime | time |  |  | SI | Copied Time |
| QUESCopiedUserDR | bigint |  | FK | SI | Copied User |
| QUESCreateDate | date |  |  | SI | Creation Date |
| QUESCreateTime | time |  |  | SI | Creation Time |
| QUESCreateUserDR | bigint |  | FK | SI | Creation User |
| QUESDate | date |  |  | SI | Last Update Date |
| QUESErrorReasonDR | bigint |  | FK | SI | Error Reason |
| QUESFHResidentDR | bigint |  | FK | SI | Resident |
| QUESMRClinicalPathWaysDR | varchar |  | FK | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | varchar |  | FK | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | varchar |  | FK | SI | Order Execution |
| QUESORPreanaestheticConsultDR | bigint |  | FK | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | varchar |  | FK | SI | Observation Entry |
| QUESOperRoomDR | bigint |  | FK | SI | Operating Room |
| QUESPAAdmDR | bigint |  | FK | SI | Admission |
| QUESPAAdverseEventDR | varchar |  | FK | SI | Adverse Event |
| QUESPAPatMasDR | bigint |  | FK | SI | Patient |
| QUESPAPregnancyDR | bigint |  | FK | SI | Pregnancy |
| QUESPAWaitingListDR | bigint |  | FK | SI | Waiting List |
| QUESPathwayItemDR | varchar |  | FK | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | varchar |  | FK | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | varchar |  | FK | SI | Appointments |
| QUESRBApptOutcomeDR | varchar |  | FK | SI | Appointment Outcome |
| QUESRBApptSlotDR | varchar |  | FK | SI | Appointment Slot |
| QUESReasonForCorrectionDR | bigint |  | FK | SI | Reason for Correction |
| QUESSSUserDefWindowDR | bigint |  | FK | SI | Questionnaire |
| QUESScore | varchar |  |  | SI | Score |
| QUESSecondUserDR | bigint |  | FK | SI | Second Signature |
| QUESStatusDR | bigint |  | FK | SI | Status |
| QUESTextResultDR | bigint |  | FK | SI | Text Result |
| QUESTime | time |  |  | SI | Last Update Time |
| QUESTransactionDR | varchar |  | FK | SI | Transaction |
| QUESUserDR | bigint |  | FK | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*