# questionnaire.QGXXXFESSO

> FESS Observations

**Schema:** questionnaire
**Columnas:** 73
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* FESS Observations

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Proptosis right |
| Q02 | varchar |  |  | SI | Proptosis left |
| Q03 | varchar |  |  | SI | Periorbital haemorrhage right |
| Q04 | varchar |  |  | SI | Periorbital haemorrhage left |
| Q05 | varchar |  |  | SI | Subconjunctival haemorrhage right |
| Q06 | varchar |  |  | SI | Subconjunctival haemorrhage left |
| Q07 | varchar |  |  | SI | Subcutaneous emphysema right |
| Q08 | varchar |  |  | SI | Subcutaneous emphysema left |
| Q09 | varchar |  |  | SI | Occular movement right |
| Q10 | varchar |  |  | SI | Occular movement left |
| Q11 | varchar |  |  | SI | Pupil reflexes right |
| Q12 | varchar |  |  | SI | Pupil reflexes left |
| Q13 | varchar |  |  | SI | Pupil size right |
| Q14 | varchar |  |  | SI | Pupil size left |
| Q15 | varchar |  |  | SI | Visual acuity right |
| Q16 | varchar |  |  | SI | Visual acuity left |
| Q17 | varchar |  |  | SI | Epistaxis right |
| Q18 | varchar |  |  | SI | Epistaxis left |
| Q19 | varchar |  |  | SI | FESS comments |
| Q20 | varchar |  |  | SI | The eye appears protruding forward |
| Q21 | varchar |  |  | SI | Bruising around the eye |
| Q22 | varchar |  |  | SI | Bleeding into the white portion of the eye |
| Q23 | varchar |  |  | SI | Bubbles of air under the skin |
| Q24 | varchar |  |  | SI | Assess lateral, medial, up and down movement |
| Q25 | varchar |  |  | SI | Light shone into eye should product constriction o... |
| Q26 | varchar |  |  | SI | Use pupil scale 1-8 |
| Q27 | varchar |  |  | SI | Check for deterioration compared with pre-op |
| Q28 | varchar |  |  | SI | Bleeding from the nose |
| Q29 | varchar |  |  | SI | Right side |
| Q30 | varchar |  |  | SI | Left side |
| Q31 | date |  |  | SI | Date |
| Q32 | time |  |  | SI | Time |
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