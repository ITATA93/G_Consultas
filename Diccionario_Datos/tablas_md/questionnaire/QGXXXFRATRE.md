# questionnaire.QGXXXFRATRE

> Falls Incident Report

**Schema:** questionnaire
**Columnas:** 85
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Falls Incident Report

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Q01 | varchar |  |  | SI | Was the fall unassisted or assisted? |
| Q02 | varchar |  |  | SI | Was the fall observed? |
| Q03 | varchar |  |  | SI | Who observed the fall? |
| Q04 | varchar |  |  | SI | Did the patient sustain a physical injury as a res... |
| Q04a | varchar |  |  | SI | Comment |
| Q05 | varchar |  |  | SI | What type of injury was sustained? CHECK ONE; IF M... |
| Q05a | varchar |  |  | SI | Other |
| Q07 | varchar |  |  | SI | Prior to the fall, what was the patient doing or t... |
| Q07a | varchar |  |  | SI | Other |
| Q08 | varchar |  |  | SI | Prior to the fall, was a fall risk assessment docu... |
| Q09 | varchar |  |  | SI | Was the patient determined to be at increased risk... |
| Q09a | varchar |  |  | SI | Other |
| Q10 | varchar |  |  | SI | At the time of the fall, were any of the following... |
| Q11 | varchar |  |  | SI | Which of the following were in place and being use... |
| Q11a | varchar |  |  | SI | Other |
| Q15 | varchar |  |  | SI | At time of the fall, was the patient on medication... |
| Q16 | varchar |  |  | SI | Was the medication considered to have contributed ... |
| Q17 | varchar |  |  | SI | Did restraints, bedrails, or other physical device... |
| Q20 | date |  |  | SI | Date of Fall |
| Q21 | time |  |  | SI | Time of Fall |
| Q22 | varchar |  |  | SI | Location of Fall |
| Q23 | varchar |  |  | SI | Was the patient confused / dizzy? |
| Q24 | varchar |  |  | SI | Has the patient previously fallen in hospital? |
| Q24a | numeric |  |  | SI | Number of falls |
| Q25 | varchar |  |  | SI | Clinical assessment completed by doctor |
| Q25a | date |  |  | SI | Date |
| Q25b | time |  |  | SI | Time |
| Q25c | varchar |  |  | SI | Reason |
| Q26 | varchar |  |  | SI | Review Falls Risk Assessment? |
| Q26a | date |  |  | SI | Date |
| Q26b | time |  |  | SI | Time |
| Q26c | varchar |  |  | SI | Reason |
| Q27 | varchar |  |  | SI | Falls alarm required? |
| Q27a | date |  |  | SI | Date |
| Q27b | time |  |  | SI | Time |
| Q27c | varchar |  |  | SI | Reason |
| Q28 | varchar |  |  | SI | Does the patient need a low-rise bed? |
| Q29 | varchar |  |  | SI | Incident report completed? |
| Q29a | varchar |  |  | SI | Incident form number |
| Q30 | varchar |  |  | SI | Patient's relatives informed |
| Q30a | varchar |  |  | SI | Reason |
| Q31 | varchar |  |  | SI | Follow-up Care |
| Q32 | varchar |  |  | SI | Incident Details |
| Q33 | varchar |  |  | SI | Follow-up |
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