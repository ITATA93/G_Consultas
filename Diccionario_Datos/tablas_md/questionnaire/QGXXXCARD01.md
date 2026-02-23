# questionnaire.QGXXXCARD01

> Cardiac History

**Schema:** questionnaire
**Columnas:** 76
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Cardiac History

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Site |
| Q02 | varchar |  |  | SI | Onset |
| Q03 | varchar |  |  | SI | Character |
| Q04 | varchar |  |  | SI | Radiation |
| Q05 | varchar |  |  | SI | Associated symptoms |
| Q06 | varchar |  |  | SI | Duration |
| Q07 | varchar |  |  | SI | Exacerbating factors |
| Q08 | varchar |  |  | SI | Severity |
| Q09 | varchar |  |  | SI | Comments |
| Q10 | varchar |  |  | SI | Relieving factors |
| Q11 | varchar |  |  | SI | Onset |
| Q12 | bit |  |  | SI | Has it been getting worse ? |
| Q13 | varchar |  |  | SI | Severity |
| Q14 | bit |  |  | SI | Orthopnea |
| Q15 | bit |  |  | SI | Paroxysmal Nocturnal Dyspnoea (PND) |
| Q16 | varchar |  |  | SI | Palpitations ? |
| Q17 | varchar |  |  | SI | Palpitations precipitating factor |
| Q18 | varchar |  |  | SI | Presyncope / Syncope? |
| Q19 | varchar |  |  | SI | Oedema ? |
| Q19ObsDR | varchar |  | FK | SI | Oedema ? DR |
| Q23 | varchar |  |  | SI | Symptoms of previous cardiac events |
| Q24 | varchar |  |  | SI | Syncope type |
| Q24ObsDR | varchar |  | FK | SI | Syncope type DR |
| Q25 | bit |  |  | SI | Fatigue |
| Q26 | varchar |  |  | SI | Previous cardiac events ? |
| Q27 | varchar |  |  | SI | Other associated symptom  |
| Q28 | varchar |  |  | SI | Other exacerbating factor |
| Q29 | varchar |  |  | SI | Other relieving factor |
| Q30 | varchar |  |  | SI | Relieving factors |
| Q31 | varchar |  |  | SI | Other relieving factor |
| Q32 | date |  |  | SI | Date |
| Q33 | time |  |  | SI | Time |
| Q40 | varchar |  |  | SI | Chest pain |
| Q41 | varchar |  |  | SI | Shortness of breath |
| Q42 | varchar |  |  | SI | Risk factors |
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